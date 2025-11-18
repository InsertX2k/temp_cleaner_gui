"""
Temp_Cleaner GUI build script file

A Script file used to automate the process of building the Temp_Cleaner GUI application from source.

Due to the limitations of pyinstaller, this script needs to be ran from the same architecture
and operating system as the intended build target system, for example, if you are targeting an x86_64 (64-bit)
Windows 10 system, you must run this script on an x86_64 (64-bit) Windows 10 system.

If you are here to customize the building process, ONLY modify the constants, DO NOT MODIFY ANYTHING ELSE,
YOU DON'T NEED TO ADD YOUR FINAL TOUCHES HERE, THIS SCRIPT IS MADE TO ENSURE A SUCCESSFUL BUILD AND WITH GURANTEES
THAT THE COMPILED (BUILT) VERSION RUNS PROPERLY WITHOUT ANY ISSUES.

Copyright (C) 2025 - Ziad (Mr.X)'s Software
"""
# imports 
import customtkinter, os, tkinterweb, configparser, datetime

# DO NOT MODIFY THESE CONSTANTS
CONSOLE = "console"
WINDOWED = "windowed"
TRACE = "TRACE"
DEBUG = "DEBUG"
INFO = "INFO"
WARN = "WARN"
DEPRECATION = "DEPRECATION"
ERROR = "ERROR"
FATAL = "FATAL"



