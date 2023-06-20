"""
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
"""

print()
print("Greetings from the Temp_Cleaner GUI Project.")
print("By Insertx2k Dev")
print("Github : https://github.com/insertx2k/temp_cleaner_gui")
print("Twitter : https://twitter.com/insertplayztw")
print()

# Importing all the required 3rd party modules.
from re import L
from tkinter import *
import WINTCMD
from tkinter import messagebox
from tkinter import ttk
import os
from PIL import Image, ImageTk
import time
import configparser
from tkinter import filedialog
from tkinter import scrolledtext
import subprocess
from subprocess import PIPE

# Defining the function that will get the current values of an configparser values.
GetConfig = configparser.ConfigParser()
GetConfig.read('Config.ini')


root = Tk()

# Trying to change the theme.
try:
    # Changing the root's theme.
    root.style = ttk.Style()
    root.style.theme_use("clam")
except Exception as excpt:
    print(f"The following exception had occured while trying to apply the theme 'clam' \n {excpt}")

root.title("The Temp_Cleaner GUI Project (v2.1)")
root.geometry('1202x600')
root.iconbitmap("icon0.ico")
root.minsize(1202,600)

# Changing the root's color.
root.configure(background='#dcdad5')
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

main_canvas.configure(background='#dcdad5')
main_frame.configure(background='#dcdad5')
show_frame.configure(background='#dcdad5')
# Defining some informative labels inside of the Temp_Cleaner GUI's Window.
banner = PhotoImage(file="banner.png")
banner_show = Label(show_frame, image=banner, width=1200, height=300)
banner_show.grid(column=0, row=1, sticky='w')

# Defining the function used to show the user the about window of the program.
def show_about_window():
    messagebox.showinfo("About The Temp_Cleaner GUI Project (v2.0)","""The Temp_Cleaner GUI Project by Insertx2k Dev\n
Version 2.1
Update 5
Written in Python by Insertx2k Dev
Support Twitter : @insertplayztw
Support Forum URL : https://creative-development.wixsite.com/cwofficial/forum
\n
In this update of The Temp_Cleaner GUI Project, you will no longer have to use Environment Variables to customize the program as you want, You will just need to go to it's configuration page.
GitHub page : https://github.com/insertx2k/temp_cleaner_gui
Better UI GitHub page : https://insertx2k.github.io/temp_cleaner_gui
""")

# Defining the function to execute the following selected commands : 
def execute_theprogram():
    ShowNotificationDone = True
    exec_btn.configure(text="Executing", command=None)
    selection = var0.get()
    if selection == '1':
        WINTCMD.term('rmdir /s /q "%systemdrive%\\$Recycle.bin"')
    selection1 = var1.get()
    if selection1 == '1':
        WINTCMD.term('cd /d %windir%&erase /s /f /q prefetch')
    selection2 = var2.get()
    if selection2 == '1':
        WINTCMD.term('cd /d %localappdata%&erase /s /f /q "D3DSCache"')
    selection3 = var3.get()
    if selection3 == '1':
        WINTCMD.term('cd /d %windir%&erase /s /f /q "Temp"')
    selection4 = var4.get()
    if selection4 == '1':
        WINTCMD.term('cd /d %localappdata%&erase /s /f /q "Temp"')
        messagebox.showinfo("Clean User Temporary Data", "All pending operations has been successfully completed!\nPlease keep in your mind that files in use won't be deleted.")
    selection5 = var5.get()
    if selection5 == '1':
        WINTCMD.term('cd /d %localappdata%&cd Google&cd Chrome&cd "User Data"&cd "Default"&erase /s /f /q "GPUCache"&erase /s /f /q Cache&erase /s /f /q "Code Cache"')
    selection6 = var6.get()
    if selection6 == '1':
        WINTCMD.term('cd /d %localappdata%&cd Google&cd Chrome&cd "User Data"&cd "Default"&del /s /q "Cookies"&del /s /q "Cookies-journal"')
    selection9 = var7.get()
    if selection9 == '1':
        WINTCMD.term('cd /d "%systemdrive%\\Users\\Default\\AppData\\Local"&erase /s /f /q Temp')
    selection10 = var8.get()
    if selection10 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Windows"&erase /s /f /q "INetCache"')
    selection11 = var9.get()
    if selection11 == '1':
        WINTCMD.term('@echo off | clip')
    selection12 = var10.get()
    if selection12 == '1':
        WINTCMD.term('cd /d %localappdata%&cd microsoft&cd windows&cd explorer&del /s /q *thumbcache*&cd /d %localappdata%\microsoft\windows\explorer&del /s /q *thumb*')
    selection13 = var11.get()
    if selection13 == '1':
        WINTCMD.term('cd /d %userprofile%\\AppData\\Roaming&cd Microsoft&cd Windows&erase /s /f /q Recent')
    selection14 = var12.get()
    if selection14 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\discord"&erase /s /f /q "Cache"&erase /s /f /q "Code Cache"&erase /s /f /q "GPUCache"&erase /s /f /q "Local Storage"')
    selection15 = var13.get()
    if selection15 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\GIMP\\2.10"&erase /s /f /q "tmp"')
    selection16 = var14.get()
    if selection16 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Steam\\htmlcache"&erase /s /f /q "Cache"&erase /s /f /q "Code Cache"&erase /s /f /q "GPUCache"')
    selection17 = var15.get()
    if selection17 == '1':
        WINTCMD.term('cd /d "%windir%\\SoftwareDistribution"&del /f /s /q "Download"')
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
    selection19 = var17.get()
    if selection19 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Windows"&erase /s /f /q "INetCookies"')
    selection20 = var18.get()
    if selection20 == '1':
        WINTCMD.term('cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "IECompatCache"&erase /s /f /q "IECompatUaCache"')
    selection21 = var19.get()
    if selection21 == '1':
        WINTCMD.term('cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "IEDownloadHistory"')
    selection22 = var20.get()
    if selection22 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Windows"&erase /s /f /q "ActionCenterCache"')
    selection23 = var21.get()
    if selection23 == '1':
        WINTCMD.term('cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "AppCache"')
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
    selection26 = var24.get()
    if selection26 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Edge\\User Data\\Default"&erase /s /f /q "GPUCache"&erase /s /f /q "Cache"&erase /s /f /q "Code Cache"')
    selection27 = var25.get()
    if selection27 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Microsoft\\Edge\\User Data\\Default"&del /s /q "Cookies"&del /s /q "Cookies-journal"')
    selection28 = var26.get()
    if selection28 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Roblox"&erase /s /f /q "Downloads"')
    selection29 = var27.get()
    if selection29 == '1':
        WINTCMD.term('cd /d "%appdata%\\Adobe\\Adobe Photoshop 2020\\Adobe Photoshop 2020 Settings\\web-cache-temp"&erase /s /f /q "GPUCache"&erase /s /f /q "Code Cache"&del /s /f /q "Visited Links"')
    selection30 = var28.get()
    if selection30 == '1':
        WINTCMD.term('cd /d "%localappdata%\\VEGAS Pro\\17.0"&erase /s /f /q "File Explorer Thumbnails"&erase /s /f /q "Device Explorer Thumbnails"&del /s /f /q "*.autosave.veg.bak"&del /s /f /q "svfx_Ofx*.log"')
    selection31 = var29.get()
    if selection31 == '1':
        WINTCMD.term('cd /d "%localappdata%\\McNeel\\Rhinoceros"&erase /s /f /q "temp"')
    selection32 = var30.get()
    if selection32 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\LocalLow\\Microsoft"&erase /s /f /q /A:S "CryptnetUrlCache"')
    selection33 = var31.get()
    if selection33 == '1':
        WINTCMD.term('cd /d "%localappdata%\\pip"&erase /s /f /q "cache"')
    selection34 = var32.get()
    if selection34 == '1':
        conf2 = messagebox.askquestion("Empty Windows Workingsets", "Would you really like to run RAMMap by Sysinternals to empty RAM Workingsets?")
        if conf2 == "yes":
            RAMMAPpath_var = GetConfig['ProgConfig']['RAMMapPath']
            if RAMMAPpath_var == '$DEFAULT':
                messagebox.showinfo("Notification", "The path of the RAMMap tool is set to '$DEFAULT', Continuing using the default configured RAMMap path.")
                WINTCMD.term(r'"%systemdrive%\RAMMap\RAMMap.exe" -Ew')
                messagebox.showinfo("Empty Windows Workingsets", "RAMMap.exe - Command sent.")
            else:
                WINTCMD.term(rf'""{RAMMAPpath_var}"\RAMMap.exe" -Ew')
                messagebox.showinfo("Empty Windows Workingsets", "RAMMap.exe - Command sent.")
        else:
            messagebox.showinfo("Empty Windows Workingsets", "Operation has been canceled.")
    selection35 = var33.get()
    if selection35 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Google\\Chrome\\User Data\\Default"&del /s /q "Extension Cookies"&del /s /q "Extension Cookies-journal"')
    selection36 = var34.get()
    if selection36 == '1':
        CDPCCPATH_var = GetConfig['ProgConfig']['CDPCCPATH']
        if CDPCCPATH_var == '$DEFAULT':
            messagebox.showinfo("Notification", "You didn't specify a custom location for the Windows activites cache cleaner to work on, Continuing using the Default values.")
            WINTCMD.term('cd /d "%localappdata%\\ConnectedDevicesPlatform"&erase /s /f /q "ee2999716b7783e6"')
        else:
            WINTCMD.term(rf'cd /d "%localappdata%\\ConnectedDevicesPlatform"&erase /s /f /q "{CDPCCPATH_var}"')
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
    selection39 = var37.get()
    if selection39 == '1':
        ADWCLRPATH_var = GetConfig['ProgConfig']['ADWCLRPath']
        if ADWCLRPATH_var == '$DEFAULT':
            messagebox.showinfo("Notification", "You didn't specify a custom working location for the AdwareCleaner Cleaner, Continuing using the default path.")
            WINTCMD.term('erase /s /f /q "%systemdrive%\\AdwCleaner\\Logs"')
        else:
            WINTCMD.term(rf'erase /s /f /q "{ADWCLRPATH_var}\Logs"')
    selection40 = var38.get()
    if selection40 == '1':
        WINTCMD.term('%systemdrive%&&cd /d \\.\\&erase /s /f /q "PerfLogs"')
    selection41 = var39.get()
    if selection41 == '1':
        WINTCMD.term('cd /d "%userprofile%"&rmdir /s /q ".cache"')
    selection42 = var40.get()
    if selection42 == '1':
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "SquirrelTemp"')
    selection43 = var41.get()
    if selection43 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\LocalLow"&erase /s /f /q "Temp"')
    selection44 = var42.get()
    if selection44 == '1':
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "ElevatedDiagnostics"')
    selection45 = var43.get()
    if selection45 == '1':
        WINTCMD.term('cd /d "%localappdata%\\VMware"&erase /s /f /q "vmware-download*"')
    selection46 = var44.get()
    if selection46 == '1':
        WINTCMD.term('cd /d "%userprofile%\\appdata\\roaming\\balena-etcher"&erase /s /f /q "blob_storage"&erase /s /f /q "Code Cache"&erase /s /f /q "GPUCache"&erase /s /f /q "Local Storage"&erase /s /f /q "Session Storage"')
    selection47 = var45.get()
    if selection47 == '1':
        WINTCMD.term('cd /d "%appdata%"&cd /d "%userprofile%\\AppData\\Roaming"&erase /s /f /q "pyinstaller"')
    selection48 = var46.get()
    if selection48 == '1':
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "Jedi"')
    selection49 = var47.get()
    if selection49 == '1':
        WINTCMD.term('cd /d "%localappdata%"&del /s /q "recently-used.xbel"')
    selection50 = var48.get()
    if selection50 == '1':
        WINTCMD.term('cd /d "%localappdata%"&del /s /q "llftool.*.agreement"')
    selection51 = var49.get()
    if selection51 == '1':
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "IdentityNexusIntegration"')
    selection52 = var50.get()
    if selection52 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Axolot Games"&cd "Scrap Mechanic"&cd "Temp"&erase /s /f /q "WorkshopIcons"')
    selection53 = var51.get()
    if selection53 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Roblox"&erase /s /f /q "logs"')
    selection54 = var52.get()
    if selection54 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\Code"&erase /s /f /q "GPUCache"&erase /s /f /q "Code Cache"&erase /s /f /q "CachedData"&erase /s /f /q "Cache"')
    selection55 = var53.get()
    if selection55 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\Code"&del /s /q "Cookies"&del /s /q "Cookies-journal"')
    selection56 = var54.get()
    if selection56 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\Code"&erase /s /f /q "CachedExtensions"&erase /s /f /q "CachedExtensionVSIXs"')
    selection57 = var55.get()
    if selection57 == '1':
        WINXPEPATH_var = GetConfig['ProgConfig']['WINXPEPATH']
        if WINXPEPATH_var == '$NONE':
            messagebox.showinfo("An ERROR has occured", "You didn't specify the path of the 'WinXPE' program, The cleaner can't continue.")
        else:
            WINTCMD.term(rf'erase /s /f /q "{WINXPEPATH_var}\Temp"')
            messagebox.showinfo("Note", "You will need to redownload all downloaded data by the tool for the exporting phase to be done!")
            
    selection58 = var56.get()
    if selection58 == '1':
        WINTCMD.term('cd /d "%localappdata%"&erase /s /f /q "ServiceHub"')
        messagebox.showinfo("Clean ServiceHub identity file", "Done deleting the Service Hub identity file (salt file)!")
        messagebox.showinfo("Note", "Some Windows 10 features that depends on this feature might not function properly.")
    selection59 = var57.get()
    if selection59 == '1':
        WINTCMD.term('erase /s /f /q "%localappdata%\\HiSuite\\log"')
    selection60 = var58.get()
    if selection60 == '1':
        WINTCMD.term('erase /s /f /q "%userprofile%\\AppData\\Roaming\\.minecraft\\webcache"')
    selection61 = var59.get()
    if selection61 == '1':
        WINTCMD.term('cd /d "%localappdata%\\Mozilla\\Firefox\\Profiles"&cd *.default-release&erase /s /f /q "cache2"&erase /s /f /q "jumpListCache"&cd /d "%userprofile%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"&cd *.default-release&erase /s /f /q "shader-cache"')
    selection62 = var60.get()
    if selection62 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"&cd *.default-release&del /s /q "cookies.sqlite"')
    selection63 = var61.get()
    if selection63 == '1':
        WINTCMD.term('cd /d "%localappdata%\\VEGAS"&erase /s /f /q "ErrorReport"')
    selection64 = var62.get()
    if selection64 == '1':
        WINTCMD.term('cd /d "%userprofile%\\AppData\\LocalLow\\Sun\\Java\\Deployment"&erase /s /f /q "tmp"')
    selection65 = var63.get()
    if selection65 == '1':
        WINTCMD.term('cd /d "%localappdata%\\HiSuite\\userdata"&erase /s /f /q "DropTemp"')
    selection66 = var64.get()
    if selection66 == '1':
        ShowNotificationDone = False
        root.destroy()
    # Sleeping a bit for longer (or equal) to 5 seconds.
    time.sleep(1)

    try:
        # Ok, let's revert everything back to what it was before.
        exec_btn.configure(text="Execute", command=execute_theprogram)
    except TclError as tkerr:
        pass

    
    # Fixing the bug that caused the user to see another tk window appearing when they select to close the program when everything had completed!
    if ShowNotificationDone == True:
        ShowNotificationAllDone()
    else:
        pass

