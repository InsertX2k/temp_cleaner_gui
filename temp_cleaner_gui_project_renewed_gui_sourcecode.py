# The Project Temp_Cleaner GUI by Insertx2k Dev.
# A simple temporary folders cleaning solution made by Insertx2k Dev under the GNU General Public License
# That will help you free up a lot of disk space in your computer through erasing all the Temporary folders
# Exist in almost all temporary folders directories either in your C:\ drive (Windows drive) or other drives. 
# Uses the same environment variables as in the version 1.32, except a renewed GUI.
# Free to modify and redistribute to fit in your needs as explained in the GNU General Public License v2.0 or later.
# 
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
# For a much better github page, try visiting https://insertx2k.github.io/temp_cleaner_gui
# 
# The program Temp_Cleaner GUI was previously Temp_Cleaner and it was using a CUI instead of a GUI. 
# 
from tkinter import *
import WINTCMD
from tkinter import messagebox
from tkinter import ttk
import os
from PIL import Image, ImageTk
import time
root = Tk()
root.title("The Temp_Cleaner GUI Project (v1.52)")
root.geometry('1202x600')
root.iconbitmap("icon0.ico")
root.minsize(1202,600)
# Configuring the scrollbar to make it available for the main program's window.
# Create a main frame.
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)
# Create a canvas.
main_canvas = Canvas(main_frame)
main_canvas.pack(side=LEFT, fill=BOTH, expand=1)
# Add a scrollbar to the canvas
main_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=main_canvas.yview)
main_scrollbar.pack(side=RIGHT, fill=Y)
# Configure the canvas.
main_canvas.configure(yscrollcommand=main_scrollbar.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion = main_canvas.bbox("all")))
# Create another frame INSIDE the canvas.
show_frame = Frame(main_canvas)
# Add that New frame to a window in the canvas.
main_canvas.create_window((0,0), window=show_frame, anchor="nw")

# Defining some informative labels inside of the Temp_Cleaner GUI's Window.
banner = PhotoImage(file="banner.png")
banner_show = Label(show_frame, image=banner, width=1200, height=300)
banner_show.grid(column=0, row=1, sticky='w')

# Defining the function used to show the user the about window of the program.
def show_about_window():
    messagebox.showinfo("About The Temp_Cleaner GUI Project (v1.52)","""The Temp_Cleaner GUI Project by Insertx2k Dev\n
Version 1.52
Update 3 (Renewed Graphical Buttons Edition)
Written in Python by Insertx2k Dev
Support Twitter : @insertplayztw
Support Forum URL : https://creative-development.wixsite.com/cwofficial/forum
\n
The following version of The Temp_Cleaner GUI Project uses the following environment variables : 
'rammappath' - used to define the full path of the program RAMMap by Sysinternals (must be entered with the full executable name of the RAMMap tool)
'cdpccpath' - used to determine the correct location of the ConnectedDevicesPlatform cache folder.
'adwclrpath' - when a custom path is specified for the program Adware cleaner in its settings page, please create this variable and specify (simply copy and paste) the path you specified for Adware cleaner to store it's data as the variable value
'winxpepath' - used to retrieve the correct path of where the files of the program WinXPE is stored in (This environment variable is COMPLETELY required for the WinXPE Downloads cleaner to work).
\n
GitHub page : https://github.com/insertx2k/temp_cleaner_gui
Better UI GitHub page : https://insertx2k.github.io/temp_cleaner_gui
""")

# Defining the function to execute the following selected commands : 
def execute_theprogram():
    # Defining the executing image to be the image of the button using Python pillow.
    pic_file_executing_image0 = Image.open("executing_icon_for_btns.png")
    picture_output_executing_execute_btn = ImageTk.PhotoImage(pic_file_executing_image0)
    exec_btn.configure(image=picture_output_executing_execute_btn)
    selection = var0.get()
    if selection == '1':
        WINTCMD.term('rmdir /s /q "%systemdrive%\\$Recycle.bin"')
        messagebox.showinfo("Clean Systemdrive Recyclebin folder", "I am done with erasing your Systemdrive Recyclebin folder!")
    selection1 = var1.get()
    if selection1 == '1':
        WINTCMD.term('cd /d %windir%&erase /s /f /q prefetch')
        messagebox.showinfo("Clean PrefetchW Local data", "I am done with erasing your PrefetchW Local Data!")
    selection2 = var2.get()
    if selection2 == '1':
        WINTCMD.term('cd /d %localappdata%&erase /s /f /q "D3DSCache"')
        messagebox.showinfo("Clean D3DSCached data", "I am done with erasing all of your D3DSCached data that exists in your Localappdata folder!")
    selection3 = var3.get()
    if selection3 == '1':
        WINTCMD.term('cd /d %windir%&erase /s /f /q "Temp"')
        messagebox.showinfo("Clean Windir Temporary Folders", "I am done with erasing all of your Windir Temporary Folders content.\nPlease keep in mind that files in use won't be erased.")
    selection4 = var4.get()
    if selection4 == '1':
        WINTCMD.term('cd /d %localappdata%&erase /s /f /q "Temp"')
        messagebox.showinfo("Clean User Temporary Data", "All pending operations has been successfully completed!\nPlease keep in your mind that files in use won't be deleted.")
    selection5 = var5.get()
    if selection5 == '1':
        WINTCMD.term('cd /d %localappdata%&cd Google&cd Chrome&cd "User Data"&cd "Default"&erase /s /f /q "GPUCache"&erase /s /f /q Cache&erase /s /f /q "Code Cache"')
        messagebox.showinfo("Clean Google Chrome Webcached data", "Done cleaning google chrome webcache and Temporary directories and GPUCache and Code Cache data.")
    selection6 = var6.get()
    if selection6 == '1':
        WINTCMD.term('cd /d %localappdata%&cd Google&cd Chrome&cd "User Data"&cd "Default"&del /s /q "Cookies"&del /s /q "Cookies-journal"')
        messagebox.showinfo("Clean Google Chrome Cookies", "Done cleaning Google Chrome cookies data.")
    selection9 = var7.get()
    if selection9 == '1':
        WINTCMD.term('cd /d "%systemdrive%\\Users\\Default\\AppData\\Local"&erase /s /f /q Temp')
        messagebox.showinfo("Clean Default User Temporary Data", "Done cleaning Default user temporary data!")
    selection10 = var8.get()
    if selection10 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Windows"&erase /s /f /q "INetCache"')
        messagebox.showinfo("Clean IECache", "Done cleaning IE Cache!")
    selection11 = var9.get()
    if selection11 == '1':
        WINTCMD.term('@echo off | clip')
        messagebox.showinfo("Clean User Clipboard Data", "Done Cleaning user clipboard data.")
    selection12 = var10.get()
    if selection12 == '1':
        WINTCMD.term('cd /d %localappdata%&cd microsoft&cd windows&cd explorer&del /s /q *thumbcache*&cd /d %localappdata%\microsoft\windows\explorer&del /s /q *thumb*')
        messagebox.showinfo("Clean Windows Explorer Thumbnails", "Done Cleaning Windows Explorer Thumbnails Data.")
    selection13 = var11.get()
    if selection13 == '1':
        WINTCMD.term('cd /d %userprofile%\\AppData\\Roaming&cd Microsoft&cd Windows&erase /s /f /q Recent')
        messagebox.showinfo("Clean Recent Documents List", "Done Cleaning Recent Documents List!")
    selection14 = var12.get()
    if selection14 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\discord"&erase /s /f /q "Cache"&erase /s /f /q "Code Cache"&erase /s /f /q "GPUCache"&erase /s /f /q "Local Storage"')
        messagebox.showinfo("Clean Discord webclient webcache", "Done cleaning Discord webclient cached data!")
    selection15 = var13.get()
    if selection15 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\GIMP\\2.10"&erase /s /f /q "tmp"')
        messagebox.showinfo("Clean GIMP's TMPs", "Done cleaning GIMP's TMPS!")
    selection16 = var14.get()
    if selection16 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Steam\\htmlcache"&erase /s /f /q "Cache"&erase /s /f /q "Code Cache"&erase /s /f /q "GPUCache"')
        messagebox.showinfo("Clean Steam webclient cache data", "Done.")
    selection17 = var15.get()
    if selection17 == '1':
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
    selection18 = var16.get()
    if selection18 == '1':
        WINTCMD.term('cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "Caches"')
        messagebox.showinfo("Clean Windows 10 Cached data", "Done!")
    selection19 = var17.get()
    if selection19 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Windows"&erase /s /f /q "INetCookies"')
        messagebox.showinfo("Clean IE Cookies", "Done cleaning IE Cookies!")
    selection20 = var18.get()
    if selection20 == '1':
        WINTCMD.term('cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "IECompatCache"&erase /s /f /q "IECompatUaCache"')
        messagebox.showinfo("Clean Additional IE Cached Data", "Done Cleaning Additional IE Cached data!")
    selection21 = var19.get()
    if selection21 == '1':
        WINTCMD.term('cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "IEDownloadHistory"')
        messagebox.showinfo("Clean IE Downloads History", "Done erasing IE Downloads History")
    selection22 = var20.get()
    if selection22 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Windows"&erase /s /f /q "ActionCenterCache"')
        messagebox.showinfo("Clean Windows 10 Action Center/Notifications Center Cache", "Done cleaning Windows 10 Notifications Center/Action Center Cached data!")
    selection23 = var21.get()
    if selection23 == '1':
        WINTCMD.term('cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "AppCache"')
        messagebox.showinfo("Clean Windows Modern Applications Cached Data", "Done cleaning Windows Modern Applications cached data!")
    selection24 = var22.get()
    if selection24 == '1':
        conf1 = messagebox.askquestion("Clean Store-based MS Edge Cached Data", "Cleaning Store-based MS Edge cached data can not be done automatically, which means you are supposed to do that manually, which will make this tool open an explorer (Windows Explorer) window for you showing you the folder where you are supposed to clean MS-Store-Based EDGE Webcache data\nPlease keep in mind that you shouldn't leave the directory opened to you by this tool\nSo do you wish to processed?")
        if conf1 == "yes":
            messagebox.showinfo("Clean Store-based MS Edge Cached Data", "Ok, opening the directory for you\nDon't forget to look for the folder Microsoft.MicrosoftEdge_[a random number], and go inside the AC folder inside of it, you will then be able to see all MS Store-based edge webcached data.")
            WINTCMD.term('explorer.exe "%localappdata%\\Packages\\"')
            messagebox.showinfo("Clean Windows Modern Applications Cached Data", "Done!")
        else:
            messagebox.showinfo("Clean Windows Modern Applications Cached Data", "Operation canceled by the user.")
    selection25 = var23.get()
    if selection25 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Windows\\Explorer"&erase /s /f /q "ThumbCacheToDelete"')
        messagebox.showinfo("Clean Additional Windows Explorer Thumbnails Cache.", "Done!")
    selection26 = var24.get()
    if selection26 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Edge\\User Data\\Default"&erase /s /f /q "GPUCache"&erase /s /f /q "Cache"&erase /s /f /q "Code Cache"')
        messagebox.showinfo("Clean Chromium-based MS Edge Webcache", "Done!")
    selection27 = var25.get()
    if selection27 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Edge\\User Data\\Default"&del /s /q "Cookies"&del /s /q "Cookies-journal"')
        messagebox.showinfo("Clean Chromium-based MS Edge Cookies", "Done!")
    selection28 = var26.get()
    if selection28 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Roblox"&erase /s /f /q "Downloads"')
        messagebox.showinfo("Clean ROBLOX Game Downloads", "Done!")
    selection29 = var27.get()
    if selection29 == '1':
        WINTCMD.term('cd /d "%appdata%\\Adobe\\Adobe Photoshop 2020\\Adobe Photoshop 2020 Settings\\web-cache-temp"&erase /s /f /q "GPUCache"&erase /s /f /q "Code Cache"&del /s /f /q "Visited Links"')
        messagebox.showinfo("Clean Adobe Photoshop 2020 Webcache", "Successfully cleaned GPUCache and Code Cache and Visited Links!")
    selection30 = var28.get()
    if selection30 == '1':
        WINTCMD.term('cd /d "%localappdata%\\VEGAS Pro\\17.0"&erase /s /f /q "File Explorer Thumbnails"&erase /s /f /q "Device Explorer Thumbnails"&del /s /f /q "*.autosave.veg.bak"&del /s /f /q "svfx_Ofx*.log"')
        messagebox.showinfo("Clean Sony Vegas Pro temp and Logs", "Successfully cleaned File explorer thumbnails and device explorer thumbnails and autosave.veg.bak files and fx log files of Sony Vegas Pro 17")
    selection31 = var29.get()
    if selection31 == '1':
        WINTCMD.term('cd /d "%localappdata%\\McNeel\\Rhinoceros"&erase /s /f /q "temp"')
        messagebox.showinfo("Clean Rhino3d moduling temp", "Done!")
    selection32 = var30.get()
    if selection32 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\LocalLow\\Microsoft"&erase /s /f /q /A:S "CryptnetUrlCache"')
        messagebox.showinfo("Clean Cryptnet URL Cache", "Done!")
    selection33 = var31.get()
    if selection33 == '1':
        WINTCMD.term('cd /d "%localappdata%\\pip"&erase /s /f /q "cache"')
        messagebox.showinfo("Clean Python PIP Cached data", "Done!")
    selection34 = var32.get()
    if selection34 == '1':
        conf2 = messagebox.askquestion("Empty Windows Workingsets", "Would you really like to run RAMMap by Sysinternals to empty RAM Workingsets?")
        if conf2 == "yes":
            if os.getenv("rammappath") is not None:
                WINTCMD.term('""%rammappath%"" -Ew')
                messagebox.showinfo("Empty Windows Workingsets", "RAMMap.exe - Command sent.")
            else:
                messagebox.showinfo("An ERROR has occured", "The environment variable 'rammappath' doesn't exist either in the current user or the SYSTEM environment variables, Please make sure this environment variable exists and then try again.\nIf you don't know how, please follow the instructions given in this window:\n1-Open Control Panel\n2-Click on System and Security then click on System\n3-At the bottom of the window, you will find a button named 'Environment Variables' click on it\n4-Under the word 'User Variables for username' locate the button 'New' and then click on it\n5-Specify the variable name as 'rammappath' and then in the variable value write the full path of the program RAMMap.exe by Sysinternals (Incl. its exe name) (For an example : C:\\Programs\\RAMMap\\RAMMap.exe).\n6-When you are done, Please press the button OK, and then OK and then click on Apply and OK, then restart this program.")
        else:
            messagebox.showinfo("Empty Windows Workingsets", "Operation has been canceled.")
    selection35 = var33.get()
    if selection35 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Google\\Chrome\\User Data\\Default"&del /s /q "Extension Cookies"&del /s /q "Extension Cookies-journal"')
        messagebox.showinfo("Clean GChrome Extension Cookies", "Done cleaning extension cookies data of Gchrome! (Included. Extension cookies-journal)")
    selection36 = var34.get()
    if selection36 == '1':
        if os.getenv("cdpccpath") is not None:
            WINTCMD.term('cd /d "%localappdata%\\ConnectedDevicesPlatform"&erase /s /f /q ""%cdpccpath%""')
            messagebox.showinfo("Clean Windows 10 Activities cache", "Done cleaning Windows activites cache.")
        else:
            messagebox.showinfo("Notification", "The custom environemnt variable 'cdpccpath' doesn't exist for custom path specification, Temp_Cleaner GUI will attempt to use the default path, which might not work properly in most cases.")
            WINTCMD.term('cd /d "%localappdata%\\ConnectedDevicesPlatform"&erase /s /f /q "ee2999716b7783e6"')
            messagebox.showinfo("Clean Windows 10 Activities cache", "Done cleaning Windows activites cache.")
    selection37 = var35.get()
    if selection37 == '1':
        conf3 = messagebox.askquestion("Clean icon cache", "Cleaning IconCache.db file can not be done automatically, which means the user is premitted to do that manually, all what you have to do is just deleting the file iconcache.db in the directory we will open to you\nDo you wish to processed?")
        if conf3 == "yes":
            WINTCMD.term('%windir%\\explorer.exe "%localappdata%"')
            messagebox.showinfo("Clean icon cache database file", "Done!")
        else:
            messagebox.showinfo("Clean Icon cache database file", "Operation has been canceled.")
    selection38 = var36.get()
    if selection38 == '1':
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "Microvirt"')
        messagebox.showinfo("Clean MEmu Microvirt Logs", "Done!")
    selection39 = var37.get()
    if selection39 == '1':
        if os.getenv("adwclrpath") is not None:
            messagebox.showinfo("Notification", "A custom environment variable ('adwclrpath') is specified for the tool Adware cleaner path, the custom path will be used instead of the default path.")
            WINTCMD.term('cd /d ""%adwclrpath%""&erase /s /f /q "Logs"')
            messagebox.showinfo("Clean AdwCleaner Logs", "Done!")
        else:
            messagebox.showinfo("Notification", "The custom environment variable for the path of the program ADWare cleaner ('adwclrpath') is not specified, the program will continue using the default path.")
            WINTCMD.term('erase /s /f /q "%systemdrive%\\AdwCleaner\\Logs"')
            messagebox.showinfo("Adware Cleaner Log files cleared!", "All pending operations has been successfully completed!\nPlease keep in mind this might not function properly due to path differences.")
    selection40 = var38.get()
    if selection40 == '1':
        WINTCMD.term('%systemdrive%&&cd /d \\.\\&erase /s /f /q "PerfLogs"')
        messagebox.showinfo("Clean Perflogs folder", "Done!")
    selection41 = var39.get()
    if selection41 == '1':
        WINTCMD.term('cd /d "%userprofile%"&rmdir /s /q ".cache"')
        messagebox.showinfo("Clean .cache folder", "Done!")
    selection42 = var40.get()
    if selection42 == '1':
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "SquirrelTemp"')
        messagebox.showinfo("Clean Discord SquirrelTemp", "Done!")
    selection43 = var41.get()
    if selection43 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\LocalLow"&erase /s /f /q "Temp"')
        messagebox.showinfo("Clean LocalLow Temporary Directory", "Done!")
    selection44 = var42.get()
    if selection44 == '1':
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "ElevatedDiagnostics"')
        messagebox.showinfo("Clean ElevatedDiagnostics Folder (Only Windows 10)", "Done cleaning the elevated diagnostics folder in your localappdata directory!")
    selection45 = var43.get()
    if selection45 == '1':
        WINTCMD.term('cd /d "%localappdata%\\VMware"&erase /s /f /q "vmware-download*"')
        messagebox.showinfo("Clean VMware Downloads", "Done!")
    selection46 = var44.get()
    if selection46 == '1':
        WINTCMD.term('cd /d "%userprofile%\\appdata\\roaming\\balena-etcher"&erase /s /f /q "blob_storage"&erase /s /f /q "Code Cache"&erase /s /f /q "GPUCache"&erase /s /f /q "Local Storage"&erase /s /f /q "Session Storage"')
        messagebox.showinfo("Clean balenaitcher's webcached data", "Successfully erased blob_storage, Code Cache, GPUCache, Local Storage, Session Storage files.")
    selection47 = var45.get()
    if selection47 == '1':
        WINTCMD.term('cd /d "%appdata%"&cd /d "%userprofile%\\AppData\\Roaming"&erase /s /f /q "pyinstaller"')
        messagebox.showinfo("Clean Pyinstaller cached data", "Done!")
    selection48 = var46.get()
    if selection48 == '1':
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "Jedi"')
        messagebox.showinfo("Clean Jedi Python Additionals", "Done cleaning Jedi Python Additionals!")
    selection49 = var47.get()
    if selection49 == '1':
        WINTCMD.term('cd /d "%localappdata%"&del /s /q "recently-used.xbel"')
        messagebox.showinfo("Clean GIMP Recent Documents List", "Successfully erased GIMP Recent Documents List!")
    selection50 = var48.get()
    if selection50 == '1':
        WINTCMD.term('cd /d "%localappdata%"&del /s /q "llftool.*.agreement"')
        messagebox.showinfo("Delete LLFTOOL agreement confirmation file.", "Now the Low Level Format Tool by HDD Guru does not remember either you accepted its license agreement or no.")
    selection51 = var49.get()
    if selection51 == '1':
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "IdentityNexusIntegration"')
        messagebox.showinfo("Clean IdentityNexusIntegration folder" ,"Done!")
    selection52 = var50.get()
    if selection52 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Axolot Games"&cd "Scrap Mechanic"&cd "Temp"&erase /s /f /q "WorkshopIcons"')
        messagebox.showinfo("Clean Scrap Mechanic WorkshopIcons cache", "Done cleaning Scrap Mechanic game Workshop Icons")
    selection53 = var51.get()
    if selection53 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Roblox"&erase /s /f /q "logs"')
        messagebox.showinfo("Clean ROBLOX Game Logs", "Done cleaning ROBLOX Game Logs!")
    selection54 = var52.get()
    if selection54 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\Code"&erase /s /f /q "GPUCache"&erase /s /f /q "Code Cache"&erase /s /f /q "CachedData"&erase /s /f /q "Cache"')
        messagebox.showinfo("Clean VS Code Webcached data", "Done cleaning VS Code Webcached data!")
    selection55 = var53.get()
    if selection55 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\Code"&del /s /q "Cookies"&del /s /q "Cookies-journal"')
        messagebox.showinfo("Clean VS Code Cookies data", "Done cleaning VS Code cookies and Cookies-journal data!")
    selection56 = var54.get()
    if selection56 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\Code"&erase /s /f /q "CachedExtensions"&erase /s /f /q "CachedExtensionVSIXs"')
        messagebox.showinfo("Clean VS Code Cached Extensions", "Done cleaning VS Code Cached Extensions data")
    selection57 = var55.get()
    if selection57 == '1':
        if os.getenv("winxpepath") is not None:
            WINTCMD.term('erase /s /f /q "%winxpepath%\\Temp"')
            messagebox.showinfo("Clean Win10XPE Temp data", "Successfully deleted all downloaded data by the WinXPE Application!")
            messagebox.showinfo("Note", "You will need to redownload all downloaded data by the tool for the exporting phase to be done!")
        else:
            messagebox.showinfo("An ERROR has occured", "The environment variable 'winxpepath' doesn't exist either in the current user or the SYSTEM environment variables, Please make sure this environment variable exists and then try again.\nIf you don't know how, please follow the instructions given in this window:\n1-Open Control Panel\n2-Click on System and Security then click on System\n3-At the bottom of the window, you will find a button named 'Environment Variables' click on it\n4-Under the word 'User Variables for username' locate the button 'New' and then click on it\n5-Specify the variable name as 'winxpepath' and then in the variable value write the full path of where the WinXPE tool is stored in.\n6-When you are done, Please press the button OK, and then OK and then click on Apply and OK, then restart this program.")
    selection58 = var56.get()
    if selection58 == '1':
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "ServiceHub"')
        messagebox.showinfo("Clean ServiceHub identity file", "Done deleting the Service Hub identity file (salt file)!")
        messagebox.showinfo("Note", "Some Windows 10 features that depends on this feature might not function properly.")
    selection59 = var57.get()
    if selection59 == '1':
        WINTCMD.term('erase /s /f /q "%localappdata%\\HiSuite\\log"')
        messagebox.showinfo("Clean HiSuite Log data", "Done cleaning HiSuite Logs data.")
    selection60 = var58.get()
    if selection60 == '1':
        WINTCMD.term('erase /s /f /q "%userprofile%\\AppData\\Roaming\\.minecraft\\webcache"')
        messagebox.showinfo("Clean Minecraft Webcache data", "Done cleaning Minecraft webcache data!")
    selection61 = var59.get()
    if selection61 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Mozilla\\Firefox\\Profiles"&cd *.default-release&erase /s /f /q "cache2"&erase /s /f /q "jumpListCache"&cd /d "%userprofile%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"&cd *.default-release&erase /s /f /q "shader-cache"')
        messagebox.showinfo("Clean Mozilla Firefox Internet Cache", "Done cleaning Mozilla Firefox internet browser cached data, and jumpListcache and shader cache!")
    selection62 = var60.get()
    if selection62 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"&cd *.default-release&del /s /q "cookies.sqlite"')
        messagebox.showinfo("Clean Mozilla Firefox Cookies SQLITE File", "Done cleaning Mozilla Firefox Cookies SQLITE File!")
    selection63 = var61.get()
    if selection63 == '1':
        WINTCMD.term('cd /d "%localappdata%\\VEGAS"&erase /s /f /q "ErrorReport"')
        messagebox.showinfo("Clean Sony Vegas Pro 17 Error Report data", "Done cleaning Sony Vegas Pro 17 Error Report Data.")
    selection64 = var62.get()
    if selection64 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\LocalLow\\Sun\\Java\\Deployment"&erase /s /f /q "tmp"')
        messagebox.showinfo("Clean SunMicroSystems Java Deployment Temp Data", "Done erasing temp data of Sun Micro Systems Java Deployment Software (aka Java Runtime)")
    selection65 = var63.get()
    if selection65 == '1':
        WINTCMD.term('cd /d "%localappdata%\\HiSuite\\userdata"&erase /s /f /q "DropTemp"')
        messagebox.showinfo("Clean Huawei HiSuite Drag 'n' Drop Temporary Data", "Done erasing temporary data of Huawei HiSuite Drag 'n' Drop Temporary Data.")
    selection66 = var64.get()
    if selection66 == '1':
        messagebox.showinfo("Close when done", "All pending operations has been successfully completed!\nPress the OK button to close the program.")
        root.destroy()
    # Sleeping a bit for longer (or equal) to 5 seconds.
    time.sleep(1)
    # Ok, let's revert everything back to what it was before.
    exec_btn.configure(text="", image=picture_output, command=execute_theprogram)
# Defining a sample get var functionaking a new checkbox.
# Defining the ON-OFF Like variable
var0 = StringVar()
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()
var9 = StringVar()
var10 = StringVar()
var11 = StringVar()
var12 = StringVar()
var13 = StringVar()
var14 = StringVar()
var15 = StringVar()
var16 = StringVar()
var17 = StringVar()
var18 = StringVar()
var19 = StringVar()
var20 = StringVar()
var21 = StringVar()
var22 = StringVar()
var23 = StringVar()
var24 = StringVar()
var25 = StringVar()
var26 = StringVar()
var27 = StringVar()
var28 = StringVar()
var29 = StringVar()
var30 = StringVar()
var31 = StringVar()
var32 = StringVar()
var33 = StringVar()
var34 = StringVar()
var35 = StringVar()
var36 = StringVar()
var37 = StringVar()
var38 = StringVar()
var39 = StringVar()
var40 = StringVar()
var41 = StringVar()
var42 = StringVar()
var43 = StringVar()
var44 = StringVar()
var45 = StringVar()
var46 = StringVar()
var47 = StringVar()
var48 = StringVar()
var49 = StringVar()
var50 = StringVar()
var51 = StringVar()
var52 = StringVar()
var53 = StringVar()
var54 = StringVar()
var55 = StringVar()
var56 = StringVar()
var57 = StringVar()
var58 = StringVar()
var59 = StringVar()
var60 = StringVar()
var61 = StringVar()
var62 = StringVar()
var63 = StringVar()
var64 = StringVar()
# Defining the checkbox button.
clr_recyclebin_sysdrive_btn = Checkbutton(show_frame, text="Clear Systemdrive Recycle Bin", variable=var0, onvalue="1", offvalue="0", command=None)
clr_recyclebin_sysdrive_btn.grid(column=0, row=2, sticky='w')
clr_prefetchw_windir_btn = Checkbutton(show_frame, text="Clean PrefetchW in Windows Directory Data.", variable=var1, onvalue="1", offvalue="0", command=None)
clr_prefetchw_windir_btn.grid(column=0, row=3, sticky='w')
clr_d3dscache_localappdata_btn = Checkbutton(show_frame, text="Clean D3DSCached data in local app data Directory", variable=var2, onvalue="1", offvalue="0", command=None)
clr_d3dscache_localappdata_btn.grid(column=0, row=4, sticky='w')
clr_windir_temp_btn = Checkbutton(show_frame, text="Clear Windir Temporary Data", variable=var3, onvalue="1", offvalue="0", command=None)
clr_windir_temp_btn.grid(column=0, row=5, sticky='w')
clr_localappdata_temp_btn = Checkbutton(show_frame, text="Clean User Temporary Data", variable=var4, onvalue="1", offvalue="0", command=None)
clr_localappdata_temp_btn.grid(column=0, row=6, sticky='w')
clr_gchrome_webcache_incl_gpucache_codecache_btn = Checkbutton(show_frame, text="Clean Google Chrome Browser Webcached data (Incl. GPUCache, Code Cache)", variable=var5, onvalue="1", offvalue="0", command=None)
clr_gchrome_webcache_incl_gpucache_codecache_btn.grid(column=0, row=7, sticky='w')
clr_gchrome_browser_cookies_btn = Checkbutton(show_frame, text="Clean Google Chrome Browser Cookies (Incl. Cookies-journal)", variable=var6, onvalue="1", offvalue="0", command=None)
clr_gchrome_browser_cookies_btn.grid(column=0, row=8, sticky='w')
clr_default_usr_appdata_temp_btn = Checkbutton(show_frame, text="Clean Default User Temporary Files", variable=var7, onvalue="1", offvalue="0", command=None)
clr_default_usr_appdata_temp_btn.grid(column=0, row=9, sticky='w')
clr_inet_cached_data_btn = Checkbutton(show_frame, text="Clean IE (Internet Explorer) Cached data", variable=var8, onvalue="1", offvalue="0", command=None)
clr_inet_cached_data_btn.grid(column=0, row=10, sticky='w')
clr_usrclipboard_content_btn = Checkbutton(show_frame, text="Clean User Clipboard Data (Excl. Content you copy 'n' paste)", variable=var9, onvalue="1", offvalue="0", command=None)
clr_usrclipboard_content_btn.grid(column=0, row=11, sticky='w')
clr_msexplorer_thumbcacheddata_btn = Checkbutton(show_frame, text="Clean Windows Explorer Thumbnails Cached Data", variable=var10, onvalue="1", offvalue="0", command=None)
clr_msexplorer_thumbcacheddata_btn.grid(column=0, row=12, sticky='w')
clr_winrecentdocs_list_btn = Checkbutton(show_frame, text="Clean User Recent Documents List", variable=var11, onvalue="1", offvalue="0", command=None)
clr_winrecentdocs_list_btn.grid(column=0, row=13, sticky='w')
clr_discordwebclient_webcacheddata_btn = Checkbutton(show_frame, text="Clean Discord Webclient Webcached data", variable=var12, onvalue="1", offvalue="0", command=None)
clr_discordwebclient_webcacheddata_btn.grid(column=0, row=14, sticky='w')
clr_gimpstmps_btn = Checkbutton(show_frame, text="Clean GNU Image Manipulation Program's Temporary data (gimp's tmps)", variable=var13, onvalue="1", offvalue="0", command=None)
clr_gimpstmps_btn.grid(column=0, row=15, sticky='w')
clr_steam_webclient_htmlcache_btn = Checkbutton(show_frame, text="Clean Steam Webclient HTML Cached data", variable=var14, onvalue="1", offvalue="0", command=None)
clr_steam_webclient_htmlcache_btn.grid(column=0, row=16, sticky='w')
clr_windowsupdate_downloaded_updates_btn = Checkbutton(show_frame, text="Clean All Downloaded Windows Update files", variable=var15, onvalue="1", offvalue="0", command=None)
clr_windowsupdate_downloaded_updates_btn.grid(column=0, row=17, sticky='w')
clr_win10os_cached_data_btn = Checkbutton(show_frame, text="Clean Windows 10 Operating System Cached Data", variable=var16, onvalue="1", offvalue="0", command=None)
clr_win10os_cached_data_btn.grid(column=0, row=18, sticky='w')
clr_inetcookies_btn = Checkbutton(show_frame, text="Clean Internet Explorer Cookies Data", variable=var17, onvalue="1", offvalue="0", command=None)
clr_inetcookies_btn.grid(column=0, row=19, sticky='w')
clr_additionalinet_cacheddata_btn = Checkbutton(show_frame, text="Clean Internet Explorer Additional Cached Data", variable=var18, onvalue="1", offvalue="0", command=None)
clr_additionalinet_cacheddata_btn.grid(column=0, row=20, sticky='w')
clr_iedownload_history_data_btn = Checkbutton(show_frame, text="Clean Internet Explorer Downloads History Data", variable=var19, onvalue="1", offvalue="0", command=None)
clr_iedownload_history_data_btn.grid(column=0, row=21, sticky='w')
clr_win10_action_center_cached_data_btn = Checkbutton(show_frame, text="Clean Windows 10 Action Center/Notifications Center Cached data", variable=var20, onvalue="1", offvalue="0", command=None)
clr_win10_action_center_cached_data_btn.grid(column=0, row=22, sticky='w')
clr_winappux_cached_data_btn = Checkbutton(show_frame, text="Clean Windows 10 Modern Applications Cached data", variable=var21, onvalue="1", offvalue="0", command=None)
clr_winappux_cached_data_btn.grid(column=0, row=23, sticky='w')
clr_msstore_based_edge_webcached_data_btn = Checkbutton(show_frame, text="Clean Microsoft Store Based Edge Web cached data", variable=var22, onvalue="1", offvalue="0", command=None)
clr_msstore_based_edge_webcached_data_btn.grid(column=0, row=24, sticky='w')
clr_winexplorer_thumbcache_to_delete_files_btn = Checkbutton(show_frame, text="Clean Additional Windows Explorer Thumbnails Cached Data (thumbcachetodelete)", variable=var23, onvalue="1", offvalue="0", command=None)
clr_winexplorer_thumbcache_to_delete_files_btn.grid(column=0, row=25, sticky='w')
clr_chromiumbased_msedge_webcached_data_btn = Checkbutton(show_frame, text="Clean Chromium-based Microsoft Edge Webcached data (Incl. GPUCache, Code cache)", variable=var24, onvalue="1", offvalue="0", command=None)
clr_chromiumbased_msedge_webcached_data_btn.grid(column=0, row=26, sticky='w')
clr_chormiumbased_msedge_cookies_data_btn = Checkbutton(show_frame, text="Clean Chromium-based Microsoft Edge Cookie data (Incl. Cookies-journal)", variable=var25, onvalue="1", offvalue="0", command=None)
clr_chormiumbased_msedge_cookies_data_btn.grid(column=0, row=27, sticky='w')
clr_roblox_game_downloads_btn = Checkbutton(show_frame, text="Clean ROBLOX Game Downloaded Textures/Data", variable=var26, onvalue="1", offvalue="0", command=None)
clr_roblox_game_downloads_btn.grid(column=0, row=28, sticky='w')
clr_adobephotoshop_webcached_data_btn = Checkbutton(show_frame, text="Clean Adobe Photoshop 2020 Webcached data", variable=var27, onvalue="1", offvalue="0", command=None)
clr_adobephotoshop_webcached_data_btn.grid(column=0, row=29, sticky='w')
clr_sony_vegas_pro_temp_and_logs_data_btn = Checkbutton(show_frame, text="Clean Sony VEGAS Pro 17 Temporary data and log files", variable=var28, onvalue="1", offvalue="0", command=None)
clr_sony_vegas_pro_temp_and_logs_data_btn.grid(column=0, row=30, sticky='w')
clr_mcneel_rhinoceros_3d_moduling_soft_cached_data_btn = Checkbutton(show_frame, text="Clean McNeel Rhinoceros 3D Moduling Software Temporary Data", variable=var29, onvalue="1", offvalue="0", command=None)
clr_mcneel_rhinoceros_3d_moduling_soft_cached_data_btn.grid(column=0, row=31, sticky='w')
clr_cryptnet_urlcache_data_btn = Checkbutton(show_frame, text="Clean Windows 10 Cryptnet URL Cached data", variable=var30, onvalue="1", offvalue="0", command=None)
clr_cryptnet_urlcache_data_btn.grid(column=0, row=32, sticky='w')
clr_python_pip_cached_data_btn = Checkbutton(show_frame, text="Clean Python PIP Cached Data", variable=var31, onvalue="1", offvalue="0", command=None)
clr_python_pip_cached_data_btn.grid(column=0, row=33, sticky='w')
empty_winworkingsets_rammap_btn = Checkbutton(show_frame, text="Empty Running Software Workingsets using RAMMap", variable=var32, onvalue="1", offvalue="0", command=None)
empty_winworkingsets_rammap_btn.grid(column=0, row=34, sticky='w')
clr_gchrome_extension_cookies_data_btn = Checkbutton(show_frame, text="Clean Google Chrome Browser Extension Cookie Data", variable=var33, onvalue="1", offvalue="0", command=None)
clr_gchrome_extension_cookies_data_btn.grid(column=0, row=35, sticky='w')
clr_connecteddevicesplatform_win10_cached_data_btn = Checkbutton(show_frame, text="Clean Windows 10 ConnectedDevicesPlatform Cached Data (Optional - a custom env-variable)", variable=var34, onvalue="1", offvalue="0", command=None)
clr_connecteddevicesplatform_win10_cached_data_btn.grid(column=0, row=36, sticky='w')
clr_iconcache_db_file_in_localappdata_dir_btn = Checkbutton(show_frame, text="Clean Icon Cache file in Local app data folder", variable=var35, onvalue="1", offvalue="0", command=None)
clr_iconcache_db_file_in_localappdata_dir_btn.grid(column=0, row=37, sticky='w')
clr_microvirt_memu_log_data_memdump_files_btn = Checkbutton(show_frame, text="Clean Microvirt MEmu Logs and Memory Dump Files", variable=var36, onvalue="1", offvalue="0", command=None)
clr_microvirt_memu_log_data_memdump_files_btn.grid(column=0, row=38, sticky='w')
clr_adwcleaner_log_files_btn = Checkbutton(show_frame, text="Clean Malwarebytes Adware Cleaner Log data and its files", variable=var37, onvalue="1", offvalue="0", command=None)
clr_adwcleaner_log_files_btn.grid(column=0, row=39, sticky='w')
clr_perflogs_in_systemdrive_btn = Checkbutton(show_frame, text="Clean the folder Perflogs in Systemdrive volume", variable=var38, onvalue="1", offvalue="0", command=None)
clr_perflogs_in_systemdrive_btn.grid(column=0, row=40, sticky='w')
clr_dotcache_folder_in_userprofile_path_btn = Checkbutton(show_frame, text="Clean Android Cached data in your computer", variable=var39, onvalue="1", offvalue="0", command=None)
clr_dotcache_folder_in_userprofile_path_btn.grid(column=0, row=41, sticky='w')
clr_discordapp_squirrel_temp_data_btn = Checkbutton(show_frame, text="Clean Discord Windows Client Squirrel Temp", variable=var40, onvalue="1", offvalue="0", command=None)
clr_discordapp_squirrel_temp_data_btn.grid(column=0, row=42, sticky='w')
clr_locallow_temporary_data_btn = Checkbutton(show_frame, text="Clean Local Low Temporary Folders", variable=var41, onvalue="1", offvalue="0", command=None)
clr_locallow_temporary_data_btn.grid(column=0, row=43, sticky='w')
clr_elevated_diagnostics_data_btn = Checkbutton(show_frame, text="Clean Elevated Diagnostics Data folder (Only for Windows 10)", variable=var42, onvalue="1", offvalue="0", command=None)
clr_elevated_diagnostics_data_btn.grid(column=0, row=44, sticky='w')
clr_vmware_downloads_folder_btn = Checkbutton(show_frame, text="Clean VMware Downloads (All files downloaded by all VMware Software)", variable=var43, onvalue="1", offvalue="0", command=None)
clr_vmware_downloads_folder_btn.grid(column=0, row=45, sticky='w')
clr_balena_itcher_webcached_data_btn = Checkbutton(show_frame, text="Clean BalenaItcher webcached data (Incl. GPUCache, Code Cache, Local Storage, Session Storage)", variable=var44, onvalue="1", offvalue="0", command=None)
clr_balena_itcher_webcached_data_btn.grid(column=0, row=46, sticky='w')
clr_pyinstaller_temporary_data_btn = Checkbutton(show_frame, text="Clean Pyinstaller Bin Cached Data", variable=var45, onvalue="1", offvalue="0", command=None)
clr_pyinstaller_temporary_data_btn.grid(column=0, row=47, sticky='w')
clr_jedipython_additionals_btn = Checkbutton(show_frame, text="Clean Jedi Python Additional Temporary Data", variable=var46, onvalue="1", offvalue="0", command=None)
clr_jedipython_additionals_btn.grid(column=0, row=48, sticky='w')
clr_gimp_recentdocs_btn = Checkbutton(show_frame, text="Clean GNU Image Manipulation Program Recent Documents List (GIMP)", variable=var47, onvalue="1", offvalue="0", command=None)
clr_gimp_recentdocs_btn.grid(column=0, row=49, sticky='w')
clr_lowlevelformattool_licenseagreement_confirmationfile_btn = Checkbutton(show_frame, text="Clean LowLevelFormatTool (LLFT) License Agreement Confirmation File", variable=var48, onvalue="1", offvalue="0", command=None)
clr_lowlevelformattool_licenseagreement_confirmationfile_btn.grid(column=0, row=50, sticky='w')
clr_identitynexus_integration_folder_btn = Checkbutton(show_frame, text="Clean IdentityNexusIntegration Folder contents (Only for Windows 10)", variable=var49, onvalue="1", offvalue="0", command=None)
clr_identitynexus_integration_folder_btn.grid(column=0, row=51, sticky='w')
clr_scrapmechanic_axolot_games_workshop_items_cached_data_btn = Checkbutton(show_frame, text="Clean Axolot Games Scrap Mechanic Workshop Items Cached data", variable=var50, onvalue="1", offvalue="0", command=None)
clr_scrapmechanic_axolot_games_workshop_items_cached_data_btn.grid(column=0, row=52, sticky='w')
clr_roblox_game_log_files_btn = Checkbutton(show_frame, text="Clean ROBLOX Game Verbosed Log files", variable=var51, onvalue="1", offvalue="0", command=None)
clr_roblox_game_log_files_btn.grid(column=0, row=53, sticky='w')
clr_vscode_webcached_data_btn = Checkbutton(show_frame, text="Clean Microsoft Visual Studio Code Webcached data (Incl. GPUCache, Code Cache, CachedData, Cache paths)", variable=var52, onvalue="1", offvalue="0", command=None)
clr_vscode_webcached_data_btn.grid(column=0, row=54, sticky='w')
clr_vscode_cookie_data_btn = Checkbutton(show_frame, text="Clean Microsoft Visual Studio Code Cookie data (Incl. Cookies-journal)", variable=var53, onvalue="1", offvalue="0", command=None)
clr_vscode_cookie_data_btn.grid(column=0, row=55, sticky='w')
clr_vscode_cached_extensions_data_btn = Checkbutton(show_frame, text="Clean Microsoft Visual Studio Code Cached Extensions Data (Incl. VSIXs)", variable=var54, onvalue="1", offvalue="0", command=None)
clr_vscode_cached_extensions_data_btn.grid(column=0, row=56, sticky='w')
clr_winxpe_app_downloads_folder_btn = Checkbutton(show_frame, text="Clean WinXPE Creator Downloads Diretory (Requires a custom env variable)", variable=var55, onvalue="1", offvalue="0", command=None)
clr_winxpe_app_downloads_folder_btn.grid(column=0, row=57, sticky='w')
clr_servicehub_identity_file_btn = Checkbutton(show_frame, text="Clean ServiceHub Identity file (that salt file)", variable=var56, onvalue="1", offvalue="0", command=None)
clr_servicehub_identity_file_btn.grid(column=0, row=58, sticky='w')
clr_huawei_hisuite_log_data_btn = Checkbutton(show_frame, text="Clean Huawei HiSuite Log data", variable=var57, onvalue="1", offvalue="0", command=None)
clr_huawei_hisuite_log_data_btn.grid(column=0, row=59, sticky='w')
clr_minecraft_webcached_data_btn = Checkbutton(show_frame, text="Clean Minecraft Webcached data", variable=var58, onvalue="1", offvalue="0", command=None)
clr_minecraft_webcached_data_btn.grid(column=0, row=60, sticky='w')
clr_mozilla_firefox_webcached_data_btn = Checkbutton(show_frame, text="Clean Mozilla Firefox Webcached data (Incl. cache2, jumpListCache, and Shader Cache)", variable=var59, onvalue="1", offvalue="0", command=None)
clr_mozilla_firefox_webcached_data_btn.grid(column=0, row=61, sticky='w')
clr_mozilla_firefox_cookies_sqlite_file_btn = Checkbutton(show_frame, text="Clean Mozilla Firefox browser Cookie data (it is just a Sqlite file)", variable=var60, onvalue="1", offvalue="0", command=None)
clr_mozilla_firefox_cookies_sqlite_file_btn.grid(column=0, row=62, sticky='w')
clr_sony_vegas_pro_error_reports_data_btn = Checkbutton(show_frame, text="Clean Sony VEGAS Pro ERROR Reports files", variable=var61, onvalue="1", offvalue="0", command=None)
clr_sony_vegas_pro_error_reports_data_btn.grid(column=0, row=63, sticky='w')
clr_java_deployment_cached_data_btn = Checkbutton(show_frame, text="Clean Java Deployment Cached Data", variable=var62, onvalue="1", offvalue="0", command=None)
clr_java_deployment_cached_data_btn.grid(column=0, row=64, sticky='w')
clr_huawei_hisuite_dnd_temp_btn = Checkbutton(show_frame, text="Clean Huawei HiSuite Drag 'n' Drop Temporary Data", variable=var63, onvalue="1", offvalue="0", command=None)
clr_huawei_hisuite_dnd_temp_btn.grid(column=0, row=65, sticky='w')
destroy_activity_after_done_btn = Checkbutton(show_frame, text="Do you want to close this program when it's done with cleaning up temp?", variable=var64, onvalue="1", offvalue="0", command=None, cursor='hand2')
destroy_activity_after_done_btn.grid(column=0, row=66, sticky='w')
# Defining the source of the image of the about button.
pic_file_about_btn = Image.open("about_btn_noclick.png")
picture_output_about_btn = ImageTk.PhotoImage(pic_file_about_btn)
# Defining the about button.
about_window_btn = Button(show_frame, width=200, height=50, text="", image=picture_output_about_btn, command=show_about_window, cursor='hand2')
about_window_btn.grid(column=0, row=67, sticky='w')
# Defining the source of the image of the execute button.
pic_file = Image.open("execute_btn_noclick.png")
picture_output = ImageTk.PhotoImage(pic_file)
# Defining the execute button.
exec_btn = Button(show_frame, width=200 ,height=50, text="", image=picture_output, command=execute_theprogram, cursor='hand2')
exec_btn.place(x=300 ,y=1929)
space = Label(show_frame, text="")
space.grid(column=0, row=68, sticky='w')

# Executing the commands required to make the buttons active and unchecked.
clr_recyclebin_sysdrive_btn.deselect()
clr_prefetchw_windir_btn.deselect()
clr_d3dscache_localappdata_btn.deselect()
clr_windir_temp_btn.deselect()
clr_localappdata_temp_btn.deselect()
clr_gchrome_webcache_incl_gpucache_codecache_btn.deselect()
clr_gchrome_browser_cookies_btn.deselect()
clr_default_usr_appdata_temp_btn.deselect()
clr_inet_cached_data_btn.deselect()
clr_usrclipboard_content_btn.deselect()
clr_msexplorer_thumbcacheddata_btn.deselect()
clr_winrecentdocs_list_btn.deselect()
clr_discordwebclient_webcacheddata_btn.deselect()
clr_gimpstmps_btn.deselect()
clr_steam_webclient_htmlcache_btn.deselect()
clr_windowsupdate_downloaded_updates_btn.deselect()
clr_win10os_cached_data_btn.deselect()
clr_inetcookies_btn.deselect()
clr_additionalinet_cacheddata_btn.deselect()
clr_iedownload_history_data_btn.deselect()
clr_win10_action_center_cached_data_btn.deselect()
clr_winappux_cached_data_btn.deselect()
clr_msstore_based_edge_webcached_data_btn.deselect()
clr_winexplorer_thumbcache_to_delete_files_btn.deselect()
clr_chromiumbased_msedge_webcached_data_btn.deselect()
clr_chormiumbased_msedge_cookies_data_btn.deselect()
clr_roblox_game_downloads_btn.deselect()
clr_adobephotoshop_webcached_data_btn.deselect()
clr_sony_vegas_pro_temp_and_logs_data_btn.deselect()
clr_mcneel_rhinoceros_3d_moduling_soft_cached_data_btn.deselect()
clr_cryptnet_urlcache_data_btn.deselect()
clr_python_pip_cached_data_btn.deselect()
empty_winworkingsets_rammap_btn.deselect()
clr_gchrome_extension_cookies_data_btn.deselect()
clr_connecteddevicesplatform_win10_cached_data_btn.deselect()
clr_iconcache_db_file_in_localappdata_dir_btn.deselect()
clr_microvirt_memu_log_data_memdump_files_btn.deselect()
clr_adwcleaner_log_files_btn.deselect()
clr_perflogs_in_systemdrive_btn.deselect()
clr_dotcache_folder_in_userprofile_path_btn.deselect()
clr_discordapp_squirrel_temp_data_btn.deselect()
clr_locallow_temporary_data_btn.deselect()
clr_elevated_diagnostics_data_btn.deselect()
clr_vmware_downloads_folder_btn.deselect()
clr_balena_itcher_webcached_data_btn.deselect()
clr_pyinstaller_temporary_data_btn.deselect()
clr_jedipython_additionals_btn.deselect()
clr_gimp_recentdocs_btn.deselect()
clr_lowlevelformattool_licenseagreement_confirmationfile_btn.deselect()
clr_identitynexus_integration_folder_btn.deselect()
clr_scrapmechanic_axolot_games_workshop_items_cached_data_btn.deselect()
clr_roblox_game_log_files_btn.deselect()
clr_vscode_webcached_data_btn.deselect()
clr_vscode_cookie_data_btn.deselect()
clr_vscode_cached_extensions_data_btn.deselect()
clr_winxpe_app_downloads_folder_btn.deselect()
clr_servicehub_identity_file_btn.deselect()
clr_huawei_hisuite_log_data_btn.deselect()
clr_minecraft_webcached_data_btn.deselect()
clr_mozilla_firefox_webcached_data_btn.deselect()
clr_mozilla_firefox_cookies_sqlite_file_btn.deselect()
clr_sony_vegas_pro_error_reports_data_btn.deselect()
clr_java_deployment_cached_data_btn.deselect()
clr_huawei_hisuite_dnd_temp_btn.deselect()
destroy_activity_after_done_btn.deselect()


# Calling the mainloop of the Tkinter window root.
root.mainloop()