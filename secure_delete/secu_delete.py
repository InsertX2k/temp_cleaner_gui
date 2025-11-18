from random import randint
from sys import argv
from os import urandom, path, SEEK_SET, unlink, remove, fsync
import psutil
# for IPC (Interprocess Communication)
from multiprocessing import shared_memory
# for handling signals (SIGINT, SIGTERM)
import signal
# i want to emulate static typing since i just came from C++
from typing import NoReturn


# for testing purposes ONLY!
fname = "C:\\Users\\pc\\Desktop\\rand_bytes.bin"

# we have to create shared memories for each value in the SecuEraseStatus class
SECU_ERASE_SHARED_MEM_CURRENT_PASS_NAME: str = "secu_erase_shmem0_curpass"
SECU_ERASE_SHARED_MEM_ALGORITHM_NAME: str = "secu_erase_shmem0_algorithm"
SECU_ERASE_SHARED_MEM_STAGE_NAME: str = "secu_erase_shmem0_stagename"

# size (in bytes) for each shared memory object, the least number
# of bytes you can assign for use on shared memory objects in Windows
# operating system is 4096 bytes (4KB)
SHARED_MEM_SIZE_BYTES: int = 4096


# we have to declare some constants to be used for our SecuEraseStatus values
SECU_ERASE_RAND_BYTES_FILL_SINGLE_PASS: str = "Random Bytes Fill (Single Pass)"
SECU_ERASE_RAND_BYTES_FILL_MULTI_PASS: str = "Random Bytes Fill (Multi Pass)"
SECU_ERASE_ZERO_BYTES_FILL_SINGLE_PASS: str = "Zero Bytes Fill (0x00) (Single Pass)"
SECU_ERASE_ZERO_BYTES_FILL_MULTI_PASS: str = "Zero Bytes Fill (0x00) (Multi Pass)"
SECU_ERASE_IDLING: str = "Idling..."
SECU_ERASE_FF_BYTES_FILL_SINGLE_PASS: str = "Fixed Bytes Fill (0xFF) (Single Pass)"
SECU_ERASE_FF_BYTES_FILL_MULTI_PASS: str = "Fixed Bytes Fill (0xFF) (Multi Pass)"
SECU_ERASE_DELETING_DISK_FILLER_FILE: str = "Delete Disk Filler File"
SECU_ERASE_ALGORITHM_NIST_800_88: str = "National Institute of Standards and Technology (NIST) 800-88 Rev.1 (Guidelines)"
SECU_ERASE_ALGORITHM_DOD_5220_22_M: str = "US DOD (Department of Defense) 5220.22-M"
SECU_ERASE_ALGORITHM_SSD_TRIM: str = "ATA SSD/NVMe TRIM Command"
SECU_ERASE_NO_ALGORITHM: str = "None"

