"""
Temp_Cleaner GUI Project by Ziad (Mr.X)

This is the script to run the tests to ensure proper functionality of Temp_Cleaner GUI before building from source into 
an executable file.

The goal of having this script is to:

    * Ensure all windows spawn normally, without any errors (like, ImportErrors, SyntaxErrors, etc.)
    * All modules required by the program can be imported properly

This script file is licensed under the same license as Temp_Cleaner GUI, since it is a part of it.

**THIS SCRIPT MUST BE RAN BEFORE ATTEMPTING TO BUILD Temp_Cleaner GUI FROM SOURCE TO MAKE SURE IT WILL WORK PROPERLY**
"""
# importing colorama for styling console text.
from colorama import Fore, Back, init, Style
# initializing colorama
init(autoreset=True)

# importing sys, os (necessary for storing current path into a variable)
# platform import is needed to access OS version details.
import sys, os, platform, importlib
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
# setting cwd to app path
os.chdir(application_path)
# extending sys.path
sys.path.append(application_path)

# Replace this string with the latest source file name (e.g. "temp_cleaner_gui_r8.0") without the '.py' suffix.
# THIS IS IMPORTANT, because without it, you are targetting tests towards the wrong version.
SOURCE_FILE_NAME = "temp_cleaner_gui_r8"


# List of modules
# DO NOT MODIFY UNDER NORMAL CIRCUMSTANCES, Updated as of v8.0-stable
# PLEASE UPDATE THIS LIST REGULARLY EVERY NEW UPDATE TO INCLUDE ALL MODULES USED BY THE PROGRAM
MODULES = [
    "error",
    "os",
    "sys",
    "shutil",
    "tkinter",
    "PIL",
    "configparser",
    "subprocess",
    "awesometkinter",
    "threading",
    "translations",
    "customtkinter",
    "webbrowser",
    "updater",
    "ctypes",
    "donators",
    "psutil",
    "tips",
    "math",
    "platform",
    "android_cleaner",
    "infobanner",
    "time",
    "msgbox",
    "tkinterweb",
    "random",
    "oobe",
    "urllib",
    "urllib.request",
    "colorama"
]
MOD_LENGTH: int = len(MODULES)

# A list containing the names of the classes of all windows present in the program
# DO NOT MODIFY, UNLESS YOU ADD ANOTHER WINDOW TO THE PROGRAM THAT YOU WANT TO BE TESTED HERE!
WINDOWS = [
    # from main program file
    (__import__(SOURCE_FILE_NAME),"MainWindowLightMode"),
    (__import__(SOURCE_FILE_NAME),"SettingsWindow"),
    (__import__(SOURCE_FILE_NAME),"LicenseWindow"),
    (__import__(SOURCE_FILE_NAME),"AboutWindow"),
    # tips module
    (__import__("tips"), "TipsWindow"),
    # updater module
    (__import__("updater"), "updaterProgramUI"),
    # donators module
    (__import__("donators"), "DonatorsWindow"),
    # oobe module
    (importlib.import_module("oobe.window"), "OOBEWindow"),
    # android cleaner module
    (importlib.import_module("android_cleaner.connection_window"), "ConnectPhoneToPCWindow"),
    (importlib.import_module("android_cleaner.connection_window"), "ConnectPhoneToPCViaWiFiWindow"),
    (importlib.import_module("android_cleaner.connection_window"), "ChooseADeviceWindow")
]

# declaring a variable to be modified during the runtime of the script
# as the status of all the tests
allTestsPassed: bool = True



def testModules() -> bool:
    """
    Attempts to import all modules required by various parts of the program

    Returns: 

    * False: if an error occurs at any stage.
    * True: if all modules are imported successfully.
    """
    global MOD_LENGTH, allTestsPassed
    CUR_POS: int = 0
    for _mod in MODULES:
        try:
            CUR_POS += 1
            __import__(_mod)
            print(f"{Fore.GREEN}{Style.BRIGHT}import[{CUR_POS}/{MOD_LENGTH}] success: module {_mod} has been successfully imported!")
        except Exception as __errImportingMod:
            # not all tests has passed, unfortunately.
            allTestsPassed = False
            print(f"{Fore.RED}{Style.BRIGHT}import[{CUR_POS}/{MOD_LENGTH}] failed: module {_mod} could not be imported due to an error: {__errImportingMod}")
            print(f"{Fore.YELLOW}{Style.BRIGHT}If you find an import error the best practice is to try to install it using pip or download it as source tarball.")
            return False
    # assuming all modules are imported successfully!
    print(f"{Fore.GREEN}{Style.BRIGHT}success [{CUR_POS}/{MOD_LENGTH}] modules imported successfully!, module import tests passed!")
    return True


