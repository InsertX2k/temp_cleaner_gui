"""
This is the module for the Updater program of Temp_Cleaner GUI

Licensed under the same license as Temp_Cleaner GUI
"""
# imports
from tkinter import *
from tkinter import ttk, messagebox, scrolledtext
from customtkinter import *
from sys import argv, exit
import urllib.request
import configparser
from colorama import Style, Fore, init
from translations import *
from PIL import ImageTk, Image
import webbrowser
import os
import threading

try:
    # initializing colorama
    init(autoreset=True)
except Exception as _errorColoramaInit:
    print(f"[ERROR]: updater module: failed to initialize colorama:{_errorColoramaInit}")
    pass



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


# a variable containing text file name and path.
# versionFilePath = f'{application_path}\\progver.txt'
# releaseNotesSaveFilePath = f'{application_path}\\releaseNotes.txt'
mrxTCGFilePath = "https://raw.githubusercontent.com/InsertX2k/software-versions/main/tcg.txt"
releaseNotesFilePath = "https://raw.githubusercontent.com/InsertX2k/software-versions/main/release_notes_tcg.txt"
downloadLink = "https://insertx2k.github.io/temp_cleaner_gui/downloads.html"


# a global variable for return values of multithreaded functions.
_RetVal = None


try:
    # a variable containing a string of the current version.
    versionNumber = configparser.ConfigParser()
    versionNumber.read(f"{application_path}\\Config.ini")
    currentVersion = str(versionNumber['ProgConfig']['version'])
    print(f"[DEBUG]: Current version is:{currentVersion}")
except Exception as _errorReadingFromCFGFile:
    print(f"[ERROR]: updater module: Couldn't read from Config.ini due to this error:\n{_errorReadingFromCFGFile}")
# ------------------------
try:
    # opening a configparser session for reading from the file 'Config.ini'
    GetConfig = configparser.ConfigParser()
    GetConfig.read(f"{application_path}\\Config.ini")
    # ------------------------
except Exception as _errorReadingCFGParser:
    print(f"[ERROR]: updater module: couldn't read from Config.ini file\nerror details are:\n{_errorReadingCFGParser}")
    raise SystemExit(255)

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
# ------------------------
def latestVersionNumber():
    """
    Gets the latest version number from server, then returns it. (with a timeout of 25 seconds)

    If it fails for some reason, it only returns None
    """
    global _RetVal
    try:
        with urllib.request.urlopen(mrxTCGFilePath, timeout=25) as file:
            text = file.read().decode('utf-8')[0:6].replace(' ', '').replace('\n', '')
            _RetVal = text
            return str(text)
    except Exception:
        print("[ERROR]: couldn't download from the server.")
        _RetVal = None
        return None
# ------------------------
# Attempting to get the latest version number.
# threading.Thread(target=latestVersionNumber).start()
# latestVerNum = None
# def multiThreadedlatestVer3Up7():
#     """
#     A function for updating the global variable `latestVerNum` using multithreading to avoid long time imports
#     """
#     global latestVerNum
#     latestVerNum = latestVersionNumber()

# threading.Thread(target=latestVerNum).start()

# ------------------------

# def downloadAndSaveVersionFile():
#     """
#     A function used to download and save the text file containing the latest version number.
#     """
#     global versionFilePath, mrxTCGFilePath
#     try:
#         with urllib.request.urlopen(mrxTCGFilePath) as file:
#             text = file.read().decode('utf-8')
#     except Exception:
#         return False

#     try:
#         with open(versionFilePath, mode='w', encoding='utf-8') as saveFile:
#             saveFile.write(text)
#         saveFile.close()
#     except Exception:
#         return False

#     return None

# def downloadAndSaveReleaseNotesFile():
#     """
#     A function used to download and save the text file containing the release notes.
#     """
#     global versionFilePath, mrxTCGFilePath, releaseNotesFilePath, releaseNotesSaveFilePath

#     try:
#         with urllib.request.urlopen(releaseNotesFilePath) as file:
#             text = file.read().decode('utf-8')
#     except Exception:
#         return False
    
#     try:
#         with open(releaseNotesSaveFilePath, mode='w', encoding='utf-8') as saveFile:
#             saveFile.write(text)
#         saveFile.close()
#     except Exception as savingDownloadedReleaseNotesFileError:
#         return False
#     return None