# let's make a class to be used to retrieve the current status of the disk erasing process
# this will be helpful for implementing this module in our program (Temp_Cleaner GUI)
class SecuEraseStatus:
    global SECU_ERASE_SHARED_MEM_CURRENT_PASS_NAME, SECU_ERASE_SHARED_MEM_ALGORITHM_NAME, SECU_ERASE_SHARED_MEM_STAGE_NAME, SHARED_MEM_SIZE_BYTES
    def __init__(self):
        """
        Constructor for SecuEraseStatus class.

        Initializes the class with default/null values as its attributes, and creates the shared memory objects for use
        with IPC (Interprocess Communication) to retrieve the current status of the worker process from within another
        running process.
        """
        print("[DEBUG] SecuEraseStatus: Constructor called!")
        self.current_pass: int = 0
        self.algorithm_name: str = ""
        self.stage_name: str = ""
        print("[DEBUG] SecuEraseStatus: Constructor: creating shared memory objects...")
        # we will declare our shared memory objects here in the constructor
        # shared memory regions for SecuEraseStatus
        self.secu_erase_cur_pass_mem: shared_memory.SharedMemory = shared_memory.SharedMemory(name=SECU_ERASE_SHARED_MEM_CURRENT_PASS_NAME, create=True, size=SHARED_MEM_SIZE_BYTES)
        self.secu_erase_algorithm_mem: shared_memory.SharedMemory = shared_memory.SharedMemory(name=SECU_ERASE_SHARED_MEM_ALGORITHM_NAME, create=True, size=SHARED_MEM_SIZE_BYTES)
        self.secu_erase_stage_name_mem: shared_memory.SharedMemory = shared_memory.SharedMemory(name=SECU_ERASE_SHARED_MEM_STAGE_NAME, create=True, size=SHARED_MEM_SIZE_BYTES)
        print("[DEBUG] SecuEraseStatus: Constructor: successfully created shared memory objects!")
        
    
    # setters and getters for current pass (integer) value
    def getCurrentPass(self) -> int:
        """Returns the current pass"""
        return self.current_pass
    
    def setCurrentPass(self, new_cur_pass: int) -> int:
        """
        Sets the current pass number

        The only difference between this and directly accessing the attribute `current_pass`, is that this
        method modifies the current pass value within the shared memory object.
        """
        print(f"[DEBUG] SecuEraseStatus.setCurrentPass() called with new_cur_pass={new_cur_pass}")
        self.current_pass = int(new_cur_pass)
        # now we have to update the current pass specified in the shared memory region
        # steps are the following:
        # shared_mem.buf[:len(text)] = bytes( text.encode() )
        # get shared_mem.buf length, and bytes_to_null (which equals to shared_mem.buf - len(text))
        # shared_mem.buf[len(text):] = bytes(b'\x00')*bytes_to_null
        print(f"[DEBUG] SecuEraseStatus.setCurrentPass(): writing new_cur_pass to shared memory buffer: secu_erase_cur_pass_mem.buf[0]")
        self.secu_erase_cur_pass_mem.buf[0] = new_cur_pass
        bytes_to_null: int = int( len(self.secu_erase_cur_pass_mem.buf) - 1 )
        print(f"[DEBUG] SecuEraseStatus.setCurrentPass(): bytes_to_null: {bytes_to_null}")
        print(f"[DEBUG] SecuEraseStatus.setCurrentPass(): zero-filling {bytes_to_null} bytes on shared memory region buffer: secu_erase_cur_pass_mem.buf")
        self.secu_erase_cur_pass_mem.buf[1:] = bytes(b'\x00')*bytes_to_null
        # if you want to read it from the memory:
        # int(secu_erase_cur_pass_mem.buf[0].to_bytes().hex(),base=16)
        return self.current_pass
    
    # setters and getters for algorithm name
    def getCurrentAlgorithmName(self) -> str:
        """Returns the current algorithm name"""
        return self.algorithm_name
    
    def setCurrentAlgorithmName(self, new_cur_algorithm_name: str) -> str:
        """
        Sets the current algorithm name to `new_cur_algorithm_name`

        The only difference between this and directly modifying the attribute `algorithm_name` is that this
        method modifies the algorithm name value stored in the shared memory object for the algorithm name.
        """
        print(f"[DEBUG] SecuEraseStatus.setCurrentAlgorithmName() called with new_cur_algorithm_name={new_cur_algorithm_name}")
        self.algorithm_name = new_cur_algorithm_name
        # now lets update the current algorithm name stored in the shared mem region
        print("[DEBUG] SecuEraseStatus.setCurrentAlgorithmName(): begin writing algorithm name string to shared memory secu_erase_algorithm_mem.buf")
        new_cur_algorithm_name_len: int = len(new_cur_algorithm_name)
        print(f"[DEBUG] SecuEraseStatus.setCurrentAlgorithmName(): got length for new_cur_algorithm_name: {new_cur_algorithm_name_len}")
        # let's first zero the memory blocks.
        print("[DEBUG] SecuEraseStatus.setCurrentAlgorithmName(): zero-filling shared memory buffer secu_erase_algorithm_mem.buf")
        self.secu_erase_algorithm_mem.buf[:len(self.secu_erase_algorithm_mem.buf)] = bytes(b'\x00')*(len(self.secu_erase_algorithm_mem.buf))
        # now we need to write algorithm name to shared memory blocks.
        print("[DEBUG] SecuEraseStatus.setCurrentAlgorithmName(): writing algorithm name to shared memory buffer secu_erase_algorithm_mem.buf")
        self.secu_erase_algorithm_mem.buf[:new_cur_algorithm_name_len] = bytes(new_cur_algorithm_name.encode())
        return self.algorithm_name
    
    # setters and getters for current stage name.
    def getCurrentStageName(self) -> str:
        """Returns the current stage name"""
        return self.stage_name
    
    def setCurrentStageName(self, new_cur_stage_name: str) -> str:
        """
        Sets the current stage name to `new_cur_stage_name`

        The only difference between this and directly modifying the attribute `stage_name` is that this
        method directly modifies the value stored in the shared memory object for the stage name.
        """
        print(f"[DEBUG] SecuEraseStatus.setCurrentStageName() called with new_cur_stage_name={new_cur_stage_name}")
        self.stage_name = new_cur_stage_name
        # now lets update the current stage name stored in the shared mem region
        # lets first zero the memory blocks
        print(f"[DEBUG] SecuEraseStatus.setCurrentStageName(): zero-filling secu_erase_stage_name_mem.buf")
        self.secu_erase_stage_name_mem.buf[:len(self.secu_erase_stage_name_mem.buf)] = bytes(b'\x00')*(len(self.secu_erase_stage_name_mem.buf))
        # now we have to store the name of the stage in the shared memory blocks
        print(f"[DEBUG] SecuEraseStatus.setCurrentStageName(): writing new_cur_stage_name to shared memory: secu_erase_stage_name_mem")
        self.secu_erase_stage_name_mem.buf[:len(new_cur_stage_name)] = bytes(new_cur_stage_name.encode())
        return self.stage_name

    # the destructor of this class will automatically release memory used for all the shared memory objects
    # and close handles open by the worker process.
    def __del__(self):
        """
        Destructor method

        Closes all open handles to all the shared memory objects used to store the current secure
        erasure process status.

        Will be called automatically upon destructing/deleting the SecuEraseStatus instance/object.
        """
        print("[DEBUG] SecuEraseStatus: Destructor called, Releasing all handles to shared memory objects...")
        # we use close() to close handles to a SharedMemory object
        # we can't use unlink() on Windows here since it will not delete the shared memory block 
        # because it will be used by our wizard process, only if all processes stop
        # using our shared memory blocks is when exactly it will be deleted
        # See: https://docs.python.org/3/library/multiprocessing.shared_memory.html#multiprocessing.shared_memory.SharedMemory.unlink
        self.secu_erase_cur_pass_mem.close()
        print("[DEBUG] SecuEraseStatus: Destructor: secu_erase_cur_pass_mem handle closed!")
        self.secu_erase_algorithm_mem.close()
        print("[DEBUG] SecuEraseStatus: Destructor: secu_erase_algorithm_mem handle closed!")
        self.secu_erase_stage_name_mem.close()
        print("[DEBUG] SecuEraseStatus: Destructor: secu_erase_stage_name_mem handle closed!")
        # --------------
        print("[DEBUG] SecuEraseStatus: Destructor method exit, released all shared memory allocated to the object!")
        return
        
