"""
The Project Temp_Cleaner GUI by Insertx2k Dev.
A simple alternative to all Temp cleaning software available for Windows available under the GNU General Public License v2.0 or later

License for the Project Temp_Cleaner GUI.
   A simple program made to help you erase temporary files in your Windows-based PC.
   Copyright (C) 2021, 2022, 2023 - Insertx2k Dev (Mr.X)

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

See github.com/insertx2k/temp_cleaner_gui
For a much better github page, try visiting https://insertx2k.github.io/temp_cleaner_gui

The program Temp_Cleaner GUI was previously Temp_Cleaner and it was using a CUI instead of a GUI. 

**THIS FILE (AS IT IS) BELONGS TO THE TEMP_CLEANER GUI PROJECT AND SHALL BE ONLY USED IN ACCORDING TO THE TERMS OF THE PRODUCT**

"""

# defining the global variable that holds the font_size of the scrolledtext.ScrolledText widget
# named 'showLicense'
font_size = 14

# print greetings text.
print()
print("Greetings from the Temp_Cleaner GUI Project.")
print("By Ziad Ahmed aka. Insertx2k Dev (Mr.X)")
print("Github : https://github.com/insertx2k/temp_cleaner_gui")
print("Twitter : https://twitter.com/insertplayztw")
print()
print("Powered by Minimal Accessibility Pack v1.0 by Insertx2k Dev (Mr.X)")
print()
# end of print greetings text.


# Imports
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
from PIL import Image, ImageTk
import configparser
from tkinter import filedialog
from tkinter import scrolledtext
import subprocess
from subprocess import PIPE
import awesometkinter as atk
import sys
import threading
from translations import *
from customtkinter import *
import webbrowser
import updater
import ctypes
import win32api
import donators

# initializing a variable containing the path where application files are stored.
application_path = ''

# attempting to get where the program files are stored
if getattr(sys, 'frozen', False): 
    # if program was frozen (compiled) using pyinstaller, the pyinstaller bootloader creates a sys attribute
    # frozen=True to indicate that the script file was compiled using pyinstaller, then it creates a
    # constant in sys that points to the directory where program executable is (where program files are).
    application_path = sys._MEIPASS
else: 
    # if program is not frozen (compiled) using pyinstaller and is running normally like a Python 3.x.x file.
    application_path = os.path.dirname(os.path.abspath(__file__))

# printing application path to console display
print(f"[DEBUG]: Temp_Cleaner GUI is installed in: {application_path}")


# Defining the function that will get the current values of an configparser values.
GetConfig = configparser.ConfigParser()
GetConfig.read(f'{application_path}\\Config.ini')

# checking if autocheck for updates is enabled or not, because if enabled will run the updater before running the main program.

