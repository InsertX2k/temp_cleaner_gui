# =================================================
# Temp_Cleaner GUI Console Program
# =================================================
# A simple way to clean up your temporary folders content for free.
# Such program is free to redistribute and to modify to fit your needs.
# Free to download from @insertplayztw official twitter or our official forum link.
# Hope you enjoy it
# License for the Project Temp_Cleaner GUI.
#    A simple program made to help you erase temporary files in your Windows-based PC.
#    Copyright (C) 2021 - Insertx2k Dev
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# See github.com/insertx2k/temp_cleaner_gui
from tkinter import *
import WINTCMD
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image
import os
root = Tk()
root.title("Temp_Cleaner Console Window (64-bit)")
root.iconbitmap("icon0.ico")
root.geometry('600x460')
root.resizable(False,False)
# Defining the function used to show the user the About window of the program.
def show_about_scr():
    messagebox.showinfo("About Temp_Cleaner Console Window (64-bit)","""
A simple way to help you clean up all temporary directories and files in your computer for free and without any restrictions! \n
Version : 1.32 (Environment Variables Edition)
Author  : Insertx2k Dev
License : The GNU General Public License Version 2.0
Github  : https://github.com/insertx2k/temp_cleaner_gui
Uses    : This program uses Environment variables to get correct user specified pathes for temporary folders, e.g. :
When the environment variable 'rammappath' is specified, the program will execute the command to Empty Workingsets from the path specified in the variable.
Variable: It uses the following variables : 
s       : 'rammappath' - used to define the full path of the program RAMMap by Sysinternals (must be entered with the full executable name of the RAMMap tool)
        : 'cdpccpath' - used to determine the correct location of the ConnectedDevicesPlatform cache folder.
        : 'adwclrpath' - when a custom path is specified for the program Adware cleaner in its settings page, please create this variable and specify (simply copy and paste) the path you specified for Adware cleaner to store it's data as the variable value
        : 'winxpepath' - used to retrieve the correct path of where the files of the program WinXPE is stored in (This environment variable is COMPLETELY required for the WinXPE Downloads cleaner to work).
Arch    : This version of program (Temp_Cleaner GUI) only functions on 64-bit Operating Systems (x64).
""")
# Defining the function used to execute the main program. (the working function for short)
def exec_confirm():
    choice = get_usr_input.get()
    if choice == "1":
        WINTCMD.term('rmdir /s /q "%systemdrive%\\$Recycle.bin"')
        messagebox.showinfo("Clean Systemdrive Recyclebin data", "Done cleaning recycle bin data!")
    if choice == "2":
        WINTCMD.term('cd /d %windir%&erase /s /f /q prefetch')
        messagebox.showinfo("Clean Prefetch data", "Done cleaning prefetchW data!")
    if choice == "3":
        WINTCMD.term('cd /d %localappdata%&erase /s /f /q "D3DSCache"')
        messagebox.showinfo("Clean D3DSCached data", "Done Cleaning D3DSCached data!")
    if choice == "4":
        WINTCMD.term('cd /d %windir%&erase /s /f /q "Temp"')
        messagebox.showinfo("Clean Windows Temp.", "Done Cleaning Windows Temporary data!")
    if choice == "5":
        WINTCMD.term('cd /d %localappdata%&erase /s /f /q "Temp"')
        messagebox.showinfo("Clean User Temporary Directory", "Done Cleaning User Temporary Directory!")
    if choice == "6":
        WINTCMD.term('cd /d %localappdata%&cd Google&cd Chrome&cd "User Data"&cd "Default"&erase /s /f /q "GPUCache"&erase /s /f /q Cache&erase /s /f /q "Code Cache"')
        messagebox.showinfo("Clean Google Chrome Webcache", "Done cleaning google chrome webcache and Temporary directories and GPUCache and Code Cache data.")
    if choice == "7":
        WINTCMD.term('cd /d %localappdata%&cd Google&cd Chrome&cd "User Data"&cd "Default"&del /s /q "Cookies"&del /s /q "Cookies-journal"')
        messagebox.showinfo("Clean Google Chrome Cookies", "Done cleaning Google Chrome cookies data.")
    if choice == "8":
        WINTCMD.term('cd /d "%systemdrive%\\Users\\Default\\AppData\\Local"&erase /s /f /q Temp')
        messagebox.showinfo("Clean Default User Temporary Data", "Done cleaning Default user temporary data!")
    if choice == "9":
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Windows"&erase /s /f /q "INetCache"')
        messagebox.showinfo("Clean IECache", "Done cleaning IE Cache!")
    if choice == "b":
        WINTCMD.term('@echo off | clip')
        messagebox.showinfo("Clean User Clipboard Data", "Done Cleaning user clipboard data.")
    if choice == "a":
        WINTCMD.term('cd /d %localappdata%&cd microsoft&cd windows&cd explorer&del /s /q *thumbcache*&cd /d %localappdata%\microsoft\windows\explorer&del /s /q *thumb*')
        messagebox.showinfo("Clean Windows Explorer Thumbnails", "Done Cleaning Windows Explorer Thumbnails Data.")
    if choice == "c":
        WINTCMD.term('cd /d %userprofile%\\AppData\\Roaming&cd Microsoft&cd Windows&erase /s /f /q Recent')
        messagebox.showinfo("Clean Recent Documents List", "Done Cleaning Recent Documents List!")
    if choice == "":
        messagebox.showinfo("ERROR", "ERROR 0 : Please choose something from the menu.")
    if choice == "d":
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\discord"&erase /s /f /q "Cache"&erase /s /f /q "Code Cache"&erase /s /f /q "GPUCache"&erase /s /f /q "Local Storage"')
        messagebox.showinfo("Clean Discord webclient webcache", "Done cleaning Discord webclient cached data!")
    if choice == "e":
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\GIMP\\2.10"&erase /s /f /q "tmp"')
        messagebox.showinfo("Clean GIMP's TMPs", "Done cleaning GIMP's TMPS!")
    if choice == "f":
        WINTCMD.term('cd /d "%localappdata%\\Steam\\htmlcache"&erase /s /f /q "Cache"&erase /s /f /q "Code Cache"&erase /s /f /q "GPUCache"')
        messagebox.showinfo("Clean Steam webclient cache data", "Done.")
    if choice == "g":
        WINTCMD.term('cd /d "%windir%\\SoftwareDistribution"&del /f /s /q "Download"')
        messagebox.showinfo("Clean Windows Update Downloads", "Done.")
        reboot_uwp = messagebox.askquestion("Restart Windows Update Service", "After you delete all Downloaded files by the Windows Update Service you should restart the whole service to commit changes you did to it\nWould you like to restart the Windows Update Service?")
        if reboot_uwp == "yes":
            # Importing the module WINTCMD by Insertx2k Dev.
            # import WINTCMD, it is already imported during the execution of the program by the way.
            root_2 = Tk()
            root_2.title("Restart Windows Update Service")
            root_2.geometry('500x90')
            root_2.resizable(False,False)
            root_2.iconbitmap("icon0.ico")
            # Defining some labels used to show the user that something is happening inside.
            lbl0x = Label(root_2, text="Restarting Windows Update Service...", font=("Arial", 19))
            lbl0x.place(x=25 ,y=20)
            # Defining the actions used to restart the Windows update service.
            WINTCMD.term('net start wuauserv')
            # Defining the commands used to show the user that all pending operations has been successfully completed!
            messagebox.showinfo("Restart Windows Update Service", "Windows Update Service Has been successfully restarted!")
            # Defining the mainloop destroy once the execution is done.
            root_2.destroy()
            root_2.mainloop()
            messagebox.showinfo("Restart Windows Update Service", "Done restarting the Windows Update Service!")
        else:
            messagebox.showinfo("Restart Windows Update Service", "Expect your device to have problems with Windows Update if you didn't restart it as soon as possible then.")
    if choice == "h":
        WINTCMD.term('cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "Caches"')
        messagebox.showinfo("Clean Windows 10 Cached data", "Done!")
    if choice == "i":
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Windows"&erase /s /f /q "INetCookies"')
        messagebox.showinfo("Clean IE Cookies", "Done cleaning IE Cookies!")
    if choice == "j":
        WINTCMD.term('cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "IECompatCache"&erase /s /f /q "IECompatUaCache"')
        messagebox.showinfo("Clean Additional IE Cached Data", "Done Cleaning Additional IE Cached data!")
    if choice == "k":
        WINTCMD.term('cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "IEDownloadHistory"')
        messagebox.showinfo("Clean IE Downloads History", "Done erasing IE Downloads History")
    if choice == "l":
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Windows"&erase /s /f /q "ActionCenterCache"')
        messagebox.showinfo("Clean Windows 10 Action Center/Notifications Center Cache", "Done cleaning Windows 10 Notifications Center/Action Center Cached data!")
    if choice == "m":
        WINTCMD.term('cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "AppCache"')
        messagebox.showinfo("Clean Windows Modern Applications Cached Data", "Done cleaning Windows Modern Applications cached data!")
    if choice == "n":
        conf1 = messagebox.askquestion("Clean Store-based MS Edge Cached Data", "Cleaning Store-based MS Edge cached data can not be done automatically, which means you are supposed to do that manually, which will make this tool open an explorer (Windows Explorer) window for you showing you the folder where you are supposed to clean MS-Store-Based EDGE Webcache data\nPlease keep in mind that you shouldn't leave the directory opened to you by this tool\nSo do you wish to processed?")
        if conf1 == "yes":
            messagebox.showinfo("Clean Store-based MS Edge Cached Data", "Ok, opening the directory for you\nDon't forget to look for the folder Microsoft.MicrosoftEdge_[a random number], and go inside the AC folder inside of it, you will then be able to see all MS Store-based edge webcached data.")
            WINTCMD.term('explorer.exe "%localappdata%\\Packages\\"')
            messagebox.showinfo("Clean Windows Modern Applications Cached Data", "Done!")
        else:
            messagebox.showinfo("Clean Windows Modern Applications Cached Data", "Operation canceled by the user.")
    if choice == "o":
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Windows\\Explorer"&erase /s /f /q "ThumbCacheToDelete"')
        messagebox.showinfo("Clean Additional Windows Explorer Thumbnails Cache.", "Done!")
    if choice == "p":
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Edge\\User Data\\Default"&erase /s /f /q "GPUCache"&erase /s /f /q "Cache"&erase /s /f /q "Code Cache"')
        messagebox.showinfo("Clean Chromium-based MS Edge Webcache", "Done!")
    if choice == "q":
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Edge\\User Data\\Default"&del /s /q "Cookies"&del /s /q "Cookies-journal"')
        messagebox.showinfo("Clean Chromium-based MS Edge Cookies", "Done!")
    if choice == "r":
        WINTCMD.term('cd /d "%localappdata%\\Roblox"&erase /s /f /q "Downloads"')
        messagebox.showinfo("Clean ROBLOX Game Downloads", "Done!")
    if choice == "s":
        WINTCMD.term('cd /d "%appdata%\\Adobe\\Adobe Photoshop 2020\\Adobe Photoshop 2020 Settings\\web-cache-temp"&erase /s /f /q "GPUCache"&erase /s /f /q "Code Cache"&del /s /f /q "Visited Links"')
        messagebox.showinfo("Clean Adobe Photoshop 2020 Webcache", "Successfully cleaned GPUCache and Code Cache and Visited Links!")
    if choice == "t":
        WINTCMD.term('cd /d "%localappdata%\\VEGAS Pro\\17.0"&erase /s /f /q "File Explorer Thumbnails"&erase /s /f /q "Device Explorer Thumbnails"&del /s /f /q "*.autosave.veg.bak"&del /s /f /q "svfx_Ofx*.log"')
        messagebox.showinfo("Clean Sony Vegas Pro temp and Logs", "Successfully cleaned File explorer thumbnails and device explorer thumbnails and autosave.veg.bak files and fx log files of Sony Vegas Pro 17")
    if choice == "u":
        WINTCMD.term('cd /d "%localappdata%\\McNeel\\Rhinoceros"&erase /s /f /q "temp"')
        messagebox.showinfo("Clean Rhino3d moduling temp", "Done!")
    if choice == "v":
        WINTCMD.term('cd /d "%userprofile%\\AppData\\LocalLow\\Microsoft"&erase /s /f /q /A:S "CryptnetUrlCache"')
        messagebox.showinfo("Clean Cryptnet URL Cache", "Done!")
    if choice == "w":
        WINTCMD.term('cd /d "%localappdata%\\pip"&erase /s /f /q "cache"')
        messagebox.showinfo("Clean Python PIP Cached data", "Done!")
    if choice == "x":
        conf2 = messagebox.askquestion("Empty Windows Workingsets", "Would you really like to run RAMMap by Sysinternals to empty RAM Workingsets?")
        if conf2 == "yes":
            if os.getenv("rammappath") is not None:
                WINTCMD.term('""%rammappath%"" -Ew')
                messagebox.showinfo("Empty Windows Workingsets", "RAMMap.exe - Command sent.")
            else:
                messagebox.showinfo("An ERROR has occured", "The environment variable 'rammappath' doesn't exist either in the current user or the SYSTEM environment variables, Please make sure this environment variable exists and then try again.\nIf you don't know how, please follow the instructions given in this window:\n1-Open Control Panel\n2-Click on System and Security then click on System\n3-At the bottom of the window, you will find a button named 'Environment Variables' click on it\n4-Under the word 'User Variables for username' locate the button 'New' and then click on it\n5-Specify the variable name as 'rammappath' and then in the variable value write the full path of the program RAMMap.exe by Sysinternals (Incl. its exe name) (For an example : C:\\Programs\\RAMMap\\RAMMap.exe).\n6-When you are done, Please press the button OK, and then OK and then click on Apply and OK, then restart this program.")
        else:
            messagebox.showinfo("Empty Windows Workingsets", "Operation has been canceled.")
    if choice == "y":
        WINTCMD.term('cd /d "%localappdata%\\Google\\Chrome\\User Data\\Default"&del /s /q "Extension Cookies"&del /s /q "Extension Cookies-journal"')
        messagebox.showinfo("Clean GChrome Extension Cookies", "Done cleaning extension cookies data of Gchrome! (Included. Extension cookies-journal)")
    if choice == "z":
        if os.getenv("cdpccpath") is not None:
            WINTCMD.term('cd /d "%localappdata%\\ConnectedDevicesPlatform"&erase /s /f /q ""%cdpccpath%""')
            messagebox.showinfo("Clean Windows 10 Activities cache", "Done cleaning Windows activites cache.")
        else:
            messagebox.showinfo("Notification", "The custom environemnt variable 'cdpccpath' doesn't exist for custom path specification, Temp_Cleaner GUI will attempt to use the default path, which might not work properly in most cases.")
            WINTCMD.term('cd /d "%localappdata%\\ConnectedDevicesPlatform"&erase /s /f /q "ee2999716b7783e6"')
            messagebox.showinfo("Clean Windows 10 Activities cache", "Done cleaning Windows activites cache.")
    if choice == "0b":
        conf3 = messagebox.askquestion("Clean icon cache", "Cleaning IconCache.db file can not be done automatically, which means the user is premitted to do that manually, all what you have to do is just deleting the file iconcache.db in the directory we will open to you\nDo you wish to processed?")
        if conf3 == "yes":
            WINTCMD.term('%windir%\\explorer.exe "%localappdata%"')
            messagebox.showinfo("Clean icon cache database file", "Done!")
        else:
            messagebox.showinfo("Clean Icon cache database file", "Operation has been canceled.")
    if choice == "0x":
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "Microvirt"')
        messagebox.showinfo("Clean MEmu Microvirt Logs", "Done!")
    if choice == "0f":
        if os.getenv("adwclrpath") is not None:
            messagebox.showinfo("Notification", "A custom environment variable ('adwclrpath') is specified for the tool Adware cleaner path, the custom path will be used instead of the default path.")
            WINTCMD.term('cd /d ""%adwclrpath%""&erase /s /f /q "Logs"')
            messagebox.showinfo("Clean AdwCleaner Logs", "Done!")
        else:
            messagebox.showinfo("Notification", "The custom environment variable for the path of the program ADWare cleaner ('adwclrpath') is not specified, the program will continue using the default path.")
    if choice == "0k":
        WINTCMD.term('%systemdrive%&&cd /d \\.\\&erase /s /f /q "PerfLogs"')
        messagebox.showinfo("Clean Perflogs folder", "Done!")
    if choice == "0l":
        WINTCMD.term('cd /d "%userprofile%"&rmdir /s /q ".cache"')
        messagebox.showinfo("Clean .cache folder", "Done!")
    if choice == "0n":
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "SquirrelTemp"')
        messagebox.showinfo("Clean Discord SquirrelTemp", "Done!")
    if choice == "0m":
        WINTCMD.term('cd /d "%userprofile%\\AppData\\LocalLow"&erase /s /f /q "Temp"')
        messagebox.showinfo("Clean LocalLow Temporary Directory", "Done!")
    if choice == "0d":
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "ElevatedDiagnostics"')
        messagebox.showinfo("Clean ElevatedDiagnostics Folder (Only Windows 10)", "Done cleaning the elevated diagnostics folder in your localappdata directory!")
    if choice == "0p":
        WINTCMD.term('cd /d "%localappdata%\\VMware"&erase /s /f /q "vmware-download*"')
        messagebox.showinfo("Clean VMware Downloads", "Done!")
    if choice == "1f":
        WINTCMD.term('cd /d "%userprofile%\\appdata\\roaming\\balena-etcher"&erase /s /f /q "blob_storage"&erase /s /f /q "Code Cache"&erase /s /f /q "GPUCache"&erase /s /f /q "Local Storage"&erase /s /f /q "Session Storage"')
        messagebox.showinfo("Clean balenaitcher's webcached data", "Successfully erased blob_storage, Code Cache, GPUCache, Local Storage, Session Storage files.")
    if choice == "1x":
        WINTCMD.term('cd /d "%appdata%"&cd /d "%userprofile%\\AppData\\Roaming"&erase /s /f /q "pyinstaller"')
        messagebox.showinfo("Clean Pyinstaller cached data", "Done!")
    if choice == "2x":
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "Jedi"')
        messagebox.showinfo("Clean Jedi Python Additionals", "Done cleaning Jedi Python Additionals!")
    if choice == "1o":
        WINTCMD.term('cd /d "%localappdata%"&del /s /q "recently-used.xbel"')
        messagebox.showinfo("Clean GIMP Recent Documents List", "Successfully erased GIMP Recent Documents List!")
    if choice == "1p":
        WINTCMD.term('cd /d "%localappdata%"&del /s /q "llftool.*.agreement"')
        messagebox.showinfo("Delete LLFTOOL agreement confirmation file.", "Now the Low Level Format Tool by HDD Guru does not remember either you accepted its license agreement or no.")
    if choice == "1q":
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "IdentityNexusIntegration"')
        messagebox.showinfo("Clean IdentityNexusIntegration folder" ,"Done!")
    if choice == "2f":
        WINTCMD.term('cd /d "%localappdata%\\Axolot Games"&cd "Scrap Mechanic"&cd "Temp"&erase /s /f /q "WorkshopIcons"')
        messagebox.showinfo("Clean Scrap Mechanic WorkshopIcons cache", "Done cleaning Scrap Mechanic game Workshop Icons")
    if choice == "2d":
        WINTCMD.term('cd /d "%localappdata%\\Roblox"&erase /s /f /q "logs"')
        messagebox.showinfo("Clean ROBLOX Game Logs", "Done cleaning ROBLOX Game Logs!")
    if choice == "3m":
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\Code"&erase /s /f /q "GPUCache"&erase /s /f /q "Code Cache"&erase /s /f /q "CachedData"&erase /s /f /q "Cache"')
        messagebox.showinfo("Clean VS Code Webcached data", "Done cleaning VS Code Webcached data!")
    if choice == "3w":
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\Code"&del /s /q "Cookies"&del /s /q "Cookies-journal"')
        messagebox.showinfo("Clean VS Code Cookies data", "Done cleaning VS Code cookies and Cookies-journal data!")
    if choice == "2c":
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\Code"&erase /s /f /q "CachedExtensions"&erase /s /f /q "CachedExtensionVSIXs"')
        messagebox.showinfo("Clean VS Code Cached Extensions", "Done cleaning VS Code Cached Extensions data")
    if choice == "2k":
        if os.getenv("winxpepath") is not None:
            WINTCMD.term('erase /s /f /q "%winxpepath%\\Temp"')
            messagebox.showinfo("Clean Win10XPE Temp data", "Successfully deleted all downloaded data by the WinXPE Application!")
            messagebox.showinfo("Note", "You will need to redownload all downloaded data by the tool for the exporting phase to be done!")
        else:
            messagebox.showinfo("An ERROR has occured", "The environment variable 'winxpepath' doesn't exist either in the current user or the SYSTEM environment variables, Please make sure this environment variable exists and then try again.\nIf you don't know how, please follow the instructions given in this window:\n1-Open Control Panel\n2-Click on System and Security then click on System\n3-At the bottom of the window, you will find a button named 'Environment Variables' click on it\n4-Under the word 'User Variables for username' locate the button 'New' and then click on it\n5-Specify the variable name as 'winxpepath' and then in the variable value write the full path of where the WinXPE tool is stored in.\n6-When you are done, Please press the button OK, and then OK and then click on Apply and OK, then restart this program.")
    if choice == "0v":
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "ServiceHub"')
        messagebox.showinfo("Clean ServiceHub identity file", "Done deleting the Service Hub identity file (salt file)!")
        messagebox.showinfo("Note", "Some Windows 10 features that depends on this feature might not function properly.")
    if choice == "0e":
        WINTCMD.term('erase /s /f /q "%localappdata%\\HiSuite\\log"')
        messagebox.showinfo("Clean HiSuite Log data", "Done cleaning HiSuite Logs data.")
    if choice == "0g":
        WINTCMD.term('erase /s /f /q "%userprofile%\\AppData\\Roaming\\.minecraft\\webcache"')
        messagebox.showinfo("Clean Minecraft Webcache data", "Done cleaning Minecraft webcache data!")
    if choice == "0t":
        WINTCMD.term('cd /d "%localappdata%\\Mozilla\\Firefox\\Profiles"&cd *.default-release&erase /s /f /q "cache2"&erase /s /f /q "jumpListCache"&cd /d "%userprofile%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"&cd *.default-release&erase /s /f /q "shader-cache"')
        messagebox.showinfo("Clean Mozilla Firefox Internet Cache", "Done cleaning Mozilla Firefox internet browser cached data, and jumpListcache and shader cache!")
    if choice == "0z":
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"&cd *.default-release&del /s /q "cookies.sqlite"')
        messagebox.showinfo("Clean Mozilla Firefox Cookies SQLITE File", "Done cleaning Mozilla Firefox Cookies SQLITE File!")
    if choice == "0r":
        WINTCMD.term('cd /d "%localappdata%\\VEGAS"&erase /s /f /q "ErrorReport"')
        messagebox.showinfo("Clean Sony Vegas Pro 17 Error Report data", "Done cleaning Sony Vegas Pro 17 Error Report Data.")
    if choice == "0":
        conf4 = messagebox.askquestion("Confirmation", "By default, the command 0 would actually have terminated the program manually, But you are premitted to confirm that manually\nWould you really like to close this tool?")
        if conf4 == "yes":
            root.destroy()
        else:
            messagebox.showinfo("Confirmation", "Operation has been canceled by the user\nThe program will not terminate.")
    if choice == "3r":
        WINTCMD.term('cd /d "%userprofile%\\AppData\\LocalLow\\Sun\\Java\\Deployment"&erase /s /f /q "tmp"')
        messagebox.showinfo("Clean SunMicroSystems Java Deployment Temp Data", "Done erasing temp data of Sun Micro Systems Java Deployment Software (aka Java Runtime)")
    if choice == "3y":
        WINTCMD.term('cd /d "%localappdata%\\HiSuite\\userdata"&erase /s /f /q "DropTemp"')
        messagebox.showinfo("Clean Huawei HiSuite Drag 'n' Drop Temporary Data", "Done erasing temporary data of Huawei HiSuite Drag 'n' Drop Temporary Data.")