# our custom signal handler
def sigHandler(sigNum, currentStackFrame) -> NoReturn:
    """
    A Custom handler for registered signals

    Must be used exclusively on SIGINT, and SIGTERM

    Used to provide signals IPC functionality to secu_delete (in case if running as a separate process).
    
    This function has no return since it will exit the interpreter/current process after it finishes execution.
    """
    # i want to (somehow) close handles to shared memory blocks used by SecuEraseStatus.
    # but this can only happen if I'm destructing an instance of it.
    
    # raising SystemExit will take care of stopping an existing disk filling or disk filler file
    # management task that's already running.
    raise SystemExit(256) # exit code 256 is for a signaled exit.


def do_bytes_array_exist_in_file(fopend, fname: str, b: bytes, box_size: int) -> bool:
    """
    Checks if bytes `b` with size of `box_size` exist in file `fname` opened in file descriptor `fopend`

    This function will ONLY work if the file `fname` opened in `fopend` was open with mode `rb`, `rb+`, or `ab+`
    and NOT `wb`, `wb+`, `a+`

    Returns: True if `b` exists within the file open in `fopend`, False otherwise.
    """
    # put the file access pointer to the first byte of the file
    fopend.seek(0, SEEK_SET)
    # we need to get full file size in bytes
    fname_fsize: int = int( path.getsize(fname) )
    # we need to get how many box_size in the full file name in bytes
    box_size_in_fname_fsize: int = int(fname_fsize / box_size)
    # right now, we will iterate over each box_size in the full size of our file (fname)
    if int(box_size_in_fname_fsize) <= 1:
        if bytes( fopend.read(box_size) ) == b:
            return True
    else:
        for cur_box_pos in range(box_size_in_fname_fsize):
            if bytes( fopend.read(box_size) ) == b:
                # bytes read from the current file stream are identical to the given bytes
                return True


    # if none of the statements above meet our conditions.
    return False


def make_rand_bytes_file(fname: str, box_size: int, count: int):
    """
    Writes `box_size`*`count` random bytes from `/dev/urandom` or the OS's PRNG (pseudo-random numbers generator)
    to the file `fname`
    
    * It writes bytes and flushes buffers after writing `box_size` bytes, but if `box_size` is 1, it will
    ONLY flush buffers after writing the entire desired `count` bytes.

    Returns: `fname`
    """
    if box_size > 1:
        for _ in range(count):
            wb_fdobj = open(fname, "ab+")
            rand_bytes = urandom(box_size)
            # we will write the byte in the file
            wb_fdobj.write(rand_bytes)
            # trying to free up some memory.
            del rand_bytes
            # force the file system to write the byte into the kernel's
            # buffer (caches) reserved in memory space for FS caches.
            # instead of keeping it into the userspace (python's cache)
            wb_fdobj.flush()
            # as i explained above, this will move the cache from the kernel's
            # buffer (for FS caching) to the disk controller (or might possibly)
            # force writing it into the disk.
            fsync(wb_fdobj.fileno())
            # written_bytes.append(rand_bytes)
            wb_fdobj.close()
    elif box_size == 1: # user wants to write data byte per byte.
        wb_fdobj = open(fname, "ab+")
        for _ in range(count): # we will write byte by byte
            rand_byte: bytes = urandom(1)
            wb_fdobj.write(rand_byte)
        wb_fdobj.flush()
        fsync(wb_fdobj.fileno())
        wb_fdobj.close()
    else:
        raise ValueError("box_size cannot be less than 1")
            
    
    return fname


def make_zero_bytes_file(fname: str, box_size: int, count: int) -> str:
    """
    Writes zero bytes to file `fname` `box_size` at a time, for `count` times

    * If `box_size` is greater than 1: flushes buffers after writing each `box_size` to the file `fname`, otherwise
    flushes buffers after it finishes writing zero bytes `count` times.

    Returns: `fname`
    """
    if box_size == 1:
        zbbf_obj = open(fname, "ab+")
    for _ in range(count):
        if box_size > 1:
            zbbf_obj = open(fname, "ab+")
        zbbf_obj.write(b"\x00"*box_size)
        if box_size > 1:
            zbbf_obj.flush()
            fsync(zbbf_obj.fileno())
            zbbf_obj.close()

    if box_size == 1:
        zbbf_obj.flush()
        fsync(zbbf_obj.fileno())
        zbbf_obj.close()

    return fname

def make_bytes_pattern_file(fname: str, pattern: bytes, box_size: int, count: int) -> str:
    """
    Writes a `box_size` multiplication of the bytes pattern `pattern` `count` times

    Returns: `fname`
    """
    if box_size == 1:
        bpfbw_obj = open(fname, "ab+")
    for _ in range(count):
        if box_size > 1:
            bpfbw_obj = open(fname, "ab+")
        bpfbw_obj.write(pattern*box_size)
        if box_size > 1:
            bpfbw_obj.flush()
            fsync(bpfbw_obj.fileno())
            bpfbw_obj.close()
    
    if box_size == 1:
        bpfbw_obj.flush()
        fsync(bpfbw_obj.fileno())
        bpfbw_obj.close()
    
    return fname