# This is program's Main Window Class.
class MainWindowLightMode(CTk):
    def __init__(self):
        global GetConfig, font_size, application_path
        super().__init__() # initializing the self.
        print(f"""[DEBUG]: Current display properties (resolution) are:
* Display Width: {self.winfo_screenwidth()}
* Display height: {self.winfo_screenheight()}
""")


        # Trying to change the theme.
        try:
            # Changing the self's theme.
            self.style = ttk.Style()
            # self.style.theme_use("native")
        except Exception as excpt:
            print(f"[ERROR]: The following exception had occured while trying to apply the style \n {excpt}")

        try:
            set_default_color_theme(f"{application_path}\\style.json")
        except Exception as apply_style_file_error:
            messagebox.showerror("Runtime Error", f"An error has occured while we were trying to load the style file 'style.json'\n{apply_style_file_error}\n\nYou can try to make sure if the file 'style.json' is in the same directory as this program and try again\nThe program will close.")
            raise SystemExit(1225) # error code 1225 is for invalid style.json file
        

        # self.configure(background='white')

        try:
            self.login = os.getlogin()
            if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                WindowNewTitle = f"{en.prog_title_1}{self.login}{en.prog_title_2}"
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                WindowNewTitle = f"{ar.prog_title_2}{self.login}{ar.prog_title_1}"
            else:
                WindowNewTitle = f"{en.prog_title_1}{self.login}{en.prog_title_2}"
            self.title(WindowNewTitle)
        except Exception as excpt129:
            self.title(getCurrentLanguage().prog_title_no_username)

        # configuring program's main window geometry (DO NOT MODIFY)
        self.geometry('1225x600')

        # attempting to change the iconbitmap attribute of the window.
        try:
            self.iconbitmap(f"{application_path}\\icon0.ico")
        except Exception as excpt12: # better high level exception handling.
            messagebox.showerror("ERROR 1 in ICONBITMAP", f"Unable to load icon file for this window due to exception:\n{excpt12}")
            pass

        # basically preventing you from resizing it smaller than it's geometry.
        self.minsize(1225,600)

        if str(GetConfig['ProgConfig']['appearancemode']) == '1': # light mode
            # making a full screen scrollable frame.
            self.main_frame = Frame(self)
            self.main_frame.pack(fill=BOTH, expand=1)
            # Create a canvas.
            self.main_canvas = Canvas(self.main_frame)
            self.main_canvas.pack(side=LEFT, fill=BOTH, expand=1)
            # Add a scrollbar to the canvas
            self.main_scrollbar = atk.SimpleScrollbar(self.main_frame, orient=VERTICAL, command=self.main_canvas.yview, bg=atk.DEFAULT_COLOR, slider_color='grey', width=12)
            self.main_scrollbar.pack(side=RIGHT, fill=Y)
            # Configure the canvas.
            self.main_canvas.configure(yscrollcommand=self.main_scrollbar.set)
            self.main_canvas.bind('<Configure>', lambda e: self.main_canvas.configure(scrollregion = self.main_canvas.bbox("all")))
            # Create another frame INSIDE the canvas.
            self.show_frame = Frame(self.main_canvas)
            # Add that New frame to a window in the canvas.
            self.main_canvas.create_window((0,0), window=self.show_frame, anchor="nw")
            self.banner = PhotoImage(file=f"{application_path}\\banner.png")
            self.banner_show = Label(self.show_frame, image=self.banner, width=1200, height=300)
            self.banner_show.grid(column=0, row=2, sticky='w')
            set_appearance_mode("light")
        elif str(GetConfig['ProgConfig']['appearancemode']) == '2': # dark mode.
            # making a full screen scrollable frame.
            self.main_frame = Frame(self, background=atk.DEFAULT_COLOR)
            self.main_frame.pack(fill=BOTH, expand=1)
            # Create a canvas.
            self.main_canvas = Canvas(self.main_frame, background=atk.DEFAULT_COLOR)
            self.main_canvas.pack(side=LEFT, fill=BOTH, expand=1)
            # Add a scrollbar to the canvas
            self.main_scrollbar = atk.SimpleScrollbar(self.main_frame, orient=VERTICAL, command=self.main_canvas.yview, bg=atk.DEFAULT_COLOR, slider_color='grey', width=12)
            self.main_scrollbar.pack(side=RIGHT, fill=Y)
            # Configure the canvas.
            self.main_canvas.configure(yscrollcommand=self.main_scrollbar.set)
            self.main_canvas.bind('<Configure>', lambda e: self.main_canvas.configure(scrollregion = self.main_canvas.bbox("all")))
            # Create another frame INSIDE the canvas.
            self.show_frame = Frame(self.main_canvas, background=atk.DEFAULT_COLOR)
            # Add that New frame to a window in the canvas.
            self.main_canvas.create_window((0,0), window=self.show_frame, anchor="nw")
            self.banner = PhotoImage(file=f"{application_path}\\banner.png")
            self.banner_show = Label(self.show_frame, image=self.banner, width=1200, height=300, background=atk.DEFAULT_COLOR)
            self.banner_show.grid(column=0, row=2, sticky='w')
            self.style.configure('TLabelframe.Label', background=atk.DEFAULT_COLOR, foreground='white')
            self.style.configure('Label', background=atk.DEFAULT_COLOR)
            self.style.configure('Label', foreground='white')
            self.style.configure('TLabelframe', background=atk.DEFAULT_COLOR, foreground='white')
            self.style.configure('TCheckbutton', background=atk.DEFAULT_COLOR, foreground='white')
            self.style.configure('label', foreground='white')
            # self.style.configure('Vertical.TScrollbar', background=atk.DEFAULT_COLOR, foreground=atk.DEFAULT_COLOR)
            self.configure(background=atk.DEFAULT_COLOR)
            set_appearance_mode("dark")
        else: 
            messagebox.showerror("Unsupported appearance mode in Config file", f"Unsupported appearance mode in config file: {str(GetConfig['ProgConfig']['appearancemode'])}.\nThe program will continue with the Light mode instead.")
            # making a full screen scrollable frame.
            self.main_frame = Frame(self)
            self.main_frame.pack(fill=BOTH, expand=1)
            # Create a canvas.
            self.main_canvas = Canvas(self.main_frame)
            self.main_canvas.pack(side=LEFT, fill=BOTH, expand=1)
            # Add a scrollbar to the canvas
            self.main_scrollbar = atk.SimpleScrollbar(self.main_frame, orient=VERTICAL, command=self.main_canvas.yview, bg=atk.DEFAULT_COLOR, slider_color='grey', width=12)
            self.main_scrollbar.pack(side=RIGHT, fill=Y)
            # Configure the canvas.
            self.main_canvas.configure(yscrollcommand=self.main_scrollbar.set)
            self.main_canvas.bind('<Configure>', lambda e: self.main_canvas.configure(scrollregion = self.main_canvas.bbox("all")))
            # Create another frame INSIDE the canvas.
            self.show_frame = Frame(self.main_canvas)
            # Add that New frame to a window in the canvas.
            self.main_canvas.create_window((0,0), window=self.show_frame, anchor="nw")
            self.banner = PhotoImage(file=f"{application_path}\\banner.png")
            self.banner_show = Label(self.show_frame, image=self.banner, width=1200, height=300)
            self.banner_show.grid(column=0, row=2, sticky='w')
            set_appearance_mode("light")

        # # defining an informative frame on top of other widgets
        # self.InformationFrame = CTkFrame(self.show_frame, width=1200, height=60, corner_radius=15, fg_color='green')
        # self.InformationFrame.grid(column=0, row=1, sticky='w')
        # self.InformationFrame.grid_propagate(0) # fix to ensure the frame remains at the specified width and height even after placing
        # # widgets into it.
        def isRecycleBinEnabledInDrive(driveLetter):
            """
            A function for checking whether if a recycle bin folder exists in the specified drive(s) or no.

            Parameters: driveLetter -> str
            
            Return values: False if not found, True if found, None if there was an error found.
            """
            # declaring an array for available recycle bin names.
            recyclebin_folder_names = ["$Recycle.bin", "$RECYCLE.BIN", "$recycle.bin"]
            # checking if $Recycle.bin folder exists.
            try:
                folders = os.listdir(driveLetter)
            except Exception as exception_details:
                return None
            # print(folders)
            for folder_name_recyclebin in recyclebin_folder_names:
                if folder_name_recyclebin in folders:
                    print(f"Recycle bin folder {folder_name_recyclebin} found in drive : {driveLetter}")
                    # returning True as the loop has found the recycle bin folder in the specified drive(s)
                    return True
                else:
                    pass
            # returning False as the loop has completed without finding any appropriate recycle bin folder in the specified drive(s)
            return False

        def execute_theprogram():
            """
            The function for cleaning the computer using the "Start Cleaning" button
            """
            self.ShowNotificationDone = True

            self.exec_btn.configure(text=getCurrentLanguage().executing_text)
            self.exec_btn.configure(command=empty_function)
            self.exec_btn.configure(state='disabled')
            # show_output() # Calling the show output method so you can actually see what's happening inside.
            self.output_show.configure(state='disabled')
            
            try:
                # getting the systemdrive letter.
                system_drive = str(os.getenv("SYSTEMDRIVE"))
                # making sure to log the disk space before the cleaning up process and after the cleaning up process.
                total_before, used_before, free_before = shutil.disk_usage(system_drive)
            except Exception as exception_fetching_freeds_bexec:
                messagebox.showerror("An ERROR has occured", f"An exception has occured while Temp_Cleaner GUI was trying to fetch the current available disk space, This can happen if the program doesn't have the administrative privileges or so on\nConsider trying to do any of the following:\n1-Restart Temp_Cleaner GUI\n2-Right click on Temp_Cleaner GUI's Icon and click on Run as Administrator and try again\n3-Create a Github issue on https://github.com/insertx2k/temp_cleaner_gui with a screenshot of this messagebox and more details you think that will be useful in solving this issue.\nMore details available below:\n{exception_fetching_freeds_bexec}")
                

            self.selection = self.var0.get()
            if self.selection == '1':
                # implement other drives recycle bin cleaning feature.
                # getting a list of all drives and their pathes.
                try:
                    drives = win32api.GetLogicalDriveStrings()
                    drives = drives.split('\000')[:-1]
                except Exception as exceptionFindingAvailableDrives:
                    self.output_show.configure(state='normal')
                    self.output_show.insert(END, f"An error has occured while trying to access the drives in this PC\nError details are:\n{exceptionFindingAvailableDrives}\n\nIf you see this error message as a user of Temp_Cleaner GUI please make sure to report it as an issue in Temp_Cleaner GUI's github repository (https://github.com/insertx2k/temp_cleaner_gui) or create a support ticket in our sourceforge project page.")
                    self.output_show.configure(state='disabled')
                # assuming you have a list of all available drives in this pc, let's continue.
                try:
                    if drives:
                        for drive in drives:
                            if isRecycleBinEnabledInDrive(drive) == True:
                                self.output_show.configure(state='normal')
                                self.output_show.insert(END, f"\n{getCurrentLanguage().recyclebin_of} {drive}")
                                self.output_show.configure(state='disabled')
                                self.process = subprocess.getoutput(f'rmdir /s /q "{drive}$Recycle.bin"')
                                self.output_show.configure(state='normal')
                                self.output_show.insert(END, f"\n {self.process}")
                                self.output_show.configure(state='disabled')
                            elif isRecycleBinEnabledInDrive(drive) == None:
                                self.output_show.configure(state='normal')
                                self.output_show.insert(END, f"\n{getCurrentLanguage().no_recyclebin_enabled}{drive}")
                                self.output_show.configure(state='disabled')
                                pass
                except NameError:
                    self.output_show.configure(state='normal')
                    self.output_show.insert(END, f"\n{getCurrentLanguage().couldnt_get_other_drives_will_clean_windrv}\n")
                    self.output_show.configure(state='disabled')
                    self.process = subprocess.getoutput('rmdir /s /q "%systemdrive%\\$Recycle.bin"')
                    self.output_show.configure(state='normal')
                    self.output_show.insert(END, f"\n {self.process}")
                    self.output_show.configure(state='disabled')
            self.selection1 = self.var1.get()
            if self.selection1 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%windir%\\prefetch"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().prefw_text}:\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection2 = self.var2.get()
            if self.selection2 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\D3DSCache"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().dxdcache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection3 = self.var3.get()
            if self.selection3 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%windir%\\Temp"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().windir_temp_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection4 = self.var4.get()
            if self.selection4 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Temp"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().user_temp_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection5 = self.var5.get()
            if self.selection5 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Google\\Chrome\\User Data\\Default\\GPUCache"&erase /s /f /q "%localappdata%\\Google\\Chrome\\User Data\\Default\\Cache"&erase /s /f /q "%localappdata%\\Google\\Chrome\\User Data\\Default\\Code Cache"&del /F /S /Q "%localappdata%\\Google\\Chrome\\User Data\\Default\\History"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().gchrome_webcache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
                try:
                    # getting localappdata value in a variable
                    localappdata = str(os.getenv('localappdata'))
                    # multi profile chrome cleaning
                    listdirs = os.listdir(f"{localappdata}\\Google\\Chrome\\User Data")
                except:
                    self.output_show.insert(END, f"\n{getCurrentLanguage().error_in_cleaning}\n")
                for dir in listdirs:
                    if "Profile" in dir:
                        if dir == "Guest Profile":
                            self.process = subprocess.getoutput(f'erase /s /f /q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\GPUCache"&erase /s /f /q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\Cache"&erase /s /f /q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\Code Cache"&del /F /S /Q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\History"')
                            self.output_show.configure(state='normal')
                            self.output_show.insert(END, f"\n {self.process}")
                            self.output_show.configure(state='disabled')
                        elif dir == "System Profile": # DON'T CLEAN SYSTEM PROFILE
                            pass
                        else:
                            self.process = subprocess.getoutput(f'erase /s /f /q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\GPUCache"&erase /s /f /q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\Cache"&erase /s /f /q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\Code Cache"&del /F /S /Q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\History"')
                            self.output_show.configure(state='normal')
                            self.output_show.insert(END, f"\n {self.process}")
                            self.output_show.configure(state='disabled')
            self.selection6 = self.var6.get()
            if self.selection6 == '1':
                self.process = subprocess.getoutput('del /s /q "%localappdata%\\Google\\Chrome\\User Data\\Default\\Cookies"&del /s /q "%localappdata%\\Google\\Chrome\\User Data\\Default\\Cookies-journal"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().gchrome_cookies_text}\n {self.process}")
                self.output_show.configure(state='disabled')
                try:
                    # getting localappdata value in a variable
                    localappdata = str(os.getenv('localappdata'))
                    # multi profile chrome cleaning
                    listdirs = os.listdir(f"{localappdata}\\Google\\Chrome\\User Data")
                except:
                    self.output_show.insert(END, f"\n{getCurrentLanguage().error_in_cleaning}\n")
                for dir in listdirs:
                    if "Profile" in dir:
                        if dir == "Guest Profile":
                            self.process = subprocess.getoutput(f'del /s /q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\Cookies"&del /s /q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\Cookies-journal"')
                            self.output_show.configure(state='normal')
                            self.output_show.insert(END, f"\n {self.process}")
                            self.output_show.configure(state='disabled')
                        elif dir == "System Profile": # DON'T CLEAN SYSTEM PROFILE
                            pass
                        else:
                            self.process = subprocess.getoutput(f'del /s /q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\Cookies"&del /s /q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\Cookies-journal"')
                            self.output_show.configure(state='normal')
                            self.output_show.insert(END, f"\n {self.process}")
                            self.output_show.configure(state='disabled')
            self.selection9 = self.var7.get()
            if self.selection9 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%systemdrive%\\Users\\Default\\AppData\\Local\\Temp"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().defuser_temp_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection10 = self.var8.get()
            if self.selection10 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Microsoft\\Windows\\INetCache"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().iecache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection11 = self.var9.get()
            if self.selection11 == '1':
                self.process = subprocess.getoutput('@echo off | clip')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().clipboard_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection12 = self.var10.get()
            if self.selection12 == '1':
                self.process = subprocess.getoutput(' cd /d %localappdata%&cd microsoft&cd windows&cd explorer&del /s /q *thumbcache*&cd /d %localappdata%\microsoft\windows\explorer&del /s /q *thumb*')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().winexp_thumbcache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection13 = self.var11.get()
            if self.selection13 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%userprofile%\\AppData\\Roaming\\Microsoft\\Windows\\Recent"&del /F /S /Q "%localappdata%\\Microsoft\\Windows\\History"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().user_recents_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection14 = self.var12.get()
            if self.selection14 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%userprofile%\\AppData\\Roaming\\discord\\Cache"&erase /s /f /q "%userprofile%\\AppData\\Roaming\\discord\\Code Cache"&erase /s /f /q "%userprofile%\\AppData\\Roaming\\discord\\GPUCache"&erase /s /f /q "%userprofile%\\AppData\\Roaming\\discord\\Local Storage"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().discord_webcache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection15 = self.var13.get()
            if self.selection15 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%userprofile%\\AppData\\Roaming\\GIMP\\2.10\\tmp"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().gimp_tmp_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection16 = self.var14.get()
            if self.selection16 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Steam\\htmlcache\\Cache"&erase /s /f /q "%localappdata%\\Steam\\htmlcache\\Code Cache"&erase /s /f /q "%localappdata%\\Steam\\htmlcache\\GPUCache"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().steam_htmlcache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection17 = self.var15.get()
            if self.selection17 == '1':
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().winupdate_downloadedfiles_text}")
                self.output_show.insert(END, f"\n{getCurrentLanguage().attempting_to_take_folder_ownership}\n")
                self.process = subprocess.getoutput('takeown /F "%windir%\\SoftwareDistribution\\Download" /A /R /D Y&icacls "%windir%\\SoftwareDistribution\\Download" /grant *S-1-5-32-544:F /T /C /Q')
                self.output_show.configure(state='normal')
                # self.output_show.insert(END, f"\n{self.process}")
                self.output_show.configure(state='disabled')
                self.process = subprocess.getoutput('takeown /F "%windir%\\Installer" /A /R /D Y&icacls "%windir%\\Installer" /grant *S-1-5-32-544:F /T /C /Q')
                self.output_show.configure(state='normal')
                # self.output_show.insert(END, f"\n{self.process}")
                self.output_show.configure(state='disabled')
                self.process = subprocess.getoutput('del /f /s /q "%windir%\\SoftwareDistribution\\Download"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n {self.process}")
                self.output_show.configure(state='disabled')
                self.process = subprocess.getoutput('del /f /s /q "%windir%\\Installer"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n {self.process}")
                self.output_show.configure(state='disabled')


                self.reboot_uwp = messagebox.askquestion(getCurrentLanguage().restart_winupdate_window_title_text, getCurrentLanguage().restart_winupdate_window_content_text)
                if self.reboot_uwp == "yes":
                    self.output_show.configure(state='normal')
                    self.output_show.insert(END, f"\n{getCurrentLanguage().restarting_winupdate_service_text}\n")
                    self.output_show.configure(state='disabled')
                    self.process = subprocess.getoutput('net start wuauserv')
                    self.output_show.configure(state='normal')
                    self.output_show.insert(END,f"\n{getCurrentLanguage().windows_update_rebooter_exit_code}\n{self.process}")
                    self.output_show.configure(state='disabled')
                    # messagebox.showinfo(getCurrentLanguage().restarting_winupdate_service_text, getCurrentLanguage().restart_winupdate_service_done_text) -> unnecessary, was really annoying.
                else:
                    # messagebox.showinfo(getCurrentLanguage().restart_winupdate_window_title_text, getCurrentLanguage().not_restarting_winupdate_service_warning_text)
                    # removed due to a suggestion, see: https://www.askwoody.com/forums/topic/temp_cleaner-gui-just-what-i-was-looking-for/
                    pass
            self.selection18 = self.var16.get()
            if self.selection18 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Microsoft\\Windows\\Caches"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().win10plus_oscache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection19 = self.var17.get()
            if self.selection19 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Microsoft\\Windows\\INetCookies"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().iecookies_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection20 = self.var18.get()
            if self.selection20 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Microsoft\\Windows\\IECompatCache"&erase /s /f /q "%localappdata%\\Microsoft\\Windows\\IECompatUaCache"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().adds_ietemp_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection21 = self.var19.get()
            if self.selection21 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Microsoft\\Windows\\IEDownloadHistory"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().iedownloadhistory_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection22 = self.var20.get()
            if self.selection22 == '1':
                self.process =  subprocess.getoutput('erase /s /f /q "%localappdata%\\Microsoft\\Windows\\ActionCenterCache"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().actioncenter_cache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection23 = self.var21.get()
            if self.selection23 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Microsoft\\Windows\\AppCache"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().modern_apps_cache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection24 = self.var22.get()
            if self.selection24 == '1':
                self.conf1 = messagebox.askquestion(getCurrentLanguage().clean_ms_store_based_edge_cache_window_title, getCurrentLanguage().clean_ms_store_based_edge_cache_dialog_one_content)
                if self.conf1 == "yes":
                    messagebox.showinfo(getCurrentLanguage().clean_ms_store_based_edge_cache_window_title, getCurrentLanguage().clean_ms_store_based_edge_cache_dialog_two_content)
                    self.process = subprocess.getoutput(' explorer.exe "%localappdata%\\Packages\\"')
                    self.output_show.configure(state='normal')
                    self.output_show.insert(END, f"\n{getCurrentLanguage().msedge_msstore_webcache_text}\n {self.process}")
                    self.output_show.configure(state='disabled')
                    messagebox.showinfo(getCurrentLanguage().clean_ms_store_based_edge_cache_window_title, getCurrentLanguage().done_text)
                else:
                    messagebox.showinfo(getCurrentLanguage().clean_ms_store_based_edge_cache_window_title, getCurrentLanguage().operation_interrupted_by_user)
            self.selection25 = self.var23.get()
            if self.selection25 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Microsoft\\Windows\\Explorer\\ThumbCacheToDelete"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().thumbcachetodelete_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection26 = self.var24.get()
            if self.selection26 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Microsoft\\Edge\\User Data\\Default\\GPUCache"&erase /s /f /q "%localappdata%\\Microsoft\\Edge\\User Data\\Default\\Cache"&erase /s /f /q "%localappdata%\\Microsoft\\Edge\\User Data\\Default\\Code Cache"&del /F /S /Q "%localappdata%\\Microsoft\\Edge\\User Data\\Default\\History"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().chromium_based_edge_webcache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
                try:
                    # getting localappdata env var
                    localappdata = str(os.getenv('localappdata'))
                    # multiprofile edge cleaning
                    listdirs = os.listdir(f"{localappdata}\\Microsoft\\Edge\\User Data")
                except:
                    self.output_show.insert(END, f"\n{getCurrentLanguage().error_in_cleaning}\n")
                for dir in listdirs:
                    if "Profile" in dir:
                        if dir == "Guest Profile":
                            self.process = subprocess.getoutput(f'erase /s /f /q "%localappdata%\\Microsoft\\Edge\\User Data\\{dir}\\GPUCache"&erase /s /f /q "%localappdata%\\Microsoft\\Edge\\User Data\\{dir}\\Cache"&erase /s /f /q "%localappdata%\\Microsoft\\Edge\\User Data\\{dir}\\Code Cache"&del /F /S /Q "%localappdata%\\Microsoft\\Edge\\User Data\\{dir}\\History"')
                            self.output_show.configure(state='normal')
                            self.output_show.insert(END, f"\n {self.process}")
                            self.output_show.configure(state='disabled')
                        elif dir == "System Profile":
                            pass
                        else:
                            self.process = subprocess.getoutput(f'erase /s /f /q "%localappdata%\\Microsoft\\Edge\\User Data\\{dir}\\GPUCache"&erase /s /f /q "%localappdata%\\Microsoft\\Edge\\User Data\\{dir}\\Cache"&erase /s /f /q "%localappdata%\\Microsoft\\Edge\\User Data\\{dir}\\Code Cache"&del /F /S /Q "%localappdata%\\Microsoft\\Edge\\User Data\\{dir}\\History"')
                            self.output_show.configure(state='normal')
                            self.output_show.insert(END, f"\n {self.process}")
                            self.output_show.configure(state='disabled')
            self.selection27 = self.var25.get()
            if self.selection27 == '1':
                self.process = subprocess.getoutput('del /s /q "%localappdata%\\Microsoft\\Edge\\User Data\\Default\\Cookies"&del /s /q "%localappdata%\\Microsoft\\Edge\\User Data\\Default\\Cookies-journal"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().chromium_based_edge_cookies_text}\n {self.process}")
                self.output_show.configure(state='disabled')
                try:
                    # getting localappdata env var
                    localappdata = str(os.getenv('localappdata'))
                    # multiprofile edge cleaning
                    listdirs = os.listdir(f"{localappdata}\\Microsoft\\Edge\\User Data")
                except:
                    self.output_show.insert(END, f"\n{getCurrentLanguage().error_in_cleaning}\n")
                for dir in listdirs:
                    if "Profile" in dir:
                        if dir == "Guest Profile":
                            self.process = subprocess.getoutput(f'del /s /q "%localappdata%\\Microsoft\\Edge\\User Data\\{dir}\\Cookies"&del /s /q "%localappdata%\\Microsoft\\Edge\\User Data\\{dir}\\Cookies-journal"')
                            self.output_show.configure(state='normal')
                            self.output_show.insert(END, f"\n {self.process}")
                            self.output_show.configure(state='disabled')
                        elif dir == "System Profile":
                            pass
                        else:
                            self.process = subprocess.getoutput(f'del /s /q "%localappdata%\\Microsoft\\Edge\\User Data\\{dir}\\Cookies"&del /s /q "%localappdata%\\Microsoft\\Edge\\User Data\\{dir}\\Cookies-journal"')
                            self.output_show.configure(state='normal')
                            self.output_show.insert(END, f"\n {self.process}")
                            self.output_show.configure(state='disabled')
            self.selection28 = self.var26.get()
            if self.selection28 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Roblox\\Downloads"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().roblox_textures_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection29 = self.var27.get()
            if self.selection29 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%appdata%\\Adobe\\Adobe Photoshop 2020\\Adobe Photoshop 2020 Settings\\web-cache-temp\\GPUCache"&erase /s /f /q "%appdata%\\Adobe\\Adobe Photoshop 2020\\Adobe Photoshop 2020 Settings\\web-cache-temp\\Code Cache"&del /s /f /q "%appdata%\\Adobe\\Adobe Photoshop 2020\\Adobe Photoshop 2020 Settings\\web-cache-temp\\Visited Links"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().ps2020_webcache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection30 = self.var28.get()
            if self.selection30 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\VEGAS Pro\\17.0"&erase /s /f /q "File Explorer Thumbnails"&erase /s /f /q "Device Explorer Thumbnails"&del /s /f /q "*.autosave.veg.bak"&del /s /f /q "svfx_Ofx*.log"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().vegaspro17_temp_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection31 = self.var29.get()
            if self.selection31 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\McNeel\\Rhinoceros\\temp"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().mcneel_rhinoceros_3d_temp_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection32 = self.var30.get()
            if self.selection32 == '1':
                self.process = subprocess.getoutput('erase /s /f /q /A:S "%userprofile%\\AppData\\LocalLow\\Microsoft\\CryptnetUrlCache"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().cryptneturl_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection33 = self.var31.get()
            if self.selection33 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\pip\\cache"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().pypip_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection34 = self.var32.get()
            if self.selection34 == '1':
                self.conf2 = messagebox.askquestion(getCurrentLanguage().erase_rammap_title, getCurrentLanguage().erase_rammap_content)
                if self.conf2 == "yes":
                    self.RAMMAPpath_var = GetConfig['ProgConfig']['RAMMapPath']
                    if self.RAMMAPpath_var == '$DEFAULT':
                        messagebox.showinfo(getCurrentLanguage().default_path_msgbox_title, getCurrentLanguage().default_path_rammap)
                        self.process = subprocess.getoutput(r'"%systemdrive%\RAMMap\RAMMap.exe" -Ew')
                        self.output_show.configure(state='normal')
                        self.output_show.insert(END, f"\n{getCurrentLanguage().empty_running_workingsets_rammap_text}\n {self.process}")
                        self.output_show.configure(state='disabled')
                        messagebox.showinfo(getCurrentLanguage().erase_rammap_title, getCurrentLanguage().commandsent_to_rammap_text)
                    else:
                        self.process = subprocess.getoutput(rf'""{self.RAMMAPpath_var}"\RAMMap.exe" -Ew')
                        self.output_show.configure(state='normal')
                        self.output_show.insert(END, f"\n{getCurrentLanguage().empty_running_workingsets_rammap_text}\n {self.process}")
                        self.output_show.configure(state='disabled')
                        messagebox.showinfo(getCurrentLanguage().erase_rammap_title, getCurrentLanguage().commandsent_to_rammap_text)
                else:
                    messagebox.showinfo(getCurrentLanguage().erase_rammap_title, getCurrentLanguage().operation_interrupted_by_user)
            self.selection35 = self.var33.get()
            if self.selection35 == '1':
                self.process = subprocess.getoutput('del /s /q "%localappdata%\\Google\\Chrome\\User Data\\Default\\Extension Cookies"&del /s /q "%localappdata%\\Google\\Chrome\\User Data\\Default\\Extension Cookies-journal"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().gchrome_extensions_cookies_text}\n {self.process}")
                self.output_show.configure(state='disabled')
                try:
                    # getting localappdata value in a variable
                    localappdata = str(os.getenv('localappdata'))
                except:
                    self.output_show.insert(END, f"\n{getCurrentLanguage().error_in_cleaning}\n")
                # multi profile chrome cleaning
                try:
                    listdirs = os.listdir(f"{localappdata}\\Google\\Chrome\\User Data")
                except:
                    self.output_show.insert(END, f"\n{getCurrentLanguage().error_in_cleaning}\n")
                for dir in listdirs:
                    if "Profile" in dir:
                        if dir == "Guest Profile":
                            self.process = subprocess.getoutput(f'del /s /q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\Extension Cookies"&del /s /q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\Extension Cookies-journal"')
                            self.output_show.configure(state='normal')
                            self.output_show.insert(END, f"\n {self.process}")
                            self.output_show.configure(state='disabled')
                        elif dir == "System Profile": # DON'T CLEAN SYSTEM PROFILE
                            pass
                        else:
                            self.process = subprocess.getoutput(f'del /s /q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\Extension Cookies"&del /s /q "%localappdata%\\Google\\Chrome\\User Data\\{dir}\\Extension Cookies-journal"')
                            self.output_show.configure(state='normal')
                            self.output_show.insert(END, f"\n {self.process}")
                            self.output_show.configure(state='disabled')
            self.selection36 = self.var34.get()
            if self.selection36 == '1':
                self.CDPCCPATH_var = GetConfig['ProgConfig']['CDPCCPATH']
                if self.CDPCCPATH_var == '$DEFAULT':
                    messagebox.showinfo(getCurrentLanguage().default_path_msgbox_title, getCurrentLanguage().default_path_winactivities_cache_text)
                    self.process = subprocess.getoutput(' cd /d "%localappdata%\\ConnectedDevicesPlatform"&erase /s /f /q *')
                    self.output_show.configure(state='normal')
                    self.output_show.insert(END, f"\n{getCurrentLanguage().connecteddevicesplatform_cache_text}\n {self.process}")
                    self.output_show.configure(state='disabled')
                else:
                    self.process = subprocess.getoutput(rf' cd /d "%localappdata%\\ConnectedDevicesPlatform"&erase /s /f /q "{self.CDPCCPATH_var}"')
                    self.output_show.configure(state='normal')
                    self.output_show.insert(END, f"\n{getCurrentLanguage().connecteddevicesplatform_cache_text}\n {self.process}")
                    self.output_show.configure(state='disabled')
            # self.selection37 = self.var35.get()
            # if self.selection37 == '1':
            #     self.conf3 = messagebox.askquestion(getCurrentLanguage().clear_icon_cache_dialog_text, getCurrentLanguage().iconcache_dialog_text)
            #     if self.conf3 == "yes":
            #         self.process = subprocess.getoutput('%windir%\\explorer.exe "%localappdata%"')
            #         self.output_show.configure(state='normal')
            #         self.output_show.insert(END, f"\n {self.process}")
            #         self.output_show.configure(state='disabled')
            #         messagebox.showinfo(getCurrentLanguage().clear_icon_cache_dialog_text, getCurrentLanguage().done_text)
            #     else:
            #         pass
            self.selection38 = self.var36.get()
            if self.selection38 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Microvirt"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().microvert_memu_logs_memdump_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection39 = self.var37.get()
            if self.selection39 == '1':
                self.ADWCLRPATH_var = GetConfig['ProgConfig']['ADWCLRPath']
                if self.ADWCLRPATH_var == '$DEFAULT':
                    messagebox.showinfo(getCurrentLanguage().default_path_msgbox_title, getCurrentLanguage().nocustom_path_foradwcleaner_text)
                    self.process = subprocess.getoutput(' erase /s /f /q "%systemdrive%\\AdwCleaner\\Logs"')
                    self.output_show.configure(state='normal')
                    self.output_show.insert(END, f"\n{getCurrentLanguage().malwarebytes_adware_cleaner_text}\n {self.process}")
                    self.output_show.configure(state='disabled')
                else:
                    self.process = subprocess.getoutput(rf' erase /s /f /q "{self.ADWCLRPATH_var}\Logs"')
                    self.output_show.configure(state='normal')
                    self.output_show.insert(END, f"\n{getCurrentLanguage().malwarebytes_adware_cleaner_text}\n {self.process}")
                    self.output_show.configure(state='disabled')
            self.selection40 = self.var38.get()
            if self.selection40 == '1':
                self.process = subprocess.getoutput(' %systemdrive%&cd /d \\.\\&erase /s /f /q "PerfLogs"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().perflogs_sysdrive_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection41 = self.var39.get()
            if self.selection41 == '1':
                self.process = subprocess.getoutput('rmdir /s /q "%userprofile%\\.cache"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().android_cached_data_text} \n{self.process}")
                self.output_show.configure(state='disabled')
                self.process = subprocess.getoutput('rmdir /S /Q "%userprofile%\\.android"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{self.process}")
                self.output_show.configure(state='disabled')
            self.selection42 = self.var40.get()
            if self.selection42 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\SquirrelTemp"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().discord_squirrel_temp}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection43 = self.var41.get()
            if self.selection43 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%userprofile%\\AppData\\LocalLow\\Temp"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().local_low_temp_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection44 = self.var42.get()
            if self.selection44 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\ElevatedDiagnostics"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().elevateddiagnostics_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection45 = self.var43.get()
            if self.selection45 == '1':
                self.process = subprocess.getoutput('cd /d "%localappdata%\\VMware"&erase /s /f /q "vmware-download*"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().vmware_downloads}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection46 = self.var44.get()
            if self.selection46 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%userprofile%\\appdata\\roaming\\balena-etcher\\blob_storage"&erase /s /f /q "%userprofile%\\appdata\\roaming\\balena-etcher\\Code Cache"&erase /s /f /q "%userprofile%\\appdata\\roaming\\balena-etcher\\GPUCache"&erase /s /f /q "%userprofile%\\appdata\\roaming\\balena-etcher\\Local Storage"&erase /s /f /q "%userprofile%\\appdata\\roaming\\balena-etcher\\Session Storage"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().balenaitcher_webcache_files_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection47 = self.var45.get()
            if self.selection47 == '1':
                self.process = subprocess.getoutput(' cd /d "%appdata%"&erase /s /f /q "%userprofile%\\AppData\\Roaming\\pyinstaller"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().pyinstaller_bin_cache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection48 = self.var46.get()
            if self.selection48 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Jedi"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().jedi_python_cache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection49 = self.var47.get()
            if self.selection49 == '1':
                self.process = subprocess.getoutput('del /s /q "%localappdata%\\recently-used.xbel"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().gimp_recent_docs_list_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            # self.selection50 = self.var48.get()
            # if self.selection50 == '1':
            #     self.process = subprocess.getoutput('cd /d "%localappdata%"&del /s /q "llftool.*.agreement"')
            #     self.output_show.insert(END, f"\n {self.process}")
            self.selection51 = self.var49.get()
            if self.selection51 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\IdentityNexusIntegration"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().identitynexusintegration_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection52 = self.var50.get()
            if self.selection52 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Axolot Games\\Scrap Mechanic\\Temp\\WorkshopIcons"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().axolot_games_scrapmechanic_workshop_cache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection53 = self.var51.get()
            if self.selection53 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\Roblox\\logs"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().roblox_verbosed_logs_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection54 = self.var52.get()
            if self.selection54 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%userprofile%\\AppData\\Roaming\\Code\\GPUCache"&erase /s /f /q "%userprofile%\\AppData\\Roaming\\Code\\Code Cache"&erase /s /f /q "%userprofile%\\AppData\\Roaming\\Code\\CachedData"&erase /s /f /q "%userprofile%\\AppData\\Roaming\\Code\\Cache"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().vscode_webcache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection55 = self.var53.get()
            if self.selection55 == '1':
                self.process = subprocess.getoutput('del /s /q "%userprofile%\\AppData\\Roaming\\Code\\Cookies"&del /s /q "%userprofile%\\AppData\\Roaming\\Code\\Cookies-journal"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().vscode_cookies_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection56 = self.var54.get()
            if self.selection56 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%userprofile%\\AppData\\Roaming\\Code\\CachedExtensions"&erase /s /f /q "%userprofile%\\AppData\\Roaming\\Code\\CachedExtensionVSIXs"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().vscode_cached_extensions_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection57 = self.var55.get()
            if self.selection57 == '1':
                self.WINXPEPATH_var = GetConfig['ProgConfig']['WINXPEPATH']
                if self.WINXPEPATH_var == "$NONE":
                    messagebox.showinfo(getCurrentLanguage().an_error_has_occured_text, getCurrentLanguage().no_path_winxpe_text)
                else:
                    self.process = subprocess.getoutput(rf' erase /s /f /q "{self.WINXPEPATH_var}\Temp"')
                    self.output_show.configure(state='normal')
                    self.output_show.insert(END, f"\n{getCurrentLanguage().winxpe_creator_downloadsdir_text}\n {self.process}")
                    self.output_show.configure(state='disabled')
                    messagebox.showinfo(getCurrentLanguage().note_text, getCurrentLanguage().winxpe_after_clean_note_text)
                    
            self.selection58 = self.var56.get()
            if self.selection58 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\ServiceHub"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().servicehub_identity_file_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection59 = self.var57.get()
            if self.selection59 == '1':
                self.process = subprocess.getoutput(' erase /s /f /q "%localappdata%\\HiSuite\\log"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().huawei_hisuite_logdata_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection60 = self.var58.get()
            if self.selection60 == '1':
                self.process = subprocess.getoutput(' erase /s /f /q "%userprofile%\\AppData\\Roaming\\.minecraft\\webcache"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().minecraft_webcache_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection61 = self.var59.get()
            if self.selection61 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\Mozilla\\Firefox\\Profiles"&cd *.default-release&erase /s /f /q "cache2"&erase /s /f /q "jumpListCache"&cd /d "%userprofile%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"&cd *.default-release&erase /s /f /q "shader-cache"&del /F /S /Q "places.sqlite"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().firefox_webcached_data_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection62 = self.var60.get()
            if self.selection62 == '1':
                self.process = subprocess.getoutput(' cd /d "%userprofile%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"&cd *.default-release&del /s /q "cookies.sqlite"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().mozilla_firefox_cookie_data_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection63 = self.var61.get()
            if self.selection63 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\VEGAS\\ErrorReport"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().vegaspro17_errorlogs_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection64 = self.var62.get()
            if self.selection64 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%userprofile%\\AppData\\LocalLow\\Sun\\Java\\Deployment\\tmp"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().javadeployment_chkbox_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection65 = self.var63.get()
            if self.selection65 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%localappdata%\\HiSuite\\userdata\\DropTemp"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().huawei_hisuite_dnddata_text}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection67 = self.var65.get()
            if self.selection67 == '1':
                self.process = subprocess.getoutput('erase /s /f /q "%systemdrive%\\ProgramData\\Microsoft\\Windows\\WER\\ReportQueue"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().wer_cleaner}\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection68 = self.var66.get()
            if self.selection68 == '1': # delivery optimization cleaning
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().delivery_optimization}\n{getCurrentLanguage().attempting_to_take_folder_ownership}\n")
                self.output_show.configure(state='disabled')
                self.process = subprocess.getoutput('takeown /F "%windir%\\ServiceProfiles\\NetworkService\\AppData\\Local\\Microsoft\\Windows\\DeliveryOptimization\\Cache" /A /R /D Y&icacls "%windir%\\ServiceProfiles\\NetworkService\\AppData\\Local\\Microsoft\\Windows\\DeliveryOptimization\\Cache" /grant *S-1-5-32-544:F /T /C /Q')
                self.output_show.configure(state='normal')
                self.output_show.configure(state='disabled')
                self.process = subprocess.getoutput('erase /s /f /q "%windir%\\ServiceProfiles\\NetworkService\\AppData\\Local\\Microsoft\\Windows\\DeliveryOptimization\\Cache"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n {self.process}")
                self.output_show.configure(state='disabled')
                # self.process = subprocess.getoutput('erase /s /f /q "%windir%\\DeliveryOptimization"')
                # self.output_show.insert(END, f"\n {self.process}")
            self.selection69 = self.var67.get()
            if self.selection69 == '1':
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().windows_log_files}\n{getCurrentLanguage().attempting_to_take_folder_ownership}\n")
                self.process = subprocess.getoutput('takeown /F "%windir%\Logs" /A /R /D Y&icacls "%windir%\Logs" /grant *S-1-5-32-544:F /T /C /Q')
                # self.output_show.insert(END, f"\n{self.process}\n")
                self.output_show.configure(state='disabled')
                self.process = subprocess.getoutput('erase /s /f /q "%windir%\\Logs"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n {self.process}")
                self.output_show.configure(state='disabled')
            self.selection70 = self.var68.get()
            if self.selection70 == "1":
                self.process = subprocess.getoutput('del /F /S /Q "%windir%\Offline Web Pages"')
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().offline_web_pages}:\n{self.process}")
                self.output_show.configure(state='disabled')
            self.selection71 = self.var69.get()
            if self.selection71 == "1":
                messagebox.showinfo(getCurrentLanguage().default_path_msgbox_title, getCurrentLanguage().winsxs_warning)
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().winsxs}\n{getCurrentLanguage().cleaner_will_take_lot_of_time}\n")
                self.output_show.configure(state='disabled')
                os.system("Dism.exe /online /Cleanup-Image /StartComponentCleanup /ResetBase")
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().cleaner_has_finished}")
                self.output_show.configure(state='disabled')
            self.selection72 = self.var70.get()
            if self.selection72 == "1":
                messagebox.showinfo(getCurrentLanguage().default_path_msgbox_title, getCurrentLanguage().winsp_cleaner_warning)
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().winsp_cleaner}\n{getCurrentLanguage().cleaner_will_take_lot_of_time}\n")
                self.output_show.configure(state='disabled')
                os.system("Dism.exe /online /Cleanup-Image /SPSuperseded")
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().cleaner_has_finished}")
                self.output_show.configure(state='disabled')
            self.selection73 = self.var71.get()
            if self.selection73 == "1":
                messagebox.showinfo(getCurrentLanguage().default_path_msgbox_title, getCurrentLanguage().winold_warning)
                self.output_show.configure(state='normal')
                self.output_show.insert(END, f"\n{getCurrentLanguage().winold}\n{getCurrentLanguage().cleaner_will_take_lot_of_time}\n")
                self.output_show.configure(state='disabled')
                # declaring a list to store the names of Windows.old folders in.
                winold_names = []
                try:
                    systemdrive = os.getenv("systemdrive")
                    listdirs = os.listdir(systemdrive)
                    for dir in listdirs:
                        if "Windows.old" in dir:
                            winold_names.append(dir)
                        elif "windows.old" in dir:
                            winold_names.append(dir)
                        elif "Windows.Old" in dir:
                            winold_names.append(dir)
                        else:
                            pass
                    for winolddir in winold_names:
                        self.process = subprocess.getoutput(f'takeown /F "%systemdrive%\\{winolddir}" /A /R /D Y&icacls "%systemdrive%\\{winolddir}" /grant *S-1-5-32-544:F /T /C /Q')
                        self.output_show.configure(state='normal')
                        self.output_show.insert(END, f"\n{self.process}")
                        self.output_show.configure(state='disabled')
                        self.process = subprocess.getoutput(f'rmdir /S /Q "%SystemDrive%\\{winolddir}"')
                        self.output_show.configure(state='normal')
                        self.output_show.insert(END, f"\n{self.process}")
                        self.output_show.configure(state='disabled')
                except:
                    self.output_show.configure(state='normal')
                    self.output_show.insert(END, f"\n{getCurrentLanguage().error_in_cleaning}\n")
                    self.output_show.configure(state='disabled')

                
            
            
            self.selection66 = self.var64.get()

            self.output_show.configure(state='normal')
            self.output_show.insert(END, f"\n\n\n{getCurrentLanguage().finish_cleaning}\n\n\n")
            self.output_show.configure(state='disabled')

            if self.selection66 == '1':
                self.destroy()
                raise SystemExit(0) # quitting program.
            # Sleeping a bit for longer (or equal) to 5 seconds.
            # time.sleep(1)
            try:
                # now logging after everything is done.
                total_after, used_after, free_after = shutil.disk_usage(system_drive)
                freed_up = (free_before - free_after)
                if convert_to_str_with_units(freed_up) == "0 bytes":
                    messagebox.showinfo(getCurrentLanguage().freed_up_diskspace_dialog_title, getCurrentLanguage().freed_up_nothing)
                else:
                    messagebox.showinfo(getCurrentLanguage().freed_up_diskspace_dialog_title, f"{getCurrentLanguage().freed_up_diskspace_dialog}{convert_to_str_with_units(freed_up)}")
            except Exception as exception_reading_free_diskspace:
                messagebox.showerror("An ERROR has occured", f"An exception has occured while Temp_Cleaner GUI was trying to fetch the current available disk space, This can happen if the program doesn't have the administrative privileges or so on\nConsider trying to do any of the following:\n1-Restart Temp_Cleaner GUI\n2-Right click on Temp_Cleaner GUI's Icon and click on Run as Administrator and try again\n3-Create a Github issue on https://github.com/insertx2k/temp_cleaner_gui with a screenshot of this messagebox and more details you think that will be useful in solving this issue.\nMore details available below:\n{exception_reading_free_diskspace}")

            

            try:
                # Ok, let's revert everything back to what it was before.
                self.exec_btn.configure(text=getCurrentLanguage().execute_text)
                self.exec_btn.configure(command=multiprocessing_execute_btn_function)
                self.exec_btn.configure(state='normal')
            except TclError as tkerr:
                messagebox.showerror("An ERROR has occured", f"An ERROR has occured during the program's mainloop\nHere are some technical details if you want to reach us\n{tkerr}\nThe program can't continue and will close after you press OK")
                raise SystemExit(15) # error code 15 is for an urgent mainloop exception.


            return None


        def multiprocessing_execute_btn_function():
            threading.Thread(target=execute_theprogram).start()
            pass
        
        
        def empty_function():
            "a function used to fix the issue when temp cleaner gui does not stop the executing button even when cleaning."
            pass
        
        def uncheck_all_options():
            """
            A function to uncheck all available cleaning options in the Home Screen UI.
            """
            try:
                self.var0.set(0)
                self.var1.set(0)
                self.var2.set(0)
                self.var3.set(0)
                self.var4.set(0)
                self.var5.set(0)
                self.var6.set(0)
                self.var7.set(0)
                self.var8.set(0)
                self.var9.set(0)
                self.var10.set(0)
                self.var11.set(0)
                self.var12.set(0)
                self.var13.set(0)
                self.var14.set(0)
                self.var15.set(0)
                self.var16.set(0)
                self.var17.set(0)
                self.var18.set(0)
                self.var19.set(0)
                self.var20.set(0)
                self.var21.set(0)
                self.var22.set(0)
                self.var23.set(0)
                self.var24.set(0)
                self.var25.set(0)
                self.var26.set(0)
                self.var27.set(0)
                self.var28.set(0)
                self.var29.set(0)
                self.var30.set(0)
                self.var31.set(0)
                self.var32.set(0)
                self.var33.set(0)
                self.var34.set(0)
                # self.var35.set(0)
                self.var36.set(0)
                self.var37.set(0)
                self.var38.set(0)
                self.var39.set(0)
                self.var40.set(0)
                self.var41.set(0)
                self.var42.set(0)
                self.var43.set(0)
                self.var44.set(0)
                self.var45.set(0)
                self.var46.set(0)
                self.var47.set(0)
                # self.var48.set(0)
                self.var49.set(0)
                self.var50.set(0)
                self.var51.set(0)
                self.var52.set(0)
                self.var53.set(0)
                self.var54.set(0)
                self.var55.set(0)
                self.var56.set(0)
                self.var57.set(0)
                self.var58.set(0)
                self.var59.set(0)
                self.var60.set(0)
                self.var61.set(0)
                self.var62.set(0)
                self.var63.set(0)
                self.var64.set(0)
                self.var65.set(0)
                self.var66.set(0)
                self.var67.set(0)
                self.var68.set(0)
                self.var69.set(0)
                self.var70.set(0)
                self.var71.set(0)
            except Exception as unable_to_uncheck_all_exception:
                print(f"[ERROR]: Unable to execute the function uncheck_all_options() due to this exception\n{unable_to_uncheck_all_exception}")
                return False
            return True

        def getCurrentLanguage(currentLanguageStr=GetConfig['ProgConfig']['languagesetting']):
            """
            Gets the current language from the config file 'Config.ini'

            Should return `en` class if the current language is set to en, and so on.
            """
            try:
                if str(currentLanguageStr) == "en":
                    return en
                elif str(currentLanguageStr) == "ar":
                    return ar
                else:
                    return en
            except Exception as exception_reading_config_file:
                messagebox.showerror("An ERROR has occured",f"Couldn't read from 'Config.ini'\nException details:\n{exception_reading_config_file}\nPress OK to close this program")
                raise SystemExit(169) # Exit code 169 is for unreadable config file or untreatable getCurrentLanguage exceptions.
                # This is needed to make sure the program doesn't act weirdly.
        
        def apply_cleaning_preset(user_choice):
            print(f"[DEBUG]: Chosen cleaning preset is: {str(self.preset_chooser.get())}")
            if str(self.preset_chooser.get()) == getCurrentLanguage().preset_default :
                try:
                    uncheck_all_options()
                    self.var0.set(1)
                    self.var2.set(1)
                    self.var9.set(1)
                    self.var3.set(1)
                    self.var4.set(1)
                    self.var8.set(1)
                    self.var23.set(1)
                except Exception as exception_applying_preset:
                    print(f"[ERROR]: Unable to apply cleaning preset due to exception: {exception_applying_preset}")
                    pass
            elif str(self.preset_chooser.get()) == getCurrentLanguage().preset_maximum_cleaning :
                try:
                    uncheck_all_options()
                    self.var0.set(1)
                    self.var1.set(1)
                    self.var2.set(1)
                    self.var3.set(1)
                    self.var4.set(1)
                    self.var5.set(1)
                    self.var6.set(1)
                    self.var7.set(1)
                    self.var8.set(1)
                    self.var9.set(1)
                    self.var10.set(1)
                    self.var11.set(1)
                    self.var12.set(1)
                    self.var13.set(1)
                    self.var14.set(1)
                    self.var15.set(1)
                    self.var16.set(1)
                    self.var17.set(1)
                    self.var18.set(1)
                    self.var19.set(1)
                    self.var20.set(1)
                    self.var21.set(1)
                    self.var22.set(1)
                    self.var23.set(1)
                    self.var24.set(1)
                    self.var25.set(1)
                    self.var26.set(1)
                    self.var27.set(1)
                    self.var28.set(1)
                    self.var29.set(1)
                    self.var30.set(1)
                    self.var31.set(1)
                    self.var32.set(1)
                    self.var33.set(1)
                    self.var34.set(1)
                    # self.var35.set(1)
                    self.var36.set(1)
                    self.var37.set(1)
                    self.var38.set(1)
                    self.var39.set(1)
                    self.var40.set(1)
                    self.var41.set(1)
                    self.var42.set(1)
                    self.var43.set(1)
                    self.var44.set(1)
                    self.var45.set(1)
                    self.var46.set(1)
                    self.var47.set(1)
                    # self.var48.set(1)
                    self.var49.set(1)
                    self.var50.set(1)
                    self.var51.set(1)
                    self.var52.set(1)
                    self.var53.set(1)
                    self.var54.set(1)
                    self.var55.set(1)
                    self.var56.set(1)
                    self.var57.set(1)
                    self.var58.set(1)
                    self.var59.set(1)
                    self.var60.set(1)
                    self.var61.set(1)
                    self.var62.set(1)
                    self.var63.set(1)
                    self.var65.set(1)
                    self.var66.set(1)
                    self.var67.set(1)
                    self.var68.set(1)
                    self.var69.set(1)
                    self.var70.set(1)
                    self.var71.set(1)
                except Exception as exception_applying_max_preset:
                    print(f"[ERROR]: couldn't apply max preset due to exception: {exception_applying_max_preset}")
                    pass
            elif str(self.preset_chooser.get()) == getCurrentLanguage().preset_recyclebin_cleaning :
                try:
                    uncheck_all_options()
                    self.var0.set(1)
                except Exception as exception_applying_recyclebin_cleaning_preset :
                    print(f"[ERROR]: couldn't apply recycle bin cleaning preset due to exception: {exception_applying_recyclebin_cleaning_preset}")
                    pass
            elif str(self.preset_chooser.get()) == getCurrentLanguage().preset_webbrowser_cleaning_with_cookies :
                try:
                    uncheck_all_options()
                    self.var5.set(1)
                    self.var6.set(1)
                    self.var33.set(1)
                    self.var24.set(1)
                    self.var25.set(1)
                    self.var59.set(1)
                    self.var60.set(1)
                    self.var17.set(1)
                    self.var18.set(1)
                    self.var19.set(1)
                    self.var8.set(1)
                except Exception as exception_applying_webbrowser_cookies_cleaning_preset:
                    print(f"[ERROR]: couldn't apply webbrowser with cookies cleaning preset due to exception: {exception_applying_webbrowser_cookies_cleaning_preset}")
                    pass
            elif str(self.preset_chooser.get()) == getCurrentLanguage().preset_webbrowser_cleaning :
                try:
                    uncheck_all_options()
                    self.var8.set(1)
                    self.var5.set(1)
                    self.var24.set(1)
                    self.var59.set(1)
                    self.var18.set(1)
                    self.var19.set(1)
                except Exception as exception_applying_webbrowser_cleaning_preset :
                    print(f"[ERROR]: couldn't apply webbrowser cleaning preset due to exception: {exception_applying_webbrowser_cleaning_preset}")
                    pass
            # elif str(self.preset_chooser.get()) == getCurrentLanguage().fix_roblox_error_preset :
            #     try:
            #         uncheck_all_options()
            #         self.var9.set(1)
            #         self.var3.set(1)
            #         self.var4.set(1)
            #         self.var41.set(1)
            #         self.var26.set(1)
            #     except Exception as exception_applying_rblxfix_preset :
            #         print(f"[ERROR]: couldn't apply rblxfix cleaning preset due to exception: {exception_applying_rblxfix_preset}")
            #         pass
            # removed as of v6.4-stable.
            elif str(self.preset_chooser.get()) == getCurrentLanguage().cancel_pending_updates :
                try:
                    uncheck_all_options()
                    # applying default preset
                    self.var0.set(1)
                    self.var2.set(1)
                    self.var9.set(1)
                    self.var3.set(1)
                    self.var4.set(1)
                    self.var8.set(1)
                    self.var23.set(1)
                    # alongwith windows update cleaning sections.
                    self.var15.set(1)
                    self.var66.set(1)
                except Exception as exception_applying_webbrowser_cleaning_preset :
                    print(f"[ERROR]: couldn't apply cancel pending updates cleaning preset due to exception: {exception_applying_webbrowser_cleaning_preset}")
                    pass
            else: # if none of these options are selected.
                pass 
            
            return None
        

        def startAboutWindow():
            """
            Opens the new About Window.
            """
            aboutWindowProcess = AboutWindow()
            aboutWindowProcess.mainloop()
            return None
        

        def close_main_screen():
            """
            A function to be executed when the user closes the window of the Home Screen UI.
            """
            print("[DEBUG]: User has sent the command WM_DESTROY_WINDOW, will safely terminate the process of this program.")
            self.destroy()
            raise SystemExit(0) # exiting python interpreter.
            return None


        # def getCurrentCustomCursorsMode(strCurrentCursorsMode=GetConfig["ProgConfig"]['customcursors']):
        #     """
        #     Gets the current status of Custom Cursors mode.

        #     Returns: 
            
        #     ```py
        #     tuple(cursor_for_main_widgets, 2, 3)
        #     ```
        #     """
        #     try:
        #         if str(strCurrentCursorsMode) == "True":
        #             return ('@cursor.cur', '@Hand.cur', '@TextSelect.cur')
        #         else:
        #             return ('arrow', "hand2", "arrow")
        #     except Exception as exception_getting_cursors_state:
        #         messagebox.showerror("An ERROR has occured", f"{exception_getting_cursors_state}")
        #         raise SystemExit(69430210)
        #     raise SystemExit(69430210) # error code 69430210 is for unable to read cursors mode.
        
        # attempts to change the current cursors mode according to the configuration in Config.ini
        # try:
        #     self.configure(cursor=getCurrentCustomCursorsMode()[0])
        # except Exception as exceptioncursor:
        #     print(f"{exceptioncursor}")
        #     messagebox.showerror("Unable to use custom Cursor", f"{exceptioncursor}")
        #     pass

        # Defining a sample get var functionaking a new checkbox.
        # Defining the ON-OFF Like variable
        self.var0 = StringVar()
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = StringVar()
        self.var6 = StringVar()
        self.var7 = StringVar()
        self.var8 = StringVar()
        self.var9 = StringVar()
        self.var10 = StringVar()
        self.var11 = StringVar()
        self.var12 = StringVar()
        self.var13 = StringVar()
        self.var14 = StringVar()
        self.var15 = StringVar()
        self.var16 = StringVar()
        self.var17 = StringVar()
        self.var18 = StringVar()
        self.var19 = StringVar()
        self.var20 = StringVar()
        self.var21 = StringVar()
        self.var22 = StringVar()
        self.var23 = StringVar()
        self.var24 = StringVar()
        self.var25 = StringVar()
        self.var26 = StringVar()
        self.var27 = StringVar()
        self.var28 = StringVar()
        self.var29 = StringVar()
        self.var30 = StringVar()
        self.var31 = StringVar()
        self.var32 = StringVar()
        self.var33 = StringVar()
        self.var34 = StringVar()
        # self.var35 = StringVar()
        self.var36 = StringVar()
        self.var37 = StringVar()
        self.var38 = StringVar()
        self.var39 = StringVar()
        self.var40 = StringVar()
        self.var41 = StringVar()
        self.var42 = StringVar()
        self.var43 = StringVar()
        self.var44 = StringVar()
        self.var45 = StringVar()
        self.var46 = StringVar()
        self.var47 = StringVar()
        # self.var48 = StringVar()
        self.var49 = StringVar()
        self.var50 = StringVar()
        self.var51 = StringVar()
        self.var52 = StringVar()
        self.var53 = StringVar()
        self.var54 = StringVar()
        self.var55 = StringVar()
        self.var56 = StringVar()
        self.var57 = StringVar()
        self.var58 = StringVar()
        self.var59 = StringVar()
        self.var60 = StringVar()
        self.var61 = StringVar()
        self.var62 = StringVar()
        self.var63 = StringVar()
        self.var64 = StringVar()
        self.var65 = StringVar() # for wer cleaner
        self.var66 = StringVar() # for delivery optimization cleaning
        self.var67 = StringVar() # for windows logs cleaning
        self.var68 = StringVar() # for offline pages cleaning
        self.var69 = StringVar() # for winsxs store cleanup
        self.var70 = StringVar() # for windows sp cleanup
        self.var71 = StringVar() # for windows old cleanup

        # ----------------------------
        # a fix for 1024x768 or lower screen resolutions:
        # ----------------------------
        if int(self.winfo_screenwidth()) <= 1024 and int(self.winfo_screenheight()) <= 768:
            font_size = 8
            self.minsize(800, 600)
            self.geometry('800x600')
        # ----------------------------
        
        # Defining the function used to show the user the about window of the program.
        def show_about_window():
            global GetConfig
            messagebox.showinfo(getCurrentLanguage().about_window_title,getCurrentLanguage().about_window_txt)
            return None
        
        def runUpdaterProgram():
            updater.updaterProgramUI()
            return None
        
        def checkForUpdatesAutomatically():
            """
            A function for automatic updates check upon startup of Temp_Cleaner GUI
            """
            try:
                if int(GetConfig["ProgConfig"]['autocheckforupdates']) == 1: # auto check for updates is enabled
                    if updater.downloadAndSaveVersionFile() == False: # downloading version file from server
                        print(f"[ERROR]: There is no internet connection, couldn't check for updates [DEBUG: VERFILE DOWNLOADER]")
                        return False 
                    else:
                        pass
                    if updater.downloadAndSaveReleaseNotesFile() == False: # downloading release notes file from server
                        print(f"[ERROR]: There is no internet connection, couldn't check for updates [DEBUG: RELEASENOTES DOWNLOADER]")
                        return False
                    else:
                        pass
                    # continue, downloaded version and release notes files from internet.
                    try:
                        isThereAnyUpdatesAvailable = updater.readVersion() # None if latest, True if not latest
                    except Exception as readingVersionFromDownloadedFileError:
                        messagebox.showerror("An error has occured", f"An error has occured causing Temp_Cleaner GUI to fail in the section of checking the latest version from Update server\nError details are:\nError type: fail to read from downloaded verinfo file\nMore details:\n{readingVersionFromDownloadedFileError}\nPlease report this error as soon as possible to Ziad (Mr.X) by creating an issue on Temp_Cleaner GUI's Github page: https://github.com/insertx2k/temp_cleaner_gui\nPress OK to continue")
                        return False
                    if isThereAnyUpdatesAvailable == True: # there is an update
                        # guiProcess = updater.updaterProgramUI()
                        # guiProcess.mainloop()
                        runUpdaterProgram()
                        # attempting to delete the unnecessary and old downloaded files from server to make sure they get updated.
                        pass
                    else: # there is no updates available
                        # there are no updates available, don't run gui program.
                        print("[INFO]: You are running the latest version of the program, no need to update it.")
                        # attempting to delete the unnecessary and old downloaded files from server to make sure they get updated.
                        try:
                            os.remove(f"{application_path}\\progver.txt")
                            os.remove(f"{application_path}\\releaseNotes.txt")
                        except Exception as exception_deleting_unneeded_downloads: # couldn't delete them.
                            messagebox.showerror("An error has occured", f"Couldn't delete the unnecessary files 'releaseNotes.txt' and 'progver.txt' due to a runtime error\nError details are:\n{exception_deleting_unneeded_downloads}\n\nIf you are a user and you see this message please create an issue on Temp_Cleaner GUI's official Github page and MAKE SURE to provide a screenshot of this messagebox\nPress OK to continue.")
                else: # auto check for updates is disabled
                    return None
            except Exception as readingFromConfigFileError:
                messagebox.showerror(f"{getCurrentLanguage().cant_read_config_frominside_file_msgbox_title}", f"{getCurrentLanguage().cant_read_config_frominside_file_msgbox_content}")
                return False


        

        

        # ------------------------------
        # getting widgets original direction according to the UI language
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en': # if UI lang is English.
            components_direction = en.widgets_sticking_direction
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar': # if UI lang is Arabic.
            components_direction = ar.widgets_sticking_direction
        else: # if UI lang is not specified.
            components_direction = en.widgets_sticking_direction
        # ------------------------------

        # placing widgets inside the information frame
        # ===============================================
        
        # self.infoframelbl0 = Label(self.InformationFrame, text=getCurrentLanguage().you_dont_need_anything, font=("Arial", 15), foreground='white', background='green')
        # self.infoframelbl0.grid(column=0, row=1, sticky=components_direction)
        # self.InformationFrame.pack_propagate(0) -> does not work.
        # ===============================================



        
        # defining the presets label frame.
        self.presets_lblframe = ttk.LabelFrame(self.show_frame, text=getCurrentLanguage().dontknow_whattodo_presets_text)
        
        
        self.preset_chooser = CTkComboBox(self.presets_lblframe, width=500, values=(getCurrentLanguage().preset_default, getCurrentLanguage().preset_maximum_cleaning, getCurrentLanguage().preset_recyclebin_cleaning, getCurrentLanguage().preset_webbrowser_cleaning, getCurrentLanguage().preset_webbrowser_cleaning_with_cookies, getCurrentLanguage().cancel_pending_updates), command=apply_cleaning_preset)
        self.preset_chooser.set('')
        # inserting values for the presets combobox.
        self.preset_chooser.grid(column=0, row=1, sticky=components_direction)

        self.presets_lblframe.grid(column=0, row=3, sticky=components_direction)
        self.preset_chooser.bind('<<ComboboxSelected>>', apply_cleaning_preset) # binding a function that gets called whenever the value of such a combobox is changed by the user.
        # ---------------------------
        


        # Defining the checkbox buttons
        # --------------------------
        self.lblframe0 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().recycle_bin_text)

        self.clr_recyclebin_sysdrive_btn = CTkCheckBox(self.lblframe0, text=getCurrentLanguage().windrv_recycle_bin_text, variable=self.var0, onvalue="1", offvalue="0", command=None)
        self.clr_recyclebin_sysdrive_btn.grid(column=0, row=1, sticky=components_direction)

        # ---------------------------
        self.lblframe0.grid(column=0, row=4, sticky=components_direction)

        self.lblframe1 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().dxdcache_text)
        # ---------------------------
        self.clr_d3dscache_localappdata_btn = CTkCheckBox(self.lblframe1, text=getCurrentLanguage().dxdcache_text_chkbox, variable=self.var2, onvalue="1", offvalue="0", command=None)
        self.clr_d3dscache_localappdata_btn.grid(column=0, row=1, sticky=components_direction)
        # ---------------------------
        self.lblframe1.grid(column=0, row=5, sticky=components_direction)

        self.lblframe2 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().sys_user_specific_text)
        # ---------------------------
        self.clr_prefetchw_windir_btn = CTkCheckBox(self.lblframe2, text=getCurrentLanguage().prefw_text, variable=self.var1, onvalue="1", offvalue="0", command=None)
        self.clr_prefetchw_windir_btn.grid(column=0, row=1, sticky=components_direction)

        self.clr_usrclipboard_content_btn = CTkCheckBox(self.lblframe2, text=getCurrentLanguage().clipboard_text, variable=self.var9, onvalue="1", offvalue="0", command=None)
        self.clr_usrclipboard_content_btn.grid(column=0, row=2, sticky=components_direction)

        self.clr_windir_temp_btn = CTkCheckBox(self.lblframe2, text=getCurrentLanguage().windir_temp_text, variable=self.var3, onvalue="1", offvalue="0", command=None)
        self.clr_windir_temp_btn.grid(column=0, row=3, sticky=components_direction)

        self.clr_localappdata_temp_btn = CTkCheckBox(self.lblframe2, text=getCurrentLanguage().user_temp_text, variable=self.var4, onvalue="1", offvalue="0", command=None)
        self.clr_localappdata_temp_btn.grid(column=0, row=4, sticky=components_direction)

        self.clr_default_usr_appdata_temp_btn = CTkCheckBox(self.lblframe2, text=getCurrentLanguage().defuser_temp_text, variable=self.var7, onvalue="1", offvalue="0", command=None)
        self.clr_default_usr_appdata_temp_btn.grid(column=0, row=5, sticky=components_direction)

        self.clr_inet_cached_data_btn = CTkCheckBox(self.lblframe2, text=getCurrentLanguage().iecache_text, variable=self.var8, onvalue="1", offvalue="0", command=None)
        self.clr_inet_cached_data_btn.grid(column=0, row=6, sticky=components_direction)

        self.clr_msexplorer_thumbcacheddata_btn = CTkCheckBox(self.lblframe2, text=getCurrentLanguage().winexp_thumbcache_text, variable=self.var10, onvalue="1", offvalue="0", command=None)
        self.clr_msexplorer_thumbcacheddata_btn.grid(column=0, row=7, sticky=components_direction)

        self.clr_winrecentdocs_list_btn = CTkCheckBox(self.lblframe2, text=getCurrentLanguage().user_recents_text, variable=self.var11, onvalue="1", offvalue="0", command=None)
        self.clr_winrecentdocs_list_btn.grid(column=0, row=8, sticky=components_direction)

        self.clr_locallow_temporary_data_btn = CTkCheckBox(self.lblframe2, text=getCurrentLanguage().local_low_temp_text, variable=self.var41, onvalue="1", offvalue="0", command=None)
        self.clr_locallow_temporary_data_btn.grid(column=0, row=9, sticky=components_direction)

        self.wercleanup = CTkCheckBox(self.lblframe2, text=getCurrentLanguage().wer_cleaner, variable=self.var65, onvalue="1", offvalue="0", command=None)
        self.wercleanup.grid(column=0, row=10, sticky=components_direction)

        self.windows_logs_cleanup = CTkCheckBox(self.lblframe2, text=getCurrentLanguage().windows_log_files, variable=self.var67, onvalue="1", offvalue="0", command=None)
        self.windows_logs_cleanup.grid(column=0, row=11, sticky=components_direction)

        self.offline_webpages_cleanup = CTkCheckBox(self.lblframe2, text=getCurrentLanguage().offline_web_pages, variable=self.var68, onvalue="1", offvalue="0", command=None)
        self.offline_webpages_cleanup.grid(column=0, row=12, sticky=components_direction)

        # ---------------------------
        self.lblframe2.grid(column=0, row=6, sticky=components_direction)

        self.lblframe3 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().webbrowsers_text)
        # ---------------------------
        self.clr_gchrome_webcache_incl_gpucache_codecache_btn = CTkCheckBox(self.lblframe3, text=getCurrentLanguage().gchrome_webcache_text, variable=self.var5, onvalue="1", offvalue="0", command=None)
        self.clr_gchrome_webcache_incl_gpucache_codecache_btn.grid(column=0, row=1, sticky=components_direction)

        self.clr_gchrome_browser_cookies_btn = CTkCheckBox(self.lblframe3, text=getCurrentLanguage().gchrome_cookies_text, variable=self.var6, onvalue="1", offvalue="0", command=None)
        self.clr_gchrome_browser_cookies_btn.grid(column=0, row=2, sticky=components_direction)

        self.clr_gchrome_extension_cookies_data_btn = CTkCheckBox(self.lblframe3, text=getCurrentLanguage().gchrome_extensions_cookies_text, variable=self.var33, onvalue="1", offvalue="0", command=None)
        self.clr_gchrome_extension_cookies_data_btn.grid(column=0, row=3, sticky=components_direction)

        self.clr_steam_webclient_htmlcache_btn = CTkCheckBox(self.lblframe3, text=getCurrentLanguage().steam_htmlcache_text, variable=self.var14, onvalue="1", offvalue="0", command=None)
        self.clr_steam_webclient_htmlcache_btn.grid(column=0, row=4, sticky=components_direction)

        self.clr_discordwebclient_webcacheddata_btn = CTkCheckBox(self.lblframe3, text=getCurrentLanguage().discord_webcache_text, variable=self.var12, onvalue="1", offvalue="0", command=None)
        self.clr_discordwebclient_webcacheddata_btn.grid(column=0, row=5, sticky=components_direction)

        self.clr_chromiumbased_msedge_webcached_data_btn = CTkCheckBox(self.lblframe3, text=getCurrentLanguage().chromium_based_edge_webcache_text, variable=self.var24, onvalue="1", offvalue="0", command=None)
        self.clr_chromiumbased_msedge_webcached_data_btn.grid(column=0, row=6, sticky=components_direction)

        self.clr_chormiumbased_msedge_cookies_data_btn = CTkCheckBox(self.lblframe3, text=getCurrentLanguage().chromium_based_edge_cookies_text, variable=self.var25, onvalue="1", offvalue="0", command=None)
        self.clr_chormiumbased_msedge_cookies_data_btn.grid(column=0, row=7, sticky=components_direction)

        self.clr_mozilla_firefox_webcached_data_btn = CTkCheckBox(self.lblframe3, text=getCurrentLanguage().firefox_webcached_data_text, variable=self.var59, onvalue="1", offvalue="0", command=None)
        self.clr_mozilla_firefox_webcached_data_btn.grid(column=0, row=8, sticky=components_direction)

        self.clr_mozilla_firefox_cookies_sqlite_file_btn = CTkCheckBox(self.lblframe3, text=getCurrentLanguage().mozilla_firefox_cookie_data_text, variable=self.var60, onvalue="1", offvalue="0", command=None)
        self.clr_mozilla_firefox_cookies_sqlite_file_btn.grid(column=0, row=9, sticky=components_direction)

        self.clr_discordapp_squirrel_temp_data_btn = CTkCheckBox(self.lblframe3, text=getCurrentLanguage().discord_squirrel_temp, variable=self.var40, onvalue="1", offvalue="0", command=None)
        self.clr_discordapp_squirrel_temp_data_btn.grid(column=0, row=10, sticky=components_direction)

        self.clr_inetcookies_btn = CTkCheckBox(self.lblframe3, text=getCurrentLanguage().iecookies_text, variable=self.var17, onvalue="1", offvalue="0", command=None)
        self.clr_inetcookies_btn.grid(column=0, row=11, sticky=components_direction)

        self.clr_additionalinet_cacheddata_btn = CTkCheckBox(self.lblframe3, text=getCurrentLanguage().adds_ietemp_text, variable=self.var18, onvalue="1", offvalue="0", command=None)
        self.clr_additionalinet_cacheddata_btn.grid(column=0, row=12, sticky=components_direction)

        self.clr_iedownload_history_data_btn = CTkCheckBox(self.lblframe3, text=getCurrentLanguage().iedownloadhistory_text, variable=self.var19, onvalue="1", offvalue="0", command=None)
        self.clr_iedownload_history_data_btn.grid(column=0, row=13, sticky=components_direction)

        # ---------------------------
        self.lblframe3.grid(column=0, row=7, sticky=components_direction)


        self.lblframe4 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().photo_editors_text)

        # ---------------------------
        self.clr_gimpstmps_btn = CTkCheckBox(self.lblframe4, text=getCurrentLanguage().gimp_tmp_text, variable=self.var13, onvalue="1", offvalue="0", command=None)
        self.clr_gimpstmps_btn.grid(column=0, row=1, sticky=components_direction)

        self.clr_gimp_recentdocs_btn = CTkCheckBox(self.lblframe4, text=getCurrentLanguage().gimp_recent_docs_list_text, variable=self.var47, onvalue="1", offvalue="0", command=None)
        self.clr_gimp_recentdocs_btn.grid(column=0, row=2, sticky=components_direction)
        
        self.clr_adobephotoshop_webcached_data_btn = CTkCheckBox(self.lblframe4, text=getCurrentLanguage().ps2020_webcache_text, variable=self.var27, onvalue="1", offvalue="0", command=None)
        self.clr_adobephotoshop_webcached_data_btn.grid(column=0, row=3, sticky=components_direction)
        # ---------------------------
        self.lblframe4.grid(column=0, row=8, sticky=components_direction)

        self.lblframe5 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().winupdate_text)
        # ---------------------------
        self.clr_windowsupdate_downloaded_updates_btn = CTkCheckBox(self.lblframe5, text=getCurrentLanguage().winupdate_downloadedfiles_text, variable=self.var15, onvalue="1", offvalue="0", command=None)
        self.clr_windowsupdate_downloaded_updates_btn.grid(column=0, row=1, sticky=components_direction)
        
        self.delivery_optimization_cleaning = CTkCheckBox(self.lblframe5, text=getCurrentLanguage().delivery_optimization, variable=self.var66, onvalue="1", offvalue="0", command=None)
        self.delivery_optimization_cleaning.grid(column=0, row=2, sticky=components_direction)
        # ---------------------------
        self.lblframe5.grid(column=0, row=9, sticky=components_direction)

        self.lblframe6 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().win10plus_cleaners_text)
        # ---------------------------
        self.clr_win10os_cached_data_btn = CTkCheckBox(self.lblframe6, text=getCurrentLanguage().win10plus_oscache_text, variable=self.var16, onvalue="1", offvalue="0", command=None)
        self.clr_win10os_cached_data_btn.grid(column=0, row=1, sticky=components_direction)

        self.clr_win10_action_center_cached_data_btn = CTkCheckBox(self.lblframe6, text=getCurrentLanguage().actioncenter_cache_text, variable=self.var20, onvalue="1", offvalue="0", command=None)
        self.clr_win10_action_center_cached_data_btn.grid(column=0, row=2, sticky=components_direction)

        self.clr_winappux_cached_data_btn = CTkCheckBox(self.lblframe6, text=getCurrentLanguage().modern_apps_cache_text, variable=self.var21, onvalue="1", offvalue="0", command=None)
        self.clr_winappux_cached_data_btn.grid(column=0, row=3, sticky=components_direction)

        self.clr_msstore_based_edge_webcached_data_btn = CTkCheckBox(self.lblframe6, text=getCurrentLanguage().msedge_msstore_webcache_text, variable=self.var22, onvalue="1", offvalue="0", command=None)
        self.clr_msstore_based_edge_webcached_data_btn.grid(column=0, row=4, sticky=components_direction)

        self.clr_winexplorer_thumbcache_to_delete_files_btn = CTkCheckBox(self.lblframe6, text=getCurrentLanguage().thumbcachetodelete_text, variable=self.var23, onvalue="1", offvalue="0", command=None)
        self.clr_winexplorer_thumbcache_to_delete_files_btn.grid(column=0, row=5, sticky=components_direction)

        self.clr_cryptnet_urlcache_data_btn = CTkCheckBox(self.lblframe6, text=getCurrentLanguage().cryptneturl_text, variable=self.var30, onvalue="1", offvalue="0", command=None)
        self.clr_cryptnet_urlcache_data_btn.grid(column=0, row=6, sticky=components_direction)

        self.clr_connecteddevicesplatform_win10_cached_data_btn = CTkCheckBox(self.lblframe6, text=getCurrentLanguage().connecteddevicesplatform_cache_text, variable=self.var34, onvalue="1", offvalue="0", command=None)
        self.clr_connecteddevicesplatform_win10_cached_data_btn.grid(column=0, row=7, sticky=components_direction)

        self.clr_elevated_diagnostics_data_btn = CTkCheckBox(self.lblframe6, text=getCurrentLanguage().elevateddiagnostics_text, variable=self.var42, onvalue="1", offvalue="0", command=None)
        self.clr_elevated_diagnostics_data_btn.grid(column=0, row=8, sticky=components_direction)

        self.clr_identitynexus_integration_folder_btn = CTkCheckBox(self.lblframe6, text=getCurrentLanguage().identitynexusintegration_text, variable=self.var49, onvalue="1", offvalue="0", command=None)
        self.clr_identitynexus_integration_folder_btn.grid(column=0, row=9, sticky=components_direction)

        self.clr_servicehub_identity_file_btn = CTkCheckBox(self.lblframe6, text=getCurrentLanguage().servicehub_identity_file_text, variable=self.var56, onvalue="1", offvalue="0", command=None)
        self.clr_servicehub_identity_file_btn.grid(column=0, row=10, sticky=components_direction)
        # ---------------------------
        self.lblframe6.grid(column=0, row=10, sticky=components_direction)

        self.lblframe7 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().games_text)
        # ---------------------------
        self.clr_roblox_game_downloads_btn = CTkCheckBox(self.lblframe7, text=getCurrentLanguage().roblox_textures_text, variable=self.var26, onvalue="1", offvalue="0", command=None)
        self.clr_roblox_game_downloads_btn.grid(column=0, row=1, sticky=components_direction)

        self.clr_roblox_game_log_files_btn = CTkCheckBox(self.lblframe7, text=getCurrentLanguage().roblox_verbosed_logs_text, variable=self.var51, onvalue="1", offvalue="0", command=None)
        self.clr_roblox_game_log_files_btn.grid(column=0, row=2, sticky=components_direction)

        self.clr_scrapmechanic_axolot_games_workshop_items_cached_data_btn = CTkCheckBox(self.lblframe7, text=getCurrentLanguage().axolot_games_scrapmechanic_workshop_cache_text, variable=self.var50, onvalue="1", offvalue="0", command=None)
        self.clr_scrapmechanic_axolot_games_workshop_items_cached_data_btn.grid(column=0, row=3, sticky=components_direction)

        self.clr_minecraft_webcached_data_btn = CTkCheckBox(self.lblframe7, text=getCurrentLanguage().minecraft_webcache_text, variable=self.var58, onvalue="1", offvalue="0", command=None)
        self.clr_minecraft_webcached_data_btn.grid(column=0, row=4, sticky=components_direction)
        # ---------------------------
        self.lblframe7.grid(column=0, row=11, sticky=components_direction)


        self.lblframe8 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().python_cleaners_text)
        # ---------------------------
        self.clr_python_pip_cached_data_btn = CTkCheckBox(self.lblframe8, text=getCurrentLanguage().pypip_text, variable=self.var31, onvalue="1", offvalue="0", command=None)
        self.clr_python_pip_cached_data_btn.grid(column=0, row=1, sticky=components_direction)

        self.clr_pyinstaller_temporary_data_btn = CTkCheckBox(self.lblframe8, text=getCurrentLanguage().pyinstaller_bin_cache_text, variable=self.var45, onvalue="1", offvalue="0", command=None)
        self.clr_pyinstaller_temporary_data_btn.grid(column=0, row=2, sticky=components_direction)

        self.clr_jedipython_additionals_btn = CTkCheckBox(self.lblframe8, text=getCurrentLanguage().jedi_python_cache_text, variable=self.var46, onvalue="1", offvalue="0", command=None)
        self.clr_jedipython_additionals_btn.grid(column=0, row=3, sticky=components_direction)
        # ---------------------------
        self.lblframe8.grid(column=0, row=12, sticky=components_direction)


        self.lblframe9 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().ram_text)
        # ---------------------------
        self.empty_winworkingsets_rammap_btn = CTkCheckBox(self.lblframe9, text=getCurrentLanguage().empty_running_workingsets_rammap_text, variable=self.var32, onvalue="1", offvalue="0", command=None)
        self.empty_winworkingsets_rammap_btn.grid(column=0, row=1, sticky=components_direction)
        # ---------------------------
        self.lblframe9.grid(column=0, row=13, sticky=components_direction)

        self.lblframe10 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().video_editing_software_text)
        # ---------------------------
        self.clr_sony_vegas_pro_temp_and_logs_data_btn = CTkCheckBox(self.lblframe10, text=getCurrentLanguage().vegaspro17_temp_text, variable=self.var28, onvalue="1", offvalue="0", command=None)
        self.clr_sony_vegas_pro_temp_and_logs_data_btn.grid(column=0, row=1, sticky=components_direction)

        self.clr_sony_vegas_pro_error_reports_data_btn = CTkCheckBox(self.lblframe10, text=getCurrentLanguage().vegaspro17_errorlogs_text, variable=self.var61, onvalue="1", offvalue="0", command=None)
        self.clr_sony_vegas_pro_error_reports_data_btn.grid(column=0, row=2, sticky=components_direction)
        # ---------------------------
        self.lblframe10.grid(column=0, row=14, sticky=components_direction)


        self.lblframe11 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().threed_moduling_software_text)
        # ---------------------------
        self.clr_mcneel_rhinoceros_3d_moduling_soft_cached_data_btn = CTkCheckBox(self.lblframe11, text=getCurrentLanguage().mcneel_rhinoceros_3d_temp_text, variable=self.var29, onvalue="1", offvalue="0", command=None)
        self.clr_mcneel_rhinoceros_3d_moduling_soft_cached_data_btn.grid(column=0, row=1, sticky=components_direction)
        # ---------------------------
        self.lblframe11.grid(column=0, row=15, sticky=components_direction)

        self.lblframe17 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().special_cleaners)
        # ---------------------------
        self.wincomponent_store_cleanup_btn = CTkCheckBox(self.lblframe17, text=getCurrentLanguage().winsxs, variable=self.var69, onvalue="1", offvalue="0", command=None)
        self.wincomponent_store_cleanup_btn.grid(column=0, row=1, sticky=components_direction)

        self.winsp_cleanup_btn = CTkCheckBox(self.lblframe17, text=getCurrentLanguage().winsp_cleaner, variable=self.var70, onvalue="1", offvalue="0", command=None)
        self.winsp_cleanup_btn.grid(column=0, row=2, sticky=components_direction)

        self.winold_cleanup_btn = CTkCheckBox(self.lblframe17, text=getCurrentLanguage().winold, variable=self.var71, onvalue="1", offvalue="0", command=None)
        self.winold_cleanup_btn.grid(column=0, row=3, sticky=components_direction)
        # ---------------------------
        self.lblframe17.grid(column=0, row=16, sticky=components_direction)


        self.lblframe12 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().adds_software_text)
        # ---------------------------
        # self.clr_iconcache_db_file_in_localappdata_dir_btn = CTkCheckBox(self.lblframe12, text=getCurrentLanguage().iconcachefile_text, variable=self.var35, onvalue="1", offvalue="0", command=None, state='disabled')
        # self.clr_iconcache_db_file_in_localappdata_dir_btn.grid(column=0, row=1, sticky=components_direction)

        self.clr_microvirt_memu_log_data_memdump_files_btn = CTkCheckBox(self.lblframe12, text=getCurrentLanguage().microvert_memu_logs_memdump_text, variable=self.var36, onvalue="1", offvalue="0", command=None)
        self.clr_microvirt_memu_log_data_memdump_files_btn.grid(column=0, row=2, sticky=components_direction)

        self.clr_adwcleaner_log_files_btn = CTkCheckBox(self.lblframe12, text=getCurrentLanguage().malwarebytes_adware_cleaner_text, variable=self.var37, onvalue="1", offvalue="0", command=None)
        self.clr_adwcleaner_log_files_btn.grid(column=0, row=3, sticky=components_direction)

        self.clr_perflogs_in_systemdrive_btn = CTkCheckBox(self.lblframe12, text=getCurrentLanguage().perflogs_sysdrive_text, variable=self.var38, onvalue="1", offvalue="0", command=None)
        self.clr_perflogs_in_systemdrive_btn.grid(column=0, row=4, sticky=components_direction)

        self.clr_dotcache_folder_in_userprofile_path_btn = CTkCheckBox(self.lblframe12, text=getCurrentLanguage().android_cached_data_text, variable=self.var39, onvalue="1", offvalue="0", command=None)
        self.clr_dotcache_folder_in_userprofile_path_btn.grid(column=0, row=5, sticky=components_direction)

        self.clr_vmware_downloads_folder_btn = CTkCheckBox(self.lblframe12, text=getCurrentLanguage().vmware_downloads, variable=self.var43, onvalue="1", offvalue="0", command=None)
        self.clr_vmware_downloads_folder_btn.grid(column=0, row=6, sticky=components_direction)

        self.clr_balena_itcher_webcached_data_btn = CTkCheckBox(self.lblframe12, text=getCurrentLanguage().balenaitcher_webcache_files_text, variable=self.var44, onvalue="1", offvalue="0", command=None)
        self.clr_balena_itcher_webcached_data_btn.grid(column=0, row=7, sticky=components_direction)

        # self.clr_lowlevelformattool_licenseagreement_confirmationfile_btn = CTkCheckBox(self.lblframe12, text=getCurrentLanguage().lowlevelformattool_agreement_file_text, variable=self.var48, onvalue="1", offvalue="0", command=None)
        # self.clr_lowlevelformattool_licenseagreement_confirmationfile_btn.grid(column=0, row=8, sticky=components_direction)

        self.clr_winxpe_app_downloads_folder_btn = CTkCheckBox(self.lblframe12, text=getCurrentLanguage().winxpe_creator_downloadsdir_text, variable=self.var55, onvalue="1", offvalue="0", command=None)
        self.clr_winxpe_app_downloads_folder_btn.grid(column=0, row=9, sticky=components_direction)

        self.clr_huawei_hisuite_log_data_btn = CTkCheckBox(self.lblframe12, text=getCurrentLanguage().huawei_hisuite_logdata_text, variable=self.var57, onvalue="1", offvalue="0", command=None)
        self.clr_huawei_hisuite_log_data_btn.grid(column=0, row=10, sticky=components_direction)

        self.clr_huawei_hisuite_dnd_temp_btn = CTkCheckBox(self.lblframe12, text=getCurrentLanguage().huawei_hisuite_dnddata_text, variable=self.var63, onvalue="1", offvalue="0", command=None)
        self.clr_huawei_hisuite_dnd_temp_btn.grid(column=0, row=11, sticky=components_direction)

        
        # ---------------------------
        self.lblframe12.grid(column=0, row=17, sticky=components_direction)


        self.lblframe13 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().vscode_text)
        # ---------------------------
        self.clr_vscode_webcached_data_btn = CTkCheckBox(self.lblframe13, text=getCurrentLanguage().vscode_webcache_text, variable=self.var52, onvalue="1", offvalue="0", command=None)
        self.clr_vscode_webcached_data_btn.grid(column=0, row=1, sticky=components_direction)

        self.clr_vscode_cookie_data_btn = CTkCheckBox(self.lblframe13, text=getCurrentLanguage().vscode_cookies_text, variable=self.var53, onvalue="1", offvalue="0", command=None)
        self.clr_vscode_cookie_data_btn.grid(column=0, row=2, sticky=components_direction)

        self.clr_vscode_cached_extensions_data_btn = CTkCheckBox(self.lblframe13, text=getCurrentLanguage().vscode_cached_extensions_text, variable=self.var54, onvalue="1", offvalue="0", command=None)
        self.clr_vscode_cached_extensions_data_btn.grid(column=0, row=3, sticky=components_direction)
        # ---------------------------
        self.lblframe13.grid(column=0, row=18, sticky=components_direction)


        self.lblframe14 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().javadeployment_text)
        # ---------------------------
        self.clr_java_deployment_cached_data_btn = CTkCheckBox(self.lblframe14, text=getCurrentLanguage().javadeployment_chkbox_text, variable=self.var62, onvalue="1", offvalue="0", command=None)
        self.clr_java_deployment_cached_data_btn.grid(column=0, row=1, sticky=components_direction)
        # ---------------------------
        self.lblframe14.grid(column=0, row=19, sticky=components_direction)

        self.lblframe15 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().alldone_text)
        # ---------------------------
        self.destroy_activity_after_done_btn = CTkCheckBox(self.lblframe15, text=getCurrentLanguage().alldone_chkbox_text, variable=self.var64, onvalue="1", offvalue="0", command=None, cursor='hand2')
        self.destroy_activity_after_done_btn.grid(column=0, row=1, sticky=components_direction)
        # ---------------------------
        self.lblframe15.grid(column=0, row=20, sticky=components_direction)

        # declaring a container frame to place main buttons in.
        self.mainButtonsContainerFrame = CTkFrame(self.show_frame, bg_color="transparent", fg_color="transparent")
        self.mainButtonsContainerFrame.grid(column=0, row=83, sticky='w', pady=20)
        # changing background color of the container frame to something more useful.
        # if str(GetConfig["ProgConfig"]['appearancemode']) == "1": # light mode
        #     pass
        # elif str(GetConfig["ProgConfig"]['appearancemode']) == "2": # dark mode
        #     self.mainButtonsContainerFrame.configure(bg_color=atk.DEFAULT_COLOR)
        # else:
        #     pass
        # placing main buttons into the main buttons container frame.
        # Defining the about button.
        self.about_window_btn = CTkButton(self.mainButtonsContainerFrame, text=getCurrentLanguage().about_text, command=startAboutWindow)
        self.about_window_btn.grid(column=0, row=1, sticky='w', ipadx=120, ipady=40)

        # Defining the execute button.
        self.exec_btn = CTkButton(self.mainButtonsContainerFrame, text=getCurrentLanguage().execute_text, command=multiprocessing_execute_btn_function)
        self.exec_btn.grid(column=1, row=1, ipadx=120, ipady=40, padx=10)

        # declaring a space.
        # self.space = Label(self.show_frame, text="", font=("Arial Bold", 50))
        # if str(GetConfig['ProgConfig']['appearancemode']) == '2':
        #     self.space.configure(background=atk.DEFAULT_COLOR)
        # self.space.grid(column=0, row=83, sticky=components_direction)
        
        # Defining the go to configuration page button.
        self.config_page_btn = CTkButton(self.mainButtonsContainerFrame, text=getCurrentLanguage().settings_text, command=self.StartConfigurationWindow)
        self.config_page_btn.grid(column=2, row=1, ipadx=120, ipady=40)


        # another spacing
        # self.another_space = Label(self.show_frame, text="", font=("Arial Bold", 30))
        # if str(GetConfig['ProgConfig']['appearancemode']) == '2':
        #     self.another_space.configure(background=atk.DEFAULT_COLOR)
        # self.another_space.grid(column=0, row=84, sticky=components_direction)

        # ----------------------------
        # a fix for 1024x768 or lower screen resolutions: (fix #2)
        # ----------------------------
        if int(self.winfo_screenwidth()) <= 1024 and int(self.winfo_screenheight()) <= 768:
            self.about_window_btn.grid(ipady=40, ipadx=50)
            self.exec_btn.grid(ipady=40, ipadx=50)
            self.config_page_btn.grid(ipady=40, ipadx=50)
            self.banner_show.configure(width=775)
            self.banner = PhotoImage(file=f"{application_path}\\bannerlowres.png")
            self.banner_show.configure(image=self.banner)
        # ----------------------------


        # declaring the clear console method/function.
        def clr_console(keybinding_arg):
            """
            Clear the output console (that `scrolledtext.ScrolledText` variable named `output_show`)
            """
            self.output_show.configure(state='normal')
            self.output_show.delete(1.0, END)
            self.output_show.insert(END, f"{getCurrentLanguage().deleted_files}")
            self.output_show.insert(END, "\n")
            self.output_show.configure(state='disabled')

            return None



        def incrFontSizeCoutput(keybinding_arg):
            """
            This function increases the font size of the text in the widget `output_show`

            This function is a part of the "Minimal Accessibility Pack" for Temp_Cleaner GUI
            """
            global font_size, GetConfig
            print(f"[DEBUG]: current widget font size is : {font_size}")
            if int(font_size) == 100:
                messagebox.showerror(getCurrentLanguage().cant_increase_more_msgbox_title, getCurrentLanguage().warning_cant_increase_more)
                return False
            else:
                font_size = font_size + 1
                self.output_show.configure(font=("Courier New", font_size))
                return None

            return None

        def decrFontSizeCoutput(keybinding_arg):
            """
            This function decreases the font size of the text in the widget `output_show`

            This function is a part of the "Minimal Accessibility Pack" for Temp_Cleaner GUI
            """
            global font_size, GetConfig
            print(f"[DEBUG]: current widgets font size is: {font_size}")
            if int(font_size) == 4:
                messagebox.showerror(getCurrentLanguage().cant_decrease_more_msgbox_title, getCurrentLanguage().warning_cant_decrease_more_msgbox)
                return False
            else:
                font_size = font_size - 1
                self.output_show.configure(font=("Courier New", font_size))
                return None

            return None

        
            


        def showHelp(keybinding_arg):
            global GetConfig
            messagebox.showinfo(getCurrentLanguage().help_on_using_minimal_accessibility_pack_msgbox_title, getCurrentLanguage().minimal_accessibility_pack_help)
            return None

        def convert_to_str_with_units(size):
            """
            Converts the given integer or float into an appropriate storage unit.

            maximum supported unit is terabytes (TB)s
            """
            try: # let's try to convert this into an integer.
                size_converted = size
            except Exception: # if all fails.
                return "N/A"
            
            # let's try to make sure the value is not negative.
            try:
                size_converted = abs(size_converted)
            except Exception as abs_convertion_error:
                return f"N/A\n{abs_convertion_error}"
            
            new_size_string = ''
            new_size_string = f"{size_converted} bytes"

            if int(size_converted) > 1024:
                size_converted = (size_converted / 1024)
                # that's in KBs
                new_size_string = str(f"{size_converted} KB")

            if int(size_converted) > 1024:
                size_converted = (size_converted / 1024)
                # now that's in megabytes.
                new_size_string = str(f"{size_converted} MB")

            if int(size_converted) > 1024:
                size_converted = (size_converted / 1024)
                # now that's in gigabytes.
                new_size_string = str(f"{size_converted} GB")

            if int(size_converted) > 1024:
                size_converted = (size_converted / 1024)
                # now that's in terabytes.
                new_size_string = str(f"{size_converted} TB")
            
                
            return new_size_string

        def show_used_systemdrive_space(keybinding_arg):
            system_drive = str(os.getenv("SYSTEMDRIVE"))
            print(f"[DEBUG]: current system drive is: {system_drive}")
            try:
                total, used, free = shutil.disk_usage(system_drive)
                messagebox.showinfo(getCurrentLanguage().usage_statistics_for_systemdrive_word, f"""{getCurrentLanguage().usage_statistics_for_sysdrv}{system_drive.replace(":", '')}:
{getCurrentLanguage().total_systemdrive_space}{convert_to_str_with_units(total)}
{getCurrentLanguage().free_systemdrive_space}{convert_to_str_with_units(free)}
{getCurrentLanguage().used_systemdrive_space}{convert_to_str_with_units(used)}

{getCurrentLanguage().press_ok_when_youre_done}
""")


            except Exception as exception_reading_sysdrv_info:
                messagebox.showerror("An ERROR has occured", f"An exception has occured while fetch system drive information\nConsider trying any of the following:\n1-Restart Temp_Cleaner GUI\n2-Right click on the Temp_Cleaner GUI's icon and click on the Run as Administrator option\n3-Reporting this to my official Github page at https://github.com/insertx2k/temp_cleaner_gui and creating an issue (requires an account at github) with a screenshot with this messagebox in.\nMore details available below:\n{exception_reading_sysdrv_info}")


            return None


        self.lblframe16 = ttk.Labelframe(self.show_frame, text=getCurrentLanguage().console_output_text)
        # ------------------------
        # Creating a scrolledtext widget.
        self.output_show = scrolledtext.ScrolledText(self.lblframe16, foreground='white', selectbackground='#009cda', selectforeground='black' ,state='disabled', font=("Courier New", font_size), width=106, background='black')
        self.output_show.pack(fill=BOTH, expand=1)
        # disabling the state of the output_show widget to prevent the GUI from glitching
        self.output_show.configure(state='disabled')
        # ------------------------
        self.lblframe16.grid(column=0, row=85, sticky=components_direction)

        # getting the right theme for the console output.
        try:
            if str(GetConfig['ProgConfig']['appearancemode']) == "2":
                self.output_show.configure(background=atk.DEFAULT_COLOR)
                self.output_show.configure(foreground='white')
            else:
                pass
        except Exception as exception_reading_theme:
            print(f"[ERROR]: couldn't read the current theme from 'Config.ini' due to exception: {exception_reading_theme}")
            messagebox.showerror(getCurrentLanguage().exception_reading_thememode_title, f"{getCurrentLanguage().exception_reading_thememode_content}\n{exception_reading_theme}")


        def _on_mousewheel(event):
            self.main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        def _bind_to_mousewheel(event):
            self.main_canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        def _unbind_from_mousewheel(event):
            self.main_canvas.unbind_all("<MouseWheel>")
        

        def activate_autodpi_scaling(event):
            """
            Reactivates AutoDpi scaling that got disabled by the `deactivate_automatic_dpi_awareness()` function
            """
            print("[DEBUG]: Window or any of it's widgets took focus, Enabling autodpi awareness")
            try: # Windows 8.1 and later
                ctypes.windll.shcore.SetProcessDpiAwareness(2)
            except Exception as e:
                print(f"[WARNING]: couldn't apply fix #1 to enable HiDPi scaling support: maybe user is not running Windows 8.1 or later: details are: {e}")
            try: # Before Windows 8.1
                ctypes.windll.user32.SetProcessDPIAware()
            except: # Windows 8 or before
                print(f"[ERROR]: couldn't apply HiDPi automatic scaling: maybe the user might need to restart the computer or Temp_Cleaner GUI")
            return None
        # calling the clr_console method with keybinding_arg = 1
        clr_console(1)

        
        # binding f6 in all frames and even in self to clear the output console's content.
        self.bind("<F6>", clr_console)
        self.show_frame.bind("<F6>", clr_console)
        # binding accessibility pack v1.0 shortcut keys to the `self` widget.
        self.bind("<Control-i>", incrFontSizeCoutput)
        self.bind("<Control-I>", incrFontSizeCoutput)
        self.bind("<Control-d>", decrFontSizeCoutput)
        self.bind("<Control-D>", decrFontSizeCoutput)
        # binding accessibility pack v1.0 shortcut keys to the `self.show_frame` widget.
        self.show_frame.bind("<Control-i>", incrFontSizeCoutput)
        self.show_frame.bind("<Control-I>", incrFontSizeCoutput)
        self.show_frame.bind("<Control-D>", decrFontSizeCoutput)
        self.show_frame.bind("<Control-d>", decrFontSizeCoutput)
        # binding accessibility pack v1.0 shortcut keys to the `output_show` widget.
        self.output_show.bind("<Control-i>", incrFontSizeCoutput)
        self.output_show.bind("<Control-I>", incrFontSizeCoutput)
        self.output_show.bind("<Control-d>", decrFontSizeCoutput)
        self.output_show.bind("<Control-D>", decrFontSizeCoutput)
        self.output_show.bind("<F1>", showHelp)
        self.show_frame.bind("<F1>", showHelp)
        self.bind("<F1>", showHelp)
        self.main_canvas.bind('<Enter>', _bind_to_mousewheel)
        self.main_canvas.bind('<Leave>', _unbind_from_mousewheel)
        self.output_show.bind('<Enter>', _unbind_from_mousewheel)
        self.output_show.bind('<Leave>', _bind_to_mousewheel)
        self.show_frame.bind("<F2>", show_used_systemdrive_space)
        self.output_show.bind("<F2>", show_used_systemdrive_space)
        self.main_canvas.bind("<F2>", show_used_systemdrive_space)
        self.main_frame.bind("<F2>", show_used_systemdrive_space)
        self.bind("<F2>", show_used_systemdrive_space)
        # executing a command to terminate the program's interpreter upon pressing the [X] button on top of the window.
        self.protocol("WM_DELETE_WINDOW", close_main_screen)
        # self.bind('<Enter>', activate_autodpi_scaling)
        self.bind("<FocusIn>", activate_autodpi_scaling)

        # calling the check for updates (in multithreading mode) function to check whether if auto updates check at startup is running or not.
        # try:
        #     checkForUpdatesMultiThreading()
        # except Exception as executingAutoCheckForUpdatesFunctionError:
        #     messagebox.showerror("Runtime exception", f"An error has occured that Temp_Cleaner GUI's Updater program couldn't handle so it will be raised here\nException details are:\n{executingAutoCheckForUpdatesFunctionError}\nPress OK to continue")

        # start the automatic check for updates function on a separate thread (fixes the issue where temp_cleaner gui's startup is delayed until updates checking is done)
        threading.Thread(target=checkForUpdatesAutomatically).start()
        # self.show_frame.bind("<MouseWheel>", mouse_scroll)
        # self.bind("<F1>", showHelp) -> causes the messagebox.showinfo help to appear twice.

        


    

    # Defining the function to execute the following selected commands : 
    

    def StartConfigurationWindow(self):
        process_2 = SettingsWindow()
        process_2.mainloop()

        return None
    

    
    






