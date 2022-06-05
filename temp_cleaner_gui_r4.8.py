"""
The Project Temp_Cleaner GUI by Insertx2k Dev.
A simple temporary folders cleaning solution made by Insertx2k Dev under the GNU General Public License
That will help you free up a lot of disk space in your computer through erasing all the Temporary folders
Exist in almost all temporary folders directories either in your C:\ drive (Windows drive) or other drives. 
Free to modify and redistribute to fit in your needs as explained in the GNU General Public License v2.0 or later.

License for the Project Temp_Cleaner GUI.
   A simple program made to help you erase temporary files in your Windows-based PC.
   Copyright (C) 2021 - Insertx2k Dev (Mr.X)

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

"""

# defining the global variable that holds the font_size of the scrolledtext.ScrolledText widget
# named 'showLicense'
font_size = 14

print()
print("Greetings from the Temp_Cleaner GUI Project.")
print("By Insertx2k Dev (Mr.X)")
print("Github : https://github.com/insertx2k/temp_cleaner_gui")
print("Twitter : https://twitter.com/insertplayztw")
print()
print("Powered by Minimal Accessibility Pack v1.0 by Insertx2k Dev (Mr.X)")
print()


# Importing all the required 3rd party modules.
# from re import L -> This import was no longer required as of Update 3.1
from tkinter import *
# import WINTCMD -> This import was no longer required as of Update 3.1
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
import awesometkinter as atk
import sys
import threading
import platform
from translations import *

# Defining the function that will get the current values of an configparser values.
GetConfig = configparser.ConfigParser()
GetConfig.read('Config.ini')