def fill_disk_with_rand_bytes_file(fname: str) -> int:
    """
    Fills all the free space on the volume storing the file `fname` with random bytes from `/dev/urandom` or the OS's PRNG (Pseudo-random numbers generator)
    till the last free byte.

    Returns: 0 only if the free disk space of the volume storing the file `fname` is 0

    NOTE: This function ignores exceptions (like `OSError`) in all stages but the last one, so you must implement exception
    handling if you plan to use this function in any real-world application.
    """
    disk_free_bytes = psutil.disk_usage(path.splitdrive(fname)[0]).free
    print(f"[DEBUG] disk free bytes are : {disk_free_bytes}")
    while disk_free_bytes > 0: # while we still have free disk space (greater than 0 byte)
        print(f"[DEBUG] Enter file write loop, disk free bytes are > 0")
        if disk_free_bytes >= 10485760: # free disk space in bytes is equal or greater to 10MB
            disk_free_10mb_blocks: int = int( disk_free_bytes/1024/1024/10 )
            print(f"[DEBUG] disk free 10 MB blocks count is {disk_free_10mb_blocks}, write 10mb random blocks to file")
            try: make_rand_bytes_file(fname, (1024*1024*10), disk_free_10mb_blocks)
            except: print(f"[WARNING] error ignored during writing 10 MB blocks stage")
        # we need to recheck for disk free bytes
        disk_free_bytes = psutil.disk_usage(path.splitdrive(fname)[0]).free
        print(f"[DEBUG] disk free bytes after Stage 1 are : {disk_free_bytes}")
        if disk_free_bytes >= 1048576 and disk_free_bytes < 10485760: # we still have a few megabytes left (but is less than 10 MB)
            disk_free_1mb_blocks: int = int( disk_free_bytes/1024/1024 )
            print(f"[DEBUG] disk free 1MB block count is {disk_free_1mb_blocks}, write 1 MB random blocks to file")
            try: make_rand_bytes_file(fname, (1024*1024), disk_free_1mb_blocks)
            except: print(f"[WARNING] error ignored during writing 1 MB blocks stage")
        # we still need to recheck for free disk bytes.
        disk_free_bytes = psutil.disk_usage(path.splitdrive(fname)[0]).free
        print(f"[DEBUG] disk free bytes after Stage 2 are : {disk_free_bytes}")
        if disk_free_bytes >= 1 and disk_free_bytes < 1048576: # we still have some free disk space in bytes (even if greater than 1 bytes)
            make_rand_bytes_file(fname, 1, disk_free_bytes)
        # we need to check for free disk space again 
        disk_free_bytes = psutil.disk_usage(path.splitdrive(fname)[0]).free
        print(f"[DEBUG] disk free bytes after all stages are : {disk_free_bytes}")
        # the loop will break if disk free bytes are 0

    # this will return 0 if disk free bytes are 0
    return 0

def fill_disk_with_zero_bytes_file(fname: str) -> int:
    """
    Fills all the free space the volume storing the file `fname` with Zero bytes till the last free byte.

    Returns: 0 only if the volume storing the file `fname` has no free space left.

    NOTE: This function ignores exceptions (like `OSError`) in all stages but the last one, so you must implement exception
    handling if you plan to use this function in any real-world application.
    """
    # we need to retrieve disk free bytes first
    disk_free_bytes: int = psutil.disk_usage(path.splitdrive(fname)[0]).free
    print(f"[DEBUG] fill_disk_with_zero_bytes_file: disk free bytes are: {disk_free_bytes}")
    while disk_free_bytes > 0: # if there is still any chance to fill the disk up.
        print(f"[DEBUG] fill_disk_with_zero_bytes_file: enter fill disk loop, disk free bytes are > 0 ({disk_free_bytes})")
        if disk_free_bytes >= 10485760: # if free disk space is greater than or equal to 10 MB
            disk_free_bytes_10MB_blocks: int = int( disk_free_bytes/1024/1024/10 )
            print(f"[DEBUG] fill_disk_with_zero_bytes_file: disk can be filled with {disk_free_bytes_10MB_blocks} 10MB blocks, will write them now")
            try: make_zero_bytes_file(fname, (1024*1024*10), disk_free_bytes_10MB_blocks)
            except: print("[WARNING] fill_disk_with_zero_bytes_file: ignored error on disk filling with 10 MB blocks stage")
        # we need to update disk_free_bytes at this stage
        disk_free_bytes: int = psutil.disk_usage(path.splitdrive(fname)[0]).free
        print(f"[DEBUG] fill_disk_with_zero_bytes_file: end of first stage (filling with 10MB blocks), free disk bytes are: {disk_free_bytes}")
        if disk_free_bytes >= 1048576 and disk_free_bytes < 10485760: # if free disk space is greater than or equal to 1 MB
            disk_free_bytes_1_mb_blocks: int = int( disk_free_bytes/1024/1024 )
            print(f"[DEBUG] fill_disk_with_zero_bytes_file: disk can be filled with {disk_free_bytes_1_mb_blocks} 1MB blocks, will write them now")
            try: make_zero_bytes_file(fname, (1024*1024), disk_free_bytes_1_mb_blocks)
            except: print("[WARNING] fill_disk_with_zero_bytes_file: ignored error on disk fill with 1 MB blocks stage")
        # we need to update disk_free_bytes at this stage
        disk_free_bytes: int = psutil.disk_usage(path.splitdrive(fname)[0]).free
        print(f"[DEBUG] fill_disk_with_zero_bytes_file: end of stage 2 (filling disk with 1 MB blocks), free disk bytes are: {disk_free_bytes}")
        if disk_free_bytes >0 and disk_free_bytes < 1048576: # we still have a few spare bytes we can write onto the disk
            make_zero_bytes_file(fname, 1, disk_free_bytes)
        # we need to update disk_free_bytes at this stage
        disk_free_bytes: int = psutil.disk_usage(path.splitdrive(fname)[0]).free
        print(f"[DEBUG] fill_disk_with_zero_bytes_file: end of all disk filling operations, disk free bytes are {disk_free_bytes}")
    # this will return 0 if disk free bytes are 0
    return 0