# ==================================================
# ==================================================
# CONSTANTS
# ==================================================
# 
# WHEN DEALING WITH PATHS IN WINDOWS YOU NEED TO DOUBLE THE BACKSLASH TO AVOID ERRORS "\\"
# 
# Full path to the source code files directory, this directory is where the main source file
# of the program is located, and it is usually the directory where this script is located, 
# if you cloned the official Temp_Cleaner GUI's repository directly without any modifications.
FULL_SRC_PATH = "F:\\Experiements\\temp_cleaner.gui.console.project.sourcecode.files"
# OUT_DIR is the directory where the final built application will be placed, this directory
# will contain the final executable built by the pyinstaller tool.
OUT_DIR = "F:\\Experiements\\temp_cleaner.gui.console.project.sourcecode.files\\build\\out"
# BUILD_TMP_DIR is the directory where the temporary files created by the pyinstaller tool
# are stored in, these files are not needed after the building process finishes, and they 
# can be safely deleted after the build is complete.
BUILD_TMP_DIR = "F:\\Experiements\\temp_cleaner.gui.console.project.sourcecode.files\\build\\tmp"
# The list of dependencies (aka modules) that will be passed to pyinstaller (using its hidden import functionality/feature)
# to be bundled within the final executable, YOU DO NOT usually need to modify this list, IT IS manually updated
# and reviewed by the author of Temp_Cleaner GUI every new release.
DEPENDENCES = [
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
    "urllib",
    "urllib.request",
    "colorama",
    "pwrcontrol",
    "toasts",
    "oobe",
    "build_date"
    "secure_delete"
]
# List of files (non-executable, non-binary) to be included within the final executable
# YOU ALSO DO NOT need to modify this list since IT IS manually updated and reviewed by the author
# of this program.
INCLUDE_FILES = [
    "about.png",
    "about_dark.png",
    "banner.png",
    "bannerlowres.png",
    "Config.ini",
    "warn.png",
    "transparent.png",
    "question.png",
    "addsclean.ini",
    "donators.ico",
    "donators.png",
    "err.ico",
    "err.png",
    "icon0.ico",
    "nul'",
    "settings.jpg",
    "settings.png",
    "style.json",
    "updater.ico",
    "updater.png",
    "updater_dark.png",
    "updatefb.png",
    "correctfb.png",
    "cleanfb.png",
    # we can just include the built binary for ata_trim 
    # instead of including its whole dir (with python source files)
    # this way, our directory tree will look a little bit more professional
    "secure_delete\\ata_trim.exe"
]
# INCLUDE_DIRS is a list of directories (folders) that will be RECURSIVELY included/bundled within the
# final built executable, these directories are needed by the program to function properly, and IT DOES NOT
# NEED TO BE MODIFIED, IT IS updated and maintained regularly by the program's author.
INCLUDE_DIRS = [
    f"{FULL_SRC_PATH}\\android_cleaner",
    f"{FULL_SRC_PATH}\\tips",
    f"{FULL_SRC_PATH}\\oobe",
    f"{FULL_SRC_PATH}\\secure_delete",
    # other directories are for other used libraries
    # which we will retrieve programmatically
    os.path.dirname(os.path.abspath(customtkinter.__file__)),
    os.path.dirname(os.path.abspath(tkinterweb.__file__))
]
# IS_FULL_BUILD controls whether pyinstaller will build the program in one directory mode
# if is True, this will build the program in one folder mode, if it is False, this will 
# build it in one file mode.
IS_FULL_BUILD: bool = True
# EXECUTABLE_ICON is the full path of the icon of the fully built executable
# On Windows, this should be a .ico file
EXECUTABLE_ICON = "F:\\Experiements\\temp_cleaner.gui.console.project.sourcecode.files\\icon0.ico"
# USE_UPX controls whether to instruct pyinstaller to use UPX to pack and compress
# executable and other binary files while building the program or not.
# BE CAREFUL, As using UPX triggers most Anti-Virus software to falsely flag this
# application as malware or PUP (Potentially Unwanted Program)
USE_UPX = False
# NAME is the full filename of the final main built executable file, it is recommended
# that you leave it the way it is unless you want to build a release for yourself only.
# default value is "temp_cleaner_gui"
NAME = "temp_cleaner_gui"
# INCLUDE_ALL_LIBRARY should include string values as names of modules and libraries to 
# have everything related to them (binary files, and non-binary files) bundled within the final
# executable, It is also recommended to leave this the way it currently is.
INCLUDE_ALL_LIBRARY = [
    "customtkinter",
    "tkinterweb",
    "oobe"
]
# Controls whether the final executable should request for Administrative privileges upon execution
# or not, it's always best to leave it to True unless you are testing.
USE_UAC_ADMIN = True
# Full path of Real-time temporary files extraction directory
# This is the directory where pyinstaller's bootloader will extract the bundled files (see INCLUDE_FILES)
# and folders/directories (see INCLUDE_DIRS) into when the program is built with the one file mode (when IS_FULL_BUILD is set to False)
# ONLY use this when you are debugging (or testing) or if you know what you are doing.
RT_TMP_DIR = ""
# Full path of the version file to be used when building the final executable.
# A version file is simply a text file that contains basic executable information
# such as Version, Company, File Description, Original Filename, Product Name, etc...
# in a specific way so that it can be read by the operating system and linked to 
# an executable file.
# (You can find these information in the properties window, the Details tab on Windows)
VERSION_FILE = "F:\\Experiements\\versioninfo.txt"
# Controls the display mode of the final executable.
# In WINDOWED mode, the console window is hidden and only the Windows shown during the execution
# of the program/or declared into are shown, in contrary to the CONSOLE mode, 
# which has the console window fully shownthe CONSOLE mode is useful for debugging 
# and testing the build to make sure it doesn't have any under-the-hood errors or 
# exceptions that haven't been fixed yet.
# THIS ONLY Accepts two values: WINDOWED or CONSOLE
DISPLAY_MODE = CONSOLE
# Controls the level of logging during the building process.
# This ONLY controls the verbosity (or aggressiveness) of the pyinstaller logger while building
# the final executable, IT DOES NOT affect the level of verbosity in the final build.
# It is better to leave it to the default value, unless of course you are debugging Pyinstaller or
# the building process.
# This ONLY accepts ONE value of these:
# TRACE, DEBUG, INFO, WARN, DEPRECATION, ERROR, FATAL
# with the default value being INFO
BUILD_TIME_LOGLEVEL = DEBUG
# Enables and controls the level of the verbosity of debugging in the final executable.
# **THIS REQUIRES THE DISPLAY_MODE = CONSOLE TO WORK**
# **NEVER ENABLE RUN-TIME DEBUGGING ON PRODUCTION VERSIONS** 
# if this value is None, it means that verbose debugging is disabled (Default)
# if not None, then It has to be one of these values:
# "all" -> Logs everything and displays them to the console (very aggressive)
# "imports" -> Only Logs import actions and displays them to the console 
# "bootloader" -> Logs pyinstaller bootloader related events and displays them to the console
# "noarchive" -> Do not store frozen python source files into an archive in the final build
# but rather store them without compression into the executable path (see OUT_DIR) (NOT RECOMMENDED)
RT_DEBUGGING_LEVEL = "all"
# File name (excluding the .py extension) of the main program source file.
# the main program source file is the main file that should be executed, and has all the logic
# for executing the program, it also includes the main window UI.
# The default value is always recommended and it isn't recommended that you modify this yourself
# since this value is manually maintained by the author of this program.
# Syntax for every main file is always: temp_cleaner_gui_r[version code]
# for example: temp_cleaner_gui_r8
MAIN_PROG_SRC_FILE = "temp_cleaner_gui_r8"
# Controls whether to modify the FirstRun value in the program's configuration file
# to set it to 1 before starting the build process.
# Setting that value to 1 is essential to make the OOBE window start when launching the final
# executable for the first time, IT IS ALSO RECOMMENDED TO LEAVE THIS VALUE AS IT IS.
SET_FIRSTRUN_VALUE = True
# **DO NOT MODIFY ANYTHING THAT COMES AFTER THESE 2 DIVIDERS**
# ==================================================
# ==================================================



