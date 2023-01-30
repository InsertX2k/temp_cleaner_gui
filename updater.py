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

# initializing colorama
init(autoreset=True)

# a variable containing text file name and path.
versionFilePath = 'progver.txt'
releaseNotesSaveFilePath = 'releaseNotes.txt'
mrxTCGFilePath = "https://raw.githubusercontent.com/InsertX2k/software-versions/main/tcg.txt"
releaseNotesFilePath = "https://raw.githubusercontent.com/InsertX2k/software-versions/main/release_notes_tcg.txt"

# a variable containing a string of the current version.
versionNumber = configparser.ConfigParser()
versionNumber.read("Config.ini")
versionNumber = versionNumber['ProgConfig']['version']
# ------------------------

# opening a configparser session for reading from the file 'Config.ini'
GetConfig = configparser.ConfigParser()
GetConfig.read("Config.ini")
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
# ------------------------

def downloadAndSaveVersionFile():
    """
    A function used to download and save the text file containing the latest version number.
    """
    global versionFilePath, mrxTCGFilePath
    with urllib.request.urlopen(mrxTCGFilePath) as file:
        text = file.read().decode('utf-8')
    
    with open(versionFilePath, mode='w', encoding='utf-8') as saveFile:
        saveFile.write(text)
    saveFile.close()
    return None

def downloadAndSaveReleaseNotesFile():
    """
    A function used to download and save the text file containing the release notes.
    """
    global versionFilePath, mrxTCGFilePath, releaseNotesFilePath, releaseNotesSaveFilePath
    with urllib.request.urlopen(releaseNotesFilePath) as file:
        text = file.read().decode('utf-8')
    
    with open(releaseNotesSaveFilePath, mode='w', encoding='utf-8') as saveFile:
        saveFile.write(text)
    saveFile.close()
    return None


def readVersion():
    """
    Reads the version number from the downloaded text file, and compares it with the current version

    If the current version is the latest one, it returns None

    If there is an update, it should return True
    """
    global versionNumber

    with open(versionFilePath, mode='r', encoding='utf-8') as readFile:
        version = str(readFile.read()[0:6]).replace(' ', '').replace('\n', '')
        print(version)

    if str(version) == versionNumber:
        readFile.close()
        # print("You are currently running the latest version of the program.")
        return None
    else:
        readFile.close()
        # print("There is an update available.")
        return True


def getServerVersionNumber():
    """
    Reads the available version number from the file downloaded from Mr.X's Github server and returns it as a string.
    """

    with open(versionFilePath, mode='r', encoding='utf-8') as readFile:
        version = str(readFile.read()[0:6]).replace(' ', '').replace('\n', '')
        print(version)
    readFile.close()
    
    return version


def readReleaseNotesFromFile():
    """
    Reads the release notes file and returns the text in it.
    """
    global versionFilePath, mrxTCGFilePath, releaseNotesFilePath, releaseNotesSaveFilePath
    try:
        with open(releaseNotesSaveFilePath, 'r', encoding='utf-8') as releaseNotesTextFile:
            releaseNotesTextInMemory = releaseNotesTextFile.read()
            releaseNotesTextFile.close()
            return releaseNotesTextInMemory
    except Exception as reading_release_notes_file_error:
        messagebox.showerror("Runtime error", f"Couldn't read the release notes file due to the error:\n{reading_release_notes_file_error}\nThe program will close.")
        return False


