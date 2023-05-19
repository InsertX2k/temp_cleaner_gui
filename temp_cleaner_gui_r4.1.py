"""
The Project Temp_Cleaner GUI by Insertx2k Dev.
A simple temporary folders cleaning solution made by Insertx2k Dev under the GNU General Public License
That will help you free up a lot of disk space in your computer through erasing all the Temporary folders
Exist in almost all temporary folders directories either in your C:\ drive (Windows drive) or other drives. 
~~Uses the same environment variables as in the version 1.32, except a renewed GUI.~~ - That no longer happens.
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

        # self.configure(background='white')

        try:
            self.login = os.getlogin()
            if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                WindowNewTitle = f"The Temp_Cleaner GUI Project (v4.1) (Windows) Running On: {self.login}'s PC (Powered by Minimal Accessibility Pack v1.0)"
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                WindowNewTitle = f"(مدعم بواسطة حزمة ادوات امكانية الوصول الأدني الاصدار 1.0) (مدعم بواسطة حزمة اللغة العربية الاصدار 1.0) {self.login} الإصدار 4.1 يعمل علي جهاز  Temp_Cleaner GUI مشروع "
            else:
                WindowNewTitle = f"The Temp_Cleaner GUI Project (v4.1) (Windows) Running On: {self.login}'s PC (Powered by Minimal Accessibility Pack v1.0)"
            self.title(WindowNewTitle)
        except Exception as excpt129:
            if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                WindowNewTitle = "The Temp_Cleaner GUI Project (v4.1) (Windows) (Powered by Minimal Accessibility Pack v1.0)"
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                WindowNewTitle = "(مدعم بواسطة حزمة ادوات امكانية الوصول الأدني الاصدار 1.0) (مدعم بواسطة حزمة اللغة العربية الاصدار 1.0)  الإصدار 4.1 Temp_Cleaner GUI مشروع "
            else:
                WindowNewTitle = "The Temp_Cleaner GUI Project (v4.1) (Windows) (Powered by Minimal Accessibility Pack v1.0)"
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


        # main_canvas.configure(background='black')
        # main_frame.configure(background='black')
        # self.show_frame.configure(background='black')
        # Defining some informative labels inside of the Temp_Cleaner GUI's Window.
        # self.banner = PhotoImage(file="banner.png")
        # self.banner_show = Label(self.show_frame, image=self.banner, width=1200, height=300)
        # self.banner_show.grid(column=0, row=1, sticky='w')
        # Defining a sample get var functionaking a new checkbox.
        # Defining the ON-OFF Like variable
        for i in range(0,65):
            setattr(self, f"var{i}", StringVar())
        # Defining the checkbox button.

        # setting the proper language pack for the program's UI.
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text0 = "Recycle Bin Cleanup"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text0 = "منظف سلة المهملات"
        else:
            text0 = "Recycle Bin Cleanup"

        self.lblframe0 = ttk.Labelframe(self.show_frame, text=text0)
        # --------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text1 = "Empty Systemdrive Recycle Bin"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text1 = "تنظيف سلة مهملات قرص النظام"
        else:
            text1 = "Empty Systemdrive Recycle Bin"

        self.clr_recyclebin_sysdrive_btn = ttk.Checkbutton(self.lblframe0, text=text1, variable=self.var0, onvalue="1", offvalue="0", command=None)
        self.clr_recyclebin_sysdrive_btn.grid(column=0, row=3, sticky='w')

        # ---------------------------
        self.lblframe0.grid(column=0, row=2, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text2 = "DirectX Shader Cache Cleanup (Win 10/11 Only)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text2 = "تنظيف ذاكرة التخزين المؤقتة الخاصة بDirectX Shader"
        else:
            text2 = "DirectX Shader Cache Cleanup (Win 10/11 Only)"

        self.lblframe1 = ttk.Labelframe(self.show_frame, text=text2)
        # ---------------------------
        self.clr_d3dscache_localappdata_btn = ttk.Checkbutton(self.lblframe1, text=text2, variable=self.var2, onvalue="1", offvalue="0", command=None)
        self.clr_d3dscache_localappdata_btn.grid(column=0, row=5, sticky='w')
        # ---------------------------
        self.lblframe1.grid(column=0, row=4, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text3 = "System and User Specific Cleaners"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text3 = "منظف ملفات النظام الغير ضرورية وملفات المستخدم الخاصة الغير ضرورية"
        else:
            text3 = "System and User Specific Cleaners"
        

        self.lblframe2 = ttk.Labelframe(self.show_frame, text=text3)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text4 = "Clean PrefetchW Files"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text4 = "منظف ملفات برنامج PrefetchW"
        else:
            text4 = "Clean PrefetchW Files"
        
        self.clr_prefetchw_windir_btn = ttk.Checkbutton(self.lblframe2, text=text4, variable=self.var1, onvalue="1", offvalue="0", command=None)
        self.clr_prefetchw_windir_btn.grid(column=0, row=7, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text5 = "Erase User Clipboard Content (Excluding Content you Copy and paste)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text5 = "تفريغ محتوي الحافظة (لا يتضمن المحتوي الذي تنسخه وتلصقه)"
        else:
            text5 = "Erase User Clipboard Content (Excluding Content you Copy and paste)"
        
        self.clr_usrclipboard_content_btn = ttk.Checkbutton(self.lblframe2, text=text5, variable=self.var9, onvalue="1", offvalue="0", command=None)
        self.clr_usrclipboard_content_btn.grid(column=0, row=8, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text6 = "Erase Windows Temporary Files"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text6 = "مسح الملفات المؤقتة الخاصة بنظام ويندوز الغير ضرورية"
        else:
            text6 = "Erase Windows Temporary Files"
        self.clr_windir_temp_btn = ttk.Checkbutton(self.lblframe2, text=text6, variable=self.var3, onvalue="1", offvalue="0", command=None)
        self.clr_windir_temp_btn.grid(column=0, row=9, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text7 = "Erase User Temporary Files"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text7 = "مسح الملفات المؤقتة الخاصة بالمستخدم الغير ضرورية"
        else:
            text7 = "Erase User Temporary Files"
        self.clr_localappdata_temp_btn = ttk.Checkbutton(self.lblframe2, text=text7, variable=self.var4, onvalue="1", offvalue="0", command=None)
        self.clr_localappdata_temp_btn.grid(column=0, row=10, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text8 = "Clean Default User Temporary Files"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text8 = "مسح الملفات المؤقتة الخاصة بالمستخدم الإفتراضي الغير ضرورية"
        else:
            text8 = "Clean Default User Temporary Files"
        self.clr_default_usr_appdata_temp_btn = ttk.Checkbutton(self.lblframe2, text=text8, variable=self.var7, onvalue="1", offvalue="0", command=None)
        self.clr_default_usr_appdata_temp_btn.grid(column=0, row=11, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text9 = "Clean IE (Internet Explorer) Cached data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text9 = "مسح ملفات متصفح مستكشف الإنترنت المؤقتة"
        else:
            text9 = "Clean IE (Internet Explorer) Cached data"
        self.clr_inet_cached_data_btn = ttk.Checkbutton(self.lblframe2, text=text9, variable=self.var8, onvalue="1", offvalue="0", command=None)
        self.clr_inet_cached_data_btn.grid(column=0, row=12, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text10 = "Clean Windows Explorer Thumbnails Cached Data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text10 = "مسح ملفات مستكشف الويندوز الخاصة بالصور المصغرة"
        else:
            text10 = "Clean Windows Explorer Thumbnails Cached Data"
        self.clr_msexplorer_thumbcacheddata_btn = ttk.Checkbutton(self.lblframe2, text=text10, variable=self.var10, onvalue="1", offvalue="0", command=None)
        self.clr_msexplorer_thumbcacheddata_btn.grid(column=0, row=13, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text11 = "Clean User Recent Documents List"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text11 = "محو قائمة اخر ملفات تم فتحها"
        else:
            text11 = "Clean User Recent Documents List"
        self.clr_winrecentdocs_list_btn = ttk.Checkbutton(self.lblframe2, text=text11, variable=self.var11, onvalue="1", offvalue="0", command=None)
        self.clr_winrecentdocs_list_btn.grid(column=0, row=14, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text12 = "Clean Local Low Temporary Files"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text12 = "محو ملفات التخزين المؤقتة الخاصة بالمستخدم Local Low"
        else:
            text12 = "Clean Local Low Temporary Files"

        self.clr_locallow_temporary_data_btn = ttk.Checkbutton(self.lblframe2, text=text12, variable=self.var41, onvalue="1", offvalue="0", command=None)
        self.clr_locallow_temporary_data_btn.grid(column=0, row=15, sticky='w')
        # ---------------------------
        self.lblframe2.grid(column=0, row=6, sticky='w')


        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text13 = "Web Browser Cleaners"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text13 = "تنظيف متصفحات الإنترنت"
        else:
            text13 = "Web Browser Cleaners"

        self.lblframe3 = ttk.Labelframe(self.show_frame, text=text13)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text14 = "Clean Google Chrome Browser Webcached data (Incl. GPUCache, Code Cache)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text14 = "تنظيف ملفات متصفح جوجل كروم المؤقتة (يتضمن ملفات وحدة معالجة الرسوميات المؤقتة وملفات التعليمات البرمجية)"
        else:
            text14 = "Clean Google Chrome Browser Webcached data (Incl. GPUCache, Code Cache)"
        self.clr_gchrome_webcache_incl_gpucache_codecache_btn = ttk.Checkbutton(self.lblframe3, text=text14, variable=self.var5, onvalue="1", offvalue="0", command=None)
        self.clr_gchrome_webcache_incl_gpucache_codecache_btn.grid(column=0, row=17, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text15 = "Clean Google Chrome Browser Cookies (Incl. Cookies-journal)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text15 = "تنظيف ملفات الكعكات الخاصة بمتصفح جوجل كروم"
        else:
            text15 = "Clean Google Chrome Browser Cookies (Incl. Cookies-journal)"
        self.clr_gchrome_browser_cookies_btn = ttk.Checkbutton(self.lblframe3, text=text15, variable=self.var6, onvalue="1", offvalue="0", command=None)
        self.clr_gchrome_browser_cookies_btn.grid(column=0, row=18, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text16 = "Clean Google Chrome Browser Extension Cookie Data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text16 = "تنظيف ملفات الكعكات الخاصة بالمكونات الإضافية الخاصة بمتصفح جوجل كروم"
        else:
            text16 = "Clean Google Chrome Browser Extension Cookie Data"
        self.clr_gchrome_extension_cookies_data_btn = ttk.Checkbutton(self.lblframe3, text=text16, variable=self.var33, onvalue="1", offvalue="0", command=None)
        self.clr_gchrome_extension_cookies_data_btn.grid(column=0, row=19, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text17 = "Clean Steam Webclient HTML Cached data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text17 = "تنظيف الملفات المؤقتة الخاصة ببرنامج Steam"
        else:
            text17 = "Clean Steam Webclient HTML Cached data"
        self.clr_steam_webclient_htmlcache_btn = ttk.Checkbutton(self.lblframe3, text=text17, variable=self.var14, onvalue="1", offvalue="0", command=None)
        self.clr_steam_webclient_htmlcache_btn.grid(column=0, row=20, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text18 = "Clean Discord Webclient Webcached data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text18 = "تنظيف الملفات المؤقتة الخاصة ببرنامج الديسكورد"
        else:
            text18 = "Clean Discord Webclient Webcached data"
        self.clr_discordwebclient_webcacheddata_btn = ttk.Checkbutton(self.lblframe3, text=text18, variable=self.var12, onvalue="1", offvalue="0", command=None)
        self.clr_discordwebclient_webcacheddata_btn.grid(column=0, row=21, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text19 = "Clean Chromium-based Microsoft Edge Webcached data (Incl. GPUCache, Code cache)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text19 = "(code cache المؤقتة و gpu يتضمن ملفات) تنظيف الملفات المؤقتة الخاصة بمتصفح ادجي المبني علي كروميم "
        else:
            text19 = "Clean Chromium-based Microsoft Edge Webcached data (Incl. GPUCache, Code cache)"
        self.clr_chromiumbased_msedge_webcached_data_btn = ttk.Checkbutton(self.lblframe3, text=text19, variable=self.var24, onvalue="1", offvalue="0", command=None)
        self.clr_chromiumbased_msedge_webcached_data_btn.grid(column=0, row=22, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text20 = "Clean Chromium-based Microsoft Edge Cookie data (Incl. Cookies-journal)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text20 = "محو الكعكات الخاصة بمتصفح ادجي المبني علي كروميم"
        else:
            text20 = "Clean Chromium-based Microsoft Edge Cookie data (Incl. Cookies-journal)"
        self.clr_chormiumbased_msedge_cookies_data_btn = ttk.Checkbutton(self.lblframe3, text=text20, variable=self.var25, onvalue="1", offvalue="0", command=None)
        self.clr_chormiumbased_msedge_cookies_data_btn.grid(column=0, row=23, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text21 = "Clean Mozilla Firefox Webcached data (Incl. cache2, jumpListCache, and Shader Cache)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text21 = "Mozilla Firefox محو الملفات المؤقتة الخاصة بمتصفح "
        else:
            text21 = "Clean Mozilla Firefox Webcached data (Incl. cache2, jumpListCache, and Shader Cache)"
        self.clr_mozilla_firefox_webcached_data_btn = ttk.Checkbutton(self.lblframe3, text=text21, variable=self.var59, onvalue="1", offvalue="0", command=None)
        self.clr_mozilla_firefox_webcached_data_btn.grid(column=0, row=24, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text22 = "Clean Mozilla Firefox browser Cookie data (it is just a Sqlite file)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text22 = "Mozilla Firefox محو الكعكات الخاصة بمتصفح "
        else:
            text22 = "Clean Mozilla Firefox browser Cookie data (it is just a Sqlite file)"
        self.clr_mozilla_firefox_cookies_sqlite_file_btn = ttk.Checkbutton(self.lblframe3, text=text22, variable=self.var60, onvalue="1", offvalue="0", command=None)
        self.clr_mozilla_firefox_cookies_sqlite_file_btn.grid(column=0, row=25, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text23 = "Clean Discord Windows Client Squirrel Temp"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text23 = "الخاصة ببرنامج الديسكورد Squirrel Temp مسح ملفات"
        else:
            text23 = "Clean Discord Windows Client Squirrel Temp"
        self.clr_discordapp_squirrel_temp_data_btn = ttk.Checkbutton(self.lblframe3, text=text23, variable=self.var40, onvalue="1", offvalue="0", command=None)
        self.clr_discordapp_squirrel_temp_data_btn.grid(column=0, row=26, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text24 = "Clean Internet Explorer Cookies Data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text24 = "مسح الكعكات الخاصة بمتصفح مستكشف الإنترنت"
        else:
            text24 = "Clean Internet Explorer Cookies Data"
        self.clr_inetcookies_btn = ttk.Checkbutton(self.lblframe3, text=text24, variable=self.var17, onvalue="1", offvalue="0", command=None)
        self.clr_inetcookies_btn.grid(column=0, row=27, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text25 = "Clean Internet Explorer Additional Cached Data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text25 = "مسح الملفات المؤقتة الزائدة الخاصة بمتصفح مستكشف الإنترنت"
        else:
            text25 = "Clean Internet Explorer Additional Cached Data"
        self.clr_additionalinet_cacheddata_btn = ttk.Checkbutton(self.lblframe3, text=text25, variable=self.var18, onvalue="1", offvalue="0", command=None)
        self.clr_additionalinet_cacheddata_btn.grid(column=0, row=28, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text26 = "Clean Internet Explorer Downloads History Data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text26 = "محو سجل التنزيلات الخاصة بمتصفح مستكشف الإنترنت"
        else:
            text26 = "Clean Internet Explorer Downloads History Data"
        self.clr_iedownload_history_data_btn = ttk.Checkbutton(self.lblframe3, text=text26, variable=self.var19, onvalue="1", offvalue="0", command=None)
        self.clr_iedownload_history_data_btn.grid(column=0, row=29, sticky='w')
        # ---------------------------
        self.lblframe3.grid(column=0, row=16, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text27 = "Photo Editors Cleanup"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text27 = "منظفات برامج تعديل الصور"
        else:
            text27 = "Photo Editors Cleanup"

        self.lblframe4 = ttk.Labelframe(self.show_frame, text=text27)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text28 = "Clean GNU Image Manipulation Program's Temporary data (gimp's tmps)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text28 = "المؤقتة GNU Image Manipulation Program محو ملفات برنامج"
        else:
            text28 = "Clean GNU Image Manipulation Program's Temporary data (gimp's tmps)"
        self.clr_gimpstmps_btn = ttk.Checkbutton(self.lblframe4, text=text28, variable=self.var13, onvalue="1", offvalue="0", command=None)
        self.clr_gimpstmps_btn.grid(column=0, row=31, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text29 = "Clean GNU Image Manipulation Program Recent Documents List (GIMP)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text29 = "GNU Image Manipulation Program محو قائمة الملفات المفتوحة مؤخرا في برنامج"
        else:
            text29 = "Clean GNU Image Manipulation Program Recent Documents List (GIMP)"
        self.clr_gimp_recentdocs_btn = ttk.Checkbutton(self.lblframe4, text=text29, variable=self.var47, onvalue="1", offvalue="0", command=None)
        self.clr_gimp_recentdocs_btn.grid(column=0, row=32, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text30 = "Clean Adobe Photoshop 2020 Webcached data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text30 = "محو ملفات الإنترنت المؤقتة الخاصة ببرنامج فوتوشوب 2020"
        else:
            text30 = "Clean Adobe Photoshop 2020 Webcached data"
        self.clr_adobephotoshop_webcached_data_btn = ttk.Checkbutton(self.lblframe4, text=text30, variable=self.var27, onvalue="1", offvalue="0", command=None)
        self.clr_adobephotoshop_webcached_data_btn.grid(column=0, row=33, sticky='w')
        # ---------------------------
        self.lblframe4.grid(column=0, row=30, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text31 = "Microsoft Windows Update Cleaners"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text31 = "منظفات برنامج تحديث الويندوز"
        else:
            text31 = "Microsoft Windows Update Cleaners"

        self.lblframe5 = ttk.Labelframe(self.show_frame, text=text31)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text32 = "Clean all Windows Update's Downloaded Update Files"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text32 = "مسح جميع الملفات التي تم تنزيلها بواسطة برنامج تحديث الويندوز"
        else:
            text32 = "Clean all Windows Update's Downloaded Update Files"
        self.clr_windowsupdate_downloaded_updates_btn = ttk.Checkbutton(self.lblframe5, text=text32, variable=self.var15, onvalue="1", offvalue="0", command=None)
        self.clr_windowsupdate_downloaded_updates_btn.grid(column=0, row=35, sticky='w')
        # ---------------------------
        self.lblframe5.grid(column=0, row=34, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text33 = "Windows 10/11 only Cleaners"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text33 = "منظفات خاصة بنظامي ويندوز 10 و ويندوز 11 فقط"
        else:
            text33 = "Windows 10/11 only Cleaners"

        self.lblframe6 = ttk.Labelframe(self.show_frame, text=text33)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text34 = "Clean Windows 10/11 Operating System Cached Data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text34 = "تنظيف ملفات نظامي التشغيل ويندوز 10 او ويندوز 11 المؤقتة"
        else:
            text34 = "Clean Windows 10/11 Operating System Cached Data"
        self.clr_win10os_cached_data_btn = ttk.Checkbutton(self.lblframe6, text=text34, variable=self.var16, onvalue="1", offvalue="0", command=None)
        self.clr_win10os_cached_data_btn.grid(column=0, row=37, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text35 = "Clean Windows 10/11 Action Center/Notifications Center Cached data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text35 = "تنظيف ملفات مركز الإشعارات المؤقتة"
        else:
            text35 = "Clean Windows 10/11 Action Center/Notifications Center Cached data"
        self.clr_win10_action_center_cached_data_btn = ttk.Checkbutton(self.lblframe6, text=text35, variable=self.var20, onvalue="1", offvalue="0", command=None)
        self.clr_win10_action_center_cached_data_btn.grid(column=0, row=38, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text36 = "Clean Windows 10/11 Modern Applications Cached data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text36 = "تنظيف الملفات المؤقتة الخاصة ببرامج ويندوز 10 او 11 الحديثة"
        else:
            text36 = "Clean Windows 10/11 Modern Applications Cached data"
        self.clr_winappux_cached_data_btn = ttk.Checkbutton(self.lblframe6, text=text36, variable=self.var21, onvalue="1", offvalue="0", command=None)
        self.clr_winappux_cached_data_btn.grid(column=0, row=39, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text37 = "Clean Microsoft Store Based Edge Web cached data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text37 = "تنظيف ملفات الانترنت المؤقتة الخاصة بمتصفح ميكروسوفت ادجي نسخة متجر ويندوز"
        else:
            text37 = "Clean Microsoft Store Based Edge Web cached data"
        self.clr_msstore_based_edge_webcached_data_btn = ttk.Checkbutton(self.lblframe6, text=text37, variable=self.var22, onvalue="1", offvalue="0", command=None)
        self.clr_msstore_based_edge_webcached_data_btn.grid(column=0, row=40, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text38 = "Clean Additional Windows Explorer Thumbnails Cached Data (thumbcachetodelete)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text38 = "(thumbcachetodelete) تنظيف ملفات الصور المصغرة الإضافية الخاصة ببرنامج مستكشف الويندوز"
        else:
            text38 = "Clean Additional Windows Explorer Thumbnails Cached Data (thumbcachetodelete)"
        self.clr_winexplorer_thumbcache_to_delete_files_btn = ttk.Checkbutton(self.lblframe6, text=text38, variable=self.var23, onvalue="1", offvalue="0", command=None)
        self.clr_winexplorer_thumbcache_to_delete_files_btn.grid(column=0, row=41, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text39 = "Clean Windows 10/11 Cryptnet URL Cached data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text39 = "المؤقتة في نظامي ويندوز11 و10 Cryptnet URL تنظيف ملفات مسار "
        else:
            text39 = "Clean Windows 10/11 Cryptnet URL Cached data"
        self.clr_cryptnet_urlcache_data_btn = ttk.Checkbutton(self.lblframe6, text=text39, variable=self.var30, onvalue="1", offvalue="0", command=None)
        self.clr_cryptnet_urlcache_data_btn.grid(column=0, row=42, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text40 = "Clean Windows 10/11 ConnectedDevicesPlatform Cached Data (Requires you to set it's path in Settings)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text40 = "الخاصة بنظامي ويندوز 10و 11 (مطلوب تعيين مسارها في الضبط) ConnectedDevicesPlatform تنظيف ملفات "
        else:
            text40 = "Clean Windows 10/11 ConnectedDevicesPlatform Cached Data (Requires you to set it's path in Settings)"
        self.clr_connecteddevicesplatform_win10_cached_data_btn = ttk.Checkbutton(self.lblframe6, text=text40, variable=self.var34, onvalue="1", offvalue="0", command=None)
        self.clr_connecteddevicesplatform_win10_cached_data_btn.grid(column=0, row=43, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text41 = "Clean Elevated Diagnostics Data folder (Only for Windows 10/11)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text41 = "تنظيف الملفات المؤقتة لبرنامج التشخيصات العليا (ويندوز 10 و 11 فقط)"
        else:
            text41 = "Clean Elevated Diagnostics Data folder (Only for Windows 10/11)"
        self.clr_elevated_diagnostics_data_btn = ttk.Checkbutton(self.lblframe6, text=text41, variable=self.var42, onvalue="1", offvalue="0", command=None)
        self.clr_elevated_diagnostics_data_btn.grid(column=0, row=44, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text42 = "Clean IdentityNexusIntegration Folder contents (Only for Windows 10/11)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text42 = "(ويندوز 10و 11 فقط) IdentityNexusIntegration تنظيف محتويات المجلد "
        else:
            text42 = "Clean IdentityNexusIntegration Folder contents (Only for Windows 10/11)"
        self.clr_identitynexus_integration_folder_btn = ttk.Checkbutton(self.lblframe6, text=text42, variable=self.var49, onvalue="1", offvalue="0", command=None)
        self.clr_identitynexus_integration_folder_btn.grid(column=0, row=45, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text43 = "Clean ServiceHub Identity file (that salt file)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text43 = "(ملف salt) ServiceHub تنظيف ملف الهوية الشخصية لبرنامج "
        else:
            text43 = "Clean ServiceHub Identity file (that salt file)"
        self.clr_servicehub_identity_file_btn = ttk.Checkbutton(self.lblframe6, text=text43, variable=self.var56, onvalue="1", offvalue="0", command=None)
        self.clr_servicehub_identity_file_btn.grid(column=0, row=46, sticky='w')
        # ---------------------------
        self.lblframe6.grid(column=0, row=36, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text44 = "Games Cleaner"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text44 = "منظفات الالعاب"
        else:
            text44 = "Games Cleaner"
        self.lblframe7 = ttk.Labelframe(self.show_frame, text=text44)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text45 = "Clean ROBLOX Game Downloaded Textures/Data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text45 = "محو جميع القوام المحملة بواسطة لعبة روبلوكس"
        else:
            text45 = "Clean ROBLOX Game Downloaded Textures/Data"
        self.clr_roblox_game_downloads_btn = ttk.Checkbutton(self.lblframe7, text=text45, variable=self.var26, onvalue="1", offvalue="0", command=None)
        self.clr_roblox_game_downloads_btn.grid(column=0, row=48, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text46 = "Clean ROBLOX Game Verbosed Log files"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text46 = "محو جميع ملفات السجلات المطولة للعبة روبلوكس"
        else:
            text46 = "Clean ROBLOX Game Verbosed Log files"
        self.clr_roblox_game_log_files_btn = ttk.Checkbutton(self.lblframe7, text=text46, variable=self.var51, onvalue="1", offvalue="0", command=None)
        self.clr_roblox_game_log_files_btn.grid(column=0, row=49, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text47 = "Clean Axolot Games Scrap Mechanic Workshop Items Cached data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text47 = "Axolot Games Scrap Mechanic محو جميع الملفات المؤقتة لعناصر لعبة "
        else:
            text47 = "Clean Axolot Games Scrap Mechanic Workshop Items Cached data"
        self.clr_scrapmechanic_axolot_games_workshop_items_cached_data_btn = ttk.Checkbutton(self.lblframe7, text=text47, variable=self.var50, onvalue="1", offvalue="0", command=None)
        self.clr_scrapmechanic_axolot_games_workshop_items_cached_data_btn.grid(column=0, row=50, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text48 = "Clean Minecraft Webcached data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text48 = "Minecraft مسح ذاكرة التخزين المؤقتة الخاصة بمتصفح الإنترنت الموجود بلعبة "
        else:
            text48 = "Clean Minecraft Webcached data"
        self.clr_minecraft_webcached_data_btn = ttk.Checkbutton(self.lblframe7, text=text48, variable=self.var58, onvalue="1", offvalue="0", command=None)
        self.clr_minecraft_webcached_data_btn.grid(column=0, row=51, sticky='w')
        # ---------------------------
        self.lblframe7.grid(column=0, row=47, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text49 = "Python Cleaners"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text49 = "منظفات بايثون"
        else:
            text49 = "Python Cleaners"

        self.lblframe8 = ttk.Labelframe(self.show_frame, text=text49)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text50 = "Clean Python PIP Cached Data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text50 = "المؤقتة pip محو ملفات بايثون "
        else:
            text50 = "Clean Python PIP Cached Data"
        self.clr_python_pip_cached_data_btn = ttk.Checkbutton(self.lblframe8, text=text50, variable=self.var31, onvalue="1", offvalue="0", command=None)
        self.clr_python_pip_cached_data_btn.grid(column=0, row=53, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text51 = "Clean Pyinstaller Bin Cached Data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text51 = "Pyinstaller محو جميع بيانات برنامج "
        else:
            text51 = "Clean Pyinstaller Bin Cached Data"
        self.clr_pyinstaller_temporary_data_btn = ttk.Checkbutton(self.lblframe8, text=text51, variable=self.var45, onvalue="1", offvalue="0", command=None)
        self.clr_pyinstaller_temporary_data_btn.grid(column=0, row=54, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text52 = "Clean Jedi Python Additional Temporary Data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text52 = "بايثون المؤقتة Jedi محو جميع ملفات "
        else:
            text52 = "Clean Jedi Python Additional Temporary Data"
        self.clr_jedipython_additionals_btn = ttk.Checkbutton(self.lblframe8, text=text52, variable=self.var46, onvalue="1", offvalue="0", command=None)
        self.clr_jedipython_additionals_btn.grid(column=0, row=55, sticky='w')
        # ---------------------------
        self.lblframe8.grid(column=0, row=52, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text53 = "RAM Cleaners"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text53 = "منظفات ذاكرة الوصول العشوائي"
        else:
            text53 = "RAM Cleaners"

        self.lblframe9 = ttk.Labelframe(self.show_frame, text=text53)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text54 = "Empty Running Software Workingsets using RAMMap"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text54 = "RAMMap تفريغ الذاكرة عن طريق مسح مجموعات العمل للبرامج الفعالة بإستخدام "
        else:
            text54 = "Empty Running Software Workingsets using RAMMap"
        self.empty_winworkingsets_rammap_btn = ttk.Checkbutton(self.lblframe9, text=text54, variable=self.var32, onvalue="1", offvalue="0", command=None)
        self.empty_winworkingsets_rammap_btn.grid(column=0, row=57, sticky='w')
        # ---------------------------
        self.lblframe9.grid(column=0, row=56, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text55 = "Video Editing Software Cleaners"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text55 = "منظفات برامج تعديل الفيديوهات (المونتاج)"
        else:
            text55 = "Video Editing Software Cleaners"

        self.lblframe10 = ttk.Labelframe(self.show_frame, text=text55)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text56 = "Clean Sony VEGAS Pro 17 Temporary data and log files"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text56 = "Sony VEGAS Pro 17 مسح جميع الملفات المؤقتة وملفات السجل لبرنامج "
        else:
            text56 = "Clean Sony VEGAS Pro 17 Temporary data and log files"
        self.clr_sony_vegas_pro_temp_and_logs_data_btn = ttk.Checkbutton(self.lblframe10, text=text56, variable=self.var28, onvalue="1", offvalue="0", command=None)
        self.clr_sony_vegas_pro_temp_and_logs_data_btn.grid(column=0, row=59, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text57 = "Clean Sony VEGAS Pro ERROR Reports files"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text57 = "Sony VEGAS Pro مسح جميع ملفات تقارير الاخطاء الخاصة ببرنامج "
        else:
            text57 = "Clean Sony VEGAS Pro ERROR Reports files"
        self.clr_sony_vegas_pro_error_reports_data_btn = ttk.Checkbutton(self.lblframe10, text=text57, variable=self.var61, onvalue="1", offvalue="0", command=None)
        self.clr_sony_vegas_pro_error_reports_data_btn.grid(column=0, row=60, sticky='w')
        # ---------------------------
        self.lblframe10.grid(column=0, row=58, sticky='w')


        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text58 = "3D Moduling Software Cleaners"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text58 = "منظفات برامج تعديل النماذج ثلاثية الابعاد"
        else:
            text58 = "3D Moduling Software Cleaners"
        self.lblframe11 = ttk.Labelframe(self.show_frame, text=text58)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text59 = "Clean McNeel Rhinoceros 3D Moduling Software Temporary Data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text59 = "McNeel Rhinoceros مسح الملفات المؤقتة الخاصة ببرنامج "
        else:
            text59 = "Clean McNeel Rhinoceros 3D Moduling Software Temporary Data"
        self.clr_mcneel_rhinoceros_3d_moduling_soft_cached_data_btn = ttk.Checkbutton(self.lblframe11, text=text59, variable=self.var29, onvalue="1", offvalue="0", command=None)
        self.clr_mcneel_rhinoceros_3d_moduling_soft_cached_data_btn.grid(column=0, row=62, sticky='w')
        # ---------------------------
        self.lblframe11.grid(column=0, row=61, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text60 = "Additional Software Cleaners"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text60 = "منظفات إضافية لبعض البرامج"
        else:
            text60 = "Additional Software Cleaners"

        self.lblframe12 = ttk.Labelframe(self.show_frame, text=text60)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text61 = "Clean Icon Cache file in Local app data folder"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text61 = "مجلد Local app data مسح ملف التخزين المؤقت للرموز الموجود في "
        else:
            text61 = "Clean Icon Cache file in Local app data folder"
        self.clr_iconcache_db_file_in_localappdata_dir_btn = ttk.Checkbutton(self.lblframe12, text=text61, variable=self.var35, onvalue="1", offvalue="0", command=None)
        self.clr_iconcache_db_file_in_localappdata_dir_btn.grid(column=0, row=64, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text62 = "Clean Microvirt MEmu Logs and Memory Dump Files"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text62 = "Microvirt MEmu مسح ملفات السجل وملفات اخطاء الذاكرة الخاصة ببرنامج "
        else:
            text62 = "Clean Microvirt MEmu Logs and Memory Dump Files"
        self.clr_microvirt_memu_log_data_memdump_files_btn = ttk.Checkbutton(self.lblframe12, text=text62, variable=self.var36, onvalue="1", offvalue="0", command=None)
        self.clr_microvirt_memu_log_data_memdump_files_btn.grid(column=0, row=65, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text63 = "Clean Malwarebytes Adware Cleaner Log data and its files"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text63 = "Malwarebytes Adware Cleaner مسح ملفات سجل برنامج "
        else:
            text63 = "Clean Malwarebytes Adware Cleaner Log data and its files"
        self.clr_adwcleaner_log_files_btn = ttk.Checkbutton(self.lblframe12, text=text63, variable=self.var37, onvalue="1", offvalue="0", command=None)
        self.clr_adwcleaner_log_files_btn.grid(column=0, row=66, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text64 = "Clean the folder Perflogs in Systemdrive volume"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text64 = "في قرص النظام Perflogs مسح ملفات المجلد "
        else:
            text64 = "Clean the folder Perflogs in Systemdrive volume"
        self.clr_perflogs_in_systemdrive_btn = ttk.Checkbutton(self.lblframe12, text=text64, variable=self.var38, onvalue="1", offvalue="0", command=None)
        self.clr_perflogs_in_systemdrive_btn.grid(column=0, row=67, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text65 = "Clean Android Cached data in your computer"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text65 = "المتروكة عند توصيل جهاز اندرويد بالكمبيوتر الخاص بك Android مسح ملفات نظام "
        else:
            text65 = "Clean Android Cached data in your computer"
        self.clr_dotcache_folder_in_userprofile_path_btn = ttk.Checkbutton(self.lblframe12, text=text65, variable=self.var39, onvalue="1", offvalue="0", command=None)
        self.clr_dotcache_folder_in_userprofile_path_btn.grid(column=0, row=68, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text66 = "Clean VMware Downloads (All files downloaded by all VMware Software)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text66 = "VMware مسح جميع الملفات التي تم تنزيلها بواسطة برامج "
        else:
            text66 = "Clean VMware Downloads (All files downloaded by all VMware Software)"
        self.clr_vmware_downloads_folder_btn = ttk.Checkbutton(self.lblframe12, text=text66, variable=self.var43, onvalue="1", offvalue="0", command=None)
        self.clr_vmware_downloads_folder_btn.grid(column=0, row=69, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text67 = "Clean BalenaItcher webcached data (Incl. GPUCache, Code Cache, Local Storage, Session Storage)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text67 = "BalenaItcher مسح ملفات التخزين المؤقت الخاصة ببرنامج "
        else:
            text67 = "Clean BalenaItcher webcached data (Incl. GPUCache, Code Cache, Local Storage, Session Storage)"
        self.clr_balena_itcher_webcached_data_btn = ttk.Checkbutton(self.lblframe12, text=text67, variable=self.var44, onvalue="1", offvalue="0", command=None)
        self.clr_balena_itcher_webcached_data_btn.grid(column=0, row=70, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text68 = "Clean LowLevelFormatTool (LLFT) License Agreement Confirmation File"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text68 = "LowLevelFormatTool (LLFT) مسح ملف قبول إتفاقية برنامج "
        else:
            text68 = "Clean LowLevelFormatTool (LLFT) License Agreement Confirmation File"
        self.clr_lowlevelformattool_licenseagreement_confirmationfile_btn = ttk.Checkbutton(self.lblframe12, text=text68, variable=self.var48, onvalue="1", offvalue="0", command=None)
        self.clr_lowlevelformattool_licenseagreement_confirmationfile_btn.grid(column=0, row=71, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text69 = "Clean WinXPE Creator Downloads Diretory (Requires you to set it's path on Settings)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text69 = "(يتطلب تعيين مسارها في الضبط) WinXPE Creator مسح جميع الملفات التي تم تنزيلها بواسطة الاداة "
        else:
            text69 = "Clean WinXPE Creator Downloads Diretory (Requires you to set it's path on Settings)"
        self.clr_winxpe_app_downloads_folder_btn = ttk.Checkbutton(self.lblframe12, text=text69, variable=self.var55, onvalue="1", offvalue="0", command=None)
        self.clr_winxpe_app_downloads_folder_btn.grid(column=0, row=72, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text70 = "Clean Huawei HiSuite Log data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text70 = "Huawei HiSuite مسح ملفات سجلات برنامج "
        else:
            text70 = "Clean Huawei HiSuite Log data"
        self.clr_huawei_hisuite_log_data_btn = ttk.Checkbutton(self.lblframe12, text=text70, variable=self.var57, onvalue="1", offvalue="0", command=None)
        self.clr_huawei_hisuite_log_data_btn.grid(column=0, row=73, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text71 = "Clean Huawei HiSuite Drag 'n' Drop Temporary Data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text71 = "Huawei HiSuite مسح جميع الملفات المؤقتة لخاصية السحب والإفلات لبرنامج "
        else:
            text71 = "Clean Huawei HiSuite Drag 'n' Drop Temporary Data"
        self.clr_huawei_hisuite_dnd_temp_btn = ttk.Checkbutton(self.lblframe12, text=text71, variable=self.var63, onvalue="1", offvalue="0", command=None)
        self.clr_huawei_hisuite_dnd_temp_btn.grid(column=0, row=74, sticky='w')
        # ---------------------------
        self.lblframe12.grid(column=0, row=63, sticky='w')


        
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text72 = "Microsoft Visual Studio Code Cleaners"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text72 = "Microsoft Visual Studio Code منظفات برنامج "
        else:
            text72 = "Microsoft Visual Studio Code Cleaners"
        self.lblframe13 = ttk.Labelframe(self.show_frame, text=text72)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text73 = "Clean Microsoft Visual Studio Code Webcached data (Incl. GPUCache, Code Cache, CachedData, Cache paths)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text73 = "(GPUCache, Code Cache, CachedData, Cache paths يتضمن ) Microsoft Visual Studio Code تنظيف الملفات المؤقتة الخاصة ببرنامج "
        else:
            text73 = "Clean Microsoft Visual Studio Code Webcached data (Incl. GPUCache, Code Cache, CachedData, Cache paths)"
        self.clr_vscode_webcached_data_btn = ttk.Checkbutton(self.lblframe13, text=text73, variable=self.var52, onvalue="1", offvalue="0", command=None)
        self.clr_vscode_webcached_data_btn.grid(column=0, row=76, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text74 = "Clean Microsoft Visual Studio Code Cookie data (Incl. Cookies-journal)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text74 = "Microsoft Visual Studio Code مسح كعكات برنامج "
        else:
            text74 = "Clean Microsoft Visual Studio Code Cookie data (Incl. Cookies-journal)"
        self.clr_vscode_cookie_data_btn = ttk.Checkbutton(self.lblframe13, text=text74, variable=self.var53, onvalue="1", offvalue="0", command=None)
        self.clr_vscode_cookie_data_btn.grid(column=0, row=77, sticky='w')
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text75 = "Clean Microsoft Visual Studio Code Cached Extensions Data (Incl. VSIXs)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text75 = "(VSIXs يتضمن ) Microsoft Visual Studio Code مسح الملفات المؤقتة الخاصة بالإضافات الخاصة ببرنامج "
        else:
            text75 = "Clean Microsoft Visual Studio Code Cached Extensions Data (Incl. VSIXs)"
        self.clr_vscode_cached_extensions_data_btn = ttk.Checkbutton(self.lblframe13, text=text75, variable=self.var54, onvalue="1", offvalue="0", command=None)
        self.clr_vscode_cached_extensions_data_btn.grid(column=0, row=78, sticky='w')
        # ---------------------------
        self.lblframe13.grid(column=0, row=75, sticky='w')


        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text76 = "Java Deployment Cache Cleaner"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text76 = "منظفات توظيف الجافا"
        else:
            text76 = "Java Deployment Cache Cleaner"

        self.lblframe14 = ttk.Labelframe(self.show_frame, text=text76)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text77 = "Clean Java Deployment Cached Data"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text77 = "مسح ملفات توظيف الجافا المؤقتة"
        else:
            text77 = "Clean Java Deployment Cached Data"
        self.clr_java_deployment_cached_data_btn = ttk.Checkbutton(self.lblframe14, text=text77, variable=self.var62, onvalue="1", offvalue="0", command=None)
        self.clr_java_deployment_cached_data_btn.grid(column=0, row=80, sticky='w')
        # ---------------------------
        self.lblframe14.grid(column=0, row=79, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text78 = "All done?"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text78 = "هل انتهيت؟"
        else:
            text78 = "All done?"
        self.lblframe15 = ttk.Labelframe(self.show_frame, text=text78)
        # ---------------------------
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            text79 = "Do you want to close this program when it's done with cleaning up temp?"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            text79 = "هل تريد ان يقوم هذا البرنامج بإغلاق نفسه تلقائيا عقب إنتهائه من التنظيف؟"
        else:
            text79 = "Do you want to close this program when it's done with cleaning up temp?"
        self.destroy_activity_after_done_btn = ttk.Checkbutton(self.lblframe15, text=text79, variable=self.var64, onvalue="1", offvalue="0", command=None, cursor='hand2')
        self.destroy_activity_after_done_btn.grid(column=0, row=82, sticky='w')
        # ---------------------------
        self.lblframe15.grid(column=0, row=81, sticky='w')


        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            about_btn_text = "About"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            about_btn_text = "حول هذا البرنامج"
        else:
            about_btn_text = "About"
        # Defining the about button.
        self.about_window_btn = ttk.Button(self.show_frame, text=about_btn_text, command=self.show_about_window, cursor='hand2')
        self.about_window_btn.place(x=10, y=2000, relwidth=0.3, relheight=0.035)
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            self.begin_cleaning_btn_text = "Execute"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            self.begin_cleaning_btn_text = "ابدأ بالتنظيف"
        else:
            self.begin_cleaning_btn_text = "Execute"
        # Defining the execute button.
        self.exec_btn = ttk.Button(self.show_frame, text=self.begin_cleaning_btn_text, command=self.execute_theprogram, cursor='hand2')
        self.exec_btn.place(x=400 ,y=2000, relwidth=0.3, relheight=0.035)

        # declaring a space.
        self.space = Label(self.show_frame, text="", font=("Arial Bold", 50))
        if str(GetConfig['ProgConfig']['appearancemode']) == '2':
            self.space.configure(background=atk.DEFAULT_COLOR)
        self.space.grid(column=0, row=83, sticky='w')

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            go_settings_btn_text = "Settings"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            go_settings_btn_text = "الضبط"
        else:
            go_settings_btn_text = "Settings"
        # Defining the go to configuration page button.
        self.config_page_btn = ttk.Button(self.show_frame, text=go_settings_btn_text, command=self.StartConfigurationWindow, cursor='hand2')
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
                warn_txt = "Is your eyesight really that low?, If yes, Then I'm sorry I can't help you anymore."
                warn_title = "Increase font size"
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                warn_txt = "هل مستوي نظرك ضعيف لهذه الدرجة؟، اسف لا يمكنني مساعدتك"
                warn_title = "تكبير الكتابة في الشاشة"
            else:
                warn_txt = "Is your eyesight really that low?, If yes, Then I'm sorry I can't help you anymore."
                warn_title = "Increase font size"

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
                warn_txt = "Is your computer's screen really that big?, If yes, Then I'm sorry I can't help you anymore."
                warn_title = "Decrease font size"
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                warn_txt = "هل شاشة الحاسب لديك حقا بهذا الكبر؟، إذا نعم لا يمكنني مساعدتك"
                warn_title = "تصغير الكتابة في الشاشة"
            else:
                warn_txt = "Is your computer's screen really that big?, If yes, Then I'm sorry I can't help you anymore."
                warn_title = "Decrease font size"

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
                msg_box_txt = """Minimal Accessibility Pack v1.0 is here!