class MainWindowLightMode(Tk):
    def __init__(self):
        global GetConfig, font_size
        super().__init__() # initializing the self.

        # Trying to change the theme.
        try:
            # Changing the self's theme.
            self.style = ttk.Style()
            # self.style.theme_use("native")
        except Exception as excpt:
            print(f"The following exception had occured while trying to apply the theme 'native' \n {excpt}")
        
        try:
            self.configure(cursor='@cursor.cur')
        except Exception as exceptioncursor:
            print(f"{exceptioncursor}")
            messagebox.showerror("Unable to use custom Cursor", f"{exceptioncursor}")
            pass
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
            if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                WindowNewTitle = en.prog_title_no_username
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                WindowNewTitle = ar.prog_title_no_username
            else:
                WindowNewTitle = en.prog_title_no_username
            self.title(WindowNewTitle)


        self.geometry('1225x600')

        # attempting to change the iconbitmap attribute of the window.
        try:
            self.iconbitmap("icon0.ico")
        except Exception as excpt12: # better high level exception handling.
            messagebox.showerror("ERROR 1 in ICONBITMAP", f"Unable to load icon file for this window due to exception:\n{excpt12}")
            pass

        self.minsize(1225,600)

        # Changing the self's color.
        # self.configure(background='black')
        # Configuring the scrollbar to make it available for the main program's window.
        # Create a main frame.
        if str(GetConfig['ProgConfig']['appearancemode']) == '1': # light mode
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
            self.banner = PhotoImage(file="banner.png")
            self.banner_show = Label(self.show_frame, image=self.banner, width=1200, height=300)
            self.banner_show.grid(column=0, row=1, sticky='w')
        elif str(GetConfig['ProgConfig']['appearancemode']) == '2': # dark mode.
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
            self.banner = PhotoImage(file="banner.png")
            self.banner_show = Label(self.show_frame, image=self.banner, width=1200, height=300, background=atk.DEFAULT_COLOR)
            self.banner_show.grid(column=0, row=1, sticky='w')
            self.style.configure('TLabelframe.Label', background=atk.DEFAULT_COLOR, foreground='white')
            self.style.configure('Label', background=atk.DEFAULT_COLOR)
            self.style.configure('Label', foreground='white')
            self.style.configure('TLabelframe', background=atk.DEFAULT_COLOR, foreground='white')
            self.style.configure('TCheckbutton', background=atk.DEFAULT_COLOR, foreground='white')
            self.style.configure('label', foreground='white')
            # self.style.configure('Vertical.TScrollbar', background=atk.DEFAULT_COLOR, foreground=atk.DEFAULT_COLOR)
        else: 
            messagebox.showerror("Unsupported appearance mode in Config file", f"Unsupported appearance mode in config file: {str(GetConfig['ProgConfig']['appearancemode'])}.\nThe program will continue with the Light mode instead.")
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
            self.banner = PhotoImage(file="banner.png")
            self.banner_show = Label(self.show_frame, image=self.banner, width=1200, height=300)
            self.banner_show.grid(column=0, row=1, sticky='w')

        def execute_theprogram():
            self.ShowNotificationDone = True
            if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                new_btn_text = en.executing_text
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                new_btn_text = ar.executing_text
            else:
                new_btn_text = en.executing_text
            self.exec_btn.configure(text=new_btn_text, command=None)
            # show_output() # Calling the show output method so you can actually see what's happening inside.
            self.output_show.configure(state='normal')
            self.selection = self.var0.get()
            if self.selection == '1':
                self.process = subprocess.getoutput('rmdir /s /q "%systemdrive%\\$Recycle.bin"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection1 = self.var1.get()
            if self.selection1 == '1':
                self.process = subprocess.getoutput(' cd /d "%windir%"&erase /s /f /q prefetch')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection2 = self.var2.get()
            if self.selection2 == '1':
                self.process = subprocess.getoutput(' cd /d %localappdata%&erase /s /f /q "D3DSCache"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection3 = self.var3.get()
            if self.selection3 == '1':
                self.process = subprocess.getoutput(' cd /d %windir%&erase /s /f /q "Temp"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection4 = self.var4.get()
            if self.selection4 == '1':
                self.process = subprocess.getoutput(' cd /d %localappdata%&erase /s /f /q "Temp"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection5 = self.var5.get()
            if self.selection5 == '1':
                self.process = subprocess.getoutput(' cd /d %localappdata%&cd Google&cd Chrome&cd "User Data"&cd "Default"&erase /s /f /q "GPUCache"&erase /s /f /q Cache&erase /s /f /q "Code Cache"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection6 = self.var6.get()
            if self.selection6 == '1':
                self.process = subprocess.getoutput(' cd /d %localappdata%&cd Google&cd Chrome&cd "User Data"&cd "Default"&del /s /q "Cookies"&del /s /q "Cookies-journal"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection9 = self.var7.get()
            if self.selection9 == '1':
                self.process = subprocess.getoutput(' cd /d "%systemdrive%\\Users\\Default\\AppData\\Local"&erase /s /f /q Temp')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection10 = self.var8.get()
            if self.selection10 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\Microsoft\\Windows"&erase /s /f /q "INetCache"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection11 = self.var9.get()
            if self.selection11 == '1':
                self.process = subprocess.getoutput(' @echo off | clip')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection12 = self.var10.get()
            if self.selection12 == '1':
                self.process = subprocess.getoutput(' cd /d %localappdata%&cd microsoft&cd windows&cd explorer&del /s /q *thumbcache*&cd /d %localappdata%\microsoft\windows\explorer&del /s /q *thumb*')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection13 = self.var11.get()
            if self.selection13 == '1':
                self.process = subprocess.getoutput(' cd /d %userprofile%\\AppData\\Roaming&cd Microsoft&cd Windows&erase /s /f /q Recent')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection14 = self.var12.get()
            if self.selection14 == '1':
                self.process = subprocess.getoutput(' cd /d "%userprofile%\\AppData\\Roaming\\discord"&erase /s /f /q "Cache"&erase /s /f /q "Code Cache"&erase /s /f /q "GPUCache"&erase /s /f /q "Local Storage"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection15 = self.var13.get()
            if self.selection15 == '1':
                self.process = subprocess.getoutput(' cd /d "%userprofile%\\AppData\\Roaming\\GIMP\\2.10"&erase /s /f /q "tmp"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection16 = self.var14.get()
            if self.selection16 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\Steam\\htmlcache"&erase /s /f /q "Cache"&erase /s /f /q "Code Cache"&erase /s /f /q "GPUCache"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection17 = self.var15.get()
            if self.selection17 == '1':
                self.process = subprocess.getoutput(' cd /d "%windir%\\SoftwareDistribution"&del /f /s /q "Download"')
                self.output_show.insert(END, f"\n {self.process}")
                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    btn0_txt = en.restart_winupdate_window_content_text
                    btn0_title = en.restart_winupdate_window_title_text
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    btn0_txt = ar.restart_winupdate_window_content_text
                    btn0_title = ar.restart_winupdate_window_title_text
                else:
                    btn0_txt = en.restart_winupdate_window_content_text
                    btn0_title = en.restart_winupdate_window_title_text
                self.reboot_uwp = messagebox.askquestion(btn0_title, btn0_txt)
                if self.reboot_uwp == "yes":
                    self.self_2 = Tk()
                    if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                        title_txt = en.restart_winupdate_window_title_text
                    elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                        title_txt = ar.restart_winupdate_window_title_text
                    else:
                        title_txt = en.restart_winupdate_window_title_text
                    self.self_2.title(title_txt)
                    self.self_2.geometry('500x90')
                    self.self_2.resizable(False,False)


                    try:
                        self.self_2.iconbitmap("icon0.ico")
                    except Exception as excpt24:
                        messagebox.showerror("ERROR 1 in ICONBITMAP process", f"Unable to load the icon file for this window due to Exception:\n{excpt24}")
                        pass

                    if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                        lbl0_txt = en.restarting_winupdate_service_text
                    elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                        lbl0_txt = ar.restarting_winupdate_service_text
                    else:
                        lbl0_txt = en.restarting_winupdate_service_text
                    # Defining some labels used to show the user that something is happening inside.
                    self.lbl0x = Label(self.self_2, text=lbl0_txt, font=("Arial", 19))
                    self.lbl0x.place(x=25 ,y=20)
                    # Defining the actions used to restart the Windows update service.
                    self.process = subprocess.getoutput('net start wuauserv')
                    if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                        lbl1_txt = en.restart_winupdate_service_done_text
                        lbl2_txt_additionals = en.restart_winupdate_service_done_text
                    elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                        lbl1_txt = ar.restart_winupdate_service_done_text
                        lbl2_txt_additionals = ar.restart_winupdate_service_done_text
                    else:
                        lbl1_txt = en.restart_winupdate_service_done_text
                        lbl2_txt_additionals = en.restart_winupdate_service_done_text
                    # Defining the commands used to show the user that all pending operations has been successfully completed!
                    messagebox.showinfo(title_txt, lbl1_txt)
                    # Defining the mainloop destroy once the execution is done.
                    self.self_2.destroy()
                    self.self_2.mainloop()
                    messagebox.showinfo(title_txt, lbl2_txt_additionals)
                else:
                    if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                        msgbox_rwup_title = en.restart_winupdate_window_title_text
                        msgbox_rwup_content = en.not_restarting_winupdate_service_warning_text
                    elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                        msgbox_rwup_title = ar.restart_winupdate_window_title_text
                        msgbox_rwup_content = ar.not_restarting_winupdate_service_warning_text
                    else:
                        msgbox_rwup_title = en.restart_winupdate_window_title_text
                        msgbox_rwup_content = en.not_restarting_winupdate_service_warning_text
                    messagebox.showinfo(msgbox_rwup_title, msgbox_rwup_content)
            self.selection18 = self.var16.get()
            if self.selection18 == '1':
                self.process = subprocess.getoutput(' cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "Caches"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection19 = self.var17.get()
            if self.selection19 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\Microsoft\\Windows"&erase /s /f /q "INetCookies"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection20 = self.var18.get()
            if self.selection20 == '1':
                self.process = subprocess.getoutput(' cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "IECompatCache"&erase /s /f /q "IECompatUaCache"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection21 = self.var19.get()
            if self.selection21 == '1':
                self.process = subprocess.getoutput(' cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "IEDownloadHistory"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection22 = self.var20.get()
            if self.selection22 == '1':
                self.process =  subprocess.getoutput(' cd /d "%localappdata%\\Microsoft\\Windows"&erase /s /f /q "ActionCenterCache"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection23 = self.var21.get()
            if self.selection23 == '1':
                self.process = subprocess.getoutput(' cd /d %localappdata%\\Microsoft\\Windows&erase /s /f /q "AppCache"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection24 = self.var22.get()
            if self.selection24 == '1':
                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    msgbox_msstoreedge_title = en.clean_ms_store_based_edge_cache_window_title
                    msgbox_msstoreedge_content = en.clean_ms_store_based_edge_cache_dialog_one_content
                    msgbox_msstoreedge_content2 = en.clean_ms_store_based_edge_cache_dialog_two_content
                    done_txt = en.done_text
                    canceled_by_user_txt = en.operation_interrupted_by_user
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    msgbox_msstoreedge_title = ar.clean_ms_store_based_edge_cache_window_title
                    msgbox_msstoreedge_content = ar.clean_ms_store_based_edge_cache_dialog_one_content
                    msgbox_msstoreedge_content2 = ar.clean_ms_store_based_edge_cache_dialog_two_content
                    done_txt = ar.done_text
                    canceled_by_user_txt = ar.operation_interrupted_by_user
                else:
                    msgbox_msstoreedge_title = en.clean_ms_store_based_edge_cache_window_title
                    msgbox_msstoreedge_content = en.clean_ms_store_based_edge_cache_dialog_one_content
                    msgbox_msstoreedge_content2 = en.clean_ms_store_based_edge_cache_dialog_two_content
                    done_txt = en.done_text
                    canceled_by_user_txt = en.operation_interrupted_by_user
                self.conf1 = messagebox.askquestion(msgbox_msstoreedge_title, msgbox_msstoreedge_content)
                if self.conf1 == "yes":
                    messagebox.showinfo(msgbox_msstoreedge_title, msgbox_msstoreedge_content2)
                    self.process = subprocess.getoutput(' explorer.exe "%localappdata%\\Packages\\"')
                    self.output_show.insert(END, f"\n {self.process}")
                    messagebox.showinfo(msgbox_msstoreedge_title, done_txt)
                else:
                    messagebox.showinfo(msgbox_msstoreedge_title, canceled_by_user_txt)
            self.selection25 = self.var23.get()
            if self.selection25 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\Microsoft\\Windows\\Explorer"&erase /s /f /q "ThumbCacheToDelete"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection26 = self.var24.get()
            if self.selection26 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\Microsoft\\Edge\\User Data\\Default"&erase /s /f /q "GPUCache"&erase /s /f /q "Cache"&erase /s /f /q "Code Cache"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection27 = self.var25.get()
            if self.selection27 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\Microsoft\\Edge\\User Data\\Default"&del /s /q "Cookies"&del /s /q "Cookies-journal"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection28 = self.var26.get()
            if self.selection28 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\Roblox"&erase /s /f /q "Downloads"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection29 = self.var27.get()
            if self.selection29 == '1':
                self.process = subprocess.getoutput(' cd /d "%appdata%\\Adobe\\Adobe Photoshop 2020\\Adobe Photoshop 2020 Settings\\web-cache-temp"&erase /s /f /q "GPUCache"&erase /s /f /q "Code Cache"&del /s /f /q "Visited Links"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection30 = self.var28.get()
            if self.selection30 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\VEGAS Pro\\17.0"&erase /s /f /q "File Explorer Thumbnails"&erase /s /f /q "Device Explorer Thumbnails"&del /s /f /q "*.autosave.veg.bak"&del /s /f /q "svfx_Ofx*.log"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection31 = self.var29.get()
            if self.selection31 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\McNeel\\Rhinoceros"&erase /s /f /q "temp"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection32 = self.var30.get()
            if self.selection32 == '1':
                self.process = subprocess.getoutput(' cd /d "%userprofile%\\AppData\\LocalLow\\Microsoft"&erase /s /f /q /A:S "CryptnetUrlCache"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection33 = self.var31.get()
            if self.selection33 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\pip"&erase /s /f /q "cache"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection34 = self.var32.get()
            if self.selection34 == '1':
                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    msgbox_eraserammap_title = en.erase_rammap_title
                    msgbox_eraserammap_content = en.erase_rammap_content
                    msgbox_confirm_defaultpath_txt = en.default_path_rammap
                    msgbox_confirm_defaultpath_title = en.default_path_msgbox_title
                    msgbox_commandsent_txt = en.commandsent_to_rammap_text
                    msgbox_operationcanceledbyuser_txt = en.operation_interrupted_by_user
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    msgbox_eraserammap_title = ar.erase_rammap_title
                    msgbox_eraserammap_content = ar.erase_rammap_content
                    msgbox_confirm_defaultpath_txt = ar.default_path_rammap
                    msgbox_confirm_defaultpath_title = ar.default_path_msgbox_title
                    msgbox_commandsent_txt = ar.commandsent_to_rammap_text
                    msgbox_operationcanceledbyuser_txt = ar.operation_interrupted_by_user
                else:
                    msgbox_eraserammap_title = en.erase_rammap_title
                    msgbox_eraserammap_content = en.erase_rammap_content
                    msgbox_confirm_defaultpath_txt = en.default_path_rammap
                    msgbox_confirm_defaultpath_title = en.default_path_msgbox_title
                    msgbox_commandsent_txt = en.commandsent_to_rammap_text
                    msgbox_operationcanceledbyuser_txt = en.operation_interrupted_by_user
                self.conf2 = messagebox.askquestion(msgbox_eraserammap_title, msgbox_eraserammap_content)
                if self.conf2 == "yes":
                    self.RAMMAPpath_var = GetConfig['ProgConfig']['RAMMapPath']
                    if self.RAMMAPpath_var == '$DEFAULT':
                        messagebox.showinfo(msgbox_confirm_defaultpath_title, msgbox_confirm_defaultpath_txt)
                        self.process = subprocess.getoutput(r'"%systemdrive%\RAMMap\RAMMap.exe" -Ew')
                        self.output_show.insert(END, f"\n {self.process}")
                        messagebox.showinfo(msgbox_eraserammap_title, msgbox_commandsent_txt)
                    else:
                        self.process = subprocess.getoutput(rf'""{self.RAMMAPpath_var}"\RAMMap.exe" -Ew')
                        self.output_show.insert(END, f"\n {self.process}")
                        messagebox.showinfo(msgbox_eraserammap_title, msgbox_commandsent_txt)
                else:
                    messagebox.showinfo(msgbox_eraserammap_title, msgbox_operationcanceledbyuser_txt)
            self.selection35 = self.var33.get()
            if self.selection35 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\Google\\Chrome\\User Data\\Default"&del /s /q "Extension Cookies"&del /s /q "Extension Cookies-journal"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection36 = self.var34.get()
            if self.selection36 == '1':
                self.CDPCCPATH_var = GetConfig['ProgConfig']['CDPCCPATH']
                if self.CDPCCPATH_var == '$DEFAULT':
                    if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                        you_didnt_specify_path_wacc_txt = en.default_path_winactivities_cache_text
                        notification_2 = en.default_path_msgbox_title
                    elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                        you_didnt_specify_path_wacc_txt = ar.default_path_winactivities_cache_text
                        notification_2 = ar.default_path_msgbox_title
                    else:
                        you_didnt_specify_path_wacc_txt = en.default_path_winactivities_cache_text
                        notification_2 = en.default_path_msgbox_title
                    messagebox.showinfo(notification_2, you_didnt_specify_path_wacc_txt)
                    self.process = subprocess.getoutput(' cd /d "%localappdata%\\ConnectedDevicesPlatform"&erase /s /f /q "ee2999716b7783e6"')
                    self.output_show.insert(END, f"\n {self.process}")
                else:
                    self.process = subprocess.getoutput(rf' cd /d "%localappdata%\\ConnectedDevicesPlatform"&erase /s /f /q "{self.CDPCCPATH_var}"')
                    self.output_show.insert(END, f"\n {self.process}")
            self.selection37 = self.var35.get()
            if self.selection37 == '1':
                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    clr_iconcache_dialogtxt = en.iconcache_dialog_text
                    clr_iconcache_dialogtitle = en.clear_icon_cache_dialog_text
                    clr_iconcache_databasefile_done = en.done_text
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    clr_iconcache_dialogtxt = ar.iconcache_dialog_text
                    clr_iconcache_dialogtitle = ar.clear_icon_cache_dialog_text
                    clr_iconcache_databasefile_done = ar.done_text
                else:
                    clr_iconcache_dialogtxt = en.iconcache_dialog_text
                    clr_iconcache_dialogtitle = en.clear_icon_cache_dialog_text
                    clr_iconcache_databasefile_done = en.done_text
                self.conf3 = messagebox.askquestion(clr_iconcache_dialogtitle, clr_iconcache_dialogtxt)
                if self.conf3 == "yes":
                    self.process = subprocess.getoutput('%windir%\\explorer.exe "%localappdata%"')
                    self.output_show.insert(END, f"\n {self.process}")
                    messagebox.showinfo(clr_iconcache_dialogtitle, clr_iconcache_databasefile_done)
                else:
                    pass
            self.selection38 = self.var36.get()
            if self.selection38 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%"&erase /s /f /q "Microvirt"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection39 = self.var37.get()
            if self.selection39 == '1':
                self.ADWCLRPATH_var = GetConfig['ProgConfig']['ADWCLRPath']
                if self.ADWCLRPATH_var == '$DEFAULT':
                    if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                        notification_3 = en.default_path_msgbox_title
                        custom_pathforadwclr_content = en.nocustom_path_foradwcleaner_text
                    elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                        notification_3 = ar.default_path_msgbox_title
                        custom_pathforadwclr_content = ar.nocustom_path_foradwcleaner_text
                    else:
                        notification_3 = en.default_path_msgbox_title
                        custom_pathforadwclr_content = en.nocustom_path_foradwcleaner_text
                    messagebox.showinfo(notification_3, custom_pathforadwclr_content)
                    self.process = subprocess.getoutput(' erase /s /f /q "%systemdrive%\\AdwCleaner\\Logs"')
                    self.output_show.insert(END, f"\n {self.process}")
                else:
                    self.process = subprocess.getoutput(rf' erase /s /f /q "{self.ADWCLRPATH_var}\Logs"')
                    self.output_show.insert(END, f"\n {self.process}")
            self.selection40 = self.var38.get()
            if self.selection40 == '1':
                self.process = subprocess.getoutput(' %systemdrive%&cd /d \\.\\&erase /s /f /q "PerfLogs"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection41 = self.var39.get()
            if self.selection41 == '1':
                self.process = subprocess.getoutput(' cd /d "%userprofile%"&rmdir /s /q ".cache"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection42 = self.var40.get()
            if self.selection42 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%"&erase /s /f /q "SquirrelTemp"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection43 = self.var41.get()
            if self.selection43 == '1':
                self.process = subprocess.getoutput(' cd /d "%userprofile%\\AppData\\LocalLow"&erase /s /f /q "Temp"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection44 = self.var42.get()
            if self.selection44 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%"&erase /s /f /q "ElevatedDiagnostics"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection45 = self.var43.get()
            if self.selection45 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\VMware"&erase /s /f /q "vmware-download*"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection46 = self.var44.get()
            if self.selection46 == '1':
                self.process = subprocess.getoutput(' cd /d "%userprofile%\\appdata\\roaming\\balena-etcher"&erase /s /f /q "blob_storage"&erase /s /f /q "Code Cache"&erase /s /f /q "GPUCache"&erase /s /f /q "Local Storage"&erase /s /f /q "Session Storage"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection47 = self.var45.get()
            if self.selection47 == '1':
                self.process = subprocess.getoutput(' cd /d "%appdata%"&cd /d "%userprofile%\\AppData\\Roaming"&erase /s /f /q "pyinstaller"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection48 = self.var46.get()
            if self.selection48 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%"&erase /s /f /q "Jedi"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection49 = self.var47.get()
            if self.selection49 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%"&del /s /q "recently-used.xbel"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection50 = self.var48.get()
            if self.selection50 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%"&del /s /q "llftool.*.agreement"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection51 = self.var49.get()
            if self.selection51 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%"&erase /s /f /q "IdentityNexusIntegration"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection52 = self.var50.get()
            if self.selection52 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\Axolot Games"&cd "Scrap Mechanic"&cd "Temp"&erase /s /f /q "WorkshopIcons"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection53 = self.var51.get()
            if self.selection53 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\Roblox"&erase /s /f /q "logs"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection54 = self.var52.get()
            if self.selection54 == '1':
                self.process = subprocess.getoutput(' cd /d "%userprofile%\\AppData\\Roaming\\Code"&erase /s /f /q "GPUCache"&erase /s /f /q "Code Cache"&erase /s /f /q "CachedData"&erase /s /f /q "Cache"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection55 = self.var53.get()
            if self.selection55 == '1':
                self.process = subprocess.getoutput(' cd /d "%userprofile%\\AppData\\Roaming\\Code"&del /s /q "Cookies"&del /s /q "Cookies-journal"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection56 = self.var54.get()
            if self.selection56 == '1':
                self.process = subprocess.getoutput(' cd /d "%userprofile%\\AppData\\Roaming\\Code"&erase /s /f /q "CachedExtensions"&erase /s /f /q "CachedExtensionVSIXs"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection57 = self.var55.get()
            if self.selection57 == '1':
                self.WINXPEPATH_var = GetConfig['ProgConfig']['WINXPEPATH']
                if self.WINXPEPATH_var == '$NONE':
                    if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                        error_title = en.an_error_has_occured_text
                        error_content_nopathforwinxpe = en.no_path_winxpe_text
                    elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                        error_title = ar.an_error_has_occured_text
                        error_content_nopathforwinxpe = ar.no_path_winxpe_text
                    else:
                        error_title = en.an_error_has_occured_text
                        error_content_nopathforwinxpe = en.no_path_winxpe_text
                    messagebox.showinfo(error_title, error_content_nopathforwinxpe)
                else:
                    self.process = subprocess.getoutput(rf' erase /s /f /q "{self.WINXPEPATH_var}\Temp"')
                    self.output_show.insert(END, f"\n {self.process}")
                    if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                        notify_title = en.note_text
                        notify_content = en.winxpe_after_clean_note_text
                    elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                        notify_title = ar.note_text
                        notify_content = ar.winxpe_after_clean_note_text
                    else:
                        notify_title = en.note_text
                        notify_content = en.winxpe_after_clean_note_text
                    messagebox.showinfo(notify_title, notify_content)
                    
            self.selection58 = self.var56.get()
            if self.selection58 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%"&erase /s /f /q "ServiceHub"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection59 = self.var57.get()
            if self.selection59 == '1':
                self.process = subprocess.getoutput(' erase /s /f /q "%localappdata%\\HiSuite\\log"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection60 = self.var58.get()
            if self.selection60 == '1':
                self.process = subprocess.getoutput(' erase /s /f /q "%userprofile%\\AppData\\Roaming\\.minecraft\\webcache"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection61 = self.var59.get()
            if self.selection61 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\Mozilla\\Firefox\\Profiles"&cd *.default-release&erase /s /f /q "cache2"&erase /s /f /q "jumpListCache"&cd /d "%userprofile%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"&cd *.default-release&erase /s /f /q "shader-cache"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection62 = self.var60.get()
            if self.selection62 == '1':
                self.process = subprocess.getoutput(' cd /d "%userprofile%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles"&cd *.default-release&del /s /q "cookies.sqlite"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection63 = self.var61.get()
            if self.selection63 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\VEGAS"&erase /s /f /q "ErrorReport"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection64 = self.var62.get()
            if self.selection64 == '1':
                self.process = subprocess.getoutput(' cd /d "%userprofile%\\AppData\\LocalLow\\Sun\\Java\\Deployment"&erase /s /f /q "tmp"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection65 = self.var63.get()
            if self.selection65 == '1':
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\HiSuite\\userdata"&erase /s /f /q "DropTemp"')
                self.output_show.insert(END, f"\n {self.process}")
            self.selection66 = self.var64.get()
            self.output_show.insert(END, "\n\n\n All pending operations has been completed!\n\n\n\nYou may press the 'F6' button in your keyboard to clear console.\n\n\n")
            self.output_show.configure(state='disabled')

            if self.selection66 == '1':
                self.destroy()
            # Sleeping a bit for longer (or equal) to 5 seconds.
            time.sleep(1)

            try:
                # Ok, let's revert everything back to what it was before.
                self.exec_btn.configure(text=self.begin_cleaning_btn_text, command=multiprocessing_execute_btn_function)
            except TclError as tkerr:
                pass


            return None


        def multiprocessing_execute_btn_function():
            threading.Thread(target=execute_theprogram).start()
            pass


        # main_canvas.configure(background='black')
        # main_frame.configure(background='black')
        # self.show_frame.configure(background='black')
        # Defining some informative labels inside of the Temp_Cleaner GUI's Window.
        # self.banner = PhotoImage(file="banner.png")
        # self.banner_show = Label(self.show_frame, image=self.banner, width=1200, height=300)
        # self.banner_show.grid(column=0, row=1, sticky='w')
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
        self.var35 = StringVar()
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
        self.var48 = StringVar()
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
        # Defining the checkbox button.

        # setting the proper language pack for the program's UI.
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text0 = en.recycle_bin_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text0 = ar.recycle_bin_text
        else:
            text0 = en.recycle_bin_text

        self.lblframe0 = ttk.Labelframe(self.show_frame, text=text0)
        # --------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text1 = en.windrv_recycle_bin_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text1 = ar.windrv_recycle_bin_text
        else:
            text1 = en.windrv_recycle_bin_text

        self.clr_recyclebin_sysdrive_btn = ttk.Checkbutton(self.lblframe0, text=text1, variable=self.var0, onvalue="1", offvalue="0", command=None)
        self.clr_recyclebin_sysdrive_btn.grid(column=0, row=3, sticky='w')

        # ---------------------------
        self.lblframe0.grid(column=0, row=2, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text2 = en.dxdcache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text2 = ar.dxdcache_text
        else:
            text2 = en.dxdcache_text

        self.lblframe1 = ttk.Labelframe(self.show_frame, text=text2)
        # ---------------------------
        self.clr_d3dscache_localappdata_btn = ttk.Checkbutton(self.lblframe1, text=text2, variable=self.var2, onvalue="1", offvalue="0", command=None)
        self.clr_d3dscache_localappdata_btn.grid(column=0, row=5, sticky='w')
        # ---------------------------
        self.lblframe1.grid(column=0, row=4, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text3 = en.sys_user_specific_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text3 = ar.sys_user_specific_text
        else:
            text3 = en.sys_user_specific_text
        

        self.lblframe2 = ttk.Labelframe(self.show_frame, text=text3)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text4 = en.prefw_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text4 = ar.prefw_text
        else:
            text4 = en.prefw_text
        
        self.clr_prefetchw_windir_btn = ttk.Checkbutton(self.lblframe2, text=text4, variable=self.var1, onvalue="1", offvalue="0", command=None)
        self.clr_prefetchw_windir_btn.grid(column=0, row=7, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text5 = en.clipboard_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text5 = ar.clipboard_text
        else:
            text5 = en.clipboard_text
        
        self.clr_usrclipboard_content_btn = ttk.Checkbutton(self.lblframe2, text=text5, variable=self.var9, onvalue="1", offvalue="0", command=None)
        self.clr_usrclipboard_content_btn.grid(column=0, row=8, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text6 = en.windir_temp_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text6 = ar.windir_temp_text
        else:
            text6 = en.windir_temp_text
        self.clr_windir_temp_btn = ttk.Checkbutton(self.lblframe2, text=text6, variable=self.var3, onvalue="1", offvalue="0", command=None)
        self.clr_windir_temp_btn.grid(column=0, row=9, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text7 = en.user_temp_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text7 = ar.user_temp_text
        else:
            text7 = en.user_temp_text
        self.clr_localappdata_temp_btn = ttk.Checkbutton(self.lblframe2, text=text7, variable=self.var4, onvalue="1", offvalue="0", command=None)
        self.clr_localappdata_temp_btn.grid(column=0, row=10, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text8 = en.defuser_temp_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text8 = ar.defuser_temp_text
        else:
            text8 = en.defuser_temp_text
        self.clr_default_usr_appdata_temp_btn = ttk.Checkbutton(self.lblframe2, text=text8, variable=self.var7, onvalue="1", offvalue="0", command=None)
        self.clr_default_usr_appdata_temp_btn.grid(column=0, row=11, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text9 = en.iecache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text9 = ar.iecache_text
        else:
            text9 = en.iecache_text
        self.clr_inet_cached_data_btn = ttk.Checkbutton(self.lblframe2, text=text9, variable=self.var8, onvalue="1", offvalue="0", command=None)
        self.clr_inet_cached_data_btn.grid(column=0, row=12, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text10 = en.winexp_thumbcache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text10 = ar.winexp_thumbcache_text
        else:
            text10 = en.winexp_thumbcache_text
        self.clr_msexplorer_thumbcacheddata_btn = ttk.Checkbutton(self.lblframe2, text=text10, variable=self.var10, onvalue="1", offvalue="0", command=None)
        self.clr_msexplorer_thumbcacheddata_btn.grid(column=0, row=13, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text11 = en.user_recents_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text11 = ar.user_recents_text
        else:
            text11 = en.user_recents_text
        self.clr_winrecentdocs_list_btn = ttk.Checkbutton(self.lblframe2, text=text11, variable=self.var11, onvalue="1", offvalue="0", command=None)
        self.clr_winrecentdocs_list_btn.grid(column=0, row=14, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text12 = en.local_low_temp_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text12 = ar.local_low_temp_text
        else:
            text12 = en.local_low_temp_text

        self.clr_locallow_temporary_data_btn = ttk.Checkbutton(self.lblframe2, text=text12, variable=self.var41, onvalue="1", offvalue="0", command=None)
        self.clr_locallow_temporary_data_btn.grid(column=0, row=15, sticky='w')
        # ---------------------------
        self.lblframe2.grid(column=0, row=6, sticky='w')


        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text13 = en.webbrowsers_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text13 = ar.webbrowsers_text
        else:
            text13 = en.webbrowsers_text

        self.lblframe3 = ttk.Labelframe(self.show_frame, text=text13)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text14 = en.gchrome_webcache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text14 = ar.gchrome_webcache_text
        else:
            text14 = en.gchrome_webcache_text
        self.clr_gchrome_webcache_incl_gpucache_codecache_btn = ttk.Checkbutton(self.lblframe3, text=text14, variable=self.var5, onvalue="1", offvalue="0", command=None)
        self.clr_gchrome_webcache_incl_gpucache_codecache_btn.grid(column=0, row=17, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text15 = en.gchrome_cookies_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text15 = ar.gchrome_cookies_text
        else:
            text15 = en.gchrome_cookies_text
        self.clr_gchrome_browser_cookies_btn = ttk.Checkbutton(self.lblframe3, text=text15, variable=self.var6, onvalue="1", offvalue="0", command=None)
        self.clr_gchrome_browser_cookies_btn.grid(column=0, row=18, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text16 = en.gchrome_extensions_cookies_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text16 = ar.gchrome_extensions_cookies_text
        else:
            text16 = en.gchrome_extensions_cookies_text
        self.clr_gchrome_extension_cookies_data_btn = ttk.Checkbutton(self.lblframe3, text=text16, variable=self.var33, onvalue="1", offvalue="0", command=None)
        self.clr_gchrome_extension_cookies_data_btn.grid(column=0, row=19, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text17 = en.steam_htmlcache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text17 = ar.steam_htmlcache_text
        else:
            text17 = en.steam_htmlcache_text
        self.clr_steam_webclient_htmlcache_btn = ttk.Checkbutton(self.lblframe3, text=text17, variable=self.var14, onvalue="1", offvalue="0", command=None)
        self.clr_steam_webclient_htmlcache_btn.grid(column=0, row=20, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text18 = en.discord_webcache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text18 = ar.discord_webcache_text
        else:
            text18 = en.discord_webcache_text
        self.clr_discordwebclient_webcacheddata_btn = ttk.Checkbutton(self.lblframe3, text=text18, variable=self.var12, onvalue="1", offvalue="0", command=None)
        self.clr_discordwebclient_webcacheddata_btn.grid(column=0, row=21, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text19 = en.chromium_based_edge_webcache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text19 = ar.chromium_based_edge_webcache_text
        else:
            text19 = en.chromium_based_edge_webcache_text
        self.clr_chromiumbased_msedge_webcached_data_btn = ttk.Checkbutton(self.lblframe3, text=text19, variable=self.var24, onvalue="1", offvalue="0", command=None)
        self.clr_chromiumbased_msedge_webcached_data_btn.grid(column=0, row=22, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text20 = en.chromium_based_edge_cookies_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text20 = ar.chromium_based_edge_cookies_text
        else:
            text20 = en.chromium_based_edge_cookies_text
        self.clr_chormiumbased_msedge_cookies_data_btn = ttk.Checkbutton(self.lblframe3, text=text20, variable=self.var25, onvalue="1", offvalue="0", command=None)
        self.clr_chormiumbased_msedge_cookies_data_btn.grid(column=0, row=23, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text21 = en.firefox_webcached_data_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text21 = ar.firefox_webcached_data_text
        else:
            text21 = en.firefox_webcached_data_text
        self.clr_mozilla_firefox_webcached_data_btn = ttk.Checkbutton(self.lblframe3, text=text21, variable=self.var59, onvalue="1", offvalue="0", command=None)
        self.clr_mozilla_firefox_webcached_data_btn.grid(column=0, row=24, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text22 = en.mozilla_firefox_cookie_data_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text22 = ar.mozilla_firefox_cookie_data_text
        else:
            text22 = en.mozilla_firefox_cookie_data_text
        self.clr_mozilla_firefox_cookies_sqlite_file_btn = ttk.Checkbutton(self.lblframe3, text=text22, variable=self.var60, onvalue="1", offvalue="0", command=None)
        self.clr_mozilla_firefox_cookies_sqlite_file_btn.grid(column=0, row=25, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text23 = en.discord_squirrel_temp
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text23 = ar.discord_squirrel_temp
        else:
            text23 = en.discord_squirrel_temp
        self.clr_discordapp_squirrel_temp_data_btn = ttk.Checkbutton(self.lblframe3, text=text23, variable=self.var40, onvalue="1", offvalue="0", command=None)
        self.clr_discordapp_squirrel_temp_data_btn.grid(column=0, row=26, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text24 = en.iecookies_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text24 = ar.iecookies_text
        else:
            text24 = en.iecookies_text
        self.clr_inetcookies_btn = ttk.Checkbutton(self.lblframe3, text=text24, variable=self.var17, onvalue="1", offvalue="0", command=None)
        self.clr_inetcookies_btn.grid(column=0, row=27, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text25 = en.adds_ietemp_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text25 = ar.adds_ietemp_text
        else:
            text25 = en.adds_ietemp_text
        self.clr_additionalinet_cacheddata_btn = ttk.Checkbutton(self.lblframe3, text=text25, variable=self.var18, onvalue="1", offvalue="0", command=None)
        self.clr_additionalinet_cacheddata_btn.grid(column=0, row=28, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text26 = en.iedownloadhistory_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text26 = ar.iedownloadhistory_text
        else:
            text26 = en.iedownloadhistory_text
        self.clr_iedownload_history_data_btn = ttk.Checkbutton(self.lblframe3, text=text26, variable=self.var19, onvalue="1", offvalue="0", command=None)
        self.clr_iedownload_history_data_btn.grid(column=0, row=29, sticky='w')
        # ---------------------------
        self.lblframe3.grid(column=0, row=16, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text27 = en.photo_editors_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text27 = ar.photo_editors_text
        else:
            text27 = en.photo_editors_text

        self.lblframe4 = ttk.Labelframe(self.show_frame, text=text27)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text28 = en.gimp_tmp_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text28 = ar.gimp_tmp_text
        else:
            text28 = en.gimp_tmp_text
        self.clr_gimpstmps_btn = ttk.Checkbutton(self.lblframe4, text=text28, variable=self.var13, onvalue="1", offvalue="0", command=None)
        self.clr_gimpstmps_btn.grid(column=0, row=31, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text29 = en.gimp_recent_docs_list_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text29 = ar.gimp_recent_docs_list_text
        else:
            text29 = en.gimp_recent_docs_list_text
        self.clr_gimp_recentdocs_btn = ttk.Checkbutton(self.lblframe4, text=text29, variable=self.var47, onvalue="1", offvalue="0", command=None)
        self.clr_gimp_recentdocs_btn.grid(column=0, row=32, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text30 = en.ps2020_webcache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text30 = ar.ps2020_webcache_text
        else:
            text30 = en.ps2020_webcache_text
        self.clr_adobephotoshop_webcached_data_btn = ttk.Checkbutton(self.lblframe4, text=text30, variable=self.var27, onvalue="1", offvalue="0", command=None)
        self.clr_adobephotoshop_webcached_data_btn.grid(column=0, row=33, sticky='w')
        # ---------------------------
        self.lblframe4.grid(column=0, row=30, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text31 = en.winupdate_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text31 = ar.winupdate_text
        else:
            text31 = en.winupdate_text

        self.lblframe5 = ttk.Labelframe(self.show_frame, text=text31)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text32 = en.winupdate_downloadedfiles_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text32 = ar.winupdate_downloadedfiles_text
        else:
            text32 = en.winupdate_downloadedfiles_text
        self.clr_windowsupdate_downloaded_updates_btn = ttk.Checkbutton(self.lblframe5, text=text32, variable=self.var15, onvalue="1", offvalue="0", command=None)
        self.clr_windowsupdate_downloaded_updates_btn.grid(column=0, row=35, sticky='w')
        # ---------------------------
        self.lblframe5.grid(column=0, row=34, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text33 = en.win10plus_cleaners_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text33 = ar.win10plus_cleaners_text
        else:
            text33 = en.win10plus_cleaners_text

        self.lblframe6 = ttk.Labelframe(self.show_frame, text=text33)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text34 = en.win10plus_oscache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text34 = ar.win10plus_oscache_text
        else:
            text34 = en.win10plus_oscache_text
        self.clr_win10os_cached_data_btn = ttk.Checkbutton(self.lblframe6, text=text34, variable=self.var16, onvalue="1", offvalue="0", command=None)
        self.clr_win10os_cached_data_btn.grid(column=0, row=37, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text35 = en.actioncenter_cache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text35 = ar.actioncenter_cache_text
        else:
            text35 = en.actioncenter_cache_text
        self.clr_win10_action_center_cached_data_btn = ttk.Checkbutton(self.lblframe6, text=text35, variable=self.var20, onvalue="1", offvalue="0", command=None)
        self.clr_win10_action_center_cached_data_btn.grid(column=0, row=38, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text36 = en.modern_apps_cache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text36 = ar.modern_apps_cache_text
        else:
            text36 = en.modern_apps_cache_text
        self.clr_winappux_cached_data_btn = ttk.Checkbutton(self.lblframe6, text=text36, variable=self.var21, onvalue="1", offvalue="0", command=None)
        self.clr_winappux_cached_data_btn.grid(column=0, row=39, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text37 = en.msedge_msstore_webcache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text37 = ar.msedge_msstore_webcache_text
        else:
            text37 = en.msedge_msstore_webcache_text
        self.clr_msstore_based_edge_webcached_data_btn = ttk.Checkbutton(self.lblframe6, text=text37, variable=self.var22, onvalue="1", offvalue="0", command=None)
        self.clr_msstore_based_edge_webcached_data_btn.grid(column=0, row=40, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text38 = en.thumbcachetodelete_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text38 = ar.thumbcachetodelete_text
        else:
            text38 = en.thumbcachetodelete_text
        self.clr_winexplorer_thumbcache_to_delete_files_btn = ttk.Checkbutton(self.lblframe6, text=text38, variable=self.var23, onvalue="1", offvalue="0", command=None)
        self.clr_winexplorer_thumbcache_to_delete_files_btn.grid(column=0, row=41, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text39 = en.cryptneturl_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text39 = ar.cryptneturl_text
        else:
            text39 = en.cryptneturl_text
        self.clr_cryptnet_urlcache_data_btn = ttk.Checkbutton(self.lblframe6, text=text39, variable=self.var30, onvalue="1", offvalue="0", command=None)
        self.clr_cryptnet_urlcache_data_btn.grid(column=0, row=42, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text40 = en.connecteddevicesplatform_cache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text40 = ar.connecteddevicesplatform_cache_text
        else:
            text40 = en.connecteddevicesplatform_cache_text
        self.clr_connecteddevicesplatform_win10_cached_data_btn = ttk.Checkbutton(self.lblframe6, text=text40, variable=self.var34, onvalue="1", offvalue="0", command=None)
        self.clr_connecteddevicesplatform_win10_cached_data_btn.grid(column=0, row=43, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text41 = en.elevateddiagnostics_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text41 = ar.elevateddiagnostics_text
        else:
            text41 = en.elevateddiagnostics_text
        self.clr_elevated_diagnostics_data_btn = ttk.Checkbutton(self.lblframe6, text=text41, variable=self.var42, onvalue="1", offvalue="0", command=None)
        self.clr_elevated_diagnostics_data_btn.grid(column=0, row=44, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text42 = en.identitynexusintegration_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text42 = ar.identitynexusintegration_text
        else:
            text42 = en.identitynexusintegration_text
        self.clr_identitynexus_integration_folder_btn = ttk.Checkbutton(self.lblframe6, text=text42, variable=self.var49, onvalue="1", offvalue="0", command=None)
        self.clr_identitynexus_integration_folder_btn.grid(column=0, row=45, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text43 = en.servicehub_identity_file_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text43 = ar.servicehub_identity_file_text
        else:
            text43 = en.servicehub_identity_file_text
        self.clr_servicehub_identity_file_btn = ttk.Checkbutton(self.lblframe6, text=text43, variable=self.var56, onvalue="1", offvalue="0", command=None)
        self.clr_servicehub_identity_file_btn.grid(column=0, row=46, sticky='w')
        # ---------------------------
        self.lblframe6.grid(column=0, row=36, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text44 = en.games_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text44 = ar.games_text
        else:
            text44 = en.games_text
        self.lblframe7 = ttk.Labelframe(self.show_frame, text=text44)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text45 = en.roblox_textures_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text45 = ar.roblox_textures_text
        else:
            text45 = en.roblox_textures_text
        self.clr_roblox_game_downloads_btn = ttk.Checkbutton(self.lblframe7, text=text45, variable=self.var26, onvalue="1", offvalue="0", command=None)
        self.clr_roblox_game_downloads_btn.grid(column=0, row=48, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text46 = en.roblox_verbosed_logs_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text46 = ar.roblox_verbosed_logs_text
        else:
            text46 = en.roblox_verbosed_logs_text
        self.clr_roblox_game_log_files_btn = ttk.Checkbutton(self.lblframe7, text=text46, variable=self.var51, onvalue="1", offvalue="0", command=None)
        self.clr_roblox_game_log_files_btn.grid(column=0, row=49, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text47 = en.axolot_games_scrapmechanic_workshop_cache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text47 = ar.axolot_games_scrapmechanic_workshop_cache_text
        else:
            text47 = en.axolot_games_scrapmechanic_workshop_cache_text
        self.clr_scrapmechanic_axolot_games_workshop_items_cached_data_btn = ttk.Checkbutton(self.lblframe7, text=text47, variable=self.var50, onvalue="1", offvalue="0", command=None)
        self.clr_scrapmechanic_axolot_games_workshop_items_cached_data_btn.grid(column=0, row=50, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text48 = en.minecraft_webcache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text48 = ar.minecraft_webcache_text
        else:
            text48 = en.minecraft_webcache_text
        self.clr_minecraft_webcached_data_btn = ttk.Checkbutton(self.lblframe7, text=text48, variable=self.var58, onvalue="1", offvalue="0", command=None)
        self.clr_minecraft_webcached_data_btn.grid(column=0, row=51, sticky='w')
        # ---------------------------
        self.lblframe7.grid(column=0, row=47, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text49 = en.python_cleaners_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text49 = ar.python_cleaners_text
        else:
            text49 = en.python_cleaners_text

        self.lblframe8 = ttk.Labelframe(self.show_frame, text=text49)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text50 = en.pypip_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text50 = ar.pypip_text
        else:
            text50 = en.pypip_text
        self.clr_python_pip_cached_data_btn = ttk.Checkbutton(self.lblframe8, text=text50, variable=self.var31, onvalue="1", offvalue="0", command=None)
        self.clr_python_pip_cached_data_btn.grid(column=0, row=53, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text51 = en.pyinstaller_bin_cache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text51 = ar.pyinstaller_bin_cache_text
        else:
            text51 = en.pyinstaller_bin_cache_text
        self.clr_pyinstaller_temporary_data_btn = ttk.Checkbutton(self.lblframe8, text=text51, variable=self.var45, onvalue="1", offvalue="0", command=None)
        self.clr_pyinstaller_temporary_data_btn.grid(column=0, row=54, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text52 = en.jedi_python_cache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text52 = ar.jedi_python_cache_text
        else:
            text52 = en.jedi_python_cache_text
        self.clr_jedipython_additionals_btn = ttk.Checkbutton(self.lblframe8, text=text52, variable=self.var46, onvalue="1", offvalue="0", command=None)
        self.clr_jedipython_additionals_btn.grid(column=0, row=55, sticky='w')
        # ---------------------------
        self.lblframe8.grid(column=0, row=52, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text53 = en.ram_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text53 = ar.ram_text
        else:
            text53 = en.ram_text

        self.lblframe9 = ttk.Labelframe(self.show_frame, text=text53)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text54 = en.empty_running_workingsets_rammap_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text54 = ar.empty_running_workingsets_rammap_text
        else:
            text54 = en.empty_running_workingsets_rammap_text
        self.empty_winworkingsets_rammap_btn = ttk.Checkbutton(self.lblframe9, text=text54, variable=self.var32, onvalue="1", offvalue="0", command=None)
        self.empty_winworkingsets_rammap_btn.grid(column=0, row=57, sticky='w')
        # ---------------------------
        self.lblframe9.grid(column=0, row=56, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text55 = en.video_editing_software_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text55 = ar.video_editing_software_text
        else:
            text55 = en.video_editing_software_text

        self.lblframe10 = ttk.Labelframe(self.show_frame, text=text55)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text56 = en.vegaspro17_temp_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text56 = ar.vegaspro17_temp_text
        else:
            text56 = en.vegaspro17_temp_text
        self.clr_sony_vegas_pro_temp_and_logs_data_btn = ttk.Checkbutton(self.lblframe10, text=text56, variable=self.var28, onvalue="1", offvalue="0", command=None)
        self.clr_sony_vegas_pro_temp_and_logs_data_btn.grid(column=0, row=59, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text57 = en.vegaspro17_errorlogs_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text57 = ar.vegaspro17_errorlogs_text
        else:
            text57 = en.vegaspro17_errorlogs_text
        self.clr_sony_vegas_pro_error_reports_data_btn = ttk.Checkbutton(self.lblframe10, text=text57, variable=self.var61, onvalue="1", offvalue="0", command=None)
        self.clr_sony_vegas_pro_error_reports_data_btn.grid(column=0, row=60, sticky='w')
        # ---------------------------
        self.lblframe10.grid(column=0, row=58, sticky='w')


        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text58 = en.threed_moduling_software_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text58 = ar.threed_moduling_software_text
        else:
            text58 = en.threed_moduling_software_text
        self.lblframe11 = ttk.Labelframe(self.show_frame, text=text58)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text59 = en.mcneel_rhinoceros_3d_temp_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text59 = ar.mcneel_rhinoceros_3d_temp_text
        else:
            text59 = en.mcneel_rhinoceros_3d_temp_text
        self.clr_mcneel_rhinoceros_3d_moduling_soft_cached_data_btn = ttk.Checkbutton(self.lblframe11, text=text59, variable=self.var29, onvalue="1", offvalue="0", command=None)
        self.clr_mcneel_rhinoceros_3d_moduling_soft_cached_data_btn.grid(column=0, row=62, sticky='w')
        # ---------------------------
        self.lblframe11.grid(column=0, row=61, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text60 = en.adds_software_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text60 = ar.adds_software_text
        else:
            text60 = en.adds_software_text

        self.lblframe12 = ttk.Labelframe(self.show_frame, text=text60)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text61 = en.iconcachefile_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text61 = ar.iconcachefile_text
        else:
            text61 = en.iconcachefile_text
        self.clr_iconcache_db_file_in_localappdata_dir_btn = ttk.Checkbutton(self.lblframe12, text=text61, variable=self.var35, onvalue="1", offvalue="0", command=None)
        self.clr_iconcache_db_file_in_localappdata_dir_btn.grid(column=0, row=64, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text62 = en.microvert_memu_logs_memdump_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text62 = ar.microvert_memu_logs_memdump_text
        else:
            text62 = en.microvert_memu_logs_memdump_text
        self.clr_microvirt_memu_log_data_memdump_files_btn = ttk.Checkbutton(self.lblframe12, text=text62, variable=self.var36, onvalue="1", offvalue="0", command=None)
        self.clr_microvirt_memu_log_data_memdump_files_btn.grid(column=0, row=65, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text63 = en.malwarebytes_adware_cleaner_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text63 = ar.malwarebytes_adware_cleaner_text
        else:
            text63 = en.malwarebytes_adware_cleaner_text
        self.clr_adwcleaner_log_files_btn = ttk.Checkbutton(self.lblframe12, text=text63, variable=self.var37, onvalue="1", offvalue="0", command=None)
        self.clr_adwcleaner_log_files_btn.grid(column=0, row=66, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text64 = en.perflogs_sysdrive_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text64 = ar.perflogs_sysdrive_text
        else:
            text64 = en.perflogs_sysdrive_text
        self.clr_perflogs_in_systemdrive_btn = ttk.Checkbutton(self.lblframe12, text=text64, variable=self.var38, onvalue="1", offvalue="0", command=None)
        self.clr_perflogs_in_systemdrive_btn.grid(column=0, row=67, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text65 = en.android_cached_data_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text65 = ar.android_cached_data_text
        else:
            text65 = en.android_cached_data_text
        self.clr_dotcache_folder_in_userprofile_path_btn = ttk.Checkbutton(self.lblframe12, text=text65, variable=self.var39, onvalue="1", offvalue="0", command=None)
        self.clr_dotcache_folder_in_userprofile_path_btn.grid(column=0, row=68, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text66 = en.vmware_downloads
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text66 = ar.vmware_downloads
        else:
            text66 = en.vmware_downloads
        self.clr_vmware_downloads_folder_btn = ttk.Checkbutton(self.lblframe12, text=text66, variable=self.var43, onvalue="1", offvalue="0", command=None)
        self.clr_vmware_downloads_folder_btn.grid(column=0, row=69, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text67 = en.balenaitcher_webcache_files_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text67 = ar.balenaitcher_webcache_files_text
        else:
            text67 = en.balenaitcher_webcache_files_text
        self.clr_balena_itcher_webcached_data_btn = ttk.Checkbutton(self.lblframe12, text=text67, variable=self.var44, onvalue="1", offvalue="0", command=None)
        self.clr_balena_itcher_webcached_data_btn.grid(column=0, row=70, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text68 = en.lowlevelformattool_agreement_file_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text68 = ar.lowlevelformattool_agreement_file_text
        else:
            text68 = en.lowlevelformattool_agreement_file_text
        self.clr_lowlevelformattool_licenseagreement_confirmationfile_btn = ttk.Checkbutton(self.lblframe12, text=text68, variable=self.var48, onvalue="1", offvalue="0", command=None)
        self.clr_lowlevelformattool_licenseagreement_confirmationfile_btn.grid(column=0, row=71, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text69 = en.winxpe_creator_downloadsdir_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text69 = ar.winxpe_creator_downloadsdir_text
        else:
            text69 = en.winxpe_creator_downloadsdir_text
        self.clr_winxpe_app_downloads_folder_btn = ttk.Checkbutton(self.lblframe12, text=text69, variable=self.var55, onvalue="1", offvalue="0", command=None)
        self.clr_winxpe_app_downloads_folder_btn.grid(column=0, row=72, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text70 = en.huawei_hisuite_logdata_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text70 = ar.huawei_hisuite_logdata_text
        else:
            text70 = en.huawei_hisuite_logdata_text
        self.clr_huawei_hisuite_log_data_btn = ttk.Checkbutton(self.lblframe12, text=text70, variable=self.var57, onvalue="1", offvalue="0", command=None)
        self.clr_huawei_hisuite_log_data_btn.grid(column=0, row=73, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text71 = en.huawei_hisuite_dnddata_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text71 = ar.huawei_hisuite_dnddata_text
        else:
            text71 = en.huawei_hisuite_dnddata_text
        self.clr_huawei_hisuite_dnd_temp_btn = ttk.Checkbutton(self.lblframe12, text=text71, variable=self.var63, onvalue="1", offvalue="0", command=None)
        self.clr_huawei_hisuite_dnd_temp_btn.grid(column=0, row=74, sticky='w')
        # ---------------------------
        self.lblframe12.grid(column=0, row=63, sticky='w')


        
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text72 = en.vscode_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text72 = ar.vscode_text
        else:
            text72 = en.vscode_text
        self.lblframe13 = ttk.Labelframe(self.show_frame, text=text72)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text73 = en.vscode_webcache_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text73 = ar.vscode_webcache_text
        else:
            text73 = en.vscode_webcache_text
        self.clr_vscode_webcached_data_btn = ttk.Checkbutton(self.lblframe13, text=text73, variable=self.var52, onvalue="1", offvalue="0", command=None)
        self.clr_vscode_webcached_data_btn.grid(column=0, row=76, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text74 = en.vscode_cookies_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text74 = ar.vscode_cookies_text
        else:
            text74 = en.vscode_cookies_text
        self.clr_vscode_cookie_data_btn = ttk.Checkbutton(self.lblframe13, text=text74, variable=self.var53, onvalue="1", offvalue="0", command=None)
        self.clr_vscode_cookie_data_btn.grid(column=0, row=77, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text75 = en.vscode_cached_extensions_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text75 = ar.vscode_cached_extensions_text
        else:
            text75 = en.vscode_cached_extensions_text
        self.clr_vscode_cached_extensions_data_btn = ttk.Checkbutton(self.lblframe13, text=text75, variable=self.var54, onvalue="1", offvalue="0", command=None)
        self.clr_vscode_cached_extensions_data_btn.grid(column=0, row=78, sticky='w')
        # ---------------------------
        self.lblframe13.grid(column=0, row=75, sticky='w')


        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text76 = en.javadeployment_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text76 = ar.javadeployment_text
        else:
            text76 = en.javadeployment_text

        self.lblframe14 = ttk.Labelframe(self.show_frame, text=text76)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text77 = en.javadeployment_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text77 = ar.javadeployment_text
        else:
            text77 = en.javadeployment_text
        self.clr_java_deployment_cached_data_btn = ttk.Checkbutton(self.lblframe14, text=text77, variable=self.var62, onvalue="1", offvalue="0", command=None)
        self.clr_java_deployment_cached_data_btn.grid(column=0, row=80, sticky='w')
        # ---------------------------
        self.lblframe14.grid(column=0, row=79, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text78 = en.alldone_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text78 = ar.alldone_text
        else:
            text78 = en.alldone_text
        self.lblframe15 = ttk.Labelframe(self.show_frame, text=text78)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text79 = en.alldone_chkbox_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text79 = ar.alldone_chkbox_text
        else:
            text79 = en.alldone_chkbox_text
        self.destroy_activity_after_done_btn = ttk.Checkbutton(self.lblframe15, text=text79, variable=self.var64, onvalue="1", offvalue="0", command=None, cursor='hand2')
        self.destroy_activity_after_done_btn.grid(column=0, row=82, sticky='w')
        # ---------------------------
        self.lblframe15.grid(column=0, row=81, sticky='w')


        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            about_btn_text = en.about_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            about_btn_text = ar.about_text
        else:
            about_btn_text = en.about_text
        # Defining the about button.
        self.about_window_btn = ttk.Button(self.show_frame, text=about_btn_text, command=self.show_about_window, cursor='@Hand.cur')
        self.about_window_btn.place(x=10, y=2000, relwidth=0.3, relheight=0.035)
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            self.begin_cleaning_btn_text = en.execute_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            self.begin_cleaning_btn_text = ar.execute_text
        else:
            self.begin_cleaning_btn_text = en.execute_text
        # Defining the execute button.
        self.exec_btn = ttk.Button(self.show_frame, text=self.begin_cleaning_btn_text, command=multiprocessing_execute_btn_function, cursor='@Hand.cur')
        self.exec_btn.place(x=400 ,y=2000, relwidth=0.3, relheight=0.035)

        # declaring a space.
        self.space = Label(self.show_frame, text="", font=("Arial Bold", 50))
        if str(GetConfig['ProgConfig']['appearancemode']) == '2':
            self.space.configure(background=atk.DEFAULT_COLOR)
        self.space.grid(column=0, row=83, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            go_settings_btn_text = en.settings_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            go_settings_btn_text = ar.settings_text
        else:
            go_settings_btn_text = en.settings_text
        # Defining the go to configuration page button.
        self.config_page_btn = ttk.Button(self.show_frame, text=go_settings_btn_text, command=self.StartConfigurationWindow, cursor='@Hand.cur')
        self.config_page_btn.place(x=790 ,y=2000, relwidth=0.3, relheight=0.035)


        # another spacing
        self.another_space = Label(self.show_frame, text="", font=("Arial Bold", 30))
        if str(GetConfig['ProgConfig']['appearancemode']) == '2':
            self.another_space.configure(background=atk.DEFAULT_COLOR)
        self.another_space.grid(column=0, row=84, sticky='w')


        # declaring the clear console method/function.
        def clr_console(keybinding_arg):
            """
            Clear the output console (that `scrolledtext.ScrolledText` variable named `output_show`)
            """
            self.output_show.configure(state='normal')
            self.output_show.delete(1.0, END)
            self.output_show.insert(END, "Temp_Cleaner GUI for Windows\nOutput Console\n\n# The console output will appear here as soon as any process begins.")
            self.output_show.insert(END, "\n")
            self.output_show.configure(state='disabled')

            return None



        def incrFontSizeCoutput(keybinding_arg):
            """
            This function increases the font size of the text in the widget `output_show`

            This function is a part of the "Minimal Accessibility Pack" for Temp_Cleaner GUI
            """
            global font_size, GetConfig
            if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                warn_txt = en.warning_cant_increase_more
                warn_title = en.cant_increase_more_msgbox_title
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                warn_txt = ar.warning_cant_increase_more
                warn_title = ar.cant_increase_more_msgbox_title
            else:
                warn_txt = en.warning_cant_increase_more
                warn_title = en.cant_increase_more_msgbox_title

            if int(font_size) == 100:
                messagebox.showerror(warn_title, warn_txt)
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
            if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                warn_txt = en.warning_cant_decrease_more_msgbox
                warn_title = en.cant_decrease_more_msgbox_title
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                warn_txt = ar.warning_cant_decrease_more_msgbox
                warn_title = ar.cant_decrease_more_msgbox_title
            else:
                warn_txt = en.warning_cant_decrease_more_msgbox
                warn_title = en.cant_decrease_more_msgbox_title

            if int(font_size) == 4:
                messagebox.showerror(warn_title, warn_txt)
                return False
            else:
                font_size = font_size - 1
                self.output_show.configure(font=("Courier New", font_size))
                return None

            return None

        
            


        def showHelp(keybinding_arg):
            global GetConfig
            if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                msg_box_txt = en.minimal_accessibility_pack_help
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                msg_box_txt = ar.minimal_accessibility_pack_help
            else:
                msg_box_txt = en.minimal_accessibility_pack_help

            if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                msg_box_title = en.help_on_using_minimal_accessibility_pack_msgbox_title
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                msg_box_title = ar.help_on_using_minimal_accessibility_pack_msgbox_title
            else:
                msg_box_title = en.help_on_using_minimal_accessibility_pack_msgbox_title

            messagebox.showinfo(msg_box_title, msg_box_txt)

            return None


        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            console_output_hint_txt = en.console_output_text
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            console_output_hint_txt = ar.console_output_text
        else:
            console_output_hint_txt = en.console_output_text
        self.lblframe16 = ttk.Labelframe(self.show_frame, text=console_output_hint_txt)
        # ------------------------
        # Creating a scrolledtext widget.
        self.output_show = scrolledtext.ScrolledText(self.lblframe16, cursor='@TextSelect.cur', foreground='white', selectbackground='#009cda', selectforeground='black' ,state='disabled', font=("Courier New", font_size), width=106, background='black')
        self.output_show.pack(fill=BOTH, expand=1)
        # disabling the state of the output_show widget to prevent the GUI from glitching
        self.output_show.configure(state='disabled')
        # ------------------------
        self.lblframe16.grid(column=0, row=85, sticky='w')


        def _on_mousewheel(event):
            self.main_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        def _bind_to_mousewheel(event):
            self.main_canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        def _unbind_from_mousewheel(event):
            self.main_canvas.unbind_all("<MouseWheel>")
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
        self.main_canvas.bind('<Enter>', _bind_to_mousewheel)
        self.main_canvas.bind('<Leave>', _unbind_from_mousewheel)
        self.output_show.bind('<Enter>', _unbind_from_mousewheel)
        self.output_show.bind('<Leave>', _bind_to_mousewheel)
        # self.show_frame.bind("<MouseWheel>", mouse_scroll)
        # self.bind("<F1>", showHelp) -> causes the messagebox.showinfo help to appear twice.


    # Defining the function used to show the user the about window of the program.
    def show_about_window(self):
        global GetConfig
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            about_window_txt = en.about_window_txt
            about_window_title = en.about_window_title
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            about_window_txt = ar.about_window_txt
            about_window_title = ar.about_window_title
        else:
            about_window_txt = en.about_window_txt
            about_window_title = en.about_window_title


        messagebox.showinfo(about_window_title,about_window_txt)

        return None

    # Defining the function to execute the following selected commands : 
    

    def StartConfigurationWindow(self):
        process_2 = SettingsWindow()
        process_2.mainloop()

        return None
    






class SettingsWindow(Tk):
    def __init__(self):
        """
        This thing here just defines the Configuration window of such software.
        
        This function is no longer experiemental.
        """
        super().__init__()
    

        global font_size, GetConfig
        # Defining the function used to destroy the whole activity without saving any changes.
        def SelfDestroy():
            self.destroy()

            return None

        # Defining the browse for directory function for all browsing folders.
        def BrowseForDirectory(parent):
            self.BrowseForDirectoryWindow = filedialog.askdirectory()
            self.FinalDirectory = self.BrowseForDirectoryWindow
            parent.delete(0, END)
            parent.insert(INSERT, self.FinalDirectory)

            return None

        def showLicenseWindow():
            """
            This method is just used to create a window that shows the user the license of the program.
            """
            self.ShowActivity = LicenseWindow()
            self.ShowActivity.mainloop()
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


        # Defining the function to retrieve the configuration from the configuration file then outputs it into the textboxes.
        def RetrieveConfig():
            """
            The function used to get the configuration information from the file "Config.ini" in the current program path.
            Do not try to call this function, it will be automatically called when needed.
            """

            self.RetrieveConfig_Init = configparser.ConfigParser()
            try:
                self.RetrieveConfig_Init.read("Config.ini")
            except:
                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    cantretrieveconfigfromfile_content = en.cant_retrieve_config_fromfile_msgbox_content
                    cantretrieveconfigfromfile_title = en.cant_retrieve_config_fromfile_msgbox_title
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    cantretrieveconfigfromfile_content = ar.cant_retrieve_config_fromfile_msgbox_content
                    cantretrieveconfigfromfile_title = ar.cant_retrieve_config_fromfile_msgbox_title
                else:
                    cantretrieveconfigfromfile_content = en.cant_retrieve_config_fromfile_msgbox_content
                    cantretrieveconfigfromfile_title = en.cant_retrieve_config_fromfile_msgbox_title
                messagebox.showerror(cantretrieveconfigfromfile_title, cantretrieveconfigfromfile_content)
                self.destroy()
            
            try:
                self.rammappath_input.insert(INSERT, self.RetrieveConfig_Init['ProgConfig']['RAMMapPath'])
                self.adwcleanerwpath_input.insert(INSERT, self.RetrieveConfig_Init['ProgConfig']['ADWCLRPath'])
                self.winxpeapppath_input.insert(INSERT, self.RetrieveConfig_Init['ProgConfig']['WINXPEPATH'])
                self.cdpccpath_input.insert(INSERT, self.RetrieveConfig_Init['ProgConfig']['CDPCCPATH'])
                
                if str(self.RetrieveConfig_Init['ProgConfig']['appearancemode']) == '1':
                    self.appearance_chooser_combo.current(0)
                elif str(self.RetrieveConfig_Init['ProgConfig']['appearancemode']) == '2':
                    self.appearance_chooser_combo.current(1) # you get it using it's index according to 0
                
                if str(self.RetrieveConfig_Init['ProgConfig']['languagesetting']) == 'ar':
                    self.language_chooser_combo.current(0)
                elif str(self.RetrieveConfig_Init['ProgConfig']['languagesetting']) == 'en':
                    self.language_chooser_combo.current(1)
                
            except Exception as excpt_rtcore_retrieve:
                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    cantreadfromconfigfile_content = en.cant_read_config_frominside_file_msgbox_content
                    cantreadfromconfigfile_title = en.cant_read_config_frominside_file_msgbox_title
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    cantreadfromconfigfile_content = ar.cant_read_config_frominside_file_msgbox_content
                    cantreadfromconfigfile_title = ar.cant_read_config_frominside_file_msgbox_title
                else:
                    cantreadfromconfigfile_content = en.cant_read_config_frominside_file_msgbox_content
                    cantreadfromconfigfile_title = en.cant_read_config_frominside_file_msgbox_title
                messagebox.showerror(cantreadfromconfigfile_title, cantreadfromconfigfile_content)
                print(excpt_rtcore_retrieve)
                self.destroy()
            
            return None



        # It is the time to define the function used to save the changes to the configuration file "Config.ini"
        def SaveConfigurationandQuit():
            try:
                self.ConfigFileSaveProcess = configparser.ConfigParser()
                self.ConfigFileSaveProcess.read("Config.ini")
            except:
                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    cantopenconfigurationfile_content = en.cant_read_config_frominside_file_msgbox_content
                    cantopenconfigurationfile_title = en.cant_read_config_frominside_file_msgbox_title
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    cantopenconfigurationfile_content = ar.cant_read_config_frominside_file_msgbox_content
                    cantopenconfigurationfile_title = ar.cant_read_config_frominside_file_msgbox_title
                else:
                    cantopenconfigurationfile_content = en.cant_read_config_frominside_file_msgbox_content
                    cantopenconfigurationfile_title = en.cant_read_config_frominside_file_msgbox_title
                messagebox.showerror(cantopenconfigurationfile_title, cantopenconfigurationfile_content)
                self.destroy()

            # Second try.
            try:
                self.ConfigFileSaveProcess['ProgConfig']['RAMMapPath'] = self.rammappath_input.get()
                self.ConfigFileSaveProcess['ProgConfig']['ADWCLRPath'] = self.adwcleanerwpath_input.get()
                self.ConfigFileSaveProcess['ProgConfig']['WINXPEPATH'] = self.winxpeapppath_input.get()
                self.ConfigFileSaveProcess['ProgConfig']['CDPCCPATH'] = self.cdpccpath_input.get()

                print(str(self.appearance_chooser_combo.get()))
                if str(self.appearance_chooser_combo.get()) == "Dark":
                    self.ConfigFileSaveProcess['ProgConfig']['appearancemode'] = '2'
                elif str(self.appearance_chooser_combo.get()) == "Light":
                    self.ConfigFileSaveProcess['ProgConfig']['appearancemode'] = '1'
                else:
                    if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                        cantsaveconfig_combostyle_content = f"{en.cant_save_config_file_text} {self.appearance_chooser_combo}"
                        cantsaveconfig_combostyle_title = en.incorrect_choice_text
                    elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                        cantsaveconfig_combostyle_content = f"{self.appearance_chooser_combo} {ar.cant_save_config_file_text}"
                        cantsaveconfig_combostyle_title = ar.incorrect_choice_text
                    else:
                        cantsaveconfig_combostyle_content = f"{en.cant_save_config_file_text} {self.appearance_chooser_combo}"
                        cantsaveconfig_combostyle_title = en.incorrect_choice_text
                    messagebox.showerror(cantsaveconfig_combostyle_title, cantsaveconfig_combostyle_content)
                    sys.exit(75) # is for an incorrect theme mode.
                
                print(str(self.language_chooser_combo.get()))
                if str(self.language_chooser_combo.get()) == "العربية (مدعمة بواسطة حزمة اللغة العربية الاصدار 1.1)":
                    self.ConfigFileSaveProcess['ProgConfig']['languagesetting'] = 'ar'
                elif str(self.language_chooser_combo.get()) == "English":
                    self.ConfigFileSaveProcess['ProgConfig']['languagesetting'] = 'en'
                else:
                    if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                        cantsaveconfig_combostyle_content = f"{en.cant_save_config_file_text} {self.appearance_chooser_combo}"
                        cantsaveconfig_combostyle_title = en.incorrect_choice_text
                    elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                        cantsaveconfig_combostyle_content = f"{self.appearance_chooser_combo} {ar.cant_save_config_file_text}"
                        cantsaveconfig_combostyle_title = ar.incorrect_choice_text
                    else:
                        cantsaveconfig_combostyle_content = f"{en.cant_save_config_file_text} {self.appearance_chooser_combo}"
                        cantsaveconfig_combostyle_title = en.incorrect_choice_text
                    messagebox.showerror(cantsaveconfig_combostyle_title, cantsaveconfig_combostyle_content)
                    sys.exit(195) # is for an incorrect language choice.


                # Right now, I guess it is enough and we should rn write the configuration data to the file "Config.ini".
                with open("Config.ini", 'w') as self.ConfigFileProcessor:
                        self.ConfigFileSaveProcess.write(self.ConfigFileProcessor)


                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    save_changes_txt = en.done_reboot_for_changes_to_apply_text
                    save_changes_title = en.changes_saved_text
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    save_changes_txt = ar.done_reboot_for_changes_to_apply_text
                    save_changes_title = ar.changes_saved_text
                else:
                    save_changes_txt = en.done_reboot_for_changes_to_apply_text
                    save_changes_title = en.changes_saved_text
                # Defining the window which will tell the user that a reboot is needed to apply the changes.
                messagebox.showinfo(save_changes_title, save_changes_txt)

                # Okay, enough with that, let's destroy the main loop ok?
                self.destroy()
            except:
                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    cantsavechangestoconfigfile_content = en.unable_to_save_your_changes_text
                    cantsavechangestoconfigfile_title = en.cant_read_config_frominside_file_msgbox_title
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    cantsavechangestoconfigfile_content = ar.unable_to_save_your_changes_text
                    cantsavechangestoconfigfile_title = ar.cant_read_config_frominside_file_msgbox_title
                else:
                    cantsavechangestoconfigfile_content = en.unable_to_save_your_changes_text
                    cantsavechangestoconfigfile_title = en.cant_read_config_frominside_file_msgbox_title
                messagebox.showerror(cantsavechangestoconfigfile_title, cantsavechangestoconfigfile_content)
            
            return None

    
        # Defining the root properties.
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            title_settings = en.settings_window_title
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            title_settings = ar.settings_window_title
        else:
            title_settings = en.settings_window_title
        self.title(title_settings)
        self.geometry('1202x600')
        self.resizable(False,False)
        self.minsize(1202,600)
        self.maxsize(1202,600)

        try:
            self.iconbitmap("icon0.ico")
        except Exception as excpt672:
            messagebox.showerror("ERROR 1 in ICONBITMAP", f"Unable to load icon file for this window due to Exception:\n{excpt672}")
            pass
    
    
        self.configure(bg='#008aff')


        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            settings_lbl0_txt = en.settings_window_title
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            settings_lbl0_txt = ar.settings_window_title
        else:
            settings_lbl0_txt = en.settings_window_title
        # Defining some informative labels (Basically some bla bla blas).
        self.lbl0_config = Label(self, text=settings_lbl0_txt, font=("Arial Bold", 32), background='#008aff', foreground='white')
        self.lbl0_config.place(x=20, y=7)
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            settings_lbl1_txt = en.settings_hint_one
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            settings_lbl1_txt = ar.settings_hint_one
        else:
            settings_lbl1_txt = en.settings_hint_one
        self.lbl1_config = Label(self, text=settings_lbl1_txt, foreground='white', background='#008aff', font=("Arial", 12))
        self.lbl1_config.place(x=20, y=70)
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            settings_lbl2_txt = en.rammap_path_settings_hint
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            settings_lbl2_txt = ar.rammap_path_settings_hint
        else:
            settings_lbl2_txt = en.rammap_path_settings_hint
        self.lbl2_config = Label(self, text=settings_lbl2_txt, foreground='white', background='#008aff', font=("Arial",12))
        self.lbl2_config.place(x=20, y=100)
        self.rammappath_input = ttk.Entry(self, width=180)
        self.rammappath_input.place(x=20, y=130)
        self.rammappath_input_browsebtn = ttk.Button(self, text="...", command=BrowseOne)
        self.rammappath_input_browsebtn.place(x=1108, y=131, relwidth=0.027, relheight=0.033)
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            settings_lbl3_txt = en.adwcleaner_working_path_settings_hint
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            settings_lbl3_txt = ar.adwcleaner_working_path_settings_hint
        else:
            settings_lbl3_txt = en.adwcleaner_working_path_settings_hint
        self.lbl3_config = Label(self, text=settings_lbl3_txt, foreground='white', background='#008aff', font=("Arial",12))
        self.lbl3_config.place(x=20, y=155)
        self.adwcleanerwpath_input = ttk.Entry(self, width=180)
        self.adwcleanerwpath_input.place(x=20, y=180)
        self.adwcleanerwpath_input_browsebtn = ttk.Button(self, text="...", command=BrowseTwo)
        self.adwcleanerwpath_input_browsebtn.place(x=1108, y=180, relwidth=0.027, relheight=0.033)
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            settings_lbl4_txt = en.winxpe_prog_path_settings_hint
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            settings_lbl4_txt = ar.winxpe_prog_path_settings_hint
        else:
            settings_lbl4_txt = en.winxpe_prog_path_settings_hint
        self.lbl4_config = Label(self, text=settings_lbl4_txt, foreground='white', background='#008aff', font=("Arial", 12))
        self.lbl4_config.place(x=20, y=205)
        self.winxpeapppath_input = ttk.Entry(self, width=180)
        self.winxpeapppath_input.place(x=20, y=230)
        self.winxpeapppath_input_browsebtn = ttk.Button(self, text="...", command=BrowseThree)
        self.winxpeapppath_input_browsebtn.place(x=1108, y=230, relwidth=0.027, relheight=0.033)
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            settings_lbl5_txt = en.userid_folder_winactivitiescache_settings_hint
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            settings_lbl5_txt = ar.userid_folder_winactivitiescache_settings_hint
        else:
            settings_lbl5_txt = en.userid_folder_winactivitiescache_settings_hint
        self.lbl5_config = Label(self, text=settings_lbl5_txt, foreground='white', background='#008aff', font=("Arial",12))
        self.lbl5_config.place(x=20, y=257)
        self.cdpccpath_input = ttk.Entry(self, width=180)
        self.cdpccpath_input.place(x=20, y=283)
        self.cdpccpath_input_browsebtn = ttk.Button(self, text="...", command=BrowseFour)
        self.cdpccpath_input_browsebtn.place(x=1108, y=283, relwidth=0.027, relheight=0.033)
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            settings_lbl6_txt = en.appearance_mode_settings_hint
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            settings_lbl6_txt = ar.appearance_mode_settings_hint
        else:
            settings_lbl6_txt = en.appearance_mode_settings_hint
        self.lbl6_config = Label(self, text=settings_lbl6_txt, foreground='white', background='#008aff', font=("Arial", 12))
        self.lbl6_config.place(x=20, y=310)
        self.appearance_chooser_combo = ttk.Combobox(self)
        self.appearance_chooser_combo['values'] = ('Light', 'Dark')
        self.appearance_chooser_combo.place(x=20, y=335, relheight=0.050, relwidth=0.936)

        self.lbl7_config = Label(self, text="Choose your language/اختار لغتك:", foreground='white', background='#008aff', font=("Arial", 12))
        self.lbl7_config.place(x=20, y=370)
        self.language_chooser_combo = ttk.Combobox(self)
        self.language_chooser_combo['values'] = ("العربية (مدعمة بواسطة حزمة اللغة العربية الاصدار 1.1)", "English")
        self.language_chooser_combo.place(relheight=0.050, relwidth=0.936, x=20, y=396)
        
        # defining the copyright window button.
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            license_show_btn_txt = en.license_window_title
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            license_show_btn_txt = ar.license_window_title
        else:
            license_show_btn_txt = en.license_window_title
        self.showcpyrights_windowbtn = ttk.Button(self, text=license_show_btn_txt, command=showLicenseWindow)
        self.showcpyrights_windowbtn.place(relwidth=0.30, relheight=0.060, x=410, y=550)

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            quit_btn_txt = en.quit_settings_btn
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            quit_btn_txt = ar.quit_settings_btn
        else:
            quit_btn_txt = en.quit_settings_btn

        self.closewindow_btn = atk.Button3d(self, text=quit_btn_txt, command=SelfDestroy)
        self.closewindow_btn.place(x=20, y=550, relwidth=0.30, relheight=0.060)

        # Tonight I'd fly, and be your lover.
        # Yeah, Yeah, Yeah....

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            apply_andquit_btn_txt = en.commit_changes_plus_exit_btn
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            apply_andquit_btn_txt = ar.commit_changes_plus_exit_btn
        else:
            apply_andquit_btn_txt = en.commit_changes_plus_exit_btn
        self.applychangesandclose_btn = atk.Button3d(self, text=apply_andquit_btn_txt, command=SaveConfigurationandQuit)
        self.applychangesandclose_btn.place(x=800, y=550, relwidth=0.30, relheight=0.060)

        # Gas Gas Gas.
        # I'm gonna run in the flash.
        # Tonight I will fight, to be the winner.

        # lbl6_config = Label(ConfigRoot, text="License : ", font=("Arial Bold", 20), foreground='white', background='#008aff')
        # lbl6_config.place(x=200, y=400) 
        # I no longer want the user to see license in the main window of the settings thing.



        # Calling the function to retrieve the configuration information from the config.ini file.
        RetrieveConfig()

        # Calling the ConfigRoot's Mainloop (Used to allow the user to interact to the window freely)
        # ConfigRoot.mainloop()
    
        



class LicenseWindow(Tk):
    def __init__(self):
        super().__init__()
        global font_size, GetConfig
        # defining a new toplevel widget to show the program's license on.
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            title = en.license_window_title
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            title = ar.license_window_title
        else:
            title = en.license_window_title
        self.title(title)
        self.geometry('640x480')
        self.minsize(640, 480)
        self.resizable(True, True)
        
        def decrFontSize(keybinding_arg):
            """
            This function decreases the font size of the text in the window (TopLevel widget) `licenseShow`

            This function is a part of the "Minimal Accessibility Pack" for Temp_Cleaner GUI
            """
            global font_size
            if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                warn_txt = en.warning_cant_decrease_more_msgbox
                warn_title = en.cant_decrease_more_msgbox_title
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                warn_txt = ar.warning_cant_decrease_more_msgbox
                warn_title = ar.cant_decrease_more_msgbox_title
            else:
                warn_txt = en.warning_cant_decrease_more_msgbox
                warn_title = en.cant_decrease_more_msgbox_title
            
            # checking if font size is equal to 4.
            if int(font_size) == 4:
                messagebox.showerror(warn_title, warn_txt)
                return False
            else:
                font_size = font_size - 1
                self.showLicenseStext.configure(font=("Arial", font_size))
                return None
            
            print("Decrease font size")
            return None


        def incrFontSize(keybinding_arg):
            """
            This function increases the font size of the text in the window (TopLevel widget) `licenseShow`

            This function is a part of the "Minimal Accessibility Pack" for Temp_Cleaner GUI
            """
            global font_size

            # checking if font size is 100.
            if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                warn_txt = en.warning_cant_increase_more
                warn_title = en.cant_increase_more_msgbox_title
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                warn_txt = ar.warning_cant_increase_more
                warn_title = ar.cant_increase_more_msgbox_title
            else:
                warn_txt = en.warning_cant_increase_more
                warn_title = en.cant_increase_more_msgbox_title
            
            if int(font_size) == 100:
                messagebox.showerror(warn_title, warn_txt)
                return False
            else:
                font_size = font_size + 1
                self.showLicenseStext.configure(font=("Arial", font_size))
                return None
            

            # print("Increase font size")
            return None


        def showHelp(keybinding_arg):
            messagebox.showinfo(en.help_on_using_minimal_accessibility_pack_msgbox_title, en.minimal_accessibility_pack_help)

            return None



        # attempting to change the iconbitmap of the show license window.
        try:
            self.iconbitmap("icon0.ico")
            pass
        except Exception as excpt0:
            messagebox.showerror("Error @ LICENSESHOW WINDOW", f"{excpt0}")
            pass
        


        # defining the scrolledtext.ScrolledText widget that holds everything in the license text.
        self.showLicenseStext = scrolledtext.ScrolledText(self, font=("Arial", font_size), foreground='black', selectbackground='#009cda', selectforeground='black', state='disabled', cursor='arrow')
        self.showLicenseStext.pack(expand=1, fill="both")

        # adding license text to that widget.
        self.showLicenseStext.configure(state='normal')
        self.showLicenseStext.delete(1.0, END)
        self.showLicenseStext.insert(END, """License for the project Temp_Cleaner GUI release 1.1 and all releases of it : 

A simple program made to help you erase temporary files in your Windows-based PC.
Copyright (C) 2021 - Insertx2k Dev (Mr.X) or The X Software Foundation

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
        self.showLicenseStext.configure(state='disabled')



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


if __name__ == '__main__':
    main_process = MainWindowLightMode()
    main_process.mainloop()

            
        
            
    # # if program was executed as a Python 3.xx.x Script file.
    # main_process = MainWindowLightMode()
    # main_process.mainloop()
    
