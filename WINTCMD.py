import os
def py_destroy():
    exit()
def version():
    print("WINTCMD Extension for Python 3.x")
    print(" ")
    print("Version 1.0")
    print(" ")
    print("By Insertx2k Dev")
    print(" ")
    print("To be used to help you execute different commands to your Windows Command Prompt directly from Python!")
    print(" ")
    print("Doesn't require any 3rd party software")
    print(" ")
def help():
    print(" ")
    print("WINTCMD Extension for Python 3.x")
    print(" ")
    print("Version 1.0")
    print(" ")
    print("By Insertx2k Dev")
    print(" ")
    print("Usage : term(cmds)")
    print("Where : cmds can be the commands you wish to execute.")
    print(" ")
    print("For an example :")
    print("term('echo Hello World!&pause >nul&exit') - Prints the word 'Hello World' in Console Window then exits.")
    print(" ")
    print("help() - To be used to show you this.")
    print("version() - To be used to show you the version of this")
    print("py_destroy() - To be used to terminate your Python session - executes exit() for short..")
    print("feedback() - To be used to ask you about your opinion of our Python module!")
    print(" ")
    print("This program is free software, which means you are premitted to use it anywhere for free and without any restrictions.")
    print(" ")
    print("Licensed under the Creative World Software Redistribution License, Free Software Chapter.")
    print(" ")
def feedback():
    # Imports the messagebox class from the Tkinter Python Module
    from tkinter import messagebox
    # Defines the messagebox used to ask the user about their feedback of the program.
    feed = messagebox.askquestion('Feedback Hub','Do you like WINTCMD Extension for Python by Insertx2k Dev?\nYour feedback is much appreciated!')
    # Defines the commands to be done either when it is answered with yes or no.
    if feed == 'yes':
        print("Thanks for your good answer!, We are glad to hear that you liked our extension!")
        print(" ")
        print("We'd like to hear that from you in our official twitter account : @insertplayztw")
    else:
        print(" ")
        print("Thanks for your feedback and honest!, but we'd like to hear some answers from you.")
        print("Please tell us at our official twitter account : @insertplayz why you don't like this module?")
        print(" ")
class term:
    def __init__(self, cmds):
        self.cmds = cmds
        os.system(cmds)
class varibs:
    ver_var = 'WINTCMD Extension for Python 3.x\nVersion 1.0\nBy Insertx2k Dev'
    help_var = "WINTCMD Extension for Python 3.x\n\n\nBy Insertx2k Dev\n\nUsage : term(cmds)\nWhere : cmds can be the commands you wish to execute.\n\nFor an example :\nterm('echo Hello World!&pause >nul&exit') - Prints the word 'Hello World' in Console Window then exits.\n\nhelp() - To be used to show you this.\nversion() - To be used to show you the version of this\npy_destroy() - To be used to terminate your Python session - executes exit() for short..\nfeedback() - To be used to ask you about your opinion of our Python module!\n\nThis program is free software, which means you are premitted to use it anywhere for free and without any restrictions.\n\nLicensed under the Creative World Software Redistribution License, Free Software Chapter.\n"
class info:
    sys_info = 'systeminfo&pause >nul&exit'
    wmic_os = 'wmic os&pause >nul&exit'
class power_mgr:
    shutdown = 'wmic os where primary=true call shutdown&pause >nul&exit'
    reboot = 'wmic os where primary=true call reboot&pause >nul&exit'
    abort = 'shutdown -a&pause >nul&exit'
    logoff = 'shutdown -f -l&pause >nul&exit'
class basic_cmds:
    notepad = 'start notepad.exe'
    wordpad = 'start wordpad.exe'
    taskmgr = 'start taskmgr.exe'
    taskmgr2 = 'start %windir%/system32/taskmgr.exe'
    explorer = 'start explorer.exe'
    explorer2 = 'start %windir%/explorer.exe'
    regedit = 'start regedit.exe'
    regedit2 = 'start %windir%/regedit.exe'
    wininit = 'start %windir%/system32/wininit.exe'
    userinit = 'start %windir%/system32/userinit.exe'
    slmgr_mgmt = 'start %windir%/system32/slmgr.vbs'
    slmgr_mgmt2 = 'start slmgr.vbs'