You can enjoy using your favorite Mr.X software, even if you have any problems either with your computer's screen or with your eyesight.

To increase the font size, You can do "Control + I"
To decrease the font size, You can do "Control + D"

And thank you for choosing Mr.X's Software!

Powered by Minimal Accessibility Pack v1.0 by Insertx2k Dev (Mr.X).
"""
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                msg_box_txt = """حزمة ادوات إمكانية الوصول الأدني موجودة في هذه النسخة!
يمكنك الان الاستمتاع بإستخدام برامج مستر اكس الرسمية، حتي إن كنت تعاني من اي نوع من المشاكل إما في شاشة الحاسوب الخاص بك او مستوي نظرك

"Control + I" لتكبير الخط، يمكنك الضغط علي الزرين 
"Control + D" لتصغير الخط، يمكنك الضغط علي الزرين 

وشكرا لإختيارك لبرمجيات مستر اكس!
"""
            else:
                msg_box_txt = """Minimal Accessibility Pack v1.0 is here!
You can enjoy using your favorite Mr.X software, even if you have any problems either with your computer's screen or with your eyesight.

To increase the font size, You can do "Control + I"
To decrease the font size, You can do "Control + D"

And thank you for choosing Mr.X's Software!

Powered by Minimal Accessibility Pack v1.0 by Insertx2k Dev (Mr.X).
"""

            if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                msg_box_title = "Help on using Minimal Accessibility Pack v1.0"
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                msg_box_title = "المساعدة في إستخدام حزمة إمكانية الوصول الإدني الاصدار 1.0"
            else:
                msg_box_title = "Help on using Minimal Accessibility Pack v1.0"

            messagebox.showinfo(msg_box_title, msg_box_txt)

            return None


        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            console_output_hint_txt = "Console Output"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            console_output_hint_txt = "إخراج وحدة التحكم"
        else:
            console_output_hint_txt = "Console Output"
        self.lblframe16 = ttk.Labelframe(self.show_frame, text=console_output_hint_txt)
        # ------------------------
        # Creating a scrolledtext widget.
        self.output_show = scrolledtext.ScrolledText(self.lblframe16, cursor='arrow', foreground='white', selectbackground='#009cda', selectforeground='black' ,state='disabled', font=("Courier New", font_size), width=106, background='black')
        self.output_show.pack(fill=BOTH, expand=1)
        # disabling the state of the output_show widget to prevent the GUI from glitching
        self.output_show.configure(state='disabled')
        # ------------------------
        self.lblframe16.grid(column=0, row=85, sticky='w')


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
        # self.bind("<F1>", showHelp) -> causes the messagebox.showinfo help to appear twice.


    # Defining the function used to show the user the about window of the program.
    def show_about_window(self):
        global GetConfig
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            about_window_txt = """The Temp_Cleaner GUI Project by Insertx2k Dev\n
Version 4.1
Written by Insertx2k Dev (Mr.X)
Support Twitter : @insertplayztw
Support Github : InsertX2k
This release of Temp_Cleaner GUI is powered by "Minimal Accessibility Pack v1.0" by Insertx2k Dev (Mr.X).
\n
GitHub page : https://github.com/insertx2k/temp_cleaner_gui
Better UI GitHub page : https://insertx2k.github.io/temp_cleaner_gui
\n
This program is Free Software (FOSS), You are allowed to modify or redistribute it under the terms of GNU General Public License v2.0 or later @ Free Software Foundation.
"""
            about_window_title = "About 'The Temp_Cleaner GUI Project (v4.1)'"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            about_window_txt = """The Temp_Cleaner GUI Project من Insertx2k Dev\n