def fill_disk_with_pattern_bytes_file(fname: str, pattern: bytes) -> int:
    """
    Fills all the free space of the volume storing the file `fname` with `pattern` bytes pattern till the last free byte.

    Returns: 0 only if the volume storing the file `fname` has no free space left.

    NOTE: This function ignores exceptions (like `OSError`) in all stages but the last one, so you must implement exception
    handling if you plan to use this function in any real-world application.
    """
    print("[DEBUG] fill_disk_with_pattern_bytes_file: function execution begin...")
    disk_free_bytes: int = psutil.disk_usage(path.splitdrive(fname)[0]).free
    print(f"[DEBUG] fill_disk_with_pattern_bytes_file: disk free bytes are: {disk_free_bytes}")
    while disk_free_bytes > 0:
        print(f"[DEBUG] fill_disk_with_pattern_bytes_file: enter write pattern bytes file loop, disk free bytes > 0 ({disk_free_bytes})")
        if disk_free_bytes >= 10485760: # free space is greater than 10 MB
            disk_free_bytes_10mb_blocks: int = int( disk_free_bytes/1024/1024/10 )
            print(f"[DEBUG] fill_disk_with_pattern_bytes_file: disk can be filled up using {disk_free_bytes_10mb_blocks} 10MB blocks, will write them")
            try: 
                make_bytes_pattern_file(fname, pattern, (1024*1024*10), disk_free_bytes_10mb_blocks)
                print("[DEBUG] fill_disk_with_pattern_bytes_file: make_bytes_pattern_file() function finished execution!")
            except:
                print("[WARNING] fill_disk_with_pattern_bytes_file: make_bytes_pattern_file() error ignored")
        # we need to reupdate the checked disk free bytes
        disk_free_bytes: int = psutil.disk_usage(path.splitdrive(fname)[0]).free
        print(f"[DEBUG] fill_disk_with_pattern_bytes_file: disk free bytes after stage 1 (filling up with 10MB blocks) finished are {disk_free_bytes}")
        if disk_free_bytes >= 1048576 and disk_free_bytes < 10485760:
            disk_free_bytes_1m_blocks: int = int( disk_free_bytes/1024/1024 )
            print(f"[DEBUG] fill_disk_with_pattern_bytes_file: disk can be filled up using {disk_free_bytes_1m_blocks} 1MB blocks, will write them")
            try:
                make_bytes_pattern_file(fname, pattern, (1024*1024), disk_free_bytes_1m_blocks)
                print("[DEBUG] fill_disk_with_pattern_bytes_file: make_bytes_pattern_file() function finished execution!")
            except:
                print("[WARNING] fill_disk_with_pattern_bytes_file: make_bytes_pattern_file() error ignored")
        # now after stage 2 finishes execution, we will have to re-update the checked free disk bytes
        disk_free_bytes: int = psutil.disk_usage(path.splitdrive(fname)[0]).free
        print(f"[DEBUG] fill_disk_with_pattern_bytes_file: disk free bytes after stage 2 finished (filling up with 1MB blocks) are {disk_free_bytes}")
        if disk_free_bytes >=1 and disk_free_bytes < 1048576:
            make_bytes_pattern_file(fname, pattern, 1, disk_free_bytes)
        # after it fills up all the remaining free disk bytes (at the current time of the execution)
        # we have to reupdate the disk free bytes detected again (to see if we still have to continue
        # keeping the loop running or not).
        disk_free_bytes: int = psutil.disk_usage(path.splitdrive(fname)[0]).free
        print(f"[DEBUG] fill_disk_with_pattern_bytes_file: disk free bytes after finishing all stages are: {disk_free_bytes}")
        # this loop will exist automatically if disk free bytes are 0

    # this function will return 0 automatically once the free disk space reaches 0 bytes.
    return 0