def readVersion():
    """
    Reads the version number from the variable text and compares it with the current version.

    If the current version is the latest one, it returns None

    If there is an update, it should return True
    """
    global versionNumber, latestVersionNumber, currentVersion, _RetVal

    version = latestVersionNumber()
    if version is not None:
        if version == currentVersion:
            # readFile.close()
            print(f"[DEBUG]: Server version is : {str(version)}")
            print("You are currently running the latest version of the program. from readVersion func")
            return None
        else:
            # readFile.close()
            print(f"[DEBUG]: Server version is : {str(version)}")
            print("There is an update available. from readVersion func")
            return True
    else:
        return None




# def readReleaseNotesFromFile():
#     """
#     Reads the release notes file and returns the text in it.
#     """
#     global mrxTCGFilePath, releaseNotesFilePath
#     try:
#         with open(releaseNotesSaveFilePath, 'r', encoding='utf-8') as releaseNotesTextFile:
#             releaseNotesTextInMemory = releaseNotesTextFile.read()
#             releaseNotesTextFile.close()
#             return releaseNotesTextInMemory
#     except Exception as reading_release_notes_file_error:
#         messagebox.showerror("Runtime error", f"Couldn't read the release notes file due to the error:\n{reading_release_notes_file_error}\nThe program will close.")
#         return False