الإصدار 4.1
تمت كتابته بواسطة: Insertx2k Dev (Mr.X)
تويتر الدعم: @insertplayztw
Github الدعم: InsertX2k
مدعمة بواسطة حزمة ادوات امكانية الوصول الإدني الاصدار 1.0 Temp_Cleaner GUI هذه النسخة من برنامج 
\n
GitHub صفحة : https://github.com/insertx2k/temp_cleaner_gui
صفحة ذو وجهة افضل : https://insertx2k.github.io/temp_cleaner_gui
\n
GNU General Public License v2.0 او احدث @ Free Software Foundation. هذا البرنامج هو برنامج مفتوح المصدر، وهذا يعني انه لديك الحق في ان تقوم بالتعديل عليه او إعادة توزيعه وفقا لشروط رخصة 
"""
            about_window_title = "حول 'The Temp_Cleaner GUI Project (v4.1)'"
        else:
            about_window_txt = """The Temp_Cleaner GUI Project by Insertx2k Dev\n
Version 4.1
Written by Insertx2k Dev (Mr.X)
Support Twitter : @insertplayztw
Support Github : InsertX2k
This release of Temp_Cleaner GUI is powered by "Minimal Accessibility Pack v1.0" by Insertx2k Dev (Mr.X).
\n
GitHub page : https://github.com/insertx2k/temp_cleaner_gui
Better UI GitHub page : https://insertx2k.github.io/temp_cleaner_gui
\n
This program is Free Software (FOSS), You are allowed to modify or redistribute it under the terms of GNU General Public License v2.0 or later @ Free Software Foundation.
"""
            about_window_title = "About 'The Temp_Cleaner GUI Project (v4.1)'"


        messagebox.showinfo(about_window_title,about_window_txt)

        return None

    # Defining the function to execute the following selected commands : 
    def execute_theprogram(self):
        self.ShowNotificationDone = True
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            new_btn_text = "Executing"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            new_btn_text = "جاري التنظيف..."
        else:
            new_btn_text = "Executing"
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
                btn0_txt = "After you delete all Downloaded files by the Windows Update Service you should restart the whole service to commit changes you did to it\nWould you like to restart the Windows Update Service?"
                btn0_title = "Restart Windows Update Service"
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                btn0_txt = "بعد مسح جميع الملفات التي تم تحميلها بواسطة برنامج ترقية ويندوز يجب عليك إعادة تشغيل الخدمة الخاصة به لتطبيق التعديلات التي اتممتها عليه\nهل تود إعادة تشغيل خدمة ترقية ويندوز؟"
                btn0_title = "إعادة تشغيل خدمة برنامج ترقية ويندوز"
            else:
                btn0_txt = "After you delete all Downloaded files by the Windows Update Service you should restart the whole service to commit changes you did to it\nWould you like to restart the Windows Update Service?"
                btn0_title = "Restart Windows Update Service"
            self.reboot_uwp = messagebox.askquestion(btn0_title, btn0_txt)
            if self.reboot_uwp == "yes":
                self.self_2 = Tk()
                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    title_txt = "Restart Windows Update Service"
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    title_txt = "إعادة تشغيل خدمة ترقية ويندوز"
                else:
                    title_txt = "Restart Windows Update Service"
                self.self_2.title(title_txt)
                self.self_2.geometry('500x90')
                self.self_2.resizable(False,False)


                try:
                    self.self_2.iconbitmap("icon0.ico")
                except Exception as excpt24:
                    messagebox.showerror("ERROR 1 in ICONBITMAP process", f"Unable to load the icon file for this window due to Exception:\n{excpt24}")
                    pass

                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    lbl0_txt = "Restarting Windows Update Service..."
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    lbl0_txt = "جاري إعادة تشغيل خدمة ترقية ويندوز..."
                else:
                    lbl0_txt = "Restarting Windows Update Service..."
                # Defining some labels used to show the user that something is happening inside.
                self.lbl0x = Label(self.self_2, text=lbl0_txt, font=("Arial", 19))
                self.lbl0x.place(x=25 ,y=20)
                # Defining the actions used to restart the Windows update service.
                self.process = subprocess.getoutput('net start wuauserv')
                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    lbl1_txt = "Windows Update Service Has been successfully restarted!"
                    lbl2_txt_additionals = "Done restarting the Windows Update Service!"
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    lbl1_txt = "تمت إعادة تشغيل خدمة ترقية ويندوز"
                    lbl2_txt_additionals = "تمت إعادة تشغيل خدمة ترقية ويندوز"
                else:
                    lbl1_txt = "Windows Update Service Has been successfully restarted!"
                    lbl2_txt_additionals = "Done restarting the Windows Update Service!"
                # Defining the commands used to show the user that all pending operations has been successfully completed!
                messagebox.showinfo(title_txt, lbl1_txt)
                # Defining the mainloop destroy once the execution is done.
                self.self_2.destroy()
                self.self_2.mainloop()
                messagebox.showinfo(title_txt, lbl2_txt_additionals)
            else:
                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    msgbox_rwup_title = "Restart Windows Update Service"
                    msgbox_rwup_content = "Expect your device to have problems with Windows Update if you didn't restart it as soon as possible then."
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    msgbox_rwup_title = "إعادة تشغيل خدمة ترقية ويندوز"
                    msgbox_rwup_content = "توقع ان تواجه مشاكل في استخدام خدمة ترقية ويندوز"
                else:
                    msgbox_rwup_title = "Restart Windows Update Service"
                    msgbox_rwup_content = "Expect your device to have problems with Windows Update if you didn't restart it as soon as possible then."
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
                msgbox_msstoreedge_title = "Clean Store-based MS Edge Cached Data"
                msgbox_msstoreedge_content = "Cleaning Store-based MS Edge cached data can not be done automatically, which means you are supposed to do that manually, which will make this tool open an explorer (Windows Explorer) window for you showing you the folder where you are supposed to clean MS-Store-Based EDGE Webcache data\nPlease keep in mind that you shouldn't leave the directory opened to you by this tool\nSo do you wish to processed?"
                msgbox_msstoreedge_content2 = "Opening the directory for you\nDon't forget to look for the folder Microsoft.MicrosoftEdge_[a random number], and go inside the AC folder inside of it, you will then be able to see all MS Store-based edge webcached data."
                done_txt = "Done!"
                canceled_by_user_txt = "Operation canceled by the user."
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                msgbox_msstoreedge_title = "مسح الملفات المؤقتة الخاصة بمتصفح ميكروسوفت ادجي نسخة متجر ويندوز"
                msgbox_msstoreedge_content = "تنظيف ملفات متصفح ميكروسوفت ادجي المؤقتة لا يمكن ان تتم بشكل تلقائي بل يجب عليك ان تقوم بها بنفسك، مما يعني انه سوف يتم فتح نافذة مستكشف ويندوز جديدة لك بها المسار الصحيح الذي يجب عليك البحث فيه عن تلك الملفات\nبرجاء الوضع في الحسبان انه لايجب عليك الرجوع للخلف عن المسار المفتوح لك بواسطة هذه الاداة\nهل تود المتابعة؟"
                msgbox_msstoreedge_content2 = "يتم فتح المسار من اجلك\nلا تنسي البحث عن المجلد Microsoft.MicrosoftEdge_[رقم عشوائي], ومن ثم ادخل في المجلد AC, سوف تجد فيه جميع الملفات المؤقتة لمتصفح ميكروسوفت ادجي نسخة متجر الويندوز"
                done_txt = "تم!"
                canceled_by_user_txt = "تمت مقاطعة العملية بواسطة المستخدم"
            else:
                msgbox_msstoreedge_title = "Clean Store-based MS Edge Cached Data"
                msgbox_msstoreedge_content = "Cleaning Store-based MS Edge cached data can not be done automatically, which means you are supposed to do that manually, which will make this tool open an explorer (Windows Explorer) window for you showing you the folder where you are supposed to clean MS-Store-Based EDGE Webcache data\nPlease keep in mind that you shouldn't leave the directory opened to you by this tool\nSo do you wish to processed?"
                msgbox_msstoreedge_content2 = "Opening the directory for you\nDon't forget to look for the folder Microsoft.MicrosoftEdge_[a random number], and go inside the AC folder inside of it, you will then be able to see all MS Store-based edge webcached data."
                done_txt = "Done!"
                canceled_by_user_txt = "Operation canceled by the user."
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
                msgbox_eraserammap_title = "Empty Windows Workingsets"
                msgbox_eraserammap_content = "Would you really like to run RAMMap by Sysinternals to empty RAM Workingsets?"
                msgbox_confirm_defaultpath_txt = "The path of the RAMMap tool is set to '$DEFAULT', Continuing using the default configured RAMMap path."
                msgbox_confirm_defaultpath_title = "Notification"
                msgbox_commandsent_txt = "RAMMap.exe - Command sent."
                msgbox_operationcanceledbyuser_txt = "Operation has been canceled."
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                msgbox_eraserammap_title = "تفريغ مجموعات العمل الخاصة بنظام ويندوز"
                msgbox_eraserammap_content = "لتفريغ مجموعات العمل الخاصة بالبرامج التي تستهلك ذاكرة الوصول العشوائي؟ RAMMap من Sysinternals هل تريد حقا تشغيل البرنامج "
                msgbox_confirm_defaultpath_txt = "RAMMap سوف يتم المتابعة بإستخدام المسار الإفتراضي المعين لأداة  ، '$DEFAULT' تم تعيينه إلي  RAMMap مسار المجلد الذي يحتوي علي الاداة "
                msgbox_confirm_defaultpath_title = "إشعار"
                msgbox_commandsent_txt = "RAMMap.exe - تم إرسال الامر."
                msgbox_operationcanceledbyuser_txt = "تم إلغاء الامر."
            else:
                msgbox_eraserammap_title = "Empty Windows Workingsets"
                msgbox_eraserammap_content = "Would you really like to run RAMMap by Sysinternals to empty RAM Workingsets?"
                msgbox_confirm_defaultpath_txt = "The path of the RAMMap tool is set to '$DEFAULT', Continuing using the default configured RAMMap path."
                msgbox_confirm_defaultpath_title = "Notification"
                msgbox_commandsent_txt = "RAMMap.exe - Command sent."
                msgbox_operationcanceledbyuser_txt = "Operation has been canceled."
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
                    you_didnt_specify_path_wacc_txt = "You didn't specify a custom location for the Windows activites cache cleaner to work on, Continuing using the Default values."
                    notification_2 = "Notification"
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    you_didnt_specify_path_wacc_txt = "لم تقم بتعيين اي مسار مخصص لكي يستخدمه منظف الملفات المؤقتة الخاصة بنشاطات الويندوز،المتابعة بإستخدام القيم الإفتراضية"
                    notification_2 = "إشعار"
                else:
                    you_didnt_specify_path_wacc_txt = "You didn't specify a custom location for the Windows activites cache cleaner to work on, Continuing using the Default values."
                    notification_2 = "Notification"
                messagebox.showinfo(notification_2, you_didnt_specify_path_wacc_txt)
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\ConnectedDevicesPlatform"&erase /s /f /q "ee2999716b7783e6"')
                self.output_show.insert(END, f"\n {self.process}")
            else:
                self.process = subprocess.getoutput(rf' cd /d "%localappdata%\\ConnectedDevicesPlatform"&erase /s /f /q "{self.CDPCCPATH_var}"')
                self.output_show.insert(END, f"\n {self.process}")
        self.selection37 = self.var35.get()
        if self.selection37 == '1':
            if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                clr_iconcache_dialogtxt = "Cleaning IconCache.db file can not be done automatically, which means the user is premitted to do that manually, all what you have to do is just deleting the file iconcache.db in the directory we will open to you\nDo you wish to processed?"
                clr_iconcache_dialogtitle = "Clean icon cache"
                clr_iconcache_databasefile_done = "Done!"
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                clr_iconcache_dialogtxt = "هل تود المتابعة؟ \n في المسار الذي سوف نقوم بفتحه لك  IconCache.db لا يمكن ان يتم تلقائيا، لهذا السبب يجب عليك اتمامه بنفسك، كل ما عليك فعله هو مسح الملف  IconCache.db مسح الملف"
                clr_iconcache_dialogtitle = "محو ذاكرة التخزين المؤقتة للرموز"
                clr_iconcache_databasefile_done = "تم!"
            else:
                clr_iconcache_dialogtxt = "Cleaning IconCache.db file can not be done automatically, which means the user is premitted to do that manually, all what you have to do is just deleting the file iconcache.db in the directory we will open to you\nDo you wish to processed?"
                clr_iconcache_dialogtitle = "Clean icon cache"
                clr_iconcache_databasefile_done = "Done!"
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
                    notification_3 = "Notification"
                    nocustom_pathforadwclr_content = "You didn't specify a custom working location for the AdwareCleaner Cleaner, Continuing using the default path."
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    notification_3 = "إشعار"
                    custom_pathforadwclr_content = "سوف يستمر بإستخدام المسار الإفتراضي ، AdwareCleaner انت لم تقم بتحديد مسار مخصص لملفات البرنامج "
                else:
                    notification_3 = "Notification"
                    custom_pathforadwclr_content = "You didn't specify a custom working location for the AdwareCleaner Cleaner, Continuing using the default path."
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
                    error_title = "An ERROR has occured"
                    error_content_nopathforwinxpe = "You didn't specify the path of the 'WinXPE' program, The cleaner can't continue."
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    error_title = "لقد حدث خطأ بسيط"
                    error_content_nopathforwinxpe = "المنظف لا يستطيع الإستمرار ، 'WinXPE' انت لم تقم بوصف مسار تواجد برنامج "
                else:
                    error_title = "An ERROR has occured"
                    error_content_nopathforwinxpe = "You didn't specify the path of the 'WinXPE' program, The cleaner can't continue."
                messagebox.showinfo(error_title, error_content_nopathforwinxpe)
            else:
                self.process = subprocess.getoutput(rf' erase /s /f /q "{self.WINXPEPATH_var}\Temp"')
                self.output_show.insert(END, f"\n {self.process}")
                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    notify_title = "Note"
                    notify_content = "You will need to redownload all downloaded data by the tool for the exporting phase to be done!"
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    notify_title = "ملحوظة"
                    notify_content = "يجب عليك إعادة تحميل كل الملفات المحملة بواسطة هذه الاداة لكي تكتمل مرحلة التصدير"
                else:
                    notify_title = "Note"
                    notify_content = "You will need to redownload all downloaded data by the tool for the exporting phase to be done!"
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
            ShowNotificationDone = False
            self.destroy()
        # Sleeping a bit for longer (or equal) to 5 seconds.
        time.sleep(1)

        try:
            # Ok, let's revert everything back to what it was before.
            self.exec_btn.configure(text=self.begin_cleaning_btn_text, command=self.execute_theprogram)
        except TclError as tkerr:
            pass


        return None

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
                    cantretrieveconfigfromfile_content = "Unable to retrieve the configuration information, this can be due to a hard exception, or a something else, the settings window will close."
                    cantretrieveconfigfromfile_title = "Runtime Exception"
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    cantretrieveconfigfromfile_content = "خطأ في الحصول علي المعلومات من الضبط، هذا قد يكون بسبب خطأ كارثي او شئ اخر، شاشة الضبط سوف تغلق"
                    cantretrieveconfigfromfile_title = "حدث خطأ في وقت التشغيل"
                else:
                    cantretrieveconfigfromfile_content = "Unable to retrieve the configuration information, this can be due to a hard exception, or a something else, the settings window will close."
                    cantretrieveconfigfromfile_title = "Runtime Exception"
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
                    cantreadfromconfigfile_content = "Unable to read the configuration file from your computer, please make sure to give this program a permission to read files in your hard disk if blocked by your antivirus software and try again, The settings window will close."
                    cantreadfromconfigfile_title = "A runtime exception"
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    cantreadfromconfigfile_content = "غير قادر علي قراءة ملف الضبط من جهازك، برجاء التأكد من إعطاء هذا البرنامج الإذن الكافي لقراءة الملفات من وحدة التخزين إذا تم حظره بواسطة برنامج مضاد الفيروسات و حاول مرة اخري، شاشة الضبط سوف تغلق"
                    cantreadfromconfigfile_title = "حدث خطأ في وقت التشغيل"
                else:
                    cantreadfromconfigfile_content = "Unable to read the configuration file from your computer, please make sure to give this program a permission to read files in your hard disk if blocked by your antivirus software and try again, The settings window will close."
                    cantreadfromconfigfile_title = "A runtime exception"
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
                    cantopenconfigurationfile_content = "Unable to open the configuration file on your computer, please make sure to give this program enough permissions to do so, and if your antivirus blocks it, please give it access and try again."
                    cantopenconfigurationfile_title = "A runtime exception"
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    cantopenconfigurationfile_content = "غير قادر علي فتح ملف الضبط الموجود في جهاز الكمبيوتر الخاص بك، برجاء التأكد من إعطاء هذا البرنامج الاذونات الكافية لإتمام هذا الامر، وإذا كان برنامج مكافح الفيروسات في جهازك يمنع هذا، برجاء إعطاءه الإذن وإعادة المحاولة"
                    cantopenconfigurationfile_title = "حدث خطأ في وقت التشغيل"
                else:
                    cantopenconfigurationfile_content = "Unable to open the configuration file on your computer, please make sure to give this program enough permissions to do so, and if your antivirus blocks it, please give it access and try again."
                    cantopenconfigurationfile_title = "A runtime exception"
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
                        cantsaveconfig_combostyle_content = f"Can't save the configuration file with the choice {self.appearance_chooser_combo}"
                        cantsaveconfig_combostyle_title = "Incorrect choice"
                    elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                        cantsaveconfig_combostyle_content = f"{self.appearance_chooser_combo} لا يمكن حفظ ملف الضبط بهذا الإختيار"
                        cantsaveconfig_combostyle_title = "إختيار غير صحيح"
                    else:
                        cantsaveconfig_combostyle_content = f"Can't save the configuration file with the choice {self.appearance_chooser_combo}"
                        cantsaveconfig_combostyle_title = "Incorrect choice"
                    messagebox.showerror(cantsaveconfig_combostyle_title, cantsaveconfig_combostyle_content)
                    sys.exit(75) # is for an incorrect theme mode.
                
                print(str(self.language_chooser_combo.get()))
                if str(self.language_chooser_combo.get()) == "العربية (مدعمة بواسطة حزمة اللغة العربية الاصدار 1.0)":
                    self.ConfigFileSaveProcess['ProgConfig']['languagesetting'] = 'ar'
                elif str(self.language_chooser_combo.get()) == "English":
                    self.ConfigFileSaveProcess['ProgConfig']['languagesetting'] = 'en'
                else:
                    if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                        cantsaveconfig_combostyle_content = f"Can't save the configuration file with the choice {self.appearance_chooser_combo}"
                        cantsaveconfig_combostyle_title = "Incorrect choice"
                    elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                        cantsaveconfig_combostyle_content = f"{self.appearance_chooser_combo} لا يمكن حفظ ملف الضبط بهذا الإختيار"
                        cantsaveconfig_combostyle_title = "إختيار غير صحيح"
                    else:
                        cantsaveconfig_combostyle_content = f"Can't save the configuration file with the choice {self.appearance_chooser_combo}"
                        cantsaveconfig_combostyle_title = "Incorrect choice"
                    messagebox.showerror(cantsaveconfig_combostyle_title, cantsaveconfig_combostyle_content)
                    sys.exit(195) # is for an incorrect language choice.


                # Right now, I guess it is enough and we should rn write the configuration data to the file "Config.ini".
                with open("Config.ini", 'w') as self.ConfigFileProcessor:
                        self.ConfigFileSaveProcess.write(self.ConfigFileProcessor)


                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    save_changes_txt = "All changes you did has been successfully saved, but for the changes to take effect, you will need to restart Temp_Cleaner GUI."
                    save_changes_title = "Saved your changes"
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    save_changes_txt = "Temp_Cleaner GUI جميع التغييرات التي قمت بها تم حفظها بنجاح، ولاكن لكي يتم تطبيقها يجب عليك إعادة تشغيل برنامج"
                    save_changes_title = "تم حفظ تعديلاتك"
                else:
                    save_changes_txt = "All changes you did has been successfully saved, but for the changes to take effect, you will need to restart Temp_Cleaner GUI."
                    save_changes_title = "Saved your changes"
                # Defining the window which will tell the user that a reboot is needed to apply the changes.
                messagebox.showinfo(save_changes_title, save_changes_txt)

                # Okay, enough with that, let's destroy the main loop ok?
                self.destroy()
            except:
                if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
                    cantsavechangestoconfigfile_content = "Unable to save your changes to the file 'Config.ini', Nothing has changed yet, and this window will not close."
                    cantsavechangestoconfigfile_title = "A runtime exception"
                elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                    cantsavechangestoconfigfile_content = "لم يتغير اي شئ حتي الان، وهذه النافذة لن تغلق ،'Config.ini' فشل في حفظ التغييرات في ملف "
                    cantsavechangestoconfigfile_title = "حدث خطأ في وقت التشغيل"
                else:
                    cantsavechangestoconfigfile_content = "Unable to save your changes to the file 'Config.ini', Nothing has changed yet, and this window will not close."
                    cantsavechangestoconfigfile_title = "A runtime exception"
                messagebox.showerror(cantsavechangestoconfigfile_title, cantsavechangestoconfigfile_content)
            
            return None

    
        # Defining the root properties.
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            title_settings = "Settings @ Temp_Cleaner GUI"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            title_settings = "الضبط @ Temp_Cleaner GUI"
        else:
            title_settings = "Settings @ Temp_Cleaner GUI"
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
            settings_lbl0_txt = "Temp_Cleaner Settings"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            settings_lbl0_txt = "Temp_Cleaner ضبط برنامج"
        else:
            settings_lbl0_txt = "Temp_Cleaner Settings"
        # Defining some informative labels (Basically some bla bla blas).
        self.lbl0_config = Label(self, text=settings_lbl0_txt, font=("Arial Bold", 32), background='#008aff', foreground='white')
        self.lbl0_config.place(x=20, y=7)
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            settings_lbl1_txt = "Configure the working pathes and other settings related to the Runtime of Temp_Cleaner"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            settings_lbl1_txt = "Temp_Cleaner قم بتغيير الضبط المتعلق بالمسارات والإعدادات الاخري المتعلقة بوقت تشغيل"
        else:
            settings_lbl1_txt = "Configure the working pathes and other settings related to the Runtime of Temp_Cleaner"
        self.lbl1_config = Label(self, text=settings_lbl1_txt, foreground='white', background='#008aff', font=("Arial", 12))
        self.lbl1_config.place(x=20, y=70)
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            settings_lbl2_txt = "Enter the path where RAMMap by Sysinternals tool executable is stored in :"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            settings_lbl2_txt = ":Sysinternals من RAMMapادخل المسار الكامل الذي يحتوي علي الملف التنفيذي ل"
        else:
            settings_lbl2_txt = "Enter the path where RAMMap by Sysinternals tool executable is stored in :"
        self.lbl2_config = Label(self, text=settings_lbl2_txt, foreground='white', background='#008aff', font=("Arial",12))
        self.lbl2_config.place(x=20, y=100)
        self.rammappath_input = ttk.Entry(self, width=180)
        self.rammappath_input.place(x=20, y=130)
        self.rammappath_input_browsebtn = ttk.Button(self, text="...", command=BrowseOne)
        self.rammappath_input_browsebtn.place(x=1108, y=131, relwidth=0.027, relheight=0.033)
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            settings_lbl3_txt = "Enter the current working path of the tool MalwareBytes AdwareCleaner :"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            settings_lbl3_txt = ":MalwareBytes AdwareCleaner ادخل المسار الكامل لملفات المستخدم لبرنامج"
        else:
            settings_lbl3_txt = "Enter the current working path of the tool MalwareBytes AdwareCleaner :"
        self.lbl3_config = Label(self, text=settings_lbl3_txt, foreground='white', background='#008aff', font=("Arial",12))
        self.lbl3_config.place(x=20, y=155)
        self.adwcleanerwpath_input = ttk.Entry(self, width=180)
        self.adwcleanerwpath_input.place(x=20, y=180)
        self.adwcleanerwpath_input_browsebtn = ttk.Button(self, text="...", command=BrowseTwo)
        self.adwcleanerwpath_input_browsebtn.place(x=1108, y=180, relwidth=0.027, relheight=0.033)
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            settings_lbl4_txt = "WinXPE Program Path :"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            settings_lbl4_txt = ":WinXPE ادخل مسار تواجد برنامج"
        else:
            settings_lbl4_txt = "WinXPE Program Path :"
        self.lbl4_config = Label(self, text=settings_lbl4_txt, foreground='white', background='#008aff', font=("Arial", 12))
        self.lbl4_config.place(x=20, y=205)
        self.winxpeapppath_input = ttk.Entry(self, width=180)
        self.winxpeapppath_input.place(x=20, y=230)
        self.winxpeapppath_input_browsebtn = ttk.Button(self, text="...", command=BrowseThree)
        self.winxpeapppath_input_browsebtn.place(x=1108, y=230, relwidth=0.027, relheight=0.033)
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            settings_lbl5_txt = "Enter the name of the User ID folder inside the WindowsActivitiesCache Folder (Optional) :"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            settings_lbl5_txt = "(إختياري) WindowsActivitiesCache ادخل اسم هوية المستخدم الموجودة داخل المجلد"
        else:
            settings_lbl5_txt = "Enter the name of the User ID folder inside the WindowsActivitiesCache Folder (Optional) :"
        self.lbl5_config = Label(self, text=settings_lbl5_txt, foreground='white', background='#008aff', font=("Arial",12))
        self.lbl5_config.place(x=20, y=257)
        self.cdpccpath_input = ttk.Entry(self, width=180)
        self.cdpccpath_input.place(x=20, y=283)
        self.cdpccpath_input_browsebtn = ttk.Button(self, text="...", command=BrowseFour)
        self.cdpccpath_input_browsebtn.place(x=1108, y=283, relwidth=0.027, relheight=0.033)
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            settings_lbl6_txt = "Choose appearance mode: (Dark, or Light)"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            settings_lbl6_txt = ":(Dark:مظلم ، Light:اختار المظهر (فاتح "
        else:
            settings_lbl6_txt = "Choose appearance mode: (Dark, or Light)"
        self.lbl6_config = Label(self, text=settings_lbl6_txt, foreground='white', background='#008aff', font=("Arial", 12))
        self.lbl6_config.place(x=20, y=310)
        self.appearance_chooser_combo = ttk.Combobox(self)
        self.appearance_chooser_combo['values'] = ('Light', 'Dark')
        self.appearance_chooser_combo.place(x=20, y=335, relheight=0.050, relwidth=0.936)

        self.lbl7_config = Label(self, text="Choose your language/اختار لغتك:", foreground='white', background='#008aff', font=("Arial", 12))
        self.lbl7_config.place(x=20, y=370)
        self.language_chooser_combo = ttk.Combobox(self)
        self.language_chooser_combo['values'] = ("العربية (مدعمة بواسطة حزمة اللغة العربية الاصدار 1.0)", "English")
        self.language_chooser_combo.place(relheight=0.050, relwidth=0.936, x=20, y=396)
        
        # defining the copyright window button.
        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            license_show_btn_txt = "License for Temp_Cleaner GUI"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            license_show_btn_txt = "Temp_Cleaner GUI الرخصة لبرنامج"
        else:
            license_show_btn_txt = "License for Temp_Cleaner GUI"
        self.showcpyrights_windowbtn = ttk.Button(self, text=license_show_btn_txt, command=showLicenseWindow)
        self.showcpyrights_windowbtn.place(relwidth=0.30, relheight=0.060, x=410, y=550)

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            quit_btn_txt = "Quit"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            quit_btn_txt = "خروج"
        else:
            quit_btn_txt = "Quit"

        self.closewindow_btn = atk.Button3d(self, text=quit_btn_txt, command=SelfDestroy)
        self.closewindow_btn.place(x=20, y=550, relwidth=0.30, relheight=0.060)

        # Tonight I'd fly, and be your lover.
        # Yeah, Yeah, Yeah....

        if str(GetConfig['ProgConfig']['languagesetting']) == 'en':
            apply_andquit_btn_txt = "Apply and Quit"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            apply_andquit_btn_txt = "حفظ التغييرات ثم الخروج"
        else:
            apply_andquit_btn_txt = "Apply and Quit"
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
            title = "License for Temp_Cleaner GUI"
        elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
            title = "Temp_Cleaner GUI رخصة البرنامج"
        else:
            title = "License for Temp_Cleaner GUI"
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
                warn_txt = "Is your computer's screen really that big?, If yes, Then I'm sorry I can't help you anymore."
                warn_title = "Do you want to decrease more?"
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                warn_txt = "هل شاشة الحاسب لديك حقا بهذا الكبر؟، إذا نعم لا يمكنني مساعدتك"
                warn_title = "تصغير الكتابة في الشاشة"
            else:
                warn_txt = "Is your computer's screen really that big?, If yes, Then I'm sorry I can't help you anymore."
                warn_title = "Do you want to decrease more?"
            
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
                warn_txt = "Is your eyesight really that low?, If yes, Then I'm sorry I can't help you anymore."
                warn_title = "Increase font size"
            elif str(GetConfig['ProgConfig']['languagesetting']) == 'ar':
                warn_txt = "هل مستوي نظرك ضعيف لهذه الدرجة؟، اسف لا يمكنني مساعدتك"
                warn_title = "تكبير الكتابة في الشاشة"
            else:
                warn_txt = "Is your eyesight really that low?, If yes, Then I'm sorry I can't help you anymore."
                warn_title = "Increase font size"
            
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
            messagebox.showinfo("Help on using 'Minimal Accessibility Pack v1.0'", f"""Minimal Accessibility Pack v1.0 is here!