# class for updater program ui window.
class updaterProgramUI(Toplevel):
    def __init__(self):
        super().__init__()
        global versionNumber
        self.title(getCurrentLanguage().updater_title)
        try: # attempt to load the icon bitmap for this window.
            self.iconbitmap("updater.ico")
        except Exception as load_iconbitmap_error:
            messagebox.showerror("Runtime error", f"Couldn't load iconbitmap for this window due to the following error\n{load_iconbitmap_error}\nThe window will continue to appear but without an icon bitmap")
            pass
        
        
        # trying to load the style.json file to apply customtkinter styles.
        try:
            set_default_color_theme("style.json")
        except Exception as style_json_file_loader_tryone_error:
            print(f"{Fore.RED}{Style.BRIGHT}error: couldn't read from file 'style.json' in the current directory due to the error:\n{style_json_file_loader_tryone_error}")
            print("Attempting to read from '../style.json', if exists, it should work properly, otherwise, the program will terminate itself automatically.")
            try: # second attempt (loading from '../style.json')
                set_default_color_theme("../style.json")
            except Exception as style_json_file_loader_trytwo_error:
                print(f"{Fore.RED}{Style.BRIGHT}error: second attempt to load from '../style.json' failed due to the error:\n{style_json_file_loader_trytwo_error}\nThe program will now terminate after reporting the error to the user.")
                messagebox.showerror("Unhandled runtime exception",f"Couldn't read from '../style.json' and 'style.json', Did 2 attempts to prevent this error from happening but nothing helped\nError details are:\n{style_json_file_loader_trytwo_error}\nThe program will close upon pressing OK")
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
                self.updaterLoader = Image.open("updater_dark.png").resize((image_width,image_height), Image.ANTIALIAS)
                self.updaterLoader = ImageTk.PhotoImage(self.updaterLoader)
            else: # light mode ui
                self.updaterLoader = Image.open("updater.png").resize((image_width,image_height), Image.ANTIALIAS)
                self.updaterLoader = ImageTk.PhotoImage(self.updaterLoader)
        except Exception as loading_updater_logo_error:
            messagebox.showerror("Runtime error", f"Couldn't load the updater logo due to the following error\n{loading_updater_logo_error}\nThe program will close.")
            return
        

        def dontUpdateAndCloseProgram():
            """
            The function for "Don't Update" button.
            """
            self.destroy() # destroying window
            try:
                os.remove("progver.txt")
                os.remove("releaseNotes.txt")
            except Exception as exception_deleting_unneeded_downloads: # couldn't delete them.
                messagebox.showerror("An error has occured", f"Couldn't delete the unnecessary files 'releaseNotes.txt' and 'progver.txt' due to a runtime error\nError details are:\n{exception_deleting_unneeded_downloads}\n\nIf you are a user and you see this message please create an issue on Temp_Cleaner GUI's official Github page and MAKE SURE to provide a screenshot of this messagebox\nPress OK to continue.")
            return None
        
        def openWebBrowserWindow():
            """
            Opens a new tab on your default browser that contains the official website for Temp_Cleaner GUI
            """
            webbrowser.open_new("https://insertx2k.github.io/temp_cleaner_gui/downloads.html")
            messagebox.showinfo(getCurrentLanguage().update_btn_updater, getCurrentLanguage().opened_webbrowser_dialog)
            self.destroy()
            try:
                os.remove("progver.txt")
                os.remove("releaseNotes.txt")
            except Exception as exception_deleting_unneeded_downloads: # couldn't delete them.
                messagebox.showerror("An error has occured", f"Couldn't delete the unnecessary files 'releaseNotes.txt' and 'progver.txt' due to a runtime error\nError details are:\n{exception_deleting_unneeded_downloads}\n\nIf you are a user and you see this message please create an issue on Temp_Cleaner GUI's official Github page and MAKE SURE to provide a screenshot of this messagebox\nPress OK to continue.")
            return None


        def getReleaseNotes():
            """
            A function used to get the content of the release notes file and insert it into the scrolledtext.ScrolledText widget of the release notes.
            """
            self.release_notes_widget.configure(state='normal') # i want it to be editable.
            downloadAndSaveReleaseNotesFile()
            self.release_notes_widget.delete(1.0, END) # clearing the release notes dialogbox.
            self.release_notes_widget.insert(END, readReleaseNotesFromFile())
            self.release_notes_widget.configure(state='disabled')
            return None

        # a label for showing the updater icon
        self.updaterIcon = Label(self, text='', background=getCurrentAppearanceMode()[0], image=self.updaterLoader)
        self.updaterIcon.place(x=0, y=60)

        # other informative labels.
        self.lbl0 = Label(self, text=getCurrentLanguage().new_update_tcg, background=getCurrentAppearanceMode()[0], foreground=getCurrentAppearanceMode()[1], font=("Arial", 14))
        self.lbl0.place(x=170, y=5)
        self.lbl1 = Label(self, text=f"{getCurrentLanguage().new_version_is}{getServerVersionNumber()}{getCurrentLanguage().current_version_is}{versionNumber}", background=getCurrentAppearanceMode()[0], foreground=getCurrentAppearanceMode()[1], font=("Arial", 9))
        self.lbl1.place(x=170, y=35)
        self.release_notes_widget = scrolledtext.ScrolledText(self, background=getCurrentAppearanceMode()[0], foreground=getCurrentAppearanceMode()[1], selectbackground='blue', state='disabled', font=("Arial", 12))
        self.release_notes_widget.place(x=170, y=55, relwidth=0.7, relheight=0.63)
        self.closebtn = CTkButton(self, text=getCurrentLanguage().close_btn_updater, command=dontUpdateAndCloseProgram, cursor='hand2')
        self.closebtn.place(x=170, y=260)
        self.downloadbtn = CTkButton(self, text=getCurrentLanguage().update_btn_updater, command=openWebBrowserWindow, cursor='hand2')
        self.downloadbtn.place(y=260, x=430)

        # Checking if there is an available update or not
        # if there is one, the window will continue to appear, otherwise, the window will close.
        if readVersion() == None:
            messagebox.showwarning(getCurrentLanguage().update_btn_updater, getCurrentLanguage().running_latest_version_dialog)
            self.destroy()
        else:
            pass

        getReleaseNotes()