if __name__ == '__main__': # if file is executed as a script file
    # with sys.argv support (although we will not use sys.argv in this script).

    # Now we need to modify the first run value in the config file.
    if SET_FIRSTRUN_VALUE == True:
        print("[DEBUG] will write 1 as the value of FirstRun in the Configuration file....")
        try:
            config = configparser.ConfigParser()
            config.read(f"{FULL_SRC_PATH}\\Config.ini")
            # modify and save value.
            print(f"[DEBUG] current FirstRun value for Config file is: {config['ProgConfig']['firstrun'.upper()]}")
            config["ProgConfig"]["firstrun".upper()] = "1"
            with open(f"{FULL_SRC_PATH}\\Config.ini", 'w') as savef:
                config.write(savef)
            print("[DEBUG] wrote 1 as FirstRun value, will close file descriptor...")
            savef.close() # close to release fs locks.
        except Exception as __errSettingFirstRunVal:
            print(f"[ERROR]: failed to set first run value: {__errSettingFirstRunVal}")
            print("The script will return with exit code 5, it can't continue...")
            raise SystemExit(5) # exit with code 5

    # lets write the module build_date
    with open(f"{FULL_SRC_PATH}\\build_date.py", 'w') as bd_openf:
        bd_openf.write(f"""# automatically generated by the build script, DO NOT MODIFY
# will be automatically overwritten as needed
BUILD_DATE = '{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} ({datetime.datetime.now().astimezone().tzname()})'
""")
        print("[DEBUG] Created build_time module!")
    bd_openf.close() # making available to other programs.
    
    # add code for building for ata_trim using Visual Studio here first.
    print(f"[DEBUG] Building ata_trim executable using Microsoft Build tools...")
    print(f"[DEBUG] In case of errors please make sure you have the MSBuild.exe executable full path listed in system or user's PATH environment variable.")
    # we must create the folder to hold disk free space secure eraser tool and its components
    print("[DEBUG] Creating folder \"disk_fspace_eraser\"")
    try:
        os.mkdir(f"{FULL_SRC_PATH}\\disk_fspace_eraser")
        print(f"[DEBUG] Successfully created: \"{FULL_SRC_PATH}\\disk_fspace_eraser\"!")
    except Exception as __errMakingDiskFSpaceEraserDir:
        print(f"[ERROR] Failed to create directory: \"{FULL_SRC_PATH}\\disk_fspace_eraser\": {__errMakingDiskFSpaceEraserDir}")
        print("[ERROR] Build process cannot continue!")
        raise SystemExit(64) # sys exit 64 is for a failure to create directory that will hold disk fspace eraser tool and its dependencies.
    # generate command line for building ata_trim executable from solution file.
    ata_trim_build_vc_cli: str = f"MSBuild.exe \"{FULL_SRC_PATH}\\secure_delete\\ata_trim\\ata_trim.sln\" -isolateProjects:False -interactive:False -property:OutDir=\"{FULL_SRC_PATH}\\disk_fspace_eraser\";AdditionalDependencies=\"$(CoreLibraryDependencies);%(AdditionalDependencies);mi.lib\" -p:Configuration=Release"
    # now let's build the ata_trim executable (aka. run the command generated above).
    os.system(ata_trim_build_vc_cli)
    # TODO: add code for building secu_delete module here
        # I think only building the wizard program and running the secu_delete module under a different
        # execution thread will be a better option.
    # TODO: add code for building the wizard program for the secu_delete module here.
        # Please don't forget to move it to the disk_fspace_eraser folder once building finishes.

    # ---------------------- This is the stage for building main program Temp_Cleaner GUI ----------------------
    # lets write a spec file
    full_cli: str = f"pyi-makespec {'--onedir' if IS_FULL_BUILD == True else '--onefile'} --log-level {BUILD_TIME_LOGLEVEL} --name {NAME} "
    for _file in INCLUDE_FILES:
        full_cli = full_cli + f'--add-data "{FULL_SRC_PATH}\\{_file};." '
    for _dir in INCLUDE_DIRS:
        full_cli = full_cli + f'--add-data "{_dir};{os.path.basename(os.path.abspath(_dir))}/" '
    for _mod in DEPENDENCES:
        full_cli = full_cli + f'--hidden-import {_mod} '
    if RT_DEBUGGING_LEVEL != None:
        full_cli = full_cli + f'-d {RT_DEBUGGING_LEVEL} '
    if USE_UPX == False:
        full_cli = full_cli + f'--noupx '
    for _collect_all_mod in INCLUDE_ALL_LIBRARY:
        full_cli = full_cli + f'--collect-all {_collect_all_mod} '
    # windowed or console?
    if DISPLAY_MODE == WINDOWED:
        full_cli = full_cli + f'--windowed '
    else: # we will assume its always console
        full_cli = full_cli + f'--console '
    
    full_cli = full_cli + f'-i "{EXECUTABLE_ICON}" --version-file "{VERSION_FILE}" '
    if USE_UAC_ADMIN == True:
        full_cli = full_cli + f'--uac-admin '

    if len(RT_TMP_DIR) != 0:
        full_cli = full_cli + f'--runtime-tmpdir "{RT_TMP_DIR}" '
    
    full_cli = full_cli + f'{MAIN_PROG_SRC_FILE}.py'
    print(f"[DEBUG] generated cli for building spec file: \n{full_cli}")
    os.system(full_cli)
    print(f"[DEBUG] Next stage is to build Temp_Cleaner GUI from the spec file: {FULL_SRC_PATH}\\{NAME}.spec")
    build_cli = f'pyinstaller --clean --log-level {BUILD_TIME_LOGLEVEL} --distpath "{OUT_DIR}" --workpath "{BUILD_TMP_DIR}" "{FULL_SRC_PATH}\\{NAME}.spec"'
    os.system(build_cli)
    