# class for updater program ui window.
class updaterProgramUI(Toplevel):
    def __init__(self):
        global versionNumber, application_path, downloadLink, readVersion, latestVersionNumber, currentVersion
        # a variable containing the latest version number from the server.
        _SrvrVerNum = latestVersionNumber()
        # a simple check cuz if it is None the window should close.
        if _SrvrVerNum == None:
            # messagebox.showerror(getCurrentLanguage().updater_title, getCurrentLanguage().couldnt_download)
            self.destroy()
        else:
            pass
        super().__init__()
        deactivate_automatic_dpi_awareness() # deactivating automatic dpi awareness in updater program.
        self.title(getCurrentLanguage().updater_title)
        self.attributes('-topmost',True)
        try: # attempt to load the icon bitmap for this window.
            self.iconbitmap(f"{application_path}\\updater.ico")
        except Exception as load_iconbitmap_error:
            messagebox.showerror("Runtime error", f"Couldn't load iconbitmap for this window due to the following error\n{load_iconbitmap_error}\nThe window will continue to appear but without an icon bitmap")
            pass
        
        
        
        # trying to load the style.json file to apply customtkinter styles.
        try:
            set_default_color_theme(f"{application_path}\\style.json")
        except Exception as style_json_file_loader_tryone_error:
            print(f"{Fore.RED}{Style.BRIGHT}[ERROR]: couldn't read from file 'style.json' in the current directory due to the error:\n{style_json_file_loader_tryone_error}")
            self.destroy()
            return # error 299 is for error loading style.json file from current and previous directories.
        # ---------------------------
        
        # adjusting window manager related properties
        self.geometry('600x300')
        self.minsize(600, 300)
        self.maxsize(600, 300)
        self.resizable(False, False)

        # checking if program is running in light or dark mode.
        try:
            if int(GetConfig["ProgConfig"]['appearancemode']) == 2: # dark mode
                self.configure(background='#333')
            else:
                set_appearance_mode("light")
        except Exception as reading_appearanace_mode_error:
            messagebox.showerror("Unhandleable Runtime error", f"Couldn't read the appearance mode or apply it due to the following error\n{reading_appearanace_mode_error}\nThe program will exit")
            self.destroy()
            return
        
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

        # declaring variables for dimensions of updater logo
        image_width = 160
        image_height = 150
        # attempting to get the current UI mode to choose the appropriate updater logo
        try:
            if str(GetConfig["ProgConfig"]['appearancemode']) == '2': # dark mode ui  
                # loading the 'updater.png' file in memory.
                self.updaterLoader = Image.open(f"{application_path}\\updater_dark.png").resize((image_width,image_height), Image.LANCZOS)
                self.updaterLoader = ImageTk.PhotoImage(self.updaterLoader)
            else: # light mode ui
                self.updaterLoader = Image.open(f"{application_path}\\updater.png").resize((image_width,image_height), Image.LANCZOS)
                self.updaterLoader = ImageTk.PhotoImage(self.updaterLoader)
        except Exception as loading_updater_logo_error:
            messagebox.showerror("Runtime error", f"Couldn't load the updater logo due to the following error\n{loading_updater_logo_error}\nThe program will close.")
            return
        

        def dontUpdateAndCloseProgram():
            """
            The function for "Don't Update" button.
            """
            self.destroy() # destroying window
            # try:
            #     os.remove(f"{application_path}\\progver.txt")
            #     os.remove(f"{application_path}\\releaseNotes.txt")
            # except Exception as exception_deleting_unneeded_downloads: # couldn't delete them.
            #     messagebox.showerror("An error has occured", f"Couldn't delete the unnecessary files 'releaseNotes.txt' and 'progver.txt' due to a runtime error\nError details are:\n{exception_deleting_unneeded_downloads}\n\nIf you are a user and you see this message please create an issue on Temp_Cleaner GUI's official Github page and MAKE SURE to provide a screenshot of this messagebox\nPress OK to continue.")
            return None
        
        def openWebBrowserWindow():
            """
            Opens a new tab on your default browser that contains the official website for Temp_Cleaner GUI
            """
            webbrowser.open_new(downloadLink)
            messagebox.showinfo(getCurrentLanguage().update_btn_updater, getCurrentLanguage().opened_webbrowser_dialog)
            self.destroy()
            # try:
            #     os.remove(f"{application_path}\\progver.txt")
            #     os.remove(f"{application_path}\\releaseNotes.txt")
            # except Exception as exception_deleting_unneeded_downloads: # couldn't delete them.
            #     messagebox.showerror("An error has occured", f"Couldn't delete the unnecessary files 'releaseNotes.txt' and 'progver.txt' due to a runtime error\nError details are:\n{exception_deleting_unneeded_downloads}\n\nIf you are a user and you see this message please create an issue on Temp_Cleaner GUI's official Github page and MAKE SURE to provide a screenshot of this messagebox\nPress OK to continue.")
            return None


        def getReleaseNotes():
            """
            A function used to get the content of the release notes file and insert it into the scrolledtext.ScrolledText widget of the release notes.

            the timeout for the download packet sent is 25 seconds.
            """
            # if downloadAndSaveReleaseNotesFile() == False:
            #     messagebox.showerror("Runtime exception", "Couldn't read from release notes file")
            #     return False
            # else:
            #     pass
            try:
                self.release_notes_widget.configure(state='normal') # i want it to be editable.
                self.release_notes_widget.delete(1.0, END) # clearing the release notes dialogbox.
                self.release_notes_widget.insert(END, getCurrentLanguage().checking_for_updates)
                self.release_notes_widget.configure(state='disabled')
            except:
                pass
            try:
                with urllib.request.urlopen(releaseNotesFilePath, timeout=25) as file:
                    releaseNotesText = file.read().decode('utf-8')
                    try:
                        self.release_notes_widget.configure(state='normal')
                        self.release_notes_widget.delete(1.0, END) # clearing the release notes dialogbox.
                        self.release_notes_widget.insert(END, releaseNotesText)
                        self.release_notes_widget.configure(state='disabled')
                    except:
                        pass
            except Exception:
                self.release_notes_widget.configure(state='normal')
                self.release_notes_widget.delete(1.0, END) # clearing the release notes dialogbox.
                self.release_notes_widget.insert(END, getCurrentLanguage().couldnt_download)
                self.release_notes_widget.configure(state='disabled')
            
            return None
        


        # a label for showing the updater icon
        self.updaterIcon = Label(self, text='', background=getCurrentAppearanceMode()[0], image=self.updaterLoader)
        self.updaterIcon.place(x=0, y=60)

        # other informative labels.
        self.lbl0 = Label(self, text=getCurrentLanguage().new_update_tcg, background=getCurrentAppearanceMode()[0], foreground=getCurrentAppearanceMode()[1], font=("Arial", 14))
        self.lbl0.place(x=170, y=5)
        self.lbl1 = Label(self, text=f"{getCurrentLanguage().new_version_is}{_SrvrVerNum}{getCurrentLanguage().current_version_is}{currentVersion}", background=getCurrentAppearanceMode()[0], foreground=getCurrentAppearanceMode()[1], font=("Arial", 9))
        self.lbl1.place(x=170, y=35)
        self.release_notes_widget = scrolledtext.ScrolledText(self, background=getCurrentAppearanceMode()[0], foreground=getCurrentAppearanceMode()[1], selectbackground='blue', state='disabled', font=("Arial", 10))
        self.release_notes_widget.place(x=170, y=55, relwidth=0.7, relheight=0.63)
        self.closebtn = CTkButton(self, text=getCurrentLanguage().close_btn_updater, command=dontUpdateAndCloseProgram, cursor='hand2')
        self.closebtn.place(x=170, y=260)
        self.downloadbtn = CTkButton(self, text=getCurrentLanguage().update_btn_updater, command=openWebBrowserWindow, cursor='hand2')
        self.downloadbtn.place(y=260, x=430)

        # Checking if there is an available update or not
        # if there is one, the window will continue to appear, otherwise, the window will close.
        if readVersion() == None:
            self.attributes('-topmost',False)
            messagebox.showwarning(getCurrentLanguage().update_btn_updater, getCurrentLanguage().running_latest_version_dialog)
            self.attributes('-topmost',True)
            self.destroy()
            return # exiting program
        elif readVersion() == False:
            self.destroy()
            return 
        else:
            pass

        # if getReleaseNotes() == False:
        #     self.destroy()
        #     return
        # else:
        #     pass
        # updating release notes.
        threading.Thread(target=getReleaseNotes).start()