def erase_free_space_with_nist800_algorithm(fname: str, secu_erase_status_obj: SecuEraseStatus = None):
    """
    Fills the disk with a disk filler file (that is, filled up with zero bytes)
    with the size of the free disk space on the disk, then deletes that zero bytes filled
    disk filler file and re-creates it again but with random bytes from `/dev/random` or
    whatever the PRNG device is on your platform.

    According to the NIST 800-88 Rev. 1 (2014) Media Sanitization guidelines (for HDDs only)

    If you are using an SSD (or a flash memory) PLEASE DO NOT USE THIS FUNCTION, instead
    refer to using the secure erase or trim ATA commands available from your SSD's firmware.

    fname: str - a full path (string) to where the disk filler file should be stored on.
    
    secu_erase_status_obj: SecuEraseStatus - an object (instance of a SecuEraseStatus) that will be used to monitor
    the current status of the secure free disk space erasing process and will be modified according to the current
    stage and phase the execution of this function is in.
    """
    print("[DEBUG] erase_free_space_with_nist800_algorithm: work begin...")
    # we will do one pass of fixed data value (0x00) to fill up the entire hard drive
    if secu_erase_status_obj is not None:
        secu_erase_status_obj.setCurrentAlgorithmName(SECU_ERASE_ALGORITHM_NIST_800_88)
        secu_erase_status_obj.setCurrentStageName(SECU_ERASE_ZERO_BYTES_FILL_SINGLE_PASS)
        secu_erase_status_obj.setCurrentPass(1)
    try: fill_disk_with_zero_bytes_file(fname);print("[DEBUG] erase_free_space_with_nist800_algorithm: fill_disk_with_zero_bytes_file() finished execution!")
    except: print("[WARNING] erase_free_space_with_nist800_algorithm: fill_disk_with_zero_bytes_file() error ignored")
    # next up, we will delete our file
    if secu_erase_status_obj is not None:
        secu_erase_status_obj.setCurrentStageName(SECU_ERASE_DELETING_DISK_FILLER_FILE)
    try: remove(fname);print("[DEBUG] erase_free_space_with_nist800_algorithm: deletion of zeroed disk filler file completed successfully!")
    except: print("[WARNING] erase_free_space_with_nist800_algorithm: deletion of zeroed disk filler file failed!")
    # now at this stage, we now have to fill up our free disk space with a more complex pattern
    # which is, in our case, the random bytes generated by the PRNG provided by the OS
    # but we will do this 3 times, as it is more secure and will help with my paranoia
    for __pass in range(3):
        print(f"[DEBUG] erase_free_space_with_nist800_algorithm: Begin random bytes disk filling pass {__pass}")
        if secu_erase_status_obj is not None:
            secu_erase_status_obj.setCurrentStageName(SECU_ERASE_RAND_BYTES_FILL_MULTI_PASS)
            secu_erase_status_obj.setCurrentPass(__pass + 1)
        try: fill_disk_with_rand_bytes_file(fname);print("[DEBUG] erase_free_space_with_nist800_algorithm: fill_disk_with_rand_bytes_file() execution finished successfully!")
        except: print("[WARNING] erase_free_space_with_nist800_algorithm: fill_disk_with_rand_bytes_file() error ignored")
        # now its the time to delete the file
        if secu_erase_status_obj is not None:
            secu_erase_status_obj.setCurrentStageName(SECU_ERASE_DELETING_DISK_FILLER_FILE)
        try: remove(fname);print("[DEBUG] erase_free_space_with_nist800_algorithm: deletion of random bytes disk filler file completed successfully!")
        except: print("[WARNING] erase_free_space_with_nist800_algorithm: deletion of random bytes disk filler file has failed!")
        print(f"[DEBUG] erase_free_space_with_nist800_algorithm: End random bytes disk filling pass {__pass}")

    print("[DEBUG] erase_free_space_with_nist800_algorithm: end of function execution!")
    if secu_erase_status_obj is not None:
        secu_erase_status_obj.setCurrentPass(0)
        secu_erase_status_obj.setCurrentStageName(SECU_ERASE_IDLING)
        secu_erase_status_obj.setCurrentAlgorithmName(SECU_ERASE_NO_ALGORITHM)
    return fname

