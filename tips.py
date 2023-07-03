"""
The Startup Tips (Tips for the Day) module for Temp_Cleaner GUI v6.8 or above.

Copyright (C) Insertx2k Dev (Mr.X) or Ziad Ahmed - 2021 - 2023

Licensed under the same license as Temp_Cleaner GUI (which is GPL 2+)

This module contains Windows and other necessary functions to implement the startup tips function in Temp_Cleaner GUI's window.

**SHOULD NOT BE REDISTRIBUTED OUTSIDE OF TEMP_CLEANER GUI**
"""
from tkinter import *
from tkinter import ttk, messagebox
import configparser
from customtkinter import *
from translations import *
import sys
import os
from tkinterweb import HtmlFrame
import random

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

print(f"{application_path}")

# opening a configparser session for reading from the file 'Config.ini'
GetConfig = configparser.ConfigParser()
GetConfig.read(f"{application_path}\\Config.ini")
# ------------------------

# attempts to get the current language for the ui mode of the updater program.
def getCurrentLanguage(currentLanguageStr=GetConfig["ProgConfig"]["languagesetting"]):
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
        return None







class TipsWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title(getCurrentLanguage().tips)
        self._window_width = 450
        self._window_height = 250
        self.geometry(f'{self._window_width}x{self._window_height}')
        self.minsize(self._window_width, self._window_height)
        self.resizable(True, True)
        self.wm_resizable(True, True)
        deactivate_automatic_dpi_awareness() # fixes for HiDPi displays
        # making window always on top.
        self.attributes('-topmost',True)
        # trying to load the style.json file to apply customtkinter styles.
        try:
            set_default_color_theme(f"{application_path}\\style.json")
        except Exception as style_json_file_loader_tryone_error:
            print(f"[ERROR]: couldn't read from file 'style.json' in the current directory due to the error:\n{style_json_file_loader_tryone_error}")
            self.destroy()
            return # error 299 is for error loading style.json file from current and previous directories.
        # ---------------------------


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
                return False
            return False
        

        try:
            self.iconbitmap(f"{application_path}\\icon0.ico")
        except Exception as errorLoadingIconBitmap:
            messagebox.showerror("ERROR in Mainloop thread", f"Couldn't load the iconbitmap for this window due to the exception:\n{errorLoadingIconBitmap}\nPress OK to acknowledge this event and continue running the program.")
            pass

        def quitBtnFunc():
            """
            The function for the 'Quit' button in the Tips window
            """
            try:
                self.destroy()
            except Exception as exceptionDestroyingMainProcess:
                print(f"[ERROR]: Background Error: Self is already destroyed\nMore details:\n{exceptionDestroyingMainProcess}")
            return None

        try:
            if str(GetConfig["ProgConfig"]["languagesetting"]) == "en":
                print("[DEBUG]: Language for tips is English")
                tips_folder_path = f"{application_path}\\tips\\en"
            elif str(GetConfig["ProgConfig"]["languagesetting"]) == "ar":
                print("[DEBUG]: Language for Tips is Arabic")
                tips_folder_path = f"{application_path}\\tips\\ar"
            else:
                print(f'[DEBUG]: Language defined in {str(GetConfig["ProgConfig"]["languagesetting"])} has no tips available')
                messagebox.showerror(getCurrentLanguage().cant_retrieve_config_fromfile_msgbox_title, getCurrentLanguage().error_unsupported_lang_in_tips)
                self.destroy()
        except Exception as errorReadingFolder:
            messagebox.showerror(getCurrentLanguage().cant_retrieve_config_fromfile_msgbox_title, f"{getCurrentLanguage().tips_folder_missing}\n{errorReadingFolder}")
            self.destroy()

        def tipsLinkClicked(link):
            """
            A function to make links in the tips window work.

            Parameters: link -> the target url of the link the user presses
            """
            self.tipswebview.load_url(f"file:///{tips_folder_path}\\{str(link).replace('file:///', '')}")
            return None
        
        
        
        def openRandomTip():
            """
            Loads a random tip file from the folder 'tips' in the program's directory.

            returns False if failed to read from folder, otherwise returns None
            """

            try:
                if str(GetConfig["ProgConfig"]["languagesetting"]) == "en":
                    print("[DEBUG]: Language for tips is English")
                    tips_files = os.listdir(tips_folder_path)
                elif str(GetConfig["ProgConfig"]["languagesetting"]) == "ar":
                    print("[DEBUG]: Language for Tips is Arabic")
                    tips_files = os.listdir(tips_folder_path)
                else:
                    print(f'[DEBUG]: Language defined in {str(GetConfig["ProgConfig"]["languagesetting"])} has no tips available')
                    messagebox.showerror(getCurrentLanguage().cant_retrieve_config_fromfile_msgbox_title, getCurrentLanguage().error_unsupported_lang_in_tips)
                    self.destroy()
                    return False
            except Exception as errorReadingFolder:
                messagebox.showerror(getCurrentLanguage().cant_retrieve_config_fromfile_msgbox_title, f"{getCurrentLanguage().tips_folder_missing}\n{errorReadingFolder}")
                self.destroy()
                return False
            tipfile_chosen = random.choice(tips_files)
            self.tipswebview.load_url(f"file:///{tips_folder_path}\\{tipfile_chosen}")
            return None

        # frame for web view widget.
        self.viewframe = Frame(self, bg=getCurrentAppearanceMode()[0])
        self.viewframe.pack(fill=BOTH, expand=True)
        self.viewframe.pack_propagate(False)



        # webview widget declaration.
        self.tipswebview = HtmlFrame(self.viewframe)
        self.tipswebview.pack(fill=BOTH, expand=True)
        self.tipswebview.on_link_click(tipsLinkClicked)
        openRandomTip()





        # close button and it's frame
        self.closebtnframe = Frame(self,bg=getCurrentAppearanceMode()[0], height=30)
        self.closebtnframe.pack(fill=X, expand=False)
        self.closebtnframe.pack_propagate(False)

        self.close_btn = CTkButton(self.closebtnframe, text=getCurrentLanguage().quit_settings_btn, command=quitBtnFunc)
        self.close_btn.pack(expand=True, fill=BOTH, side=LEFT)
        self.next_btn = CTkButton(self.closebtnframe, text=getCurrentLanguage().tips_next, command=openRandomTip)
        self.next_btn.pack(expand=True, fill=BOTH, side=RIGHT)




if __name__ == '__main__':
    process = TipsWindow()
    process.mainloop()
    raise SystemExit(0)