# ----------------------



if __name__ == '__main__': # if program wasn't imported as a Python 3.x.x Module file.
    if len(argv) == 1:
        print(f"[DEBUG]: sys.argv is: {argv}")
        # run the gui updater program normally, the program was executed with no arguments.
        guiProcess = updaterProgramUI()
        guiProcess.mainloop()
        raise SystemExit(0) # gui program ran very well.
    elif len(argv) == 2:
        if str(argv[1]) == "--silent":
            # don't inform user if program is on latest version, if it isn't, show the updater ui.
            try:
                isThereAnyUpdatesAvailable = readVersion()
                if isThereAnyUpdatesAvailable == True:
                    guiProcess = updaterProgramUI()
                    guiProcess.mainloop()
                    raise SystemExit(0)
                else:
                    # there are no updates available, don't run gui program.
                    print(f"{Fore.GREEN}{Style.BRIGHT}[INFO]: you are running the latest version of the program, no need to update it.")
                    raise SystemExit(0) # exit code 0 means there is no update available.
            except Exception as reading_server_version_error:
                print(f"{Fore.RED}{Style.BRIGHT}[ERROR]: couldn't download from Mr.X's github server due to an error\nerror details:\n{reading_server_version_error}")
                raise SystemExit(20) # exit code 20 is for errors downloading version text file.
            raise SystemExit(1111111111) # error code 1111111111 is for unhandled or unexpected statement end
        else:
            print(f"{Fore.RED}{Style.BRIGHT}[ERROR]: invalid argument: {str(argv[1])}, the only valid option is: --silent")
            raise SystemExit(2) # exit code 2 is for invalid argument.
    else:
        print(f"{Fore.YELLOW}{Style.BRIGHT}[WARNING]: one or more unnecessary command line arguments found\nother options will be ignored'")
        if str(argv[1]) == "--silent":
            # don't inform user if program is on latest version, if it isn't, show the updater ui.
            try:
                isThereAnyUpdatesAvailable = readVersion()
                if isThereAnyUpdatesAvailable == True:
                    guiProcess = updaterProgramUI()
                    guiProcess.mainloop()
                    raise SystemExit(0)
                else:
                    # there are no updates available, don't run gui program.
                    print(f"{Fore.GREEN}{Style.BRIGHT}[INFO]: you are running the latest version of the program, no need to update it.")
                    raise SystemExit(0) # exit code 0 means there is no update available.
            except Exception as reading_server_version_error:
                print(f"{Fore.RED}{Style.BRIGHT}[ERROR]: couldn't download from Mr.X's github server due to an error\nerror details:\n{reading_server_version_error}")
                raise SystemExit(20) # exit code 20 is for errors downloading version text file.
            raise SystemExit(1111111111) # error code 1111111111 is for unhandled or unexpected statement end
        else:
            print(f"{Fore.RED}{Style.BRIGHT}[ERROR]: invalid argument: {str(argv[1])}, the only valid option is: --silent")
            raise SystemExit(2) # exit code 2 is for invalid argument.