def erase_free_space_with_dod5220_algorithm(fname: str, secu_erase_status_obj: SecuEraseStatus = None):
    """
    Performs disk free space erasing using the DoD (Department of Defense) 5220.22-M disk sanitization algorithm

    This basically does:
    
    * Filling of all the free disk space with a zeroed disk filler file, then deleting that disk filler file
    * Filling of all the free disk space with a fixed data pattern (0xFF), then deleting that disk filler file
    * Filling of all the free disk space with a random pattern, then deleting that disk filler file

    Parameters:

    fname: str - a string representing the full path to a disk filler file

    secu_erase_status_obj: SecuEraseStatus - an object of SecuEraseStatus (instance of the class) that will have
    its attributes automatically updated during the execution of various stages of the function, it will be useful
    to use this to represent the current status of the secure erasing process to the user.
    (Defaults to None if no object is given, although it is strongly recommended to specify one, at least if you intend
    to use this function on a GUI application)
    """
    print("[DEBUG] erase_free_space_with_dod5220_algorithm: function execution begin")
    if secu_erase_status_obj is not None:
        secu_erase_status_obj.setCurrentAlgorithmName(SECU_ERASE_ALGORITHM_DOD_5220_22_M)
        secu_erase_status_obj.setCurrentPass(1)
        secu_erase_status_obj.setCurrentStageName(SECU_ERASE_ZERO_BYTES_FILL_SINGLE_PASS)
    
    # first things first, we have to do a one pass of zero bytes filling
    try: 
        fill_disk_with_zero_bytes_file(fname)
        print("[DEBUG] erase_free_space_with_dod5220_algorithm: fill_disk_with_zero_bytes_file() successfully finished execution!")
    except: print("[WARNING] erase_free_space_with_dod5220_algorithm: fill_disk_with_zero_bytes_file() error ignored")
    if secu_erase_status_obj is not None:
        secu_erase_status_obj.setCurrentStageName(SECU_ERASE_IDLING)
    
    # now we have to delete the disk filler file
    if secu_erase_status_obj is not None:
        secu_erase_status_obj.setCurrentStageName(SECU_ERASE_DELETING_DISK_FILLER_FILE)
    try: 
        remove(fname)
        print("[DEBUG] erase_free_space_with_dod5220_algorithm: deleted zeroed disk filler file successfully!")
    except: print("[WARNING] erase_free_space_with_dod5220_algorithm: failed to delete zeroed disk filler file!")
    if secu_erase_status_obj is not None:
        secu_erase_status_obj.setCurrentStageName(SECU_ERASE_IDLING)
    
    # now we have to fill our disk with FF characters 
    if secu_erase_status_obj is not None:
        secu_erase_status_obj.setCurrentStageName(SECU_ERASE_FF_BYTES_FILL_SINGLE_PASS)
    try: 
        fill_disk_with_pattern_bytes_file(fname, b'\xFF')
        print("[DEBUG] erase_free_space_with_dod5220_algorithm: fill_disk_with_pattern_bytes_file() function finished execution!")
    except: print("[WARNING] erase_free_space_with_dod5220_algorithm: fill_disk_with_pattern_bytes_file() error ignored")
    # now we have to delete our FF filled file
    if secu_erase_status_obj is not None:
        secu_erase_status_obj.setCurrentStageName(SECU_ERASE_DELETING_DISK_FILLER_FILE)
    try: 
        remove(fname)
        print("[DEBUG] erase_free_space_with_dod5220_algorithm: removed FF filled disk filler file!")
    except: print("[DEBUG] erase_free_space_with_dod5220_algorithm: failed to delete FF filled disk filler file!")
    if secu_erase_status_obj is not None:
        secu_erase_status_obj.setCurrentStageName(SECU_ERASE_IDLING)
    
    # now that we have filled up our disk with 0x00 and 0xFF
    # let's jump straight into the random bytes filling
    if secu_erase_status_obj is not None:
        secu_erase_status_obj.setCurrentStageName(SECU_ERASE_RAND_BYTES_FILL_SINGLE_PASS)
    try: 
        fill_disk_with_rand_bytes_file(fname)
        print(f"[DEBUG] erase_free_space_with_dod5220_algorithm: fill_disk_with_rand_bytes_file() function finished execution!")
    except: print("[WARNING] erase_free_space_with_dod5220_algorithm: fill_disk_with_rand_bytes_file() error ignored")
    # we have to delete the random bytes disk filler file
    if secu_erase_status_obj is not None:
        secu_erase_status_obj.setCurrentStageName(SECU_ERASE_DELETING_DISK_FILLER_FILE)
    try: 
        remove(fname)
        print("[DEBUG] erase_free_space_with_dod5220_algorithm: removed random bytes disk filler file!")
    except: print("[ERROR] erase_free_space_with_dod5220_algorithm: failed to remove random bytes disk filler file!")

    # finished all free disk space erase operations
    print("[DEBUG] erase_free_space_with_dod5220_algorithm: DOD 5220 Algorithm free space erasure has finished execution")
    if secu_erase_status_obj is not None:
        secu_erase_status_obj.setCurrentPass(0)
        secu_erase_status_obj.setCurrentAlgorithmName(SECU_ERASE_NO_ALGORITHM)
        secu_erase_status_obj.setCurrentStageName(SECU_ERASE_IDLING)
    
    return fname

def erase_free_space_with_edod5220_algorithm(fname: str, secu_erase_status_obj: SecuEraseStatus = None) -> str:
    """
    Enchanced Department of Defense 5220.22-M media sanitization algorithm (my own enchancement of that algorithm)

    Actually, the DoD (Department of Defense) 5220.22-M secure media sanitization algorithm was deprecated very long ago
    (25 years ago+) but it remained in media sanitization programs for marketing (mostly) and legacy reasons.

    Source:
    DoD 5220.22-M, National Industrial Security Program Operating Manual (NISPOM).
    Notes: The main body never included a wiping algorithm. Vendor-claimed "7-pass 5220.22-M" isn't in the actual manual. 
    Digging into archived versions shows the appendix that once mentioned overwrites was later removed.

    So I made this function as my own enchancement to this very old and deprecated disk wiping algorithm for those *very*
    paranoid people.

    Here's what it does in detail:

    * Fills free disk space of the volume storing the file `fname` with zero bytes
    * Fills free disk space of the volume storing the file `fname` with a different bytes pattern (66)
    * Fills free disk space of the volume storing the file `fname` with a complementary bytes pattern (99)
    * Fills free disk space of the volume storing the file `fname` with a random bytes from OS's PRNG
    * Fills free disk space of the volume storing the file `fname` with a different bytes pattern (11)
    * Fills free disk space of the volume storing the file `fname` with a different bytes pattern (EE)
    * then lastly, Fills free disk space of the volume storing the file `fname` with random bytes from OS's PRNG.

    PLEASE NOTE: that if volume compression is active, filling free volume space with a single pattern will not actually
    write that pattern into the clusters or the sectors, and all these steps will only be as if we filled the volume
    with random bytes from the OS's PRNG twice.
    
    Returns: `fname`

    Parameters:

    fname: str - full path to the disk filler file that will be used throughout the process.

    secu_erase_status_obj: SecuEraseStatus - a SecuEraseStatus object that will be modified throughout the process and 
    will be used as an indication of the current progress for use with IPC (Interprocess Communication), See the definition
    of the SecuEraseStatus class for more information.
    """
    # here's what we will do
    # fill entire volume's free disk space with zero bytes
    # then delete the disk filler file
    # then fill with 0x66
    # and delete the disk filler file
    # fill with 0x99
    # delete disk filler file
    # fill with rand bytes from OS's PRNG
    # then delete disk filler file
    # fill with 0x11
    # then delete disk filler file
    # fill with 0xEE
    # then delete disk filler file
    # then fill with rand bytes from OS's PRNG
    # then delete disk filler file.
    return fname


