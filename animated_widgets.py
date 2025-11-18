"""
Animated widgets for use in the UI (User Interface) of Temp_Cleaner GUI


Licensed under the same license as Temp_Cleaner GUI
"""
from customtkinter import *
import threading
import error
import ctypes
import sys, os
from random import randint
from time import sleep, time
import signal
# DEBUGGING ONLY!
# import pdb

# creating a logged Lock to log exactly where the deadlocks might happen.
class LoggedLock(object):
    def __init__(self, name: str) -> None:
        """
        A fancy clone of threading.Lock but with logging to allow you to see if your lock has been released
        after being acquired or not.
        """
        self.name: str = str(name)
        self.lock: threading.Lock = threading.Lock()
        self.__className: str = "LoggedLock"
        self.__acquiredBy: str = ":"
        # used to assist in debugging ONLY
        self.__timeAtAcquiration: float = 0.0
        self.__timeAtRelease: float = 0.0
    
    def acquire(self, blocking=True, timeout: float = -1):
        # pdb.set_trace()
        print(f"[DEBUG] {self.__className}: - Trying to acquire lock \"{self.name}\"@{id(self)} by thread {threading.current_thread().name}" +
              f" with ID: {threading.current_thread().ident}" + f"...")
        retVal: bool = self.lock.acquire(blocking, timeout)
        self.__acquiredBy = f"{threading.current_thread().name}:{threading.current_thread().ident}"
        if retVal == True:
            # we will start counting timeAtAquiration from here only since at this point
            # the Lock would be acquired.
            # PLEASE NOTE: That this approach may not be the most suitable one, especially if the program
            # is running on a computer that may change its time at any stage while the Lock was acquired
            # or is being released.
            self.__timeAtAcquiration = time()
            print(f"[DEBUG] {self.__className}: - Successfully Acquired Lock \"{self.name}\"@{id(self)} by thread {threading.current_thread().name}" +
                  f" with ID: {threading.current_thread().ident}!")
            return True
        else:
            print(f"[DEBUG] {self.__className}: - Failed to acquire non-blocking lock \"{self.name}\"@{id(self)} by thread {threading.current_thread().name}" + 
                  f" with ID: {threading.current_thread().ident}!")
            return False
    
    def release(self):
        # pdb.set_trace()
        print(f"[DEBUG] {self.__className}: - Releasing Lock \"{self.name}\"@{id(self)} by thread {threading.current_thread().name}" + 
              f" with ID: {threading.current_thread().ident}...")
        try:
            self.lock.release()
            self.__acquiredBy = ":"
            # we will get the time at this point since here it will only calculate if the lock was successfully
            # released.
            self.__timeAtRelease = time()
        except RuntimeError:
            # we tried to release a lock that wasn't acquired in the first place.
            print(f"[DEBUG] {self.__className}: - Failed to release Lock\"{self.name}\"@{id(self)} by thread {threading.current_thread().name}" + 
                  f" with ID: {threading.current_thread().ident}: Lock was not acquired in the first place!")
            return None
        except Exception as __errReleasingLock:
            # we failed to release the lock, silently log to debugging console.
            print(f"[DEBUG] {self.__className}: - Failed to release Lock \"{self.name}\"@{id(self)} by thread {threading.current_thread().name}" + 
                  f" with ID: {threading.current_thread().ident}: {__errReleasingLock}!")
            return None
        # for printing to the debugging console that Lock was successfully released.
        __acquiredFor: float = abs(float(self.__timeAtRelease - self.__timeAtAcquiration))
        print(f"[DEBUG] {self.__className}: - Released Lock \"{self.name}\"@{id(self)} by thread {threading.current_thread().name}" +
              f" with ID: {threading.current_thread().ident}!, The Lock was acquired for {__acquiredFor} seconds.")
        return None

    def _acquiredBy(self) -> str:
        """
        For internal debugging use ONLY!
        """
        return self.__acquiredBy

    def __enter__(self):
        self.acquire()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()
        return None # for not wanting to swallow exceptions.


# we must retrieve the absolute path where this module is located in first
# initializing a variable containing the path where program executable is stored.
application_path = ''

# a quick check whether if program is a compiled bundle by pyinstaller or a simple python file.
if getattr(sys, 'frozen', False):
    # pyinstaller creates a sys attribute frozen=True during startup of pyinstaller bootloader to indicate
    # that pyinstaller has compiled (frozen) this program, then it creates a sys constant _MEIPASS containing the path
    # where the executable is found.
    application_path = sys._MEIPASS
else: # if program is running as a python script via python terminal
    application_path = os.path.dirname(os.path.abspath(__file__))

print(f"[DEBUG]: animated_widgets module located at: {application_path}")


# list that holds numbers generated used for thread names so we don't use them again
usedNumbers: list[int] = []

def generateThreadName(prefix: str, start_range=1, end_range=10240) -> str:
    """
    Generates a thread name with 'prefix' as the prefix and with some random integers at the end

    Parameters:

    * prefix: str - a prefix for the generated thread name, should be something good enough to represent
    what will this thread be used for.

    * start_range: int - the start range to use in the random number generator, default is 1

    * end_range: int - the end range to use in the random number generator, default is 1024
    """
    global usedNumbers
    _thd_name: str = f"{prefix}_"
    # initially set to True, will set to False when not found
    _num_used_before: bool = True
    while _num_used_before:
        _generated_rand_int: int = randint(start_range, end_range)
        # if the number generated was not used before, we will claim it
        # and add it to the list, otherwise, we will ignore it and keep
        # generating.
        if _generated_rand_int not in usedNumbers:
            _num_used_before = False # which breaks the loop
    # appending our uniquely generated number into usedNumbers list
    usedNumbers.append(_generated_rand_int)
    # appending our _generated_rand_int to the generated thread name.
    _thd_name = f"{_thd_name}{_generated_rand_int}"
    # next up, we return it to the caller.
    return _thd_name


# will be used for automatically terminating any animation thread.
def _async_raise(tid, exctype=error.AutomatedThreadTermination):
    """
    Raises an exception in the threads with ID using ExceptionType defined

    `tid` -> is the ID (identification number) of the thread you want to raise the Exception in

    `exctype` -> Is the class/object of the Exception you want to raise in the thread.
    """
    # if not threading.inspect.isclass(exctype):
    #     raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid),
                                                    ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # "if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


# a controllable thread class that we will use for the thread objects for the animation
class ControllableThread(threading.Thread):
    def __init__(self, *args, **kwargs) -> None:
        """
        A class for a thread that can be stopped manually (or automatically) within any parts of the program

        It has all the following functions:
        
        `_get_my_tid()` -> Returns the current Thread ID (Identification Number)

        `raiseExc()` -> Used to raise an Exception in the current thread.

        Used primarly in the cleaning thread but may be later used in any parts of the program
        """
        super(__class__, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()
    
    def _get_my_tid(self):
        """determines this (self's) thread id

        CAREFUL: this function is executed in the context of the caller
        thread, to get the identity of the thread represented by this
        instance.
        """
        if not self.is_alive():
            raise threading.ThreadError("the thread is not active")

        # do we have it cached?
        if hasattr(self, "_thread_id"):
            return self._thread_id

        # no, look for it in the _active dict
        for tid, tobj in threading._active.items():
            if tobj is self:
                self._thread_id = tid
                return tid

        # TODO: in python 2.6, there's a simpler way to do: self.ident

        raise AssertionError("could not determine the thread's id")

    def raiseExc(self):
        """Raises the default exception type `UserInitiatedThreadStop` in the context of this thread.

        If the thread is busy in a system call (time.sleep(),
        socket.accept(), ...), the exception is simply ignored until the another command is executed

        If you are sure that your exception should terminate the thread,
        one way to ensure that it works is:

            t = ThreadWithExc( ... )
            ...
            t.raiseExc( SomeException )
            while t.isAlive():
                time.sleep( 0.1 )
                t.raiseExc( SomeException )

        If the exception is to be caught by the thread, you need a way to
        check that your thread has caught it.

        CAREFUL: this function is executed in the context of the
        caller thread, to raise an exception in the context of the
        thread represented by this instance.
        """
        _async_raise(self._get_my_tid())


class HoverShrinkAnimatedButton(CTkFrame):
    def __init__(self, master, buttonCommand=None, buttonText="Button", *args, **kwargs):
        """
        A button with rounded corners and shrink hover animation.

        * UPDATE 1: Improved Exception handling and Fixed deadlocks that occured when destroying the button while 
        any animation was already running on it.

        Accepts args and kwargs the same way a normal CTkFrame would, except for some additional parameters:

        * buttonCommand - a callable object that will be called when the button is clicked
        * buttonText - Text to be displayed on the button

        * Don't forget to give it a foreground color (via the keyword arg: fg_color) to make it distinguishable
        from other UI elements.
        """
        global application_path
        super().__init__(master, *args, **kwargs)
        self.buttonCommand = buttonCommand
        self.buttonText = buttonText
        # a Lock to prevent race conditions.
        self.sharedAttribsLocker: LoggedLock = LoggedLock(name="sharedAttribsLocker")
        def __poll_shutdown_evt():
            if self.__canDestroy.is_set():
                super().destroy()
            return
        # a threading.Event to use so that we can tell the main thread to safely destroy Tk.
        self.__canDestroy: threading.Event = threading.Event()
        # clear the event (just in case)
        self.__canDestroy.clear()
        # control variables we use to help us determine if the button or the frame was destroyed or not.
        with self.sharedAttribsLocker:
            self.rootExists: bool = False
        # let's try to load our style file
        try:
            set_default_color_theme(f"{application_path}\\style.json")
        except Exception as __errorLoadingStyleF:
            print(f"[DEBUG] {self.__str__}: failed to load custom style file: {__errorLoadingStyleF}")
        # we must construct a simple CTkButton inside.
        # this CTkButton is what we will actually be animating
        # and our frame will just be a placeholder to prevent animation glitches
        self.button = CTkButton(self, text=self.buttonText, command=self.buttonCommand)
        # I want it to fill up the entire frame for now.
        self.button.place(relx=0, rely=0, relwidth=1, relheight=1)

        # enter event handler function definition
        def enterEventHandler(keybinding_arg) -> bool | None:
            FUNCTION_NAME: str = "enterEventHandler"
            """
            Handler function for <Enter> event.

            Responsible for starting the size reduction thread, and ensuring only one instance of it is running.
            """
            # lets first check if thread is already running
            print(f"[DEBUG] {FUNCTION_NAME}: checking if animation thread is already running or not")
            for __thd in threading.enumerate():
                print(f"[DEBUG] {FUNCTION_NAME}: thread {__thd.name}")
                if str(__thd.name) == self.sizeReductionAnimationThdName:
                    print(f"[DEBUG] {FUNCTION_NAME}: thread {self.sizeReductionAnimationThdName} is running, will NOT start it again!")
                    return False
            # if the function is still executing til this stage, it means thread is not running.
            # but let's redefine it just in case it previously ran.
            self.sizeReductionAnimationThdObj = ControllableThread(target=self.runSizeReductionAnimation, name=self.sizeReductionAnimationThdName, daemon=False)
            try:
                print(f"[DEBUG] {FUNCTION_NAME}: size reduction animation thread was not found to be running, will start it now...")
                self.sizeReductionAnimationThdObj.start()
                print(f"[DEBUG] {FUNCTION_NAME}: started thread {self.sizeReductionAnimationThdName}!")
            except RuntimeError:
                print(f"[WARNING] {FUNCTION_NAME}: thread {self.sizeReductionAnimationThdName} is running but not detected by first detection stage, will not start it again.")
                return False
            except Exception as __errStartingThd:
                # report error to console (visible in DEBUG builds ONLY)
                print(f"[ERROR] {FUNCTION_NAME}: failed to start thread {self.sizeReductionAnimationThdName}!: {__errStartingThd}")
                print(f"[INFO] {FUNCTION_NAME}: a visible error window has been shown to the user, please attach a screenshot of it and create a support ticket/issue.")
                # I think in this case it is safe to report the error to the user
                errWindow: error.ErrorWindow = error.ErrorWindow(f"An error has occured at the execution of the function {FUNCTION_NAME}!\nStage: attempt to start thread {self.sizeReductionAnimationThdName}\nError details:\n{__errStartingThd}\nPlease screenshot this window and attach it with an issue in the program's official Github repository or support tickets...")
                errWindow.wait_window()
                print(f"[DEBUG] {FUNCTION_NAME}: visible error window has been dismissed/closed")
                # we return False if something went wrong.
                return False
            return
        
        def leaveEventHandler(keybinding_arg) -> bool | None:
            FUNCTION_NAME: str = "leaveEventHandler"
            """
            Handler Function for <Leave> Event.

            Responsible for starting the size restoration animation thread, and ensuring there will be only a single instance of it
            running.
            """
            # let's check if the thread is already running.
            print(f"[DEBUG] {FUNCTION_NAME}: checking for running instances of {self.sizeRestorationAnimationThdName}...")
            for __thd in threading.enumerate():
                print(f"[DEBUG] {FUNCTION_NAME}: thread {__thd.name}")
                if str(__thd.name) == self.sizeRestorationAnimationThdName:
                    # an instance of the size restoration animation thread is already running.
                    print(f"[DEBUG] {FUNCTION_NAME}: size restoration animation thread instance is already running, will not run another instance.")
                    return False
            # if it reaches this point then size restoration animation thread is not running.
            print(f"[DEBUG] {FUNCTION_NAME}: size restoration animation thread is not running, starting now...")
            # let's redefine the thread object in case it previously ran.
            self.sizeRestorationAnimationThdObj = ControllableThread(target=self.runSizeRestorationAnimation, name=self.sizeRestorationAnimationThdName, daemon=False)
            try:
                self.sizeRestorationAnimationThdObj.start()
                print(f"[DEBUG] {FUNCTION_NAME}: size restoration animation thread has been started!")
            except RuntimeError:
                print(f"[WARNING] {FUNCTION_NAME}: size restoration animation thread {self.sizeRestorationAnimationThdName} is already running but not detected by first stage.")
                return False
            except Exception as __errStartingSizeRestoreThd:
                # silently log to DEBUG console.
                print(f"[ERROR] {FUNCTION_NAME}: failed to start size restoration animation thread, error details: {__errStartingSizeRestoreThd}")
                return False
            return
        
        # generated thread name for the safe destroy flag.
        self.__setSafeDestroyFlagThdName: str = generateThreadName("AnimatedBtn_SetSafeDestroyFlagThread").upper()
        self.__setSafeDestroyFlagThdObj: ControllableThread = ControllableThread(target=self.__internal_setSafeDestroyFlag, name=self.__setSafeDestroyFlagThdName, daemon=False)

        # generated thread name for the size reduction animation thread.
        self.sizeReductionAnimationThdName: str = generateThreadName("AnimatedBtn_SizeReduction_Animation").upper()
        # the controllable thread object used for the size reduction animation.
        self.sizeReductionAnimationThdObj: ControllableThread = ControllableThread(target=self.runSizeReductionAnimation, name=self.sizeReductionAnimationThdName, daemon=False)
        # generated thread name for the size restoration animation thread.
        self.sizeRestorationAnimationThdName: str = generateThreadName("AnimatedBtn_SizeRestoration_Animation").upper()
        # the controllable thread object used for size restoration animation.
        self.sizeRestorationAnimationThdObj: ControllableThread = ControllableThread(target=self.runSizeRestorationAnimation, name=self.sizeRestorationAnimationThdName, daemon=False)
        self.bind("<Enter>", lambda e: enterEventHandler(e)) # we will bind those to a function that detects if thread is already running or not.
        self.button.bind("<Enter>", lambda e: enterEventHandler(e))
        # binding leave event to the leave event handler
        self.bind("<Leave>", lambda e: leaveEventHandler(e))
        self.button.bind("<Leave>", lambda e: leaveEventHandler(e))
        # binding the click event on the frame to run the command of the button
        self.bind("<Button-1>", lambda e: self.buttonCommand())
        # let's disable grid propagation just in case
        self.grid_propagate(False)
        # register our poll shutdown event
        self.after(500, __poll_shutdown_evt)
        # a method to handle the destroy event for each widget.        
        # making a new thread object to run the destroy event handler.
        # note how I only binded that <Destroy> event to the button widget, not to the entire root
        # this because if I binded that event to the root window, the bound function gets called for the
        # number of widgets (children of the root) that were destroyed too.
        # update control variables.
        with self.sharedAttribsLocker:
            self.rootExists = True
    
    # a method for setting the destroy flag and actually destroying the widget.
    def __internal_setSafeDestroyFlag(self) -> None:
        FUNCTION_NAME: str = "__internal_setSafeDestroyFlag"
        # let's change the safe destroy flag (to instruct our animation threads that we want to exit)
        with self.sharedAttribsLocker:
            self.rootExists = False
        
        # let's join animation threads.. (just in case they were running)
        if self.sizeReductionAnimationThdObj.is_alive():
            print(f"[DEBUG] {FUNCTION_NAME}@{id(self)}: joining size reduction animation thread...")
            self.sizeReductionAnimationThdObj.join()
        
        if self.sizeRestorationAnimationThdObj.is_alive():
            print(f"[DEBUG] {FUNCTION_NAME}@{id(self)}: joining size restoration animation thread...")
            self.sizeRestorationAnimationThdObj.join()
        
        print(f"[DEBUG] {FUNCTION_NAME}@{id(self)}: It is safe to destroy widget right now!")
        # super().destroy() -> causes a deadlock when called from another thread other than
        # the main thread.
        self.__canDestroy.set()
        return None
    
    # we have to override the configure method to allow us to change text manually
    def configure(self, require_redraw=False, state=None, text=None, command=None, **kwargs):
        """
        super class method override for configure()

        # update 2: adds exception handling for the case when widget is already destroyed.
        """
        if self.sharedAttribsLocker.acquire() and (self.sharedAttribsLocker.release() or True) and self.rootExists:
            if text != None:
                self.buttonText = text
                self.button.configure(text=self.buttonText)
            if state != None:
                self.button.configure(state=state)
            if command != None:
                self.buttonCommand = command
                self.button.configure(command=self.buttonCommand)
            return super().configure(require_redraw, **kwargs)
        # we won't do anything if our widget does not exist or is destroyed
        return None

    def runSizeReductionAnimation(self) -> bool | None:
        # the function that contains the exception handling for the thread that will run the size reduction animation
        FUNCTION_NAME_0: str = "runSizeReductionAnimation"
        try: 
            print(f"[DEBUG] {FUNCTION_NAME_0}@{threading.current_thread().name}:{threading.current_thread().ident}: executing self.applySizeReductionAnimation()...")
            self.applySizeReductionAnimation()
            print(f"[DEBUG] {FUNCTION_NAME_0}@{threading.current_thread().name}:{threading.current_thread().ident}: self.applySizeReductionAnimation() finished execution!")
        except error.AutomatedThreadTermination:
            # thread has been terminated automatically from a function that does some job
            # that can't bear seeing it running, so in this case we will do nothing but exit the function
            self.sharedAttribsLocker.release()
            return
        except Exception as __errDetails:
            self.sharedAttribsLocker.release()
            # silently print error to console (visible in DEBUG builds ONLY)
            print(f"[WARNING] {FUNCTION_NAME_0}@{threading.current_thread().name}:{threading.current_thread().ident}: execution of self.applySizeReductionAnimation() failed, Error details: {__errDetails}")
            # we will return False if an error occurs.
            return False
        print(f"[DEBUG] {FUNCTION_NAME_0}@{threading.current_thread().name}:{threading.current_thread().ident}: finished execution!")
        return


    def applySizeReductionAnimation(self):
        FUNCTION_NAME: str = "applySizeReductionAnimation"
        """
        The function that has the actual logic for reducing the button's size

        MUST NOT BE BINDED TO THE ENTER EVENT DIRECTLY, INSTEAD, SHOULD BE CALLED FROM WITHIN
        A FUNCTION THAT HAS EXCEPTION HANDLING AND RUNS UNDER A DIFFERENT THREAD.
        """
        # we need to check if mouse pointer is still on top of the button or the widget itself
        try:
            __isHoveringOverParent: bool = self.winfo_containing(self.winfo_pointerx(), self.winfo_pointery()).master == self
        except AttributeError: # AttributeError is raised if mouse pointer was quickly moved out of parent's boundaries.
            __isHoveringOverParent: bool = False
        except Exception:
            __isHoveringOverParent: bool = False
        
        try:
            __isHoveringOverButton: bool = self.winfo_containing(self.winfo_pointerx(), self.winfo_pointery()).master == self.button
        except AttributeError:
            __isHoveringOverButton: bool = False
        except Exception:
            __isHoveringOverButton: bool = False
        
        if ((
            # checking first if the root exists or not (for thread safety).
            self.sharedAttribsLocker.acquire() and (self.sharedAttribsLocker.release() or True) and self.rootExists
        ) and (
            __isHoveringOverParent or __isHoveringOverButton
        )):
            print(f"[DEBUG] {FUNCTION_NAME}: mouse pointer is on top of button or the button parent (holding frame)")
            # this means the user actually intends to run the size reduction animation!
            # now we must check if the button has relwidth = 1.0 and relheight = 1.0 too
            if ((
                # check if our button/root has already been destroyed or not (for thread safety)
                self.sharedAttribsLocker.acquire() and (self.sharedAttribsLocker.release() or True) and self.rootExists
            ) and (
                (round(float(self.button.place_info().get("relwidth")),1) == 1.0) and (
                round(float(self.button.place_info().get("relheight")),1) == 1.0)
            )):
                # button size hasn't been modified by any other thread yet, therefore it is safe to run animation
                print(f"[DEBUG] {FUNCTION_NAME}: button relwidth = 1 & button relheight = 1, which means its safe to run size reduction animation!")
                # now we need to check if our button has the default relx and rely
                if ((
                    # check if parent was destroyed or not (for thread safety)
                    self.sharedAttribsLocker.acquire() and (self.sharedAttribsLocker.release() or True) and self.rootExists
                ) and ((
                    round(float(self.button.place_info().get("relx")),1) == 0.0
                ) and (
                    round(float(self.button.place_info().get("rely")),1) == 0.0
                ))):
                    # button has default relx and rely, it is safe to run animation
                    print(f"[DEBUG] {FUNCTION_NAME}: button has default relx = 0 & default rely = 0, we can run animation on it!")
                    # now let's actually reduce the button's size
                    # constants and variables needed to achieve this job:
                    _steps: int = 35 # controls animation smoothness, higher value means more smooth
                    _target_btn_relwidth: float = 0.6000
                    _target_btn_relheight: float = 0.6000
                    _delta_w: float = ((1.0 - _target_btn_relwidth) / _steps)
                    _delta_h: float = ((1.0 - _target_btn_relheight) / _steps)
                    print(f"[DEBUG] {FUNCTION_NAME}: target relwidth: {_target_btn_relwidth}, target relheight: {_target_btn_relheight}, and steps are: {_steps}")
                    print(f"[DEBUG] {FUNCTION_NAME}: delta_w is {_delta_w}, and delta_h is {_delta_h}")
                    # sleep for 0.25 sec to make sure user really serious about hovering over the widget
                    sleep(0.25)
                    # enter loop
                    for _step in range(1, _steps, 1): # start from 1, end at _steps, go 1 step at a time.
                        # we must (again) check if mouse pointer is still hovering over the button
                        # or its holding frame before we start to actually reduce the size of the button.
                        # exception handling: for the case when user moves mouse pointer quickly outside the widget's boundaries.
                        try:
                            __isHoveringOverParent: bool = self.winfo_containing(self.winfo_pointerx(), self.winfo_pointery()).master == self
                        except AttributeError:
                            __isHoveringOverParent: bool = False
                        except Exception:
                            __isHoveringOverParent: bool = False

                        try:
                            __isHoveringOverButton: bool = self.winfo_containing(self.winfo_pointerx(), self.winfo_pointery()).master == self.button
                        except AttributeError:
                            __isHoveringOverButton: bool = False
                        except Exception:
                            __isHoveringOverButton: bool = False
                        
                        if ((
                            self.sharedAttribsLocker.acquire() and (self.sharedAttribsLocker.release() or True) and self.rootExists
                        ) and ((
                            __isHoveringOverParent
                        ) or (
                            __isHoveringOverButton
                        ))):
                            # pointer is still over the button holder frame or the button itself,
                            # therefore it is safe to continue!
                            # declare variables that will hold new relwidth, relheight, relx, and rely.
                            _new_relwidth: float = (1.0 - (_delta_w * _step))
                            _new_relheight: float = (1.0 - (_delta_h * _step))
                            _new_relx: float = ((1 - _new_relwidth) / 2)
                            _new_rely: float = ((1 - _new_relheight) / 2)
                            # we will do place configure for the button
                            with self.sharedAttribsLocker:
                                if not self.rootExists:
                                    print(f"[DEBUG] {FUNCTION_NAME}@{id(self)}: will not continue since button has been destroyed.")
                                    return None
                                self.button.place_configure(
                                    relx=_new_relx,
                                    rely=_new_rely,
                                    relwidth=_new_relwidth,
                                    relheight=_new_relheight
                                )
                            # might aswell add some delay
                            sleep(0.010)
                        else:
                            # pointer is not hovering over the button holder frame or the button itself
                            # we will silently exit the execution of this function and log it to the debug console
                            print(f"[DEBUG] {FUNCTION_NAME}: at step {_step}/{_steps} mouse is not hovering over button or its holder frame, will not continue")
                            # Run restore animation function but with a special argument that prevents it from 
                            # stopping this thread (the size reduction animation thread)
                            self.applySizeRestorationAnimation(terminateSizeReductionAnimationThd=False)
                            return False
                else:
                    # button doesn't have default relx and rely, therefore we will silently report this
                    print(f"[DEBUG] {FUNCTION_NAME}: button doesn't have default relx or rely, therefore we will not run animation on it.")
                    return
            else:
                # button size has been modified by some other running thread, therefore it isn't safe to
                # reduce its size manually right now, so we will silently quit for now
                print(f"[DEBUG] {FUNCTION_NAME}: button relwidth and relheight aren't the default ones, it is possible that it is being modified right now.")
                return
        else:
            # mouse is not on top of the button or the widget, therefore no need to animate anything
            print(f"[DEBUG] {FUNCTION_NAME}: mouse is NOT over the button or the holding frame, No need to run animation!")
            return # exit from function.
        # just in case.
        return

    def __str__(self) -> str:
        return "HoverShrinkAnimatedButton class"
    
    # methods for button size restoration animation (internal methods, DO NOT CALL MANUALLY)
    def applySizeRestorationAnimation(self, terminateSizeReductionAnimationThd=True):
        FUNCTION_NAME: str = "applySizeRestorationAnimation"
        print(f"[DEBUG] {FUNCTION_NAME}: execution begin...")
        # check if mouse cursor is still hovering over the button or its holder frame
        try:
            __isHoveringOverButton: bool = self.winfo_containing(self.winfo_pointerx(), self.winfo_pointery()).master == self.button
        except AttributeError:
            __isHoveringOverButton: bool = False
        except Exception:
            __isHoveringOverButton: bool = False
        
        try:
            __isHoveringOverMaster: bool = self.winfo_containing(self.winfo_pointerx(), self.winfo_pointery()).master == self
        except AttributeError:
            __isHoveringOverMaster: bool = False
        except Exception:
            __isHoveringOverMaster: bool = False
        if (
            (
                # check to see if the widget was destroyed or not (for thread safety, of course).
                self.sharedAttribsLocker.acquire() and (self.sharedAttribsLocker.release() or True) and self.rootExists
            )
            and
            (
                (
                    __isHoveringOverMaster
                ) or (
                    __isHoveringOverButton
                )
            )
        ):
            # release the lock (Important!)
            # self.sharedAttribsLocker.release()
            # mouse pointer is on top of the button or its holder frame
            print(f"[DEBUG] {FUNCTION_NAME}: mouse pointer is hovering over button or its holder frame, we can't continue running the animation!")
            return False # we don't need to do anything for now.
        else:
            # release the lock (Important!)
            # self.sharedAttribsLocker.release()
            # mouse pointer is not hovering over button or its holder frame
            # therefore its safe to continue running the animation
            print(f"[DEBUG] {FUNCTION_NAME}: mouse pointer is not hovering over button or its holder frame, executing animation logic...")
            # next up we will need to check if we must terminate the size reduction animation thread
            if terminateSizeReductionAnimationThd:
                # yes, we must terminate the size reduction animation thread.
                print(f"[DEBUG] {FUNCTION_NAME}: size reduction animation thread will be terminated!")
                try:
                    while self.sizeReductionAnimationThdObj.is_alive(): # condition is only True if thread is running
                        print(f"[DEBUG] {FUNCTION_NAME}: size reduction animation thread is alive, will terminate it forceibly...")
                        with self.sharedAttribsLocker:
                            self.sizeReductionAnimationThdObj.raiseExc()
                        print(f"[DEBUG] {FUNCTION_NAME}: sent exception to the size reduction animation thread.")
                    # if we exit this loop, it means that our thread has been successfully terminated!
                    print(f"[DEBUG] {FUNCTION_NAME}: size reduction animation thread has been successfully terminated!")
                except Exception as __errTerminatingThd:
                    # we will silently log to the DEBUG console
                    print(f"[ERROR] {FUNCTION_NAME}: failed to terminate size reduction animation thread, error details: {__errTerminatingThd}")
            # now let's check if current relwidth and relheight both are 1.0 (the default values) of the button
            # but we must store the values into variables for later use (in calculating deltas)
            # thread safety additions (fixes deadlocks)
            with self.sharedAttribsLocker:
                if not self.rootExists:
                    print(f"[DEBUG] {FUNCTION_NAME}: button has already been destroyed, can't continue!")
                    return False
                __current_relwidth: float = float(self.button.place_info().get("relwidth"))
                __current_relheight: float = float(self.button.place_info().get("relheight"))
            # now let's do the comparsion.
            if float(__current_relwidth) == 1.0 and float(__current_relheight) == 1.0:
                # current relwidth and relheight both are 1.0 (default values)
                # so we must return False since button already has default size (before the size reduction animation)
                print(f"[DEBUG] {FUNCTION_NAME}: current button relwidth and relheight are 1.0 (default values), no need to run any size restoration animation!")
                return False
            else:
                # current relwidth and relheight aren't the default values (1.0)
                # something could possibly have modified them (for example the size reduction thread)
                # therefore we must run the size restoration animation
                # but first we have to check if button's relx and rely are the default values (0)
                with self.sharedAttribsLocker:
                    if not self.rootExists:
                        print(f"[DEBUG] {FUNCTION_NAME}: button has already been destroyed, can't continue!")
                        return False
                    __current_relx: float = float(self.button.place_info().get("relx"))
                    __current_rely: float = float(self.button.place_info().get("rely"))
                if float(__current_relx) == 0 and float(__current_rely) == 0:
                    # widget has default relx and rely, it's not safe to run the size restoration animation thread for now.
                    print(f"[DEBUG] {FUNCTION_NAME}: button has default relx and rely (0), can't run size restoration animation!")
                    return False
                else:
                    # widget doesn't have default relx and rely, it's safe to run the size restoration animation thread!
                    # but first we have to declare some variables
                    __steps: int = 35
                    __target_relwidth: float = 1.0
                    __target_relheight: float = 1.0
                    __delta_h: float = ((__target_relheight - __current_relheight) / __steps)
                    __delta_w: float = ((__target_relwidth - __current_relwidth) / __steps)
                    # enter loop
                    for __step in range(1, __steps, 1):
                        # declare some variables
                        __new_relwidth: float = float(__current_relwidth) + (__delta_w * __step)
                        __new_relheight: float = float(__current_relheight) + (__delta_h * __step)
                        __new_rely: float = ((__target_relheight - __new_relheight) / 2)
                        __new_relx: float = ((__target_relwidth - __new_relwidth) / 2)
                        with self.sharedAttribsLocker:
                            if not self.rootExists:
                                print(f"[DEBUG] {FUNCTION_NAME}: button has been destroyed, can't continue!")
                                return False
                            self.button.place_configure(
                                relwidth=__new_relwidth,
                                relheight=__new_relheight,
                                relx=__new_relx,
                                rely=__new_rely
                            )
                        sleep(0.010)
        return # just in case


    def runSizeRestorationAnimation(self) -> bool | None:
        FUNCTION_NAME: str = "runSizeRestorationAnimation"
        # a function that will be ran by the button size restoration animation thread
        print(f"[DEBUG] {FUNCTION_NAME}@{threading.current_thread().name}:{threading.current_thread().ident}: execution started...")
        try:
            print(f"[DEBUG] {FUNCTION_NAME}@{threading.current_thread().name}:{threading.current_thread().ident}: executing applySizeRestorationAnimation()...")
            self.applySizeRestorationAnimation()
            print(f"[DEBUG] {FUNCTION_NAME}@{threading.current_thread().name}:{threading.current_thread().ident}: function applySizeRestorationAnimation() finished execution!")
        except error.AutomatedThreadTermination:
            # we will not do anything here, nor log anything to the DEBUG console
            # since this error will be thrown when the thread is terminated automatically
            # Fix for Lock that gets aquired even after the thread is terminated.
            # if self.sharedAttribsLocker._acquiredBy() == f"{threading.current_thread().name}:{threading.current_thread().ident}":
            self.sharedAttribsLocker.release()
            return
        except Exception as __errDetails:
            # if self.sharedAttribsLocker._acquiredBy() == f"{threading.current_thread().name}:{threading.current_thread().ident}":
            self.sharedAttribsLocker.release()
            # exception handling for when an actual error happens
            # we will silently log the error to the debug console for now.
            print(f"[ERROR] {FUNCTION_NAME}@{threading.current_thread().name}:{threading.current_thread().ident}: error on function applySizeRestorationAnimation() execution, error details: {__errDetails}")
            return False # will return False to indicate an error.
        print(f"[DEBUG] {FUNCTION_NAME}@{threading.current_thread().name}:{threading.current_thread().ident}: finished execution!")
        return # on call success
    
    # overriding the destroy method
    def destroy(self) -> None:
        """
        Class method destroy() override, this ensures safe destruction.

        PLEASE NOTE THAT INSTRUCTIONS/STATEMENTS WRITTEN IN HERE WILL BE EXECUTED BY THE MAIN THREAD!
        """
        FUNCTION_NAME: str = "destroy"
        print(f"[DEBUG] {FUNCTION_NAME}@{id(self)}: execution started...")
        # we will run the thread that sets the flag and does the actual widget destruction.
        # BUT NOT SO FAST, we have to first check whether or not it is currently running.
        __thds_objs: list[threading.Thread] = threading.enumerate()
        for __thd_obj in __thds_objs:
            print(f"[DEBUG] {FUNCTION_NAME}@{id(self)}: Thread: {__thd_obj.name}")
            if str(__thd_obj.name).upper() == self.__setSafeDestroyFlagThdName:
                print(f"[DEBUG] {FUNCTION_NAME}@{id(self)}: Found set safe destroy flag thread to be already running, will not continue!")
                return None
        
        # let's redefine our thread object (just in case)
        self.__setSafeDestroyFlagThdObj = ControllableThread(target=self.__internal_setSafeDestroyFlag, name=self.__setSafeDestroyFlagThdName, daemon=False)
        # next up, we will try to run it.
        try:
            self.__setSafeDestroyFlagThdObj.start()
        except RuntimeError:
            print(f"[WARNING] {FUNCTION_NAME}@{id(self)}: set safe destroy flag thread is running but was not detected as running in the first detection stage, Can't continue!")
            return None
        except Exception as __errStartingSSDFThd:
            # silently log to debugging console (or maybe display explicitly to the user?)
            print(f"[ERROR] {FUNCTION_NAME}@{id(self)}: failed to start the set safe destroy flag thread: {__errStartingSSDFThd}!")
            return None
                
        return None


# constructing a simple test window
class TestWindow(CTk):
    def __init__(self, fg_color = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.title("sample window")
        self.geometry("800x600")
        self.resizable(True, True)
        for _0 in range(3):
            # for rows
            for _ in range(3):
                # for columns
                setattr(
                    self,
                    f"btn{_0}{_}",
                    HoverShrinkAnimatedButton(self, buttonCommand=None, buttonText=f"{_0}x{_}", fg_color="#333")
                )
                getattr(self, f"btn{_0}{_}").grid(column=_, row=_0, sticky='w')    

if __name__ == '__main__':
    wnd = TestWindow()
    wnd.mainloop()