# Defining the labels inside the window.
lbl0 = Label(root, text="This should help you clean all Temporary files in your computer.", font=("arial", 10))
lbl0.grid(column=0, row=1, sticky='w')
lbl1 = Label(root, text="Please choose something from the menu", font=("arial", 10))
lbl1.grid(column=0, row=2, sticky='w')
# Defining the scrolledtext window used to show the user all available options to choose from.
menu_show = scrolledtext.ScrolledText(root, width=72, height=22)
menu_show.grid(column=0, row=3, sticky='w')
# Setting the text of a scolledtext.
menu_show.insert(INSERT, """
\n
 1-Clean SystemDrive Recycle Bin\n
\n
 2-Clean Prefetch data\n
\n
 3-Clean D3DSCache files.\n
\n
 4-Clean Windows Temp Directory. windir\\temp.\n
\n
 5-Clean User Temporary Directory.\n
\n
 6-Clean Google Chrome Temporary Data, and GPUCache and Code Cache data\n
\n
 7-Clean Google Chrome Cookies Files Cookies, and Cookies-Journal\n
\n
 8-Clean Default User Temporary Data\n
\n
 9-Clean Internet Explorer Cached Data \n
 Please keep in mind that cleaning IE Cached data will of course slow down your Internet experince, but Will make browsing internet more safe for you\n
\n
 a-Clean Windows Explorer Thumbnail Cache\n
 Please keep in mind that this process will cause 100% Disk Usage on Some Computers with low disk space, and with old slow HDDs\n
\n
 b-Clean User Clipboard\n
 Please keep in mind that this doesn't clean pictures you copy, and doesn't clean select on files you copy or cut\n
\n
 c-Clean Recent Documents List User Recent Documents List\n
\n
 d-Clean Discord Windows Client Temporary data incl GPUCache, and Code Cache, and Session Storage data\n
\n
 e-Clean GNU Image Manipulation Program TMP data GIMP's tmp\n
\n
 f-Clean Steam App HTML Cache files incl GPUCache, Code Cache, excl Cookies, and Cookies-Journal\n
\n
 g-Clean Windows Update Downloaded Updates\n
 Please keep in mind that you will have to restart Windows Update Service to commit changes\n
 This process will make updates arrive lately to your computer, and Delivery Optimization might not function properly If on Windows 10\n
\n
 h-Clean Windows OS Cached Data\n
 This might cause problems to your Windows Configuration, and might also cause some problems with Windows Start Menu and Modern Settings UI\n
\n
 i-Clean Internet Explorer Cookie Data\n
 This will log you out of websites you are logged in with 3rd party accounts\n
 This doesn't clean all IE extensions cookies data\n
\n
 j-Clean Additional IE Cached Data\n
 This may slow down your Internet Explorer experience, and will of course slow down apps that rely on it's cache to load their content properly\n
\n
 k-Clear Internet Explorer Downloads History\n
 This will make you lose information about the recent data you've downloaded from any IE-based browsers\n
\n
 l-Clean Windows 10 Action Center Cached Data\n
 Please keep in mind that this may cause some problems to the Windows 10's Action Center If Notifications exist in the Center\n
\n
 m-Clean Modern UI Applications Cached Data\n
 Please keep in mind that this process will of course slow down your experience with Modern UI Applications\n
\n
 n-Clean Windows Store-based Microsoft Edge Cached Data and Cookies\n
\n
 o-Clean Additional Windows Explorer Thumbnail Cached Data\n
\n
 p-Clean Chromium-based Microsoft Edge Cached data incl GPUCache, Code Cache data\n
\n
 q-Clean Chromium-Based Microsoft Edge Cookies data incl Cookies-Journal file excl Extensions cookies\n
\n
 r-Clean ROBLOX Game Downloads\n
\n
 s-Clean Adobe Photoshop Web content cached data incl GPUCache, Code Cache, Session Storage data\n
\n
 t-Clean Sony Vegas 17 Pro Temporary data\n
\n
 u-Clean Rhino 3D Moduling App Cached data\n
\n
 v-Clean Windows 10's CryptNet Data\n
\n
 w-Clean Python PIP Cached data\n
 This may slow down python experience\n
\n
 x-Empty Windows Workingsets (Requires the user to specify the directory to the RAMMap tool by Sysinternals) (Requires the user to accept the EULA of Sysinternals Software)\n
\n
 y-Clean Google Chrome Extensions Cookies data Files : Extension Cookies and Extension Cookies-journal\n
\n
 z-Clean Windows 10's Activities cache - ConnectedDevicesPlatform Cached data\n
\n
 0b-Delete Icon Cache file in User Local Applications Data Directory\n
\n
 0x-Clean Memory Dump and log data of Microvirt MEmu Android Emulator application\n
\n
 0f-Clean MalwareBytes Adware Cleaner Log files User must specify the location of such directory when a custom directory is specified\n
\n
 0k-Clean the folder PerfLogs in systemdrive volume.\n
\n
 0l-Delete the folder cache in userprofile that Android devices create in your computer when they are attached to your computer ,This usually won't help freeing up a lot of disk space, Not more than 5 MBs of total size in most cases\n
\n
 0n-Clean Temporary data of Squirrelapp Formerly known as Discord windows client additional temporary data folder\n
\n
 0m-Clean LocalLow Temporary folder data or contents\n
\n
 0d-Clean ElevatedDiagnostics folder in User Local App Data Directory Only available to Windows 10 Users\n
\n
 0p-Clean the folder that contains all Downloaded data from the Internet by VMware Software\n
\n
 1f-Clean BalenaEtcher's Web content temporary data Incl Code Cache, GPUCache, Session Storage, Local Storage, blob_storage directories\n
\n
 1x-Clean Pyinstaller's bincache temporary data\n
\n
 2x-Clean Jedi Python additional temporary data\n
\n
 1o-Clean GIMP's GNU Image Manipulation Program's Recent Documents list\n
\n
 1p-Delete the file that tells the tool Low Level Format Tool for Windows that you have accepted it's license agreement\n
\n
 1q-Clean IdentityNexusIntegration folder contents\n
\n
 2f-Clean Scrap Mechanic Temporary Workshop icons directory\n
\n
 2d-Clean ROBLOX Game Verbose Logs \n
\n
 3m-Clean Visual Studio Code All Versions Webdata Temporary files Incl GPUCache, Code Cache, Cache, Cached Data\n
\n
 3w-Clean Visual Studio Code All Versions Webdata Cookies files Incl Cookies, Cookies-journal files\n
\n
 2c-Clean Visual Studio Code All Versions Cached Extensions data \n
\n
 2k-Clean WindowsXPE Folder Temporary data All Versions Contains the directory where the downloaded applications of WinXPE is stored (Requires the user to change the directory of where WinXPE is installed in when necessary)\n
\n
 0v-Delete the identity file of ServiceHub Only available to Windows 10 Users, salt file\n
\n
 0e-Clean HiSuite Log data\n
 This might prevent you from using HiSuite properly\n
\n
 0g-Clean Minecraft game web cache data Incl Cache, Code Cache, GPUCache files\n
\n
 0t-Clean Mozilla Firefox Internet Cache Incl Shader Cache files\n
\n
 0z-Clean Mozilla Firefox Cookies data\n
\n
 0r-Clean Sony VEGAS Error Report files\n
\n
 3r-Clean Java Deployment Cached Data.\n
\n
 3y-Clean Huawei Mobile Hisuite Drag 'n' Drop Temporary Data.\n
\n
 0-Close this tool\n
\n
""")
# Disabling the scrollabletext widget to prevent the user from inputing any text inside of it.
menu_show.configure(state=DISABLED)
# Defining the combobox widget used to get the input from the user of the tool.
get_usr_input = Combobox(root, width=59)
get_usr_input.place(x=10 ,y=409)
# Defining the values of the combobox used to get input from the user.
get_usr_input['values']= (1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0b", "0x", "0f", "0k", "0l", "0n", "0m", "0d", "0p", "1f", "1x", "2x", "1o", "1p", "1q", "2f", "2d", "3m", "3w", "2c", "2k", "0v", "0e", "0g", "0t", "0z", "0r", "3r", "3y", 0)
# Defining the button used to commit selection and GO.
go_commit = Button(root, text="Execute", command=exec_confirm)
go_commit.place(x=520 ,y=405)
# Defining the about button used to show the user more information about this program.
about_btn = Button(root, text="About", command=show_about_scr)
about_btn.place(x=520 ,y=0)
root.mainloop()