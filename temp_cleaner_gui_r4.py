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
            self.title(f"The Temp_Cleaner GUI Project (v4) (Windows) Running On: {self.login}'s PC (Powered by Minimal Accessibility Pack v1.0)")
        except Exception as excpt129:
            self.title("The Temp_Cleaner GUI Project (v4) (Windows) (Powered by Minimal Accessibility Pack v1.0)")


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



        self.lblframe0 = ttk.Labelframe(self.show_frame, text="Recycle Bin Cleanup")
        # --------------------------

        self.clr_recyclebin_sysdrive_btn = ttk.Checkbutton(self.lblframe0, text="Empty Systemdrive Recycle Bin", variable=self.var0, onvalue="1", offvalue="0", command=None)
        self.clr_recyclebin_sysdrive_btn.grid(column=0, row=3, sticky='w')

        # ---------------------------
        self.lblframe0.grid(column=0, row=2, sticky='w')



        self.lblframe1 = ttk.Labelframe(self.show_frame, text="DirectX Shader Cache Cleanup (Win 10/11 Only)")
        # ---------------------------
        self.clr_d3dscache_localappdata_btn = ttk.Checkbutton(self.lblframe1, text="Clean D3DSCached data in local app data Directory", variable=self.var2, onvalue="1", offvalue="0", command=None)
        self.clr_d3dscache_localappdata_btn.grid(column=0, row=5, sticky='w')
        # ---------------------------
        self.lblframe1.grid(column=0, row=4, sticky='w')

        self.lblframe2 = ttk.Labelframe(self.show_frame, text="System and User Specific Cleaner")
        # ---------------------------
        self.clr_prefetchw_windir_btn = ttk.Checkbutton(self.lblframe2, text="Clean PrefetchW in Windows Directory Data.", variable=self.var1, onvalue="1", offvalue="0", command=None)
        self.clr_prefetchw_windir_btn.grid(column=0, row=7, sticky='w')
        self.clr_usrclipboard_content_btn = ttk.Checkbutton(self.lblframe2, text="Clean User Clipboard Data (Excl. Content you copy 'n' paste)", variable=self.var9, onvalue="1", offvalue="0", command=None)
        self.clr_usrclipboard_content_btn.grid(column=0, row=8, sticky='w')
        self.clr_windir_temp_btn = ttk.Checkbutton(self.lblframe2, text="Clear Windir Temporary Data", variable=self.var3, onvalue="1", offvalue="0", command=None)
        self.clr_windir_temp_btn.grid(column=0, row=9, sticky='w')
        self.clr_localappdata_temp_btn = ttk.Checkbutton(self.lblframe2, text="Clean User Temporary Data", variable=self.var4, onvalue="1", offvalue="0", command=None)
        self.clr_localappdata_temp_btn.grid(column=0, row=10, sticky='w')
        self.clr_default_usr_appdata_temp_btn = ttk.Checkbutton(self.lblframe2, text="Clean Default User Temporary Files", variable=self.var7, onvalue="1", offvalue="0", command=None)
        self.clr_default_usr_appdata_temp_btn.grid(column=0, row=11, sticky='w')
        self.clr_inet_cached_data_btn = ttk.Checkbutton(self.lblframe2, text="Clean IE (Internet Explorer) Cached data", variable=self.var8, onvalue="1", offvalue="0", command=None)
        self.clr_inet_cached_data_btn.grid(column=0, row=12, sticky='w')
        self.clr_msexplorer_thumbcacheddata_btn = ttk.Checkbutton(self.lblframe2, text="Clean Windows Explorer Thumbnails Cached Data", variable=self.var10, onvalue="1", offvalue="0", command=None)
        self.clr_msexplorer_thumbcacheddata_btn.grid(column=0, row=13, sticky='w')
        self.clr_winrecentdocs_list_btn = ttk.Checkbutton(self.lblframe2, text="Clean User Recent Documents List", variable=self.var11, onvalue="1", offvalue="0", command=None)
        self.clr_winrecentdocs_list_btn.grid(column=0, row=14, sticky='w')
        self.clr_locallow_temporary_data_btn = ttk.Checkbutton(self.lblframe2, text="Clean Local Low Temporary Folders", variable=self.var41, onvalue="1", offvalue="0", command=None)
        self.clr_locallow_temporary_data_btn.grid(column=0, row=15, sticky='w')
        # ---------------------------
        self.lblframe2.grid(column=0, row=6, sticky='w')


        self.lblframe3 = ttk.Labelframe(self.show_frame, text="Web Browser Cleaner")
        # ---------------------------
        self.clr_gchrome_webcache_incl_gpucache_codecache_btn = ttk.Checkbutton(self.lblframe3, text="Clean Google Chrome Browser Webcached data (Incl. GPUCache, Code Cache)", variable=self.var5, onvalue="1", offvalue="0", command=None)
        self.clr_gchrome_webcache_incl_gpucache_codecache_btn.grid(column=0, row=17, sticky='w')
        self.clr_gchrome_browser_cookies_btn = ttk.Checkbutton(self.lblframe3, text="Clean Google Chrome Browser Cookies (Incl. Cookies-journal)", variable=self.var6, onvalue="1", offvalue="0", command=None)
        self.clr_gchrome_browser_cookies_btn.grid(column=0, row=18, sticky='w')
        self.clr_gchrome_extension_cookies_data_btn = ttk.Checkbutton(self.lblframe3, text="Clean Google Chrome Browser Extension Cookie Data", variable=self.var33, onvalue="1", offvalue="0", command=None)
        self.clr_gchrome_extension_cookies_data_btn.grid(column=0, row=19, sticky='w')
        self.clr_steam_webclient_htmlcache_btn = ttk.Checkbutton(self.lblframe3, text="Clean Steam Webclient HTML Cached data", variable=self.var14, onvalue="1", offvalue="0", command=None)
        self.clr_steam_webclient_htmlcache_btn.grid(column=0, row=20, sticky='w')
        self.clr_discordwebclient_webcacheddata_btn = ttk.Checkbutton(self.lblframe3, text="Clean Discord Webclient Webcached data", variable=self.var12, onvalue="1", offvalue="0", command=None)
        self.clr_discordwebclient_webcacheddata_btn.grid(column=0, row=21, sticky='w')
        self.clr_chromiumbased_msedge_webcached_data_btn = ttk.Checkbutton(self.lblframe3, text="Clean Chromium-based Microsoft Edge Webcached data (Incl. GPUCache, Code cache)", variable=self.var24, onvalue="1", offvalue="0", command=None)
        self.clr_chromiumbased_msedge_webcached_data_btn.grid(column=0, row=22, sticky='w')
        self.clr_chormiumbased_msedge_cookies_data_btn = ttk.Checkbutton(self.lblframe3, text="Clean Chromium-based Microsoft Edge Cookie data (Incl. Cookies-journal)", variable=self.var25, onvalue="1", offvalue="0", command=None)
        self.clr_chormiumbased_msedge_cookies_data_btn.grid(column=0, row=23, sticky='w')
        self.clr_mozilla_firefox_webcached_data_btn = ttk.Checkbutton(self.lblframe3, text="Clean Mozilla Firefox Webcached data (Incl. cache2, jumpListCache, and Shader Cache)", variable=self.var59, onvalue="1", offvalue="0", command=None)
        self.clr_mozilla_firefox_webcached_data_btn.grid(column=0, row=24, sticky='w')
        self.clr_mozilla_firefox_cookies_sqlite_file_btn = ttk.Checkbutton(self.lblframe3, text="Clean Mozilla Firefox browser Cookie data (it is just a Sqlite file)", variable=self.var60, onvalue="1", offvalue="0", command=None)
        self.clr_mozilla_firefox_cookies_sqlite_file_btn.grid(column=0, row=25, sticky='w')
        self.clr_discordapp_squirrel_temp_data_btn = ttk.Checkbutton(self.lblframe3, text="Clean Discord Windows Client Squirrel Temp", variable=self.var40, onvalue="1", offvalue="0", command=None)
        self.clr_discordapp_squirrel_temp_data_btn.grid(column=0, row=26, sticky='w')
        self.clr_inetcookies_btn = ttk.Checkbutton(self.lblframe3, text="Clean Internet Explorer Cookies Data", variable=self.var17, onvalue="1", offvalue="0", command=None)
        self.clr_inetcookies_btn.grid(column=0, row=27, sticky='w')
        self.clr_additionalinet_cacheddata_btn = ttk.Checkbutton(self.lblframe3, text="Clean Internet Explorer Additional Cached Data", variable=self.var18, onvalue="1", offvalue="0", command=None)
        self.clr_additionalinet_cacheddata_btn.grid(column=0, row=28, sticky='w')
        self.clr_iedownload_history_data_btn = ttk.Checkbutton(self.lblframe3, text="Clean Internet Explorer Downloads History Data", variable=self.var19, onvalue="1", offvalue="0", command=None)
        self.clr_iedownload_history_data_btn.grid(column=0, row=29, sticky='w')
        # ---------------------------
        self.lblframe3.grid(column=0, row=16, sticky='w')


        self.lblframe4 = ttk.Labelframe(self.show_frame, text="Photo Editors Cleanup")
        # ---------------------------
        self.clr_gimpstmps_btn = ttk.Checkbutton(self.lblframe4, text="Clean GNU Image Manipulation Program's Temporary data (gimp's tmps)", variable=self.var13, onvalue="1", offvalue="0", command=None)
        self.clr_gimpstmps_btn.grid(column=0, row=31, sticky='w')
        self.clr_gimp_recentdocs_btn = ttk.Checkbutton(self.lblframe4, text="Clean GNU Image Manipulation Program Recent Documents List (GIMP)", variable=self.var47, onvalue="1", offvalue="0", command=None)
        self.clr_gimp_recentdocs_btn.grid(column=0, row=32, sticky='w')
        self.clr_adobephotoshop_webcached_data_btn = ttk.Checkbutton(self.lblframe4, text="Clean Adobe Photoshop 2020 Webcached data", variable=self.var27, onvalue="1", offvalue="0", command=None)
        self.clr_adobephotoshop_webcached_data_btn.grid(column=0, row=33, sticky='w')
        # ---------------------------
        self.lblframe4.grid(column=0, row=30, sticky='w')

        self.lblframe5 = ttk.Labelframe(self.show_frame, text="Microsoft Windows Update Cleaners")
        # ---------------------------
        self.clr_windowsupdate_downloaded_updates_btn = ttk.Checkbutton(self.lblframe5, text="Clean all Windows Update's Downloaded Update Files", variable=self.var15, onvalue="1", offvalue="0", command=None)
        self.clr_windowsupdate_downloaded_updates_btn.grid(column=0, row=35, sticky='w')
        # ---------------------------
        self.lblframe5.grid(column=0, row=34, sticky='w')

        self.lblframe6 = ttk.Labelframe(self.show_frame, text="Windows 10/11 only Cleaners")
        # ---------------------------
        self.clr_win10os_cached_data_btn = ttk.Checkbutton(self.lblframe6, text="Clean Windows 10/11 Operating System Cached Data", variable=self.var16, onvalue="1", offvalue="0", command=None)
        self.clr_win10os_cached_data_btn.grid(column=0, row=37, sticky='w')
        self.clr_win10_action_center_cached_data_btn = ttk.Checkbutton(self.lblframe6, text="Clean Windows 10/11 Action Center/Notifications Center Cached data", variable=self.var20, onvalue="1", offvalue="0", command=None)
        self.clr_win10_action_center_cached_data_btn.grid(column=0, row=38, sticky='w')
        self.clr_winappux_cached_data_btn = ttk.Checkbutton(self.lblframe6, text="Clean Windows 10/11 Modern Applications Cached data", variable=self.var21, onvalue="1", offvalue="0", command=None)
        self.clr_winappux_cached_data_btn.grid(column=0, row=39, sticky='w')
        self.clr_msstore_based_edge_webcached_data_btn = ttk.Checkbutton(self.lblframe6, text="Clean Microsoft Store Based Edge Web cached data", variable=self.var22, onvalue="1", offvalue="0", command=None)
        self.clr_msstore_based_edge_webcached_data_btn.grid(column=0, row=40, sticky='w')
        self.clr_winexplorer_thumbcache_to_delete_files_btn = ttk.Checkbutton(self.lblframe6, text="Clean Additional Windows Explorer Thumbnails Cached Data (thumbcachetodelete)", variable=self.var23, onvalue="1", offvalue="0", command=None)
        self.clr_winexplorer_thumbcache_to_delete_files_btn.grid(column=0, row=41, sticky='w')
        self.clr_cryptnet_urlcache_data_btn = ttk.Checkbutton(self.lblframe6, text="Clean Windows 10/11 Cryptnet URL Cached data", variable=self.var30, onvalue="1", offvalue="0", command=None)
        self.clr_cryptnet_urlcache_data_btn.grid(column=0, row=42, sticky='w')
        self.clr_connecteddevicesplatform_win10_cached_data_btn = ttk.Checkbutton(self.lblframe6, text="Clean Windows 10/11 ConnectedDevicesPlatform Cached Data (Requires you to set it's path in Settings)", variable=self.var34, onvalue="1", offvalue="0", command=None)
        self.clr_connecteddevicesplatform_win10_cached_data_btn.grid(column=0, row=43, sticky='w')
        self.clr_elevated_diagnostics_data_btn = ttk.Checkbutton(self.lblframe6, text="Clean Elevated Diagnostics Data folder (Only for Windows 10/11)", variable=self.var42, onvalue="1", offvalue="0", command=None)
        self.clr_elevated_diagnostics_data_btn.grid(column=0, row=44, sticky='w')
        self.clr_identitynexus_integration_folder_btn = ttk.Checkbutton(self.lblframe6, text="Clean IdentityNexusIntegration Folder contents (Only for Windows 10/11)", variable=self.var49, onvalue="1", offvalue="0", command=None)
        self.clr_identitynexus_integration_folder_btn.grid(column=0, row=45, sticky='w')
        self.clr_servicehub_identity_file_btn = ttk.Checkbutton(self.lblframe6, text="Clean ServiceHub Identity file (that salt file)", variable=self.var56, onvalue="1", offvalue="0", command=None)
        self.clr_servicehub_identity_file_btn.grid(column=0, row=46, sticky='w')
        # ---------------------------
        self.lblframe6.grid(column=0, row=36, sticky='w')


        self.lblframe7 = ttk.Labelframe(self.show_frame, text="Games Cleaner")
        # ---------------------------
        self.clr_roblox_game_downloads_btn = ttk.Checkbutton(self.lblframe7, text="Clean ROBLOX Game Downloaded Textures/Data", variable=self.var26, onvalue="1", offvalue="0", command=None)
        self.clr_roblox_game_downloads_btn.grid(column=0, row=48, sticky='w')
        self.clr_roblox_game_log_files_btn = ttk.Checkbutton(self.lblframe7, text="Clean ROBLOX Game Verbosed Log files", variable=self.var51, onvalue="1", offvalue="0", command=None)
        self.clr_roblox_game_log_files_btn.grid(column=0, row=49, sticky='w')
        self.clr_scrapmechanic_axolot_games_workshop_items_cached_data_btn = ttk.Checkbutton(self.lblframe7, text="Clean Axolot Games Scrap Mechanic Workshop Items Cached data", variable=self.var50, onvalue="1", offvalue="0", command=None)
        self.clr_scrapmechanic_axolot_games_workshop_items_cached_data_btn.grid(column=0, row=50, sticky='w')
        self.clr_minecraft_webcached_data_btn = ttk.Checkbutton(self.lblframe7, text="Clean Minecraft Webcached data", variable=self.var58, onvalue="1", offvalue="0", command=None)
        self.clr_minecraft_webcached_data_btn.grid(column=0, row=51, sticky='w')
        # ---------------------------
        self.lblframe7.grid(column=0, row=47, sticky='w')


        self.lblframe8 = ttk.Labelframe(self.show_frame, text="Python Cleaners")
        # ---------------------------
        self.clr_python_pip_cached_data_btn = ttk.Checkbutton(self.lblframe8, text="Clean Python PIP Cached Data", variable=self.var31, onvalue="1", offvalue="0", command=None)
        self.clr_python_pip_cached_data_btn.grid(column=0, row=53, sticky='w')
        self.clr_pyinstaller_temporary_data_btn = ttk.Checkbutton(self.lblframe8, text="Clean Pyinstaller Bin Cached Data", variable=self.var45, onvalue="1", offvalue="0", command=None)
        self.clr_pyinstaller_temporary_data_btn.grid(column=0, row=54, sticky='w')
        self.clr_jedipython_additionals_btn = ttk.Checkbutton(self.lblframe8, text="Clean Jedi Python Additional Temporary Data", variable=self.var46, onvalue="1", offvalue="0", command=None)
        self.clr_jedipython_additionals_btn.grid(column=0, row=55, sticky='w')
        # ---------------------------
        self.lblframe8.grid(column=0, row=52, sticky='w')


        self.lblframe9 = ttk.Labelframe(self.show_frame, text="RAM Cleaners")
        # ---------------------------
        self.empty_winworkingsets_rammap_btn = ttk.Checkbutton(self.lblframe9, text="Empty Running Software Workingsets using RAMMap", variable=self.var32, onvalue="1", offvalue="0", command=None)
        self.empty_winworkingsets_rammap_btn.grid(column=0, row=57, sticky='w')
        # ---------------------------
        self.lblframe9.grid(column=0, row=56, sticky='w')


        self.lblframe10 = ttk.Labelframe(self.show_frame, text="Video Editing Software Cleaners")
        # ---------------------------
        self.clr_sony_vegas_pro_temp_and_logs_data_btn = ttk.Checkbutton(self.lblframe10, text="Clean Sony VEGAS Pro 17 Temporary data and log files", variable=self.var28, onvalue="1", offvalue="0", command=None)
        self.clr_sony_vegas_pro_temp_and_logs_data_btn.grid(column=0, row=59, sticky='w')
        self.clr_sony_vegas_pro_error_reports_data_btn = ttk.Checkbutton(self.lblframe10, text="Clean Sony VEGAS Pro ERROR Reports files", variable=self.var61, onvalue="1", offvalue="0", command=None)
        self.clr_sony_vegas_pro_error_reports_data_btn.grid(column=0, row=60, sticky='w')
        # ---------------------------
        self.lblframe10.grid(column=0, row=58, sticky='w')



        self.lblframe11 = ttk.Labelframe(self.show_frame, text="3D Moduling Software Cleaners")
        # ---------------------------
        self.clr_mcneel_rhinoceros_3d_moduling_soft_cached_data_btn = ttk.Checkbutton(self.lblframe11, text="Clean McNeel Rhinoceros 3D Moduling Software Temporary Data", variable=self.var29, onvalue="1", offvalue="0", command=None)
        self.clr_mcneel_rhinoceros_3d_moduling_soft_cached_data_btn.grid(column=0, row=62, sticky='w')
        # ---------------------------
        self.lblframe11.grid(column=0, row=61, sticky='w')


        self.lblframe12 = ttk.Labelframe(self.show_frame, text="Additional Software Cleaners")
        # ---------------------------
        self.clr_iconcache_db_file_in_localappdata_dir_btn = ttk.Checkbutton(self.lblframe12, text="Clean Icon Cache file in Local app data folder", variable=self.var35, onvalue="1", offvalue="0", command=None)
        self.clr_iconcache_db_file_in_localappdata_dir_btn.grid(column=0, row=64, sticky='w')
        self.clr_microvirt_memu_log_data_memdump_files_btn = ttk.Checkbutton(self.lblframe12, text="Clean Microvirt MEmu Logs and Memory Dump Files", variable=self.var36, onvalue="1", offvalue="0", command=None)
        self.clr_microvirt_memu_log_data_memdump_files_btn.grid(column=0, row=65, sticky='w')
        self.clr_adwcleaner_log_files_btn = ttk.Checkbutton(self.lblframe12, text="Clean Malwarebytes Adware Cleaner Log data and its files", variable=self.var37, onvalue="1", offvalue="0", command=None)
        self.clr_adwcleaner_log_files_btn.grid(column=0, row=66, sticky='w')
        self.clr_perflogs_in_systemdrive_btn = ttk.Checkbutton(self.lblframe12, text="Clean the folder Perflogs in Systemdrive volume", variable=self.var38, onvalue="1", offvalue="0", command=None)
        self.clr_perflogs_in_systemdrive_btn.grid(column=0, row=67, sticky='w')
        self.clr_dotcache_folder_in_userprofile_path_btn = ttk.Checkbutton(self.lblframe12, text="Clean Android Cached data in your computer", variable=self.var39, onvalue="1", offvalue="0", command=None)
        self.clr_dotcache_folder_in_userprofile_path_btn.grid(column=0, row=68, sticky='w')
        self.clr_vmware_downloads_folder_btn = ttk.Checkbutton(self.lblframe12, text="Clean VMware Downloads (All files downloaded by all VMware Software)", variable=self.var43, onvalue="1", offvalue="0", command=None)
        self.clr_vmware_downloads_folder_btn.grid(column=0, row=69, sticky='w')
        self.clr_balena_itcher_webcached_data_btn = ttk.Checkbutton(self.lblframe12, text="Clean BalenaItcher webcached data (Incl. GPUCache, Code Cache, Local Storage, Session Storage)", variable=self.var44, onvalue="1", offvalue="0", command=None)
        self.clr_balena_itcher_webcached_data_btn.grid(column=0, row=70, sticky='w')
        self.clr_lowlevelformattool_licenseagreement_confirmationfile_btn = ttk.Checkbutton(self.lblframe12, text="Clean LowLevelFormatTool (LLFT) License Agreement Confirmation File", variable=self.var48, onvalue="1", offvalue="0", command=None)
        self.clr_lowlevelformattool_licenseagreement_confirmationfile_btn.grid(column=0, row=71, sticky='w')
        self.clr_winxpe_app_downloads_folder_btn = ttk.Checkbutton(self.lblframe12, text="Clean WinXPE Creator Downloads Diretory (Requires you to set it's path on Settings)", variable=self.var55, onvalue="1", offvalue="0", command=None)
        self.clr_winxpe_app_downloads_folder_btn.grid(column=0, row=72, sticky='w')
        self.clr_huawei_hisuite_log_data_btn = ttk.Checkbutton(self.lblframe12, text="Clean Huawei HiSuite Log data", variable=self.var57, onvalue="1", offvalue="0", command=None)
        self.clr_huawei_hisuite_log_data_btn.grid(column=0, row=73, sticky='w')
        self.clr_huawei_hisuite_dnd_temp_btn = ttk.Checkbutton(self.lblframe12, text="Clean Huawei HiSuite Drag 'n' Drop Temporary Data", variable=self.var63, onvalue="1", offvalue="0", command=None)
        self.clr_huawei_hisuite_dnd_temp_btn.grid(column=0, row=74, sticky='w')
        # ---------------------------
        self.lblframe12.grid(column=0, row=63, sticky='w')



        self.lblframe13 = ttk.Labelframe(self.show_frame, text="Microsoft Visual Studio Code Cleaners")
        # ---------------------------
        self.clr_vscode_webcached_data_btn = ttk.Checkbutton(self.lblframe13, text="Clean Microsoft Visual Studio Code Webcached data (Incl. GPUCache, Code Cache, CachedData, Cache paths)", variable=self.var52, onvalue="1", offvalue="0", command=None)
        self.clr_vscode_webcached_data_btn.grid(column=0, row=76, sticky='w')
        self.clr_vscode_cookie_data_btn = ttk.Checkbutton(self.lblframe13, text="Clean Microsoft Visual Studio Code Cookie data (Incl. Cookies-journal)", variable=self.var53, onvalue="1", offvalue="0", command=None)
        self.clr_vscode_cookie_data_btn.grid(column=0, row=77, sticky='w')
        self.clr_vscode_cached_extensions_data_btn = ttk.Checkbutton(self.lblframe13, text="Clean Microsoft Visual Studio Code Cached Extensions Data (Incl. VSIXs)", variable=self.var54, onvalue="1", offvalue="0", command=None)
        self.clr_vscode_cached_extensions_data_btn.grid(column=0, row=78, sticky='w')
        # ---------------------------
        self.lblframe13.grid(column=0, row=75, sticky='w')


        self.lblframe14 = ttk.Labelframe(self.show_frame, text="Java Deployment Cache Cleaner")
        # ---------------------------
        self.clr_java_deployment_cached_data_btn = ttk.Checkbutton(self.lblframe14, text="Clean Java Deployment Cached Data", variable=self.var62, onvalue="1", offvalue="0", command=None)
        self.clr_java_deployment_cached_data_btn.grid(column=0, row=80, sticky='w')
        # ---------------------------
        self.lblframe14.grid(column=0, row=79, sticky='w')


        self.lblframe15 = ttk.Labelframe(self.show_frame, text="All done?")
        # ---------------------------
        self.destroy_activity_after_done_btn = ttk.Checkbutton(self.lblframe15, text="Do you want to close this program when it's done with cleaning up temp?", variable=self.var64, onvalue="1", offvalue="0", command=None, cursor='hand2')
        self.destroy_activity_after_done_btn.grid(column=0, row=82, sticky='w')
        # ---------------------------
        self.lblframe15.grid(column=0, row=81, sticky='w')


        # Defining the about button.
        self.about_window_btn = ttk.Button(self.show_frame, text="About", command=self.show_about_window, cursor='hand2')
        self.about_window_btn.place(x=10, y=2000, relwidth=0.3, relheight=0.035)
        # Defining the execute button.
        self.exec_btn = ttk.Button(self.show_frame, text="Execute", command=self.execute_theprogram, cursor='hand2')
        self.exec_btn.place(x=400 ,y=2000, relwidth=0.3, relheight=0.035)

        # declaring a space.
        self.space = Label(self.show_frame, text="", font=("Arial Bold", 50))
        if str(GetConfig['ProgConfig']['appearancemode']) == '2':
            self.space.configure(background=atk.DEFAULT_COLOR)
        self.space.grid(column=0, row=83, sticky='w')

        # Defining the go to configuration page button.
        self.config_page_btn = ttk.Button(self.show_frame, text="Settings", command=self.StartConfigurationWindow, cursor='hand2')
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
            global font_size

            if int(font_size) == 100:
                messagebox.showerror("Increase font size", "Is your eyesight really that low?, If yes, Then I'm sorry I can't help you anymore.")
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
            global font_size

            if int(font_size) == 4:
                messagebox.showerror("Decrease font size", "Is your computer's screen really that big?, If yes, Then I'm sorry I can't help you anymore.")
                return False
            else:
                font_size = font_size - 1
                self.output_show.configure(font=("Courier New", font_size))
                return None

            return None


        def showHelp(keybinding_arg):
            messagebox.showinfo("Help on using Minimal Accessibility Pack v1.0", f"""Minimal Accessibility Pack v1.0 is here!
        You can enjoy using your favorite Mr.X software, even if you have any problems either with your computer's screen or with your eyesight.

        To increase the font size, You can do "Control + I"
        To decrease the font size, You can do "Control + D"

        And thank you for choosing Mr.X's Software!

        Powered by Minimal Accessibility Pack v1.0 by Insertx2k Dev (Mr.X).
        """)

            return None


        self.lblframe16 = ttk.Labelframe(self.show_frame, text="Console Output")
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
        messagebox.showinfo("About 'The Temp_Cleaner GUI Project (v4)'","""The Temp_Cleaner GUI Project by Insertx2k Dev\n
Version 4.0
Written by Insertx2k Dev (Mr.X)
Support Twitter : @insertplayztw
Support Github : InsertX2k
This release of Temp_Cleaner GUI is powered by "Minimal Accessibility Pack v1.0" by Insertx2k Dev (Mr.X).
\n
GitHub page : https://github.com/insertx2k/temp_cleaner_gui
Better UI GitHub page : https://insertx2k.github.io/temp_cleaner_gui
\n
This program is Free Software (FOSS), You are allowed to modify or redistribute it under the terms of GNU General Public License v2.0 or later @ Free Software Foundation.
""")

        return None

    # Defining the function to execute the following selected commands : 
    def execute_theprogram(self):
        self.ShowNotificationDone = True
        self.exec_btn.configure(text="Executing", command=None)
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
            self.reboot_uwp = messagebox.askquestion("Restart Windows Update Service", "After you delete all Downloaded files by the Windows Update Service you should restart the whole service to commit changes you did to it\nWould you like to restart the Windows Update Service?")
            if self.reboot_uwp == "yes":
                self.self_2 = Tk()
                self.self_2.title("Restart Windows Update Service")
                self.self_2.geometry('500x90')
                self.self_2.resizable(False,False)


                try:
                    self.self_2.iconbitmap("icon0.ico")
                except Exception as excpt24:
                    messagebox.showerror("ERROR 1 in ICONBITMAP process", f"Unable to load the icon file for this window due to Exception:\n{excpt24}")
                    pass


                # Defining some labels used to show the user that something is happening inside.
                self.lbl0x = Label(self.self_2, text="Restarting Windows Update Service...", font=("Arial", 19))
                self.lbl0x.place(x=25 ,y=20)
                # Defining the actions used to restart the Windows update service.
                self.process = subprocess.getoutput('net start wuauserv')
                # Defining the commands used to show the user that all pending operations has been successfully completed!
                messagebox.showinfo("Restart Windows Update Service", "Windows Update Service Has been successfully restarted!")
                # Defining the mainloop destroy once the execution is done.
                self.self_2.destroy()
                self.self_2.mainloop()
                messagebox.showinfo("Restart Windows Update Service", "Done restarting the Windows Update Service!")
            else:
                messagebox.showinfo("Restart Windows Update Service", "Expect your device to have problems with Windows Update if you didn't restart it as soon as possible then.")
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
            self.conf1 = messagebox.askquestion("Clean Store-based MS Edge Cached Data", "Cleaning Store-based MS Edge cached data can not be done automatically, which means you are supposed to do that manually, which will make this tool open an explorer (Windows Explorer) window for you showing you the folder where you are supposed to clean MS-Store-Based EDGE Webcache data\nPlease keep in mind that you shouldn't leave the directory opened to you by this tool\nSo do you wish to processed?")
            if self.conf1 == "yes":
                messagebox.showinfo("Clean Store-based MS Edge Cached Data", "Opening the directory for you\nDon't forget to look for the folder Microsoft.MicrosoftEdge_[a random number], and go inside the AC folder inside of it, you will then be able to see all MS Store-based edge webcached data.")
                self.process = subprocess.getoutput(' explorer.exe "%localappdata%\\Packages\\"')
                self.output_show.insert(END, f"\n {self.process}")
                messagebox.showinfo("Clean Windows Modern Applications Cached Data", "Done!")
            else:
                messagebox.showinfo("Clean Windows Modern Applications Cached Data", "Operation canceled by the user.")
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
            self.conf2 = messagebox.askquestion("Empty Windows Workingsets", "Would you really like to run RAMMap by Sysinternals to empty RAM Workingsets?")
            if self.conf2 == "yes":
                self.RAMMAPpath_var = GetConfig['ProgConfig']['RAMMapPath']
                if self.RAMMAPpath_var == '$DEFAULT':
                    messagebox.showinfo("Notification", "The path of the RAMMap tool is set to '$DEFAULT', Continuing using the default configured RAMMap path.")
                    self.process = subprocess.getoutput(r'"%systemdrive%\RAMMap\RAMMap.exe" -Ew')
                    self.output_show.insert(END, f"\n {self.process}")
                    messagebox.showinfo("Empty Windows Workingsets", "RAMMap.exe - Command sent.")
                else:
                    self.process = subprocess.getoutput(rf'""{self.RAMMAPpath_var}"\RAMMap.exe" -Ew')
                    self.output_show.insert(END, f"\n {self.process}")
                    messagebox.showinfo("Empty Windows Workingsets", "RAMMap.exe - Command sent.")
            else:
                messagebox.showinfo("Empty Windows Workingsets", "Operation has been canceled.")
        self.selection35 = self.var33.get()
        if self.selection35 == '1':
            self.process = subprocess.getoutput(' cd /d "%localappdata%\\Google\\Chrome\\User Data\\Default"&del /s /q "Extension Cookies"&del /s /q "Extension Cookies-journal"')
            self.output_show.insert(END, f"\n {self.process}")
        self.selection36 = self.var34.get()
        if self.selection36 == '1':
            self.CDPCCPATH_var = GetConfig['ProgConfig']['CDPCCPATH']
            if self.CDPCCPATH_var == '$DEFAULT':
                messagebox.showinfo("Notification", "You didn't specify a custom location for the Windows activites cache cleaner to work on, Continuing using the Default values.")
                self.process = subprocess.getoutput(' cd /d "%localappdata%\\ConnectedDevicesPlatform"&erase /s /f /q "ee2999716b7783e6"')
                self.output_show.insert(END, f"\n {self.process}")
            else:
                self.process = subprocess.getoutput(rf' cd /d "%localappdata%\\ConnectedDevicesPlatform"&erase /s /f /q "{self.CDPCCPATH_var}"')
                self.output_show.insert(END, f"\n {self.process}")
        self.selection37 = self.var35.get()
        if self.selection37 == '1':
            self.conf3 = messagebox.askquestion("Clean icon cache", "Cleaning IconCache.db file can not be done automatically, which means the user is premitted to do that manually, all what you have to do is just deleting the file iconcache.db in the directory we will open to you\nDo you wish to processed?")
            if self.conf3 == "yes":
                self.process = subprocess.getoutput('%windir%\\explorer.exe "%localappdata%"')
                self.output_show.insert(END, f"\n {self.process}")
                messagebox.showinfo("Clean icon cache database file", "Done!")
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
                messagebox.showinfo("Notification", "You didn't specify a custom working location for the AdwareCleaner Cleaner, Continuing using the default path.")
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
                messagebox.showinfo("An ERROR has occured", "You didn't specify the path of the 'WinXPE' program, The cleaner can't continue.")
            else:
                self.process = subprocess.getoutput(rf' erase /s /f /q "{self.WINXPEPATH_var}\Temp"')
                self.output_show.insert(END, f"\n {self.process}")
                messagebox.showinfo("Note", "You will need to redownload all downloaded data by the tool for the exporting phase to be done!")
                
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
            self.exec_btn.configure(text="Execute", command=self.execute_theprogram)
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
    

        global font_size
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
                messagebox.showerror("Runtime Exception", "Unable to retrieve the configuration information, this can be due to a hard exception, or a something else, the settings window will close.")
                self.destroy()
            
            try:
                self.rammappath_input.insert(INSERT, self.RetrieveConfig_Init['ProgConfig']['RAMMapPath'])
                self.adwcleanerwpath_input.insert(INSERT, self.RetrieveConfig_Init['ProgConfig']['ADWCLRPath'])
                self.winxpeapppath_input.insert(INSERT, self.RetrieveConfig_Init['ProgConfig']['WINXPEPATH'])
                self.cdpccpath_input.insert(INSERT, self.RetrieveConfig_Init['ProgConfig']['CDPCCPATH'])
                
                if str(self.RetrieveConfig_Init['ProgConfig']['appearancemode']) == '1':
                    self.appearance_chooser_combo.current(0)
                elif str(self.RetrieveConfig_Init['ProgConfig']['appearancemode']) == '2':
                    self.appearance_chooser_combo.current(1)
            except Exception as excpt_rtcore_retrieve:
                messagebox.showerror("A runtime exception", "Unable to read the configuration file from your computer, please make sure to give this program a permission to read files in your hard disk if blocked by your antivirus software and try again, The settings window will close.")
                print(excpt_rtcore_retrieve)
                self.destroy()
            
            return None



        # It is the time to define the function used to save the changes to the configuration file "Config.ini"
        def SaveConfigurationandQuit():
            try:
                self.ConfigFileSaveProcess = configparser.ConfigParser()
                self.ConfigFileSaveProcess.read("Config.ini")
            except:
                messagebox.showerror("A runtime exception", "Unable to open the configuration file on your computer, please make sure to give this program enough permissions to do so, and if your antivirus blocks it, please give it access and try again.")
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
                    messagebox.showerror("Incorrect choice", f"Can't save the configuration file with the choice {self.appearance_chooser_combo}")
                    sys.exit(75) # is for an incorrect theme mode.


                # Right now, I guess it is enough and we should rn write the configuration data to the file "Config.ini".
                with open("Config.ini", 'w') as self.ConfigFileProcessor:
                        self.ConfigFileSaveProcess.write(self.ConfigFileProcessor)

                # Defining the window which will tell the user that a reboot is needed to apply the changes.
                messagebox.showinfo("Saved your changes", "All changes you did has been successfully saved, but for the changes to take effect, you will need to restart Temp_Cleaner GUI.")

                # Okay, enough with that, let's destroy the main loop ok?
                self.destroy()
            except:
                messagebox.showerror("A runtime exception", "Unable to save your changes to the file 'Config.ini', Nothing has changed yet, and this window will not close.")
            
            return None

    
        # Defining the root properties.
        self.title("Settings @ Temp_Cleaner GUI")
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



        # Defining some informative labels (Basically some bla bla blas).
        self.lbl0_config = Label(self, text="Temp_Cleaner Settings", font=("Arial Bold", 32), background='#008aff', foreground='white')
        self.lbl0_config.place(x=20, y=7)
        self.lbl1_config = Label(self, text="Configure the working pathes and other settings related to the Runtime of Temp_Cleaner", foreground='white', background='#008aff', font=("Arial", 12))
        self.lbl1_config.place(x=20, y=70)
        self.lbl2_config = Label(self, text="Enter the path where RAMMap by Sysinternals tool executable is stored in :", foreground='white', background='#008aff', font=("Arial",12))
        self.lbl2_config.place(x=20, y=100)
        self.rammappath_input = ttk.Entry(self, width=180)
        self.rammappath_input.place(x=20, y=130)
        self.rammappath_input_browsebtn = ttk.Button(self, text="...", command=BrowseOne)
        self.rammappath_input_browsebtn.place(x=1108, y=131, relwidth=0.027, relheight=0.033)
        self.lbl3_config = Label(self, text="Enter the current working path of the tool MalwareBytes AdwareCleaner :", foreground='white', background='#008aff', font=("Arial",12))
        self.lbl3_config.place(x=20, y=155)
        self.adwcleanerwpath_input = ttk.Entry(self, width=180)
        self.adwcleanerwpath_input.place(x=20, y=180)
        self.adwcleanerwpath_input_browsebtn = ttk.Button(self, text="...", command=BrowseTwo)
        self.adwcleanerwpath_input_browsebtn.place(x=1108, y=180, relwidth=0.027, relheight=0.033)
        self.lbl4_config = Label(self, text="WinXPE Program Path :", foreground='white', background='#008aff', font=("Arial", 12))
        self.lbl4_config.place(x=20, y=205)
        self.winxpeapppath_input = ttk.Entry(self, width=180)
        self.winxpeapppath_input.place(x=20, y=230)
        self.winxpeapppath_input_browsebtn = ttk.Button(self, text="...", command=BrowseThree)
        self.winxpeapppath_input_browsebtn.place(x=1108, y=230, relwidth=0.027, relheight=0.033)
        self.lbl5_config = Label(self, text="Enter the name of the User ID folder inside the WindowsActivitiesCache Folder (Optional) :", foreground='white', background='#008aff', font=("Arial",12))
        self.lbl5_config.place(x=20, y=257)
        self.cdpccpath_input = ttk.Entry(self, width=180)
        self.cdpccpath_input.place(x=20, y=283)
        self.cdpccpath_input_browsebtn = ttk.Button(self, text="...", command=BrowseFour)
        self.cdpccpath_input_browsebtn.place(x=1108, y=283, relwidth=0.027, relheight=0.033)
        self.lbl6_config = Label(self, text="Choose appearance mode: (Dark, or Light)", foreground='white', background='#008aff', font=("Arial", 12))
        self.lbl6_config.place(x=20, y=310)
        self.appearance_chooser_combo = ttk.Combobox(self)
        self.appearance_chooser_combo['values'] = ('Light', 'Dark')
        self.appearance_chooser_combo.place(x=20, y=335, relheight=0.050, relwidth=0.936)
        
        # defining the copyright window button.
        self.showcpyrights_windowbtn = ttk.Button(self, text="License for Temp_Cleaner GUI", command=showLicenseWindow)
        self.showcpyrights_windowbtn.place(relwidth=0.30, relheight=0.060, x=410, y=550)

        self.closewindow_btn = atk.Button3d(self, text="Quit", command=SelfDestroy)
        self.closewindow_btn.place(x=20, y=550, relwidth=0.30, relheight=0.060)

        # Tonight I'd fly, and be your lover.
        # Yeah, Yeah, Yeah....

        self.applychangesandclose_btn = atk.Button3d(self, text="Apply and Quit", command=SaveConfigurationandQuit)
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
        global font_size
        # defining a new toplevel widget to show the program's license on.
        
        self.title("License for Temp_Cleaner GUI")
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
                messagebox.showerror("Do you want to decrease more?", "Is your computer's screen really that big?, If yes, Then I'm sorry I can't help you anymore.")
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

            if int(font_size) == 100:
                messagebox.showerror("Increase font size", "Is your eyesight really that low?, If yes, Then I'm sorry I can't help you anymore.")
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
    