class SettingsWindow(Toplevel):
    def __init__(self):
        """
        This thing here just defines the Configuration window of such software.
        
        This function is no longer experiemental.
        """
        super().__init__()
        deactivate_automatic_dpi_awareness() # deactivating automatic api awareness
    

        global font_size, GetConfig, application_path
        # declaring a boolean var for the custom cursors state.
        # self.custom_cursors_enable_state = BooleanVar()
        # Defining the function used to destroy the whole activity without saving any changes.
        def SelfDestroy():
            self.destroy()

            return None

        def getCurrentLanguage(CurrentLanguageStr=GetConfig['ProgConfig']['languagesetting']):
            """
            Returns `en` if the current UI language is set to English and so on
            """
            try:
                if str(CurrentLanguageStr) == "en":
                    return en
                elif str(CurrentLanguageStr) == "ar":
                    return ar
                else:
                    return en
            except Exception as exception_getting_current_language:
                messagebox.showerror("An ERROR has occured",f"It seems like this is getting serious now, An Exception has occured preventing Temp_Cleaner GUI from loading strings\nException details are\n{exception_getting_current_language}\nPress OK to close the program")
                raise SystemExit(16901) # Exit code 16901 is for an error that prevents Settings window strings from being loaded.

        # Defining the browse for directory function for all browsing folders.
        def BrowseForDirectory(parent):
            self.BrowseForDirectoryWindow = filedialog.askdirectory()
            self.FinalDirectory = self.BrowseForDirectoryWindow
            parent.delete(0, END)
            parent.insert(INSERT, self.FinalDirectory)

            return None


        # Defining the browse 1 func.
        def BrowseOne():
            BrowseForDirectory(self.rammappath_input)
            return None
        
        def BrowseTwo():
            BrowseForDirectory(self.adwcleanerwpath_input)
            return None
        
        def BrowseThree():
            BrowseForDirectory(self.winxpeapppath_input)
            return None
        
        def BrowseFour():
            BrowseForDirectory(self.cdpccpath_input)
            return None

        # a variable for the check status of the checkforupdatesautomatically check box.
        self.autocheckboxvalue = IntVar()

        # Defining the function to retrieve the configuration from the configuration file then outputs it into the textboxes.
        def RetrieveConfig():
            """
            The function used to get the configuration information from the file "Config.ini" in the current program path.
            Do not try to call this function, it will be automatically called when needed.
            """

            self.RetrieveConfig_Init = configparser.ConfigParser()
            try:
                self.RetrieveConfig_Init.read(f"{application_path}\\Config.ini")
            except:
                messagebox.showerror(getCurrentLanguage().cant_retrieve_config_fromfile_msgbox_title, getCurrentLanguage().cant_retrieve_config_fromfile_msgbox_content)
                self.destroy()
            
            try:
                self.rammappath_input.insert(INSERT, self.RetrieveConfig_Init['ProgConfig']['RAMMapPath'])
                self.adwcleanerwpath_input.insert(INSERT, self.RetrieveConfig_Init['ProgConfig']['ADWCLRPath'])
                self.winxpeapppath_input.insert(INSERT, self.RetrieveConfig_Init['ProgConfig']['WINXPEPATH'])
                self.cdpccpath_input.insert(INSERT, self.RetrieveConfig_Init['ProgConfig']['CDPCCPATH'])
                
                if str(self.RetrieveConfig_Init['ProgConfig']['appearancemode']) == '1': # light mode
                    self.appearance_chooser_combo.set(getCurrentLanguage().light_mode)
                elif str(self.RetrieveConfig_Init['ProgConfig']['appearancemode']) == '2': # dark mode
                    self.appearance_chooser_combo.set(getCurrentLanguage().dark_mode) # you get it using it's index according to 0
                
                if str(self.RetrieveConfig_Init['ProgConfig']['languagesetting']) == 'ar':
                    self.language_chooser_combo.set("العربية (مدعمة بواسطة حزمة اللغة العربية الاصدار 1.1)")
                elif str(self.RetrieveConfig_Init['ProgConfig']['languagesetting']) == 'en':
                    self.language_chooser_combo.set("English")
                
                if str(self.RetrieveConfig_Init['ProgConfig']['autocheckforupdates']) == "1": # enabled
                    self.autocheckboxvalue.set(1)
                    print(f"[DEBUG]: Status for autocheckforupdates: {self.checkforupdatesautomatically.get()}")
                else: # disabled
                    self.autocheckboxvalue.set(0)
                    print(f"[DEBUG]: Status for autocheckforupdates: {self.checkforupdatesautomatically.get()}")
                
                # if str(self.RetrieveConfig_Init['ProgConfig']['customcursors']) == "True":
                #     self.custom_cursors_enable_state.set(True)
                # else:
                #     self.custom_cursors_enable_state.set(False)
                
            except Exception as excpt_rtcore_retrieve:
                messagebox.showerror(getCurrentLanguage().cant_read_config_frominside_file_msgbox_title, getCurrentLanguage().cant_read_config_frominside_file_msgbox_content)
                print(f"[ERROR]: couldn't read the current configuration due to exception: {excpt_rtcore_retrieve}")
                self.destroy()
            
            return None



        # It is the time to define the function used to save the changes to the configuration file "Config.ini"
        def SaveConfigurationandQuit():
            self.attributes('-topmost',False) # disabling window is always on top feature.
            try:
                self.ConfigFileSaveProcess = configparser.ConfigParser()
                self.ConfigFileSaveProcess.read(f"{application_path}\\Config.ini")
            except:
                messagebox.showerror(getCurrentLanguage().cant_read_config_frominside_file_msgbox_title, getCurrentLanguage().cant_read_config_frominside_file_msgbox_content)
                self.destroy()

            # Second try.
            try:
                self.ConfigFileSaveProcess['ProgConfig']['RAMMapPath'] = self.rammappath_input.get()
                self.ConfigFileSaveProcess['ProgConfig']['ADWCLRPath'] = self.adwcleanerwpath_input.get()
                self.ConfigFileSaveProcess['ProgConfig']['WINXPEPATH'] = self.winxpeapppath_input.get()
                self.ConfigFileSaveProcess['ProgConfig']['CDPCCPATH'] = self.cdpccpath_input.get()

                print(f"[DEBUG]: current appearance mode as set in settings window is: {str(self.appearance_chooser_combo.get())}")
                if str(self.appearance_chooser_combo.get()) == getCurrentLanguage().dark_mode:
                    self.ConfigFileSaveProcess['ProgConfig']['appearancemode'] = '2'
                elif str(self.appearance_chooser_combo.get()) == getCurrentLanguage().light_mode:
                    self.ConfigFileSaveProcess['ProgConfig']['appearancemode'] = '1'
                else:
                    cantsaveconfig_combostyle_content = f"{getCurrentLanguage().cant_save_config_file_text} {self.appearance_chooser_combo}"
                    cantsaveconfig_combostyle_title = getCurrentLanguage().incorrect_choice_text
                    messagebox.showerror(cantsaveconfig_combostyle_title, cantsaveconfig_combostyle_content)
                    sys.exit(75) # is for an incorrect theme mode.
                
                print(f"[DEBUG]: current language as set in settings window is: {str(self.language_chooser_combo.get())}")
                if str(self.language_chooser_combo.get()) == "العربية (مدعمة بواسطة حزمة اللغة العربية الاصدار 1.1)":
                    self.ConfigFileSaveProcess['ProgConfig']['languagesetting'] = 'ar'
                elif str(self.language_chooser_combo.get()) == "English":
                    self.ConfigFileSaveProcess['ProgConfig']['languagesetting'] = 'en'
                else:
                    cantsaveconfig_combostyle_content = f"{getCurrentLanguage().cant_save_config_file_text} {self.appearance_chooser_combo}"
                    cantsaveconfig_combostyle_title = getCurrentLanguage().incorrect_choice_text
                    messagebox.showerror(cantsaveconfig_combostyle_title, cantsaveconfig_combostyle_content)
                    sys.exit(195) # is for an incorrect language choice.
                
                if int(self.checkforupdatesautomatically.get()) == 1: # checked/enabled
                    self.ConfigFileSaveProcess['ProgConfig']['autocheckforupdates'] = "1"
                else: # unchecked/disabled
                    self.ConfigFileSaveProcess['ProgConfig']['autocheckforupdates'] = "0"

                # if str(self.custom_cursors_enable_state.get()) == "True":
                #     self.ConfigFileSaveProcess['ProgConfig']['customcursors'] = "True"
                # else:
                #     self.ConfigFileSaveProcess['ProgConfig']['customcursors'] = "False"


                # Right now, I guess it is enough and we should rn write the configuration data to the file "Config.ini".
                with open(f"{application_path}\\Config.ini", 'w') as self.ConfigFileProcessor:
                    self.ConfigFileSaveProcess.write(self.ConfigFileProcessor)

                # Defining the window which will tell the user that a reboot is needed to apply the changes.
                messagebox.showinfo(getCurrentLanguage().changes_saved_text, getCurrentLanguage().done_reboot_for_changes_to_apply_text)

                # Okay, enough with that, let's destroy the main loop ok?
                self.destroy()
            except:
                messagebox.showerror(getCurrentLanguage().cant_read_config_frominside_file_msgbox_title, getCurrentLanguage().unable_to_save_your_changes_text)

            return None

        def getCurrentAppearanceMode():
            """
            Gets the current appearance mode to apply to the background of the widgets.
            
            Returns a tuple containing the values of text color and background color for widgets.

            Order goes like that:

            ```py
            (background_color, text_color)
            ```
            """
            global GetConfig
            try:
                if str(GetConfig["ProgConfig"]['appearancemode']) == "1": # 1 is for light mode
                    return (None, 'black')
                elif str(GetConfig["ProgConfig"]['appearancemode']) == "2": # 2 is for dark mode
                    return ('#333', "white")
                else:
                    return (None, "black")
            except Exception as exception_reading_appearance_mode:
                messagebox.showerror("An ERROR has occured", f"{exception_reading_appearance_mode}")
                raise SystemExit(6969) # exit code 6969 is for unhandled appearance mode exceptions
            return False
    
        
        # Defining the root properties.
        self.title(getCurrentLanguage().settings_window_title)
        self.geometry('1202x540')
        self.resizable(False,False)
        self.minsize(1202,540)
        self.maxsize(1202,540)

        try:
            self.iconbitmap(f"{application_path}\\icon0.ico")
        except Exception as excpt672:
            messagebox.showerror("ERROR 1 in ICONBITMAP", f"Unable to load icon file for this window due to Exception:\n{excpt672}")
            pass
    
    
        self.configure(bg=getCurrentAppearanceMode()[0])
        self.attributes('-topmost',True)
        # loading the side banner image.
        self.side_banner_loader = Image.open(f"{application_path}\\settings.jpg")
        self.side_banner_loader = ImageTk.PhotoImage(self.side_banner_loader)

        # declaring the side banner image label.
        self.side_banner = Label(self, image=self.side_banner_loader, background='#333')
        self.side_banner.image = self.side_banner_loader
        self.side_banner.place(x=0, y=0)

        # Defining some informative labels (Basically some bla bla blas).
        self.lbl0_config = Label(self, text=getCurrentLanguage().settings_window_title, font=("Arial Bold", 32), background=getCurrentAppearanceMode()[0], foreground=getCurrentAppearanceMode()[1])
        self.lbl0_config.place(x=260, y=7)
        self.lbl1_config = Label(self, text=getCurrentLanguage().settings_hint_one, foreground=getCurrentAppearanceMode()[1], background=getCurrentAppearanceMode()[0], font=("Arial", 12))
        self.lbl1_config.place(x=260, y=70)
        self.lbl2_config = Label(self, text=getCurrentLanguage().rammap_path_settings_hint, foreground=getCurrentAppearanceMode()[1], background=getCurrentAppearanceMode()[0], font=("Arial",12))
        self.lbl2_config.place(x=260, y=100)
        self.rammappath_input = CTkEntry(self, width=900, height=10)
        self.rammappath_input.place(x=260, y=130)
        self.rammappath_input_browsebtn = CTkButton(self, text="...", command=BrowseOne)
        self.rammappath_input_browsebtn.place(x=1164, y=131, relwidth=0.031, relheight=0.033)
        self.lbl3_config = Label(self, text=getCurrentLanguage().adwcleaner_working_path_settings_hint, foreground=getCurrentAppearanceMode()[1], background=getCurrentAppearanceMode()[0], font=("Arial",12))
        self.lbl3_config.place(x=260, y=155)
        self.adwcleanerwpath_input = CTkEntry(self, width=900, height=10)
        self.adwcleanerwpath_input.place(x=260, y=180)
        self.adwcleanerwpath_input_browsebtn = CTkButton(self, text="...", command=BrowseTwo)
        self.adwcleanerwpath_input_browsebtn.place(x=1164, y=180, relwidth=0.031, relheight=0.033)
        self.lbl4_config = Label(self, text=getCurrentLanguage().winxpe_prog_path_settings_hint, foreground=getCurrentAppearanceMode()[1], background=getCurrentAppearanceMode()[0], font=("Arial", 12))
        self.lbl4_config.place(x=260, y=205)
        self.winxpeapppath_input = CTkEntry(self, width=900, height=10)
        self.winxpeapppath_input.place(x=260, y=230)
        self.winxpeapppath_input_browsebtn = CTkButton(self, text="...", command=BrowseThree)
        self.winxpeapppath_input_browsebtn.place(x=1164, y=230, relwidth=0.031, relheight=0.033)
        self.lbl5_config = Label(self, text=getCurrentLanguage().userid_folder_winactivitiescache_settings_hint, foreground=getCurrentAppearanceMode()[1], background=getCurrentAppearanceMode()[0], font=("Arial",12))
        self.lbl5_config.place(x=260, y=257)
        self.cdpccpath_input = CTkEntry(self, width=900, height=10)
        self.cdpccpath_input.place(x=260, y=283)
        self.cdpccpath_input_browsebtn = CTkButton(self, text="...", command=BrowseFour)
        self.cdpccpath_input_browsebtn.place(x=1164, y=283, relwidth=0.031, relheight=0.033)
        self.lbl6_config = Label(self, text=getCurrentLanguage().appearance_mode_settings_hint, foreground=getCurrentAppearanceMode()[1], background=getCurrentAppearanceMode()[0], font=("Arial", 12))
        self.lbl6_config.place(x=260, y=310)
        self.appearance_chooser_combo = CTkComboBox(self, values=(getCurrentLanguage().light_mode, getCurrentLanguage().dark_mode))
        self.appearance_chooser_combo.place(x=260, y=335, relheight=0.050, relwidth=0.780)

        self.lbl7_config = Label(self, text="Choose your language/اختار لغتك:", foreground=getCurrentAppearanceMode()[1], background=getCurrentAppearanceMode()[0], font=("Arial", 12))
        self.lbl7_config.place(x=260, y=370)
        self.language_chooser_combo = CTkComboBox(self, values=("العربية (مدعمة بواسطة حزمة اللغة العربية الاصدار 1.1)", "English"))
        self.language_chooser_combo.place(relheight=0.050, relwidth=0.780, x=260, y=396)

        self.lbl8_config = Label(self, text=getCurrentLanguage().checking_for_updates, foreground=getCurrentAppearanceMode()[1], background=getCurrentAppearanceMode()[0], font=("Arial", 12))
        self.lbl8_config.place(x=260, y=430)
        

        # the checkbox for automatic updates check
        self.checkforupdatesautomatically = CTkCheckBox(self, text=getCurrentLanguage().auto_check_for_updates, variable=self.autocheckboxvalue, onvalue=1, offvalue=0, command=None)
        self.checkforupdatesautomatically.place(x=260, y=460)


        # self.lbl8_config = Label(self, text=getCurrentLanguage().use_custom_cursors_text, foreground=getCurrentAppearanceMode()[1], background=getCurrentAppearanceMode()[0], font=("Arial", 12))
        # self.lbl8_config.place(x=260, y=430)
        # self.lbl9_config = Label(self, text=getCurrentLanguage().use_custom_cursors_hint, foreground='red', background=getCurrentAppearanceMode()[0], font=("Arial", 11))
        # self.lbl9_config.place(x=260, y=450)


        
        # self.enable_custom_cursors_checkbutton = CTkCheckBox(self, text=getCurrentLanguage().use_custom_cursors_checkbox_text, variable=self.custom_cursors_enable_state)
        # self.enable_custom_cursors_checkbutton.place(x=260, y=470)
        
        # defining the copyright window button.
        


        self.closewindow_btn = CTkButton(self, text=getCurrentLanguage().quit_settings_btn, command=SelfDestroy)
        self.closewindow_btn.place(x=260, y=495, relwidth=0.20, relheight=0.060)

        self.applychangesandclose_btn = CTkButton(self, text=getCurrentLanguage().commit_changes_plus_exit_btn, command=SaveConfigurationandQuit)
        self.applychangesandclose_btn.place(x=958, y=495, relwidth=0.20, relheight=0.060)

        # ----------------------------
        # a fix for 1024x768 or lower screen resolutions: (fix #3 - settings window)
        # ----------------------------
        if int(self.winfo_screenwidth()) <= 1024 and int(self.winfo_screenheight()) <= 768:
            self.minsize(900,540)
            self.maxsize(900,540)
            self.geometry('900x540')
            self.rammappath_input.configure(width=600)
            self.adwcleanerwpath_input.configure(width=600)
            self.winxpeapppath_input.configure(width=600)
            self.cdpccpath_input.configure(width=600)
            self.appearance_chooser_combo.place(x=260, y=335, relheight=0.050, relwidth=0.667)
            self.language_chooser_combo.place(relheight=0.050, relwidth=0.667, x=260, y=396)
            self.lbl5_config.configure(font=("Arial",10))
            self.lbl3_config.configure(font=("Arial",11))
            self.closewindow_btn.place(x=260, y=500, relwidth=0.12, relheight=0.060)
            self.applychangesandclose_btn.place(x=742, y=500, relwidth=0.12, relheight=0.060)
            # declaring a variable to contain the x position of browse buttons.
            x_browse_btns = 865
            new_width = 0.033
            # ------------------------
            self.rammappath_input_browsebtn.place(x=x_browse_btns, y=131, relwidth=new_width, relheight=0.033)
            self.adwcleanerwpath_input_browsebtn.place(x=x_browse_btns, y=180, relwidth=new_width, relheight=0.033)
            self.winxpeapppath_input_browsebtn.place(x=x_browse_btns, y=230, relwidth=new_width, relheight=0.033)
            self.cdpccpath_input_browsebtn.place(x=x_browse_btns, y=283, relwidth=new_width, relheight=0.033)
        # ----------------------------


        # Calling the function to retrieve the configuration information from the config.ini file.
        RetrieveConfig()

        # Calling the ConfigRoot's Mainloop (Used to allow the user to interact to the window freely)
        # ConfigRoot.mainloop()
    
        