def printInfoText() -> None:
    """
    Prints the greeting text that contains useful information about this script, full script path
    and other useful stuff.
    """
    # times to repeat characters used as separators.
    TIMES: int = 45
    print("="*TIMES)
    print(f"""Temp_Cleaner GUI before building test script.
Version 1.0 
Copyright (C) 2025 - Ziad (Mr.X)'s Software
Licensed under the same license as Temp_Cleaner GUI.
          
Environment information:
    * Python version: {sys.version}
    * Script full path: {application_path}
    * Running as user {os.getlogin()} , Process with ID: {os.getpid()}""")
    if os.name == 'nt': print(f"    * OS type: Windows, version: {platform.version()} ({platform.machine()})")
    else: print(f"    * OS type: {os.name}, {platform.platform()}")
    print(f"    * Temp_Cleaner GUI source file: {SOURCE_FILE_NAME}")
    try:
        import PyInstaller
        print(f"    {Fore.GREEN}{Style.BRIGHT}* Pyinstaller is installed, version: {PyInstaller.__version__}")
    except:
        print(f"    {Fore.RED}{Style.BRIGHT}* Pyinstaller is NOT installed!")
    print("="*TIMES)
    return None


def testWindows() -> None:
    """
    This function will test windows by trying to call their classes.
    """
    global SOURCE_FILE_NAME, WINDOWS, allTestsPassed
    try: __import__(SOURCE_FILE_NAME);print(f"{Fore.GREEN}{Style.BRIGHT}success: importing {SOURCE_FILE_NAME} has sucessed!")
    except Exception as __errImportingSrcFile:
        print(f"{Fore.RED}{Style.BRIGHT}error: failed to import source file {SOURCE_FILE_NAME}: {__errImportingSrcFile}")
        print(f"{Fore.RED}{Style.BRIGHT}All tests fail!")
        return None
    
    # now onto the actual testing.
    # we will iterate over each window specified in constant WINDOWS using getattr()
    # if no error occurs, we are safe, otherwise, we will inform the user and continue til the end.
    counter: int = 0
    did_error_happen: bool = False
    for _window in WINDOWS:
        # now lets try to instantiate them all
        # if an error occurs, we will print the error and continue to instantiate the next window.
        try:
            # increment counter
            counter += 1
            # storing getattr of window module, window class name into variable __test.
            __test = getattr(_window[0], _window[1])
            # informing user that tests are successfully done!
            print(f"{Fore.GREEN}{Style.BRIGHT}success window[{counter}/{len(WINDOWS)}]: successfully loaded window {_window[1]} from module {_window[0].__name__}!")
            # to free up memory.
            del __test
        except Exception as __errLoadingWindow:
            did_error_happen = True
            allTestsPassed = False
            print(f"{Fore.RED}{Style.BRIGHT}window[{counter}/{len(WINDOWS)}]error: failed to load window {_window[1]} from module {_window[0].__name__}: {__errLoadingWindow}")
            continue

    # Did any errors occur?
    if not did_error_happen:    
        print(f"{Fore.GREEN}{Style.BRIGHT}windows[{len(WINDOWS)}/{len(WINDOWS)}] successfully loaded!, all windows have been loaded properly!")
    
    return None


def printSeparator() -> None:
    """
    just prints a separator
    """
    TIMES: int = 45
    print("="*TIMES)
    return None



if __name__ == '__main__':
    printInfoText()
    testModules()
    printSeparator()
    testWindows()
    printSeparator()
    if allTestsPassed:
        print(f"{Fore.GREEN}{Style.BRIGHT}success: all tests passed, now you can processed to building Temp_Cleaner GUI into an executable file!")
    else:
        print(f"{Fore.RED}{Style.BRIGHT}error: one or more tests has failed, please fix the errors and try again!")
        # system exit signal 2 is for a test or more that has failed
        raise SystemExit(2)
    # now lets see if pyinstaller is installed or not
    try:
        import PyInstaller
    except ImportError:
        print(f"{Fore.RED}{Style.BRIGHT}error: PyInstaller is not installed!, you need to have Pyinstaller installed before you can build Temp_Cleaner GUI!")
        # system exit signal 3 is for an error that pyinstaller doesn't exist.
        raise SystemExit(3)
    # sys exit 0 is for success!
    raise SystemExit(0)