if __name__ == '__main__':
    # SIGINT, SIGTERM handling (necessary!)
    signal.signal()
    # argv parsing...
    argc: int = len(argv)
    if argc >= 3: # greater than or eq 3 (executable name, algorithm name, disk filler file full path,
                  # count of passes when using algorithm fill disk with random bytes)
        # argv[1] - algorithm name
        # argv[2] - disk filler file full path
        # argv[3] - optional count of passes when using fill disk with rand bytes algorithm
        secu_erase_status_obj: SecuEraseStatus = SecuEraseStatus()
        if str( argv[1] ) == "rand_bytes_fill": # we are using the rand bytes fill algorithm
                                                # therefore, the user has to explicitly specify
                                                # the number of passes to repeat the random bytes
                                                # disk filling process.
            if argc < 4:
                print(f"[ERROR] secu_delete: passes count is missing!")
                raise SystemExit(67)
            passes_count: int = int( argv[3] )
            disk_filler_fname: str = str( argv[2] )
            print(f"[DEBUG] secu_delete: using algorithm: rand_bytes_fill, passes: {passes_count}, disk filler file: {disk_filler_fname}")
            if passes_count < 1: 
                print(f"[ERROR] secu_delete: passes count is invalid!")
                raise SystemExit(45) # system exit 45 is for invalid number of passes.
            for __cur_pass in range(passes_count):
                secu_erase_status_obj.setCurrentPass(__cur_pass + 1)
                if passes_count > 1: secu_erase_status_obj.setCurrentStageName(SECU_ERASE_RAND_BYTES_FILL_MULTI_PASS)
                else: secu_erase_status_obj.setCurrentStageName(SECU_ERASE_RAND_BYTES_FILL_SINGLE_PASS)
                secu_erase_status_obj.setCurrentAlgorithmName(SECU_ERASE_NO_ALGORITHM)
                # we will write the disk filler file, then delete it
                try: fill_disk_with_rand_bytes_file(disk_filler_fname);print("[DEBUG]: successfully filled disk with rand bytes file!")
                except: print("[WARNING] Error ignored while writing disk filler file")
                secu_erase_status_obj.setCurrentStageName(SECU_ERASE_IDLING)
                # now its the time to delete the disk filler file
                secu_erase_status_obj.setCurrentStageName(SECU_ERASE_DELETING_DISK_FILLER_FILE)
                try: remove(disk_filler_fname);print("[DEBUG] deleted disk filler file successfully!")
                except: print("[WARNING] [CRITICAL] Error ignored while deleting disk filler file")
                secu_erase_status_obj.setCurrentStageName(SECU_ERASE_IDLING)
                print(f"[DEBUG] pass number {__cur_pass} completed!")
        else: # we are using any other disk secure erasure algorithm.
            if str( argv[1] ) == "nist80088": 
                disk_filler_fname: str = str( argv[2] )
                print(f"[DEBUG] secu_delete: using algorithm: {SECU_ERASE_ALGORITHM_NIST_800_88}, disk filler file: {disk_filler_fname}")
                try: 
                    erase_free_space_with_nist800_algorithm(disk_filler_fname, secu_erase_status_obj=secu_erase_status_obj)
                    print("[DEBUG] secu_delete: free space secure erasure with NIST 800.88 completed successfully!")
                except Exception as __algorithm_application_error:
                    print(f"[ERROR] secu_delete: error: {__algorithm_application_error}")
                    raise SystemExit(255) # sys exit 255 is for an algorithm application error.
            elif str( argv[1] ) == "dod522022":
                disk_filler_fname: str = str( argv[2] )
                print(f"[DEBUG] secu_delete: using algorithm: {SECU_ERASE_ALGORITHM_DOD_5220_22_M}, disk filler file: {disk_filler_fname}")
                try:
                    erase_free_space_with_dod5220_algorithm(disk_filler_fname, secu_erase_status_obj=secu_erase_status_obj)
                    print("[DEBUG] secu_delete: free space secure erasure with DoD 5220.22 M completed successfully!")
                except Exception as __algorithm_application_error:
                    print(f"[ERROR] secu_delete: error: {__algorithm_application_error}")
                    raise SystemExit(255)
            else: # not a valid algorithm name
                raise SystemExit(259) # exit code 259 is for an undefined algorithm name

        # we need to delete secu erase status object for shared memory reserved to it
        # to be freed up by the OS.
        del secu_erase_status_obj
        
    else:
        raise SystemExit(25) # exit code 25 is for invalid argc
    raise SystemExit(0)