class LicenseWindow(Tk):
    def __init__(self):
        super().__init__()
        global font_size, GetConfig, application_path
        self.attributes('-topmost',True) # making the window always on top
        def getCurrentAppearanceMode():
            """
            Gets the current appearance mode to apply to the background of the widgets.
            
            Returns a tuple containing the values of text color and background color for widgets.

            Order goes like that:

            ```py
            (background_color, text_color)
            ```
            """
            global GetConfig
            try:
                if str(GetConfig["ProgConfig"]['appearancemode']) == "1": # 1 is for light mode
                    return ('white', 'black')
                elif str(GetConfig["ProgConfig"]['appearancemode']) == "2": # 2 is for dark mode
                    return ('#333', "white")
                else:
                    return ('white', "black")
            except Exception as exception_reading_appearance_mode:
                messagebox.showerror("An ERROR has occured", f"{exception_reading_appearance_mode}")
                raise SystemExit(6969) # exit code 6969 is for unhandled appearance mode exceptions
            return False

        def getCurrentLanguage(CurrentLanguageStr=GetConfig["ProgConfig"]['languagesetting']):
            try:
                if str(CurrentLanguageStr) == "en":
                    return en
                elif str(CurrentLanguageStr) == "ar":
                    return ar
                else:
                    return en
            except Exception as exception_cant_detect_currentlang:
                messagebox.showerror("An ERROR has occured", f"This is getting serious now, An Exception has occured preventing Temp_Cleaner GUI from loading Strings\nException details available below:\n{exception_cant_detect_currentlang}\nPress OK to close this program")
                raise SystemExit(16945) # Exit code 16945 is for unable to load strings on license window.
            pass

        # defining a new toplevel widget to show the program's license on.
        self.title(getCurrentLanguage().license_window_title)
        self.geometry('640x480')
        self.minsize(640, 480)
        self.resizable(True, True)
        
        def decrFontSize(keybinding_arg):
            """
            This function decreases the font size of the text in the window (TopLevel widget) `licenseShow`

            This function is a part of the "Minimal Accessibility Pack" for Temp_Cleaner GUI
            """
            global font_size
            
            # checking if font size is equal to 4.
            if int(font_size) == 4:
                messagebox.showerror(getCurrentLanguage().cant_decrease_more_msgbox_title, getCurrentLanguage().warning_cant_decrease_more_msgbox)
                return False
            else:
                font_size = font_size - 1
                self.showLicenseStext.configure(font=("Arial", font_size))
                return None
            
            print("[DEBUG]: Decrease font size command was ran")
            return None


        def incrFontSize(keybinding_arg):
            """
            This function increases the font size of the text in the window (TopLevel widget) `licenseShow`

            This function is a part of the "Minimal Accessibility Pack" for Temp_Cleaner GUI
            """
            global font_size

            # checking if font size is 100.
            if int(font_size) == 100:
                messagebox.showerror(getCurrentLanguage().cant_increase_more_msgbox_title, getCurrentLanguage().warning_cant_increase_more)
                return False
            else:
                font_size = font_size + 1
                self.showLicenseStext.configure(font=("Arial", font_size))
                return None
            

            print("[DEBUG]: Increase font size command was ran")
            return None


        def showHelp(keybinding_arg):
            messagebox.showinfo(getCurrentLanguage().help_on_using_minimal_accessibility_pack_msgbox_title, getCurrentLanguage().minimal_accessibility_pack_help)

            return None



        # attempting to change the iconbitmap of the show license window.
        try:
            self.iconbitmap(f"{application_path}\\icon0.ico")
            pass
        except Exception as excpt0:
            messagebox.showerror("An error has occured", f"An error has occured while trying to load the icon bitmap for the license window\nError or exception details are:\n{excpt0}\n\nIf you are a user and you are seeing this, consider creating an issue on Temp_Cleaner GUI's official Github page: https://github.com/insertx2k/temp_cleaner_gui")
            pass
        


        # defining the scrolledtext.ScrolledText widget that holds everything in the license text.
        self.showLicenseStext = scrolledtext.ScrolledText(self, font=("Arial", font_size), foreground='black', selectbackground='#009cda', selectforeground='black', state='disabled', cursor='arrow')
        self.showLicenseStext.pack(expand=1, fill="both")

        # adding license text to that widget.
        self.showLicenseStext.configure(state='normal')
        self.showLicenseStext.delete(1.0, END)
        self.showLicenseStext.insert(END, """License for the project Temp_Cleaner GUI release 1.1 and all releases of it : 

A simple program made to help you erase temporary files in your Windows-based PC.
Copyright (C) 2021, 2022, 2023 - Insertx2k Dev (Mr.X) or Ziad Ahmed (Mr.X) or The X Software Foundation

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
    """)
        
        # I don't want the widget to be editable anymore.
        self.showLicenseStext.configure(state='disabled', background=getCurrentAppearanceMode()[0], foreground=getCurrentAppearanceMode()[1])



        # binding keystrokes "Control-D" to decrease font size, and "Control-I" to increase the font size.
        self.bind("<Control-d>", decrFontSize)
        self.bind("<Control-D>", decrFontSize)
        self.bind("<Control-i>", incrFontSize)
        self.bind("<Control-I>", incrFontSize)
        self.bind("<F1>", showHelp)
        # calling the mainloop() of the toplevel widget licenseShow.
        # licenseShow.mainloop()

        # if mainloop was destroyed, return this function with None.
        return None