# ----------------------



if __name__ == '__main__': # if program wasn't imported as a Python 3.x.x Module file.
    downloadAndSaveVersionFile()
    downloadAndSaveReleaseNotesFile()
    if len(argv) == 1:
        print(argv)
        # run the gui updater program normally, the program was executed with no arguments.
        downloadAndSaveVersionFile()
        downloadAndSaveReleaseNotesFile()
        guiProcess = updaterProgramUI()
        guiProcess.mainloop()
        exit(0) # gui program ran very well.
    elif len(argv) == 2:
        if str(argv[1]) == "--silent":
            # don't inform user if program is on latest version, if it isn't, show the updater ui.
            try:
                downloadAndSaveVersionFile()
                downloadAndSaveReleaseNotesFile()
                isThereAnyUpdatesAvailable = readVersion()
                if isThereAnyUpdatesAvailable == True:
                    guiProcess = updaterProgramUI()
                    guiProcess.mainloop()
                    raise SystemExit(0)
                else:
                    # there are no updates available, don't run gui program.
                    print(f"{Fore.GREEN}{Style.BRIGHT}info: you are running the latest version of the program, no need to update it.")
                    exit(0) # exit code 0 means there is no update available.
            except Exception as reading_server_version_error:
                print(f"{Fore.RED}{Style.BRIGHT}error: couldn't download from Mr.X's github server due to an error\nerror details:\n{reading_server_version_error}")
                exit(20) # exit code 20 is for errors downloading version text file.
            exit(1111111111) # error code 1111111111 is for unhandled or unexpected statement end
        else:
            print(f"{Fore.RED}{Style.BRIGHT}error: invalid argument: {str(argv[1])}, the only valid option is: --silent")
            exit(2) # exit code 2 is for invalid argument.
    else:
        print(f"{Fore.YELLOW}{Style.BRIGHT}warning: one or more unnecessary command line arguments found\nother options will be ignored'")
        if str(argv[1]) == "--silent":
            # don't inform user if program is on latest version, if it isn't, show the updater ui.
            try:
                downloadAndSaveVersionFile()
                downloadAndSaveReleaseNotesFile()
                isThereAnyUpdatesAvailable = readVersion()
                if isThereAnyUpdatesAvailable == True:
                    guiProcess = updaterProgramUI()
                    guiProcess.mainloop()
                    raise SystemExit(0)
                else:
                    # there are no updates available, don't run gui program.
                    print(f"{Fore.GREEN}{Style.BRIGHT}info: you are running the latest version of the program, no need to update it.")
                    exit(0) # exit code 0 means there is no update available.
            except Exception as reading_server_version_error:
                print(f"{Fore.RED}{Style.BRIGHT}error: couldn't download from Mr.X's github server due to an error\nerror details:\n{reading_server_version_error}")
                exit(20) # exit code 20 is for errors downloading version text file.
            exit(1111111111) # error code 1111111111 is for unhandled or unexpected statement end
        else:
            print(f"{Fore.RED}{Style.BRIGHT}error: invalid argument: {str(argv[1])}, the only valid option is: --silent")
            exit(2) # exit code 2 is for invalid argument.