You can enjoy using your favorite Mr.X software, even if you have any problems either with your computer's screen or with your eyesight.

To increase the font size, You can do "Control + I"
To decrease the font size, You can do "Control + D"

And thank you for choosing Mr.X's Software!

Powered by Minimal Accessibility Pack v1.0 by Insertx2k Dev (Mr.X).
""")

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
    try: # trying to check for the appearance mode.
        check_appearance_mode = configparser.ConfigParser()
        check_appearance_mode.read("Config.ini")
        appearance_mode = str(check_appearance_mode['ProgConfig']['appearancemode'])

        if str(appearance_mode) == "1":
            main_process = MainWindowLightMode()
            main_process.mainloop()
            sys.exit(0) # everything is just fine.
        elif str(appearance_mode) == "2":
            main_process = MainWindowLightMode()
            main_process.mainloop()
            sys.exit(0) # everything is just fine.
        else:
            print("ERROR: Unsupported appearance mode in 'Config.ini' file")
            print("Program can't continue")
            sys.exit(20) # 20 is for unsupported appearance mode!
    except Exception as excpt_main:
        print(f"error: an Exception has occured preventing the mainloop from booting up.")
        print(f"\nException details are:\n{excpt_main}")
        sys.exit(15) # 15 is for an exception that occured.
            
    # # if program was executed as a Python 3.xx.x Script file.
    # main_process = MainWindowLightMode()
    # main_process.mainloop()
    