class AboutWindow(Toplevel):
    def __init__(self):
        super().__init__()
        global application_path
        deactivate_automatic_dpi_awareness() # deactivating automatic dpi awareness
        # applying style file 'style.json'
        try:
            set_default_color_theme(f"{application_path}\\style.json")
        except Exception as exception_loading_color_theme:
            messagebox.showerror("An unhandleable exception has occured", f"Unable to apply the color theme file 'style.json' due to an error\nError details are:\n{exception_loading_color_theme}\nYou can try some of the following before trying to contact the developer of Temp_Cleaner GUI:\n1-Make sure your Antivirus software isn't blocking Temp_Cleaner GUI\n2-Make sure the file 'style.json' exists in this directory (The directory where Temp_Cleaner GUI is installed in, i.e.: C:\\Program Files (x86)\\Temp_Cleaner GUI)\nif the issue still presents you may want to contact the developer(s) of Temp_Cleaner GUI by creating an issue on the official Temp_Cleaner GUI's Github repository at: https://github.com/insertx2k/temp_cleaner_gui\nPlease MAKE SURE to provide us with a screenshot of this dialog box\nThe program will terminate when you press OK")
            raise SystemExit(400) # unable to apply color theme file 'style.json' to 'aboutwindow'.
        


        def getCurrentLanguage(currentLanguageStr=GetConfig['ProgConfig']['languagesetting']):
            """
            Gets the current language from the config file 'Config.ini'

            Should return `en` class if the current language is set to en, and so on.
            """
            try:
                if str(currentLanguageStr) == "en":
                    return en
                elif str(currentLanguageStr) == "ar":
                    return ar
                else:
                    return en
            except Exception as exception_reading_config_file:
                messagebox.showerror("An ERROR has occured",f"Couldn't read from 'Config.ini'\nException details:\n{exception_reading_config_file}\nPress OK to close this program")
                raise SystemExit(169) # Exit code 169 is for unreadable config file or untreatable getCurrentLanguage exceptions.
                # This is needed to make sure the program doesn't act weirdly.
        

        def getCurrentAppearanceMode():
            """
            Gets the current appearance mode to apply to the background of the widgets.
            
            Returns a tuple containing the values of text color and background color for widgets.

            Order goes like that:

            ```py
            (background_color, text_color)
            ```
            """
            global GetConfig
            try:
                if str(GetConfig["ProgConfig"]['appearancemode']) == "1": # 1 is for light mode
                    return (None, 'black')
                elif str(GetConfig["ProgConfig"]['appearancemode']) == "2": # 2 is for dark mode
                    return ('#333', "white")
                else:
                    return (None, "black")
            except Exception as exception_reading_appearance_mode:
                messagebox.showerror("An ERROR has occured", f"{exception_reading_appearance_mode}")
                raise SystemExit(6969) # exit code 6969 is for unhandled appearance mode exceptions
            return False
        
        def closeAboutWindow():
            """
            A function used to close the about window.
            """
            self.destroy()
            return None
        
        def showLicenseWindow():
            """
            This method is just used to create a window that shows the user the license of the program.
            """
            self.ShowActivity = LicenseWindow()
            self.ShowActivity.mainloop()
            return None
        
        def opentcgwebsiteonbrowser():
            webbrowser.open_new("https://insertx2k.github.io/temp_cleaner_gui/")
            return None
        
        def updateCheckFunction():
            """
            Attempt to check for updates by manually running the updater program.
            """
            print("[DEBUG]: User has manually initializied the UpdateCheck function, The program will display the updater window.")
            if updater.downloadAndSaveVersionFile() == False: # attempts to download the version file from the server, if fails will do the following
                messagebox.showerror(getCurrentLanguage().couldntcheckforupdates, getCurrentLanguage().couldnt_download)
                return False
            else: # didn't fail in downloading version file from server
                pass
            
            # attempts to download the release notes file from server, if fails, will do the following
            if updater.downloadAndSaveReleaseNotesFile() == False:
                messagebox.showerror(getCurrentLanguage().couldntcheckforupdates, getCurrentLanguage().couldnt_download)
                return False
            else: # didn't fail in downloading release notes file from server
                pass
            updaterProgramUIProcess = updater.updaterProgramUI()
            updaterProgramUIProcess.mainloop()
            return None


        def showDonatorsWindow():
            """
            A function for the donators button in the About screen.
            """
            donators.DonatorsWindow().mainloop()


        w_width = 830
        w_height = 410
        self.title(getCurrentLanguage().about_window_title)
        self.geometry(f'{w_width}x{w_height}')
        self.resizable(False, False) # not resizable
        self.wm_resizable(False, False) # not resizable (Fix 2 - WM MANAGER CLASS)

        try:
            if int(GetConfig['ProgConfig']['appearancemode']) == 2: # dark mode
                self.configure(background='#333')
            else:
                self.configure(background=None)
                set_appearance_mode("light")
        except Exception as reading_appearance_mode_error:
            messagebox.showerror("Runtime Error", f"An error has occured causing this program to be unable to continue\nError details are:\n{reading_appearance_mode_error}\n\nPlease try again later.")
            raise SystemExit(25584) # error code 25584 is for unable to read appearance mode in about window.
        
        # ------------------------------
        # getting widgets original direction according to the UI language
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en': # if UI lang is English.
            components_direction = en.widgets_sticking_direction
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar': # if UI lang is Arabic.
            components_direction = ar.widgets_sticking_direction
        else: # if UI lang is not specified.
            components_direction = en.widgets_sticking_direction
        # ------------------------------

        try:
            self.iconbitmap(f"{application_path}\\icon0.ico")
        except Exception as loading_iconbitmap_error:
            messagebox.showerror("Runtime error", f"Couldn't load iconbitmap for the window 'About' due to the following error:\n{loading_iconbitmap_error}\nThe program will continue to work but without a Window icon")
            pass
        
        self.lbl0 = Label(self, text=getCurrentLanguage().about_window_title, font=("Arial Bold", 14), foreground=getCurrentAppearanceMode()[1], background=getCurrentAppearanceMode()[0])
        self.lbl0.place(x=0, y=0)
        self.lbl1 = scrolledtext.ScrolledText(self, foreground=getCurrentAppearanceMode()[1], background=getCurrentAppearanceMode()[0], font=("Arial", 13), selectbackground='#f87026', state='disabled')
        self.lbl1.place(x=160, y=30, relwidth=0.80, relheight=0.89)

        # test
        # self.lbl1.insert(INSERT, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nfdkfpgdnsognodsngodfnokvncxvoxcov\n5405430504357084580") -> working!!!
        # inserting help text on the scrolledtext widget.
        self.lbl1.configure(state='normal')
        self.lbl1.delete(1.0, END)
        self.lbl1.insert(INSERT, getCurrentLanguage().about_window_txt)
        self.lbl1.configure(state='disabled')
        # end --------------------

        # declaring the close window button
        self.close_window_btn = CTkButton(self, text=getCurrentLanguage().ok, command=closeAboutWindow)
        self.close_window_btn.place(x=10, y=200)

        self.showcpyrights_windowbtn = CTkButton(self, text=getCurrentLanguage().open_license_window_btn_text, command=showLicenseWindow)
        self.showcpyrights_windowbtn.place(x=10, y=240)

        self.goto_website_btn = CTkButton(self, text=getCurrentLanguage().goto_tcg_website, command=opentcgwebsiteonbrowser)
        self.goto_website_btn.place(x=10, y=280)

        self.runupdater_btn = CTkButton(self, text=getCurrentLanguage().check_for_updates, command=updateCheckFunction)
        self.runupdater_btn.place(x=10, y=320)

        self.donatorswindow_btn = CTkButton(self, text=getCurrentLanguage().donators_btn, command=showDonatorsWindow)
        self.donatorswindow_btn.place(x=10, y=360)

        # the about tcg icon.
        self.tcgiconabout = Label(self, text='', background=getCurrentAppearanceMode()[0])
        self.tcgiconabout.place(x=0, y=30)
        # a group of variables declaring the width and height of the tcg about logo
        tcglogo_width = 150
        tcglogo_height = 150
        try:
            if int(GetConfig['ProgConfig']['appearancemode']) == 2: # dark mode
                self.imageloader = Image.open(f"{application_path}\\about_dark.png")
                self.imageloader = self.imageloader.resize((tcglogo_width,tcglogo_height), Image.ANTIALIAS)
            else: # light mode
                self.imageloader = Image.open(f"{application_path}\\about.png")
                self.imageloader = self.imageloader.resize((tcglogo_width,tcglogo_height), Image.ANTIALIAS)
        except Exception as reading_appearance_mode_error:
            messagebox.showerror("Runtime Error", f"An error has occured causing this program to be unable to continue\nError details are:\n{reading_appearance_mode_error}\n\nPlease try again later.")
            raise SystemExit(25585) # error code 25585 is for unable to read appearance mode in about window for icon image.
        self.photoimageloader = ImageTk.PhotoImage(image=self.imageloader)
        self.tcgiconabout.configure(image=self.photoimageloader)




# when you double-click or run via terminals (command prompt or windows powershell)
if __name__ == '__main__': 
    # change the current working directory (cwd) to application_path
    os.chdir(application_path)
    # attempting to start the main program UI
    main_process = MainWindowLightMode()
    main_process.mainloop()
    # test = AboutWindow()
    # test.mainloop()
    # ensuring the program closes properly.
    raise SystemExit(0)