def ShowNotificationAllDone():
    # Now, let's send the user a message telling them that everything had done.
    messagebox.showinfo("Complete", "All pending operations has been completed!")


def show_output():
    # Configuring the root.
    output_root = Tk()
    output_root.title("Console Output @ Temp_Cleaner GUI")
    output_root.geometry('600x200')
    output_root.minsize(600, 300)
    output_root.resizable(True, True)
    try:
        output_root.iconbitmap('icon0.ico')
    except Exception as excpt462:
        print(f"\nUnable to load the icon file 'icon0.ico' due to the following exception : \n {excpt462}")
    # Trying to change the theme.
    try:
        # Changing the root's theme.
        output_root.style = ttk.Style()
        output_root.style.theme_use("clam")
    except Exception as excpt:
       print(f"The following exception had occured while trying to apply the theme 'clam' \n {excpt}")
    
    # Creating a scrolledtext widget.
    output_show = scrolledtext.ScrolledText(output_root, cursor='arrow', background='#282c34', foreground='white', selectbackground='orange', state='disabled', font=("Arial", 14))
    output_show.pack(fill=BOTH, expand=1)

    output_show.configure(state='normal')
    output_show.delete(1.0, END)
    output_show.insert(END, "The Temp_Cleaner GUI Project\nDebugging Console\n\n# The console output will appear here as soon as any process begins.")
    output_show.insert(END, "\n")
    output_show.configure(state='disabled')

    # Calling the tk mainloop.
    output_root.mainloop()

# Defining the function that calls the configuration window of this program.
def StartConfigurationWindow():
    """
    This thing here just defines the Configuration window of such software.
    WARNING : THIS THING HERE IS COMPLETELY EXPERIEMENTAL, SO PLEASE DO NOT MESS WITH IT SO MUCH.
    """
    # Defining the function used to destroy the whole activity without saving any changes.
    def SelfDestroy():
        ConfigRoot.destroy()

    # Defining the browse for directory function for all browsing folders.
    def BrowseForDirectory(parent):
        BrowseForDirectoryWindow = filedialog.askdirectory()
        FinalDirectory = BrowseForDirectoryWindow
        parent.delete(0, END)
        parent.insert(INSERT, FinalDirectory)

    # Defining the browse 1 func.
    def BrowseOne():
        BrowseForDirectory(rammappath_input)
    
    def BrowseTwo():
        BrowseForDirectory(adwcleanerwpath_input)
    
    def BrowseThree():
        BrowseForDirectory(winxpeapppath_input)
    
    def BrowseFour():
        BrowseForDirectory(cdpccpath_input)


    # Defining the function to retrieve the configuration from the configuration file then outputs it into the textboxes.
    def RetrieveConfig():
        """
        The function used to get the configuration information from the file "Config.ini" in the current program path.
        Do not try to call this function, it will be automatically called when needed.
        """

        RetrieveConfig_Init = configparser.ConfigParser()
        try:
            RetrieveConfig_Init.read("Config.ini")
        except:
            messagebox.showerror("Runtime Exception", "Unable to retrieve the configuration information, this can be due to a hard exception, or a something else, the settings window will close.")
            ConfigRoot.destroy()
        
        try:
            rammappath_input.insert(INSERT, RetrieveConfig_Init['ProgConfig']['RAMMapPath'])
            adwcleanerwpath_input.insert(INSERT, RetrieveConfig_Init['ProgConfig']['ADWCLRPath'])
            winxpeapppath_input.insert(INSERT, RetrieveConfig_Init['ProgConfig']['WINXPEPATH'])
            cdpccpath_input.insert(INSERT, RetrieveConfig_Init['ProgConfig']['CDPCCPATH'])
        except:
            messagebox.showerror("A runtime exception", "Unable to read the configuration file from your computer, please make sure to give this program a permission to read files in your hard disk if blocked by your antivirus software and try again, The settings window will close.")
            ConfigRoot.destroy()



    # It is the time to define the function used to save the changes to the configuration file "Config.ini"
    def SaveConfigurationandQuit():
        try:
            ConfigFileSaveProcess = configparser.ConfigParser()
            ConfigFileSaveProcess.read("Config.ini")
        except:
            messagebox.showerror("A runtime exception", "Unable to open the configuration file on your computer, please make sure to give this program enough permissions to do so, and if your antivirus blocks it, please give it access and try again.")
            ConfigRoot.destroy()

        # Second try.
        try:
            ConfigFileSaveProcess['ProgConfig']['RAMMapPath'] = rammappath_input.get()
            ConfigFileSaveProcess['ProgConfig']['ADWCLRPath'] = adwcleanerwpath_input.get()
            ConfigFileSaveProcess['ProgConfig']['WINXPEPATH'] = winxpeapppath_input.get()
            ConfigFileSaveProcess['ProgConfig']['CDPCCPATH'] = cdpccpath_input.get()

            # Right now, I guess it is enough and we should rn write the configuration data to the file "Config.ini".
            with open("Config.ini", 'w') as ConfigFileProcessor:
                    ConfigFileSaveProcess.write(ConfigFileProcessor)

            # Defining the window which will tell the user that a reboot is needed to apply the changes.
            messagebox.showinfo("Saved your changes", "All changes you did has been successfully saved, but for the changes to take effect, you will need to restart Temp_Cleaner GUI.")

            # Okay, enough with that, let's destroy the main loop ok?
            ConfigRoot.destroy()
        except:
            messagebox.showerror("A runtime exception", "Unable to save your changes to the file 'Config.ini', Nothing has changed yet, and this window will not close.")

    # Defining the root constructor.
    ConfigRoot = Tk()
    
    # Defining the root properties.
    ConfigRoot.title("Settings @ Temp_Cleaner GUI")
    ConfigRoot.geometry('1202x600')
    ConfigRoot.resizable(False,False)
    ConfigRoot.minsize(1202,600)
    ConfigRoot.maxsize(1202,600)
    ConfigRoot.iconbitmap("icon0.ico")
    ConfigRoot.configure(bg='#008aff')

    # Defining some informative labels (Basically some bla bla blas).
    lbl0_config = Label(ConfigRoot, text="Temp_Cleaner Settings", font=("Arial Bold", 32), background='#008aff', foreground='white')
    lbl0_config.place(x=20, y=7)
    lbl1_config = Label(ConfigRoot, text="Configure The Working Pathes and all related settings of Temp_Cleaner GUI", foreground='white', background='#008aff', font=("Arial", 12))
    lbl1_config.place(x=20, y=70)
    lbl2_config = Label(ConfigRoot, text="Enter the path where RAMMap by Sysinternals tool executable is stored in :", foreground='white', background='#008aff', font=("Arial",12))
    lbl2_config.place(x=20, y=100)
    rammappath_input = ttk.Entry(ConfigRoot, width=180)
    rammappath_input.place(x=20, y=130)
    rammappath_input_browsebtn = ttk.Button(ConfigRoot, text="...", command=BrowseOne)
    rammappath_input_browsebtn.place(x=1108, y=131, relwidth=0.027, relheight=0.033)
    lbl3_config = Label(ConfigRoot, text="Enter the current working path of the tool MalwareBytes AdwareCleaner :", foreground='white', background='#008aff', font=("Arial",12))
    lbl3_config.place(x=20, y=155)
    adwcleanerwpath_input = ttk.Entry(ConfigRoot, width=180)
    adwcleanerwpath_input.place(x=20, y=180)
    adwcleanerwpath_input_browsebtn = ttk.Button(ConfigRoot, text="...", command=BrowseTwo)
    adwcleanerwpath_input_browsebtn.place(x=1108, y=180, relwidth=0.027, relheight=0.033)
    lbl4_config = Label(ConfigRoot, text="WinXPE Program Path :", foreground='white', background='#008aff', font=("Arial", 12))
    lbl4_config.place(x=20, y=205)
    winxpeapppath_input = ttk.Entry(ConfigRoot, width=180)
    winxpeapppath_input.place(x=20, y=230)
    winxpeapppath_input_browsebtn = ttk.Button(ConfigRoot, text="...", command=BrowseThree)
    winxpeapppath_input_browsebtn.place(x=1108, y=230, relwidth=0.027, relheight=0.033)
    lbl5_config = Label(ConfigRoot, text="Enter the name of the User ID folder inside the WindowsActivitiesCache Folder (Optional) :", foreground='white', background='#008aff', font=("Arial",12))
    lbl5_config.place(x=20, y=257)
    cdpccpath_input = ttk.Entry(ConfigRoot, width=180)
    cdpccpath_input.place(x=20, y=283)
    cdpccpath_input_browsebtn = ttk.Button(ConfigRoot, text="...", command=BrowseFour)
    cdpccpath_input_browsebtn.place(x=1108, y=283, relwidth=0.027, relheight=0.033)
    # Defining the copyright notice label.
    copyright_lbl0 = Label(ConfigRoot, text="""Copyright (C) Insertx2k Dev (Mr.X) 2018-2021 - All rights reserved.

 A simple program made to help you erase temporary files in your Windows-based PC.
 Copyright (C) 2021 - Insertx2k Dev
 
 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License along
 with this program; if not, write to the Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
""", font=("Arial Bold", 8), background='#008aff', foreground='white')
    copyright_lbl0.place(x=345, y=307)
    # Defining the buttons used to destroy the configuration window, or to save changes and to close the window (I honestly don't know)
    # Ok.
    # Gas Gas Gas, I'm gonna step on the gas.

    closewindow_btn = ttk.Button(ConfigRoot, text="Quit", command=SelfDestroy)
    closewindow_btn.place(x=20, y=550, relwidth=0.30, relheight=0.060)

    # Tonight I'd fly, and be your lover.
    # Yeah, Yeah, Yeah....

    applychangesandclose_btn = ttk.Button(ConfigRoot, text="Apply and Quit", command=SaveConfigurationandQuit)
    applychangesandclose_btn.place(x=800, y=550, relwidth=0.30, relheight=0.060)

    # Gas Gas Gas.
    # I'm gonna run in the flash.
    # Tonight I will fight, to be the winner.

    lbl6_config = Label(ConfigRoot, text="License : ", font=("Arial Bold", 20), foreground='white', background='#008aff')
    lbl6_config.place(x=200, y=400)



    # Calling the function to retrieve the configuration information from the config.ini file.
    RetrieveConfig()

    # Calling the ConfigRoot's Mainloop (Used to allow the user to interact to the window freely)
    ConfigRoot.mainloop()

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
clr_recyclebin_sysdrive_btn = ttk.Checkbutton(show_frame, text="Clear Systemdrive Recycle Bin", variable=var0, onvalue="1", offvalue="0", command=None)
clr_recyclebin_sysdrive_btn.grid(column=0, row=2, sticky='w')
clr_prefetchw_windir_btn = ttk.Checkbutton(show_frame, text="Clean PrefetchW in Windows Directory Data.", variable=var1, onvalue="1", offvalue="0", command=None)
clr_prefetchw_windir_btn.grid(column=0, row=3, sticky='w')
clr_d3dscache_localappdata_btn = ttk.Checkbutton(show_frame, text="Clean D3DSCached data in local app data Directory", variable=var2, onvalue="1", offvalue="0", command=None)
clr_d3dscache_localappdata_btn.grid(column=0, row=4, sticky='w')
clr_windir_temp_btn = ttk.Checkbutton(show_frame, text="Clear Windir Temporary Data", variable=var3, onvalue="1", offvalue="0", command=None)
clr_windir_temp_btn.grid(column=0, row=5, sticky='w')
clr_localappdata_temp_btn = ttk.Checkbutton(show_frame, text="Clean User Temporary Data", variable=var4, onvalue="1", offvalue="0", command=None)
clr_localappdata_temp_btn.grid(column=0, row=6, sticky='w')
clr_gchrome_webcache_incl_gpucache_codecache_btn = ttk.Checkbutton(show_frame, text="Clean Google Chrome Browser Webcached data (Incl. GPUCache, Code Cache)", variable=var5, onvalue="1", offvalue="0", command=None)
clr_gchrome_webcache_incl_gpucache_codecache_btn.grid(column=0, row=7, sticky='w')
clr_gchrome_browser_cookies_btn = ttk.Checkbutton(show_frame, text="Clean Google Chrome Browser Cookies (Incl. Cookies-journal)", variable=var6, onvalue="1", offvalue="0", command=None)
clr_gchrome_browser_cookies_btn.grid(column=0, row=8, sticky='w')
clr_default_usr_appdata_temp_btn = ttk.Checkbutton(show_frame, text="Clean Default User Temporary Files", variable=var7, onvalue="1", offvalue="0", command=None)
clr_default_usr_appdata_temp_btn.grid(column=0, row=9, sticky='w')
clr_inet_cached_data_btn = ttk.Checkbutton(show_frame, text="Clean IE (Internet Explorer) Cached data", variable=var8, onvalue="1", offvalue="0", command=None)
clr_inet_cached_data_btn.grid(column=0, row=10, sticky='w')
clr_usrclipboard_content_btn = ttk.Checkbutton(show_frame, text="Clean User Clipboard Data (Excl. Content you copy 'n' paste)", variable=var9, onvalue="1", offvalue="0", command=None)
clr_usrclipboard_content_btn.grid(column=0, row=11, sticky='w')
clr_msexplorer_thumbcacheddata_btn = ttk.Checkbutton(show_frame, text="Clean Windows Explorer Thumbnails Cached Data", variable=var10, onvalue="1", offvalue="0", command=None)
clr_msexplorer_thumbcacheddata_btn.grid(column=0, row=12, sticky='w')
clr_winrecentdocs_list_btn = ttk.Checkbutton(show_frame, text="Clean User Recent Documents List", variable=var11, onvalue="1", offvalue="0", command=None)
clr_winrecentdocs_list_btn.grid(column=0, row=13, sticky='w')
clr_discordwebclient_webcacheddata_btn = ttk.Checkbutton(show_frame, text="Clean Discord Webclient Webcached data", variable=var12, onvalue="1", offvalue="0", command=None)
clr_discordwebclient_webcacheddata_btn.grid(column=0, row=14, sticky='w')
clr_gimpstmps_btn = ttk.Checkbutton(show_frame, text="Clean GNU Image Manipulation Program's Temporary data (gimp's tmps)", variable=var13, onvalue="1", offvalue="0", command=None)
clr_gimpstmps_btn.grid(column=0, row=15, sticky='w')
clr_steam_webclient_htmlcache_btn = ttk.Checkbutton(show_frame, text="Clean Steam Webclient HTML Cached data", variable=var14, onvalue="1", offvalue="0", command=None)
clr_steam_webclient_htmlcache_btn.grid(column=0, row=16, sticky='w')
clr_windowsupdate_downloaded_updates_btn = ttk.Checkbutton(show_frame, text="Clean All Downloaded Windows Update files", variable=var15, onvalue="1", offvalue="0", command=None)
clr_windowsupdate_downloaded_updates_btn.grid(column=0, row=17, sticky='w')
clr_win10os_cached_data_btn = ttk.Checkbutton(show_frame, text="Clean Windows 10 Operating System Cached Data", variable=var16, onvalue="1", offvalue="0", command=None)
clr_win10os_cached_data_btn.grid(column=0, row=18, sticky='w')
clr_inetcookies_btn = ttk.Checkbutton(show_frame, text="Clean Internet Explorer Cookies Data", variable=var17, onvalue="1", offvalue="0", command=None)
clr_inetcookies_btn.grid(column=0, row=19, sticky='w')
clr_additionalinet_cacheddata_btn = ttk.Checkbutton(show_frame, text="Clean Internet Explorer Additional Cached Data", variable=var18, onvalue="1", offvalue="0", command=None)
clr_additionalinet_cacheddata_btn.grid(column=0, row=20, sticky='w')
clr_iedownload_history_data_btn = ttk.Checkbutton(show_frame, text="Clean Internet Explorer Downloads History Data", variable=var19, onvalue="1", offvalue="0", command=None)
clr_iedownload_history_data_btn.grid(column=0, row=21, sticky='w')
clr_win10_action_center_cached_data_btn = ttk.Checkbutton(show_frame, text="Clean Windows 10 Action Center/Notifications Center Cached data", variable=var20, onvalue="1", offvalue="0", command=None)
clr_win10_action_center_cached_data_btn.grid(column=0, row=22, sticky='w')
clr_winappux_cached_data_btn = ttk.Checkbutton(show_frame, text="Clean Windows 10 Modern Applications Cached data", variable=var21, onvalue="1", offvalue="0", command=None)
clr_winappux_cached_data_btn.grid(column=0, row=23, sticky='w')
clr_msstore_based_edge_webcached_data_btn = ttk.Checkbutton(show_frame, text="Clean Microsoft Store Based Edge Web cached data", variable=var22, onvalue="1", offvalue="0", command=None)
clr_msstore_based_edge_webcached_data_btn.grid(column=0, row=24, sticky='w')
clr_winexplorer_thumbcache_to_delete_files_btn = ttk.Checkbutton(show_frame, text="Clean Additional Windows Explorer Thumbnails Cached Data (thumbcachetodelete)", variable=var23, onvalue="1", offvalue="0", command=None)
clr_winexplorer_thumbcache_to_delete_files_btn.grid(column=0, row=25, sticky='w')
clr_chromiumbased_msedge_webcached_data_btn = ttk.Checkbutton(show_frame, text="Clean Chromium-based Microsoft Edge Webcached data (Incl. GPUCache, Code cache)", variable=var24, onvalue="1", offvalue="0", command=None)
clr_chromiumbased_msedge_webcached_data_btn.grid(column=0, row=26, sticky='w')
clr_chormiumbased_msedge_cookies_data_btn = ttk.Checkbutton(show_frame, text="Clean Chromium-based Microsoft Edge Cookie data (Incl. Cookies-journal)", variable=var25, onvalue="1", offvalue="0", command=None)
clr_chormiumbased_msedge_cookies_data_btn.grid(column=0, row=27, sticky='w')
clr_roblox_game_downloads_btn = ttk.Checkbutton(show_frame, text="Clean ROBLOX Game Downloaded Textures/Data", variable=var26, onvalue="1", offvalue="0", command=None)
clr_roblox_game_downloads_btn.grid(column=0, row=28, sticky='w')
clr_adobephotoshop_webcached_data_btn = ttk.Checkbutton(show_frame, text="Clean Adobe Photoshop 2020 Webcached data", variable=var27, onvalue="1", offvalue="0", command=None)
clr_adobephotoshop_webcached_data_btn.grid(column=0, row=29, sticky='w')
clr_sony_vegas_pro_temp_and_logs_data_btn = ttk.Checkbutton(show_frame, text="Clean Sony VEGAS Pro 17 Temporary data and log files", variable=var28, onvalue="1", offvalue="0", command=None)
clr_sony_vegas_pro_temp_and_logs_data_btn.grid(column=0, row=30, sticky='w')
clr_mcneel_rhinoceros_3d_moduling_soft_cached_data_btn = ttk.Checkbutton(show_frame, text="Clean McNeel Rhinoceros 3D Moduling Software Temporary Data", variable=var29, onvalue="1", offvalue="0", command=None)
clr_mcneel_rhinoceros_3d_moduling_soft_cached_data_btn.grid(column=0, row=31, sticky='w')
clr_cryptnet_urlcache_data_btn = ttk.Checkbutton(show_frame, text="Clean Windows 10 Cryptnet URL Cached data", variable=var30, onvalue="1", offvalue="0", command=None)
clr_cryptnet_urlcache_data_btn.grid(column=0, row=32, sticky='w')
clr_python_pip_cached_data_btn = ttk.Checkbutton(show_frame, text="Clean Python PIP Cached Data", variable=var31, onvalue="1", offvalue="0", command=None)
clr_python_pip_cached_data_btn.grid(column=0, row=33, sticky='w')
empty_winworkingsets_rammap_btn = ttk.Checkbutton(show_frame, text="Empty Running Software Workingsets using RAMMap", variable=var32, onvalue="1", offvalue="0", command=None)
empty_winworkingsets_rammap_btn.grid(column=0, row=34, sticky='w')
clr_gchrome_extension_cookies_data_btn = ttk.Checkbutton(show_frame, text="Clean Google Chrome Browser Extension Cookie Data", variable=var33, onvalue="1", offvalue="0", command=None)
clr_gchrome_extension_cookies_data_btn.grid(column=0, row=35, sticky='w')
clr_connecteddevicesplatform_win10_cached_data_btn = ttk.Checkbutton(show_frame, text="Clean Windows 10 ConnectedDevicesPlatform Cached Data (Requires you to set it's path in Settings)", variable=var34, onvalue="1", offvalue="0", command=None)
clr_connecteddevicesplatform_win10_cached_data_btn.grid(column=0, row=36, sticky='w')
clr_iconcache_db_file_in_localappdata_dir_btn = ttk.Checkbutton(show_frame, text="Clean Icon Cache file in Local app data folder", variable=var35, onvalue="1", offvalue="0", command=None)
clr_iconcache_db_file_in_localappdata_dir_btn.grid(column=0, row=37, sticky='w')
clr_microvirt_memu_log_data_memdump_files_btn = ttk.Checkbutton(show_frame, text="Clean Microvirt MEmu Logs and Memory Dump Files", variable=var36, onvalue="1", offvalue="0", command=None)
clr_microvirt_memu_log_data_memdump_files_btn.grid(column=0, row=38, sticky='w')
clr_adwcleaner_log_files_btn = ttk.Checkbutton(show_frame, text="Clean Malwarebytes Adware Cleaner Log data and its files", variable=var37, onvalue="1", offvalue="0", command=None)
clr_adwcleaner_log_files_btn.grid(column=0, row=39, sticky='w')
clr_perflogs_in_systemdrive_btn = ttk.Checkbutton(show_frame, text="Clean the folder Perflogs in Systemdrive volume", variable=var38, onvalue="1", offvalue="0", command=None)
clr_perflogs_in_systemdrive_btn.grid(column=0, row=40, sticky='w')
clr_dotcache_folder_in_userprofile_path_btn = ttk.Checkbutton(show_frame, text="Clean Android Cached data in your computer", variable=var39, onvalue="1", offvalue="0", command=None)
clr_dotcache_folder_in_userprofile_path_btn.grid(column=0, row=41, sticky='w')
clr_discordapp_squirrel_temp_data_btn = ttk.Checkbutton(show_frame, text="Clean Discord Windows Client Squirrel Temp", variable=var40, onvalue="1", offvalue="0", command=None)
clr_discordapp_squirrel_temp_data_btn.grid(column=0, row=42, sticky='w')
clr_locallow_temporary_data_btn = ttk.Checkbutton(show_frame, text="Clean Local Low Temporary Folders", variable=var41, onvalue="1", offvalue="0", command=None)
clr_locallow_temporary_data_btn.grid(column=0, row=43, sticky='w')
clr_elevated_diagnostics_data_btn = ttk.Checkbutton(show_frame, text="Clean Elevated Diagnostics Data folder (Only for Windows 10)", variable=var42, onvalue="1", offvalue="0", command=None)
clr_elevated_diagnostics_data_btn.grid(column=0, row=44, sticky='w')
clr_vmware_downloads_folder_btn = ttk.Checkbutton(show_frame, text="Clean VMware Downloads (All files downloaded by all VMware Software)", variable=var43, onvalue="1", offvalue="0", command=None)
clr_vmware_downloads_folder_btn.grid(column=0, row=45, sticky='w')
clr_balena_itcher_webcached_data_btn = ttk.Checkbutton(show_frame, text="Clean BalenaItcher webcached data (Incl. GPUCache, Code Cache, Local Storage, Session Storage)", variable=var44, onvalue="1", offvalue="0", command=None)
clr_balena_itcher_webcached_data_btn.grid(column=0, row=46, sticky='w')
clr_pyinstaller_temporary_data_btn = ttk.Checkbutton(show_frame, text="Clean Pyinstaller Bin Cached Data", variable=var45, onvalue="1", offvalue="0", command=None)
clr_pyinstaller_temporary_data_btn.grid(column=0, row=47, sticky='w')
clr_jedipython_additionals_btn = ttk.Checkbutton(show_frame, text="Clean Jedi Python Additional Temporary Data", variable=var46, onvalue="1", offvalue="0", command=None)
clr_jedipython_additionals_btn.grid(column=0, row=48, sticky='w')
clr_gimp_recentdocs_btn = ttk.Checkbutton(show_frame, text="Clean GNU Image Manipulation Program Recent Documents List (GIMP)", variable=var47, onvalue="1", offvalue="0", command=None)
clr_gimp_recentdocs_btn.grid(column=0, row=49, sticky='w')
clr_lowlevelformattool_licenseagreement_confirmationfile_btn = ttk.Checkbutton(show_frame, text="Clean LowLevelFormatTool (LLFT) License Agreement Confirmation File", variable=var48, onvalue="1", offvalue="0", command=None)
clr_lowlevelformattool_licenseagreement_confirmationfile_btn.grid(column=0, row=50, sticky='w')
clr_identitynexus_integration_folder_btn = ttk.Checkbutton(show_frame, text="Clean IdentityNexusIntegration Folder contents (Only for Windows 10)", variable=var49, onvalue="1", offvalue="0", command=None)
clr_identitynexus_integration_folder_btn.grid(column=0, row=51, sticky='w')
clr_scrapmechanic_axolot_games_workshop_items_cached_data_btn = ttk.Checkbutton(show_frame, text="Clean Axolot Games Scrap Mechanic Workshop Items Cached data", variable=var50, onvalue="1", offvalue="0", command=None)
clr_scrapmechanic_axolot_games_workshop_items_cached_data_btn.grid(column=0, row=52, sticky='w')
clr_roblox_game_log_files_btn = ttk.Checkbutton(show_frame, text="Clean ROBLOX Game Verbosed Log files", variable=var51, onvalue="1", offvalue="0", command=None)
clr_roblox_game_log_files_btn.grid(column=0, row=53, sticky='w')
clr_vscode_webcached_data_btn = ttk.Checkbutton(show_frame, text="Clean Microsoft Visual Studio Code Webcached data (Incl. GPUCache, Code Cache, CachedData, Cache paths)", variable=var52, onvalue="1", offvalue="0", command=None)
clr_vscode_webcached_data_btn.grid(column=0, row=54, sticky='w')
clr_vscode_cookie_data_btn = ttk.Checkbutton(show_frame, text="Clean Microsoft Visual Studio Code Cookie data (Incl. Cookies-journal)", variable=var53, onvalue="1", offvalue="0", command=None)
clr_vscode_cookie_data_btn.grid(column=0, row=55, sticky='w')
clr_vscode_cached_extensions_data_btn = ttk.Checkbutton(show_frame, text="Clean Microsoft Visual Studio Code Cached Extensions Data (Incl. VSIXs)", variable=var54, onvalue="1", offvalue="0", command=None)
clr_vscode_cached_extensions_data_btn.grid(column=0, row=56, sticky='w')
clr_winxpe_app_downloads_folder_btn = ttk.Checkbutton(show_frame, text="Clean WinXPE Creator Downloads Diretory (Requires you to set it's path on Settings)", variable=var55, onvalue="1", offvalue="0", command=None)
clr_winxpe_app_downloads_folder_btn.grid(column=0, row=57, sticky='w')
clr_servicehub_identity_file_btn = ttk.Checkbutton(show_frame, text="Clean ServiceHub Identity file (that salt file)", variable=var56, onvalue="1", offvalue="0", command=None)
clr_servicehub_identity_file_btn.grid(column=0, row=58, sticky='w')
clr_huawei_hisuite_log_data_btn = ttk.Checkbutton(show_frame, text="Clean Huawei HiSuite Log data", variable=var57, onvalue="1", offvalue="0", command=None)
clr_huawei_hisuite_log_data_btn.grid(column=0, row=59, sticky='w')
clr_minecraft_webcached_data_btn = ttk.Checkbutton(show_frame, text="Clean Minecraft Webcached data", variable=var58, onvalue="1", offvalue="0", command=None)
clr_minecraft_webcached_data_btn.grid(column=0, row=60, sticky='w')
clr_mozilla_firefox_webcached_data_btn = ttk.Checkbutton(show_frame, text="Clean Mozilla Firefox Webcached data (Incl. cache2, jumpListCache, and Shader Cache)", variable=var59, onvalue="1", offvalue="0", command=None)
clr_mozilla_firefox_webcached_data_btn.grid(column=0, row=61, sticky='w')
clr_mozilla_firefox_cookies_sqlite_file_btn = ttk.Checkbutton(show_frame, text="Clean Mozilla Firefox browser Cookie data (it is just a Sqlite file)", variable=var60, onvalue="1", offvalue="0", command=None)
clr_mozilla_firefox_cookies_sqlite_file_btn.grid(column=0, row=62, sticky='w')
clr_sony_vegas_pro_error_reports_data_btn = ttk.Checkbutton(show_frame, text="Clean Sony VEGAS Pro ERROR Reports files", variable=var61, onvalue="1", offvalue="0", command=None)
clr_sony_vegas_pro_error_reports_data_btn.grid(column=0, row=63, sticky='w')
clr_java_deployment_cached_data_btn = ttk.Checkbutton(show_frame, text="Clean Java Deployment Cached Data", variable=var62, onvalue="1", offvalue="0", command=None)
clr_java_deployment_cached_data_btn.grid(column=0, row=64, sticky='w')
clr_huawei_hisuite_dnd_temp_btn = ttk.Checkbutton(show_frame, text="Clean Huawei HiSuite Drag 'n' Drop Temporary Data", variable=var63, onvalue="1", offvalue="0", command=None)
clr_huawei_hisuite_dnd_temp_btn.grid(column=0, row=65, sticky='w')
destroy_activity_after_done_btn = ttk.Checkbutton(show_frame, text="Do you want to close this program when it's done with cleaning up temp?", variable=var64, onvalue="1", offvalue="0", command=None, cursor='hand2')
destroy_activity_after_done_btn.grid(column=0, row=66, sticky='w')
# Defining the about button.
about_window_btn = ttk.Button(show_frame, text="About", command=show_about_window, cursor='hand2')
about_window_btn.place(x=10, y=1670, relwidth=0.3, relheight=0.039)
# Defining the execute button.
exec_btn = ttk.Button(show_frame, text="Execute", command=execute_theprogram, cursor='hand2')
exec_btn.place(x=400 ,y=1670, relwidth=0.3, relheight=0.039)
space = Label(show_frame, text="", font=("Arial Bold", 50))
space.grid(column=0, row=67, sticky='w')

# Defining the go to configuration page button.
config_page_btn = ttk.Button(show_frame, text="Settings", command=StartConfigurationWindow, cursor='hand2')
config_page_btn.place(x=790 ,y=1670, relwidth=0.3, relheight=0.039)


show_output()
# Calling the mainloop of the Tkinter window root.
root.mainloop()