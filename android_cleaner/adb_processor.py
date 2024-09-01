"""
Provides normal functions for ADB USB Connectivity to Android smartphones for Temp_Cleaner GUI's Android 7.x+ phones Cleaner.

Copyright (C) 2024 - Ziad Ahmed (Mr.X)
ADB (Android Debug Bridge) is a product of Google, inc. for Android and Android Studio, and is not owned nor is copyrighted by the owner of Temp_Cleaner GUI.
"""
# imports
import os, sys
from subprocess import getoutput
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

print(f"[DEBUG]: connection_window module located at: {application_path}")
# fixes for translations module outside of cwd.
sys.path.append(f"{application_path}\\..")
# adb executable path.
adb_exe_path = f"{application_path}\\adb\\adb.exe"

def requestADBConnection():
    """
    Requests an ADB Connection to the currently connected Android smartphone.
    
    Returns the output of the ADB connection command.
    """
    global adb_exe_path
    adb_connection_cmd_out = getoutput(f"{adb_exe_path} usb")
    return adb_connection_cmd_out

def killADBDaemon():
    """
    Requests to kill the currently running ADB Daemon
    
    Returns the output of the kill ADB Daemon command
    """
    global adb_exe_path
    adb_kill_daemon_cmd = getoutput(f"{adb_exe_path} kill-server")
    return adb_kill_daemon_cmd

def listADBDevices():
    """
    Returns a list containing all devices connected in USB Debugging mode.
    """
    global adb_exe_path
    dummy_words = ["daemon", "List", "attached", "started", "successfully", "starting"]
    real_devs = []
    
    
    adb_devices_output = getoutput(f"{adb_exe_path} devices")
    adb_devices_output = adb_devices_output.splitlines()
    pas = 0
    for output in adb_devices_output:
        for word in output.split():
            if word in dummy_words:
                pas = 1
                break
        if pas == 1:
            pas = 0
            continue
        else:
            real_devs.append(output)
    
    # adb_devices_output = adb_devices_output[len(adb_devices_output) -1]
    return real_devs

def needToShowInstructionsWindow():
    """
    This function returns a boolean, indicating whether the application needs to show the user the instructions
    for a proper ADB USB Connection or no.
    
    True means yes, False means No
    """
    dev_list = listADBDevices()
    if len(dev_list) == 0: # no devices attached
        print("[DEBUG] No devices attached that supports ADB Communication.")
        return True
    else: # we need to check for unauthorization
        print("[DEBUG] Found devices that run ADB services.")
        for dev in dev_list:
            if "unauthorized" in dev:
                print(f"[DEBUG]: device:{dev} looks unauthorized")
                return True
            else:
                pass
    print("[DEBUG]: Everything seems okay, no need to display anything to user.")
    return False

def isMoreThanOneDeviceConnected():
    """
    Checks the list of currently supported ADB Devices connected to this PC and returns whether
    they are more than one device or no.
    
    True if yes, False if no.
    """
    devs_count = len(listADBDevices())
    if devs_count == 0:
        return False
    elif devs_count == 1:
        return False
    else:
        return True
    return False


def cleanCachesViaADB(deviceName:str=None) -> str:
    """
    The function for clearing all caches stored by 3rd party and system apps on the connected android device.
    
    If multiple devices are connected, you need to pass each device SN as an argument to this function
    
    If no arguments are passed, it will clean the currently connected device.
    """
    global adb_exe_path
    device_arg = ''
    
    if deviceName == None:
        deviceName = ''
        device_arg = ''
    else:
        deviceName = deviceName
        device_arg = f"-s {deviceName}"
        
    
    userpkg_list = []
    output_str = ''
    
    for package in getoutput(f"{adb_exe_path} {device_arg} shell pm list packages -3").split("\n"):
        pkg = package.replace("package:",'')
        userpkg_list.append(pkg)
    print(f"query user packages list: \n{userpkg_list}")
    output_str = output_str + "\nqueried user packages list"

    for package in userpkg_list:
        pkgclr = getoutput(f"{adb_exe_path} {device_arg} shell am force-stop {package}")
        print(f"[DEBUG]: package: '{package}' has been force stopped!\n{pkgclr}")
        output_str = output_str + f"\npackage: {package} has been force stopped!"    
    print("[DEBUG]: force stopping all user packages has been completed!\n\n")
    output_str = output_str + "\nForce stopping all user packages is completed!"

    trc = getoutput(f"{adb_exe_path} {device_arg} shell pm trim-caches 10000G")
    print(f"trim-caches 10000G command finished with output:\n{trc}\n\n")
    output_str = output_str + f"\n[INFO]: Clean caches command finished with output: {trc}\n"
    
    return output_str

def startADBDaemon():
    """
    Starts ADB Daemon
    
    Returns the output of the command.
    """
    global adb_exe_path
    out = getoutput(f"{adb_exe_path} start-server")
    return out


if __name__ == '__main__':
    # killADBDaemon()
    # requestADBConnection()

    # print(f"{listADBDevices()}, len:{len(listADBDevices())}")
    # print(needToShowInstructionsWindow())
    print(cleanCachesViaADB())