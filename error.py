"""
Temp_Cleaner GUI's built-in Exception/Error User Friendly Notifier module

Copyright (C) Ziad Ahmed (Mr.X) - 2021 - 2023

Licensed under the same license as Temp_Cleaner GUI, and might not work properly when used outside of it.
"""
# imports
from tkinter import *
from tkinter import ttk, messagebox, scrolledtext
from translations import *
import sys, os
import configparser
from PIL import ImageTk, Image

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
os.chdir(application_path)

# printing application path to console display
print(f"[DEBUG]: Temp_Cleaner GUI is installed in: {application_path}")

try:
    # Defining the function that will get the current values of an configparser values.
    GetConfig = configparser.ConfigParser()
    GetConfig.read(f'{application_path}\\Config.ini')
except Exception as readingFromConfigFileError:
    print(f" Unhandled runtime exception\n\nCouldn't read from local configuration file (Config.ini), please make sure it exists in the current directory of the program and try again.\n\nError details for technical assistance:\n{readingFromConfigFileError}")
    raise SystemExit(255)
# checking if autocheck for updates is enabled or not, because if enabled will run the updater before running the main program.
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

class ErrorWindow(Tk):
    def __init__(self, errorMsgContent=getCurrentLanguage().gathering_error_details) -> None:
        """
        This class represents the Error Window (inherited from the `Tk` class)

        Optional keyword arguments are:
        
        `errorMsgContent` - Is the string representing the error details text to be shown in the window, for example: (where `x` is the variable that holds the exception information)

        ```py
        f"Import Error, error details are:{x}"
        ```
        """
        global getCurrentLanguage
        self.errorMsgContent = errorMsgContent
        super().__init__()
        self.title(getCurrentLanguage().an_error_has_occured_text)
        self.width = 600
        self.height = 300
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        try:
            self.iconbitmap(f"{application_path}\\err.ico")
        except Exception as errorL23ap:
            messagebox.showerror("Runtime error has occured", f"Couldn't load iconbitmap for this window\nThis can happen due to many reasons including the antivirus software blocking of this program\nError details are:\n{errorL23ap}\n\nPress OK to continue")
            pass
        
        def updateErrorInfoWidget():
            """
            The function for inserting error details in the errorInformationSText widget (it must clear it first)
            """
            self.errorInformationSText.configure(state='normal')
            self.errorInformationSText.delete(1.0, END)
            self.errorInformationSText.insert(END, self.errorMsgContent)
            self.errorInformationSText.configure(state='disabled')
            return None
        
        def exitProgram():
            """
            The function for the 'exit program' button in the Error window
            """
            self.destroy()
            # tries by using sys.exit(0) first
            sys.exit(0)
            # if it fails, tries by raising SystemExit
            raise SystemExit(0)
            return None
        
        def continueApp():
            """
            The function for the 'continue' button in the Error window
            """
            self.destroy()
            return None

        # defining the top frame that will hold the informative label and the error image.
        self.topframe = Frame(self, height=55)
        # define inside frame widgets here....
        try:
            self.imgopen = Image.open(f"{application_path}\\err.png")
            self.imgopen = self.imgopen.resize((32,32), Image.LANCZOS)
            self.photoimgsrc = ImageTk.PhotoImage(self.imgopen)
            self.errIcoDisp = Label(self.topframe, image=self.photoimgsrc)
            self.errIcoDisp.pack(anchor=W, side=LEFT)
        except Exception as errloadingimg:
            print(f"[ERROR]: An error has occured preventing the error image from properly loading, will continue without loading it\nerror details are:\n{errloadingimg}")
            messagebox.showerror("Runtime error", f"Couldn't load 'err.png' for this window\nIt's either missing or there is something wrong with your PC\nError details are:\n{errloadingimg}\n\nPress OK to continue")
            pass

        # defining the label that tells the user that something is wrong
        self.lbl0 = Label(self.topframe, text=getCurrentLanguage().error_window_warning, font=("Arial", 9), fg='black', justify=LEFT)
        self.lbl0.pack(side=LEFT)

        self.topframe.pack(side=TOP, fill=X, expand=False, anchor=N)
        # a small configuration to ensure we can set the sizes of frames properly.
        self.pack_propagate(True)

        # defining another frame that will hold the scrolledtext widget to hold error information in.
        self.middleframe = Frame(self, height=214)
        # define inside frame (the scrolledtext widget) here
        self.errorInformationSText = scrolledtext.ScrolledText(self.middleframe, height=12.49, state='disabled')
        self.errorInformationSText.pack(fill=BOTH, expand=True)

        self.middleframe.pack(anchor=N, fill=X, expand=False)

        # defining the bottom frame (that will hold the action buttons) in it.
        self.bottomframe = Frame(self)
        # define action buttons here....
        self.exitAppBtn = ttk.Button(self.bottomframe, text=getCurrentLanguage().close_app, command=exitProgram)
        self.exitAppBtn.pack(side=RIGHT, ipadx=40, anchor=E)
        self.continueAppBtn = ttk.Button(self.bottomframe, text=getCurrentLanguage().continue_app, command=continueApp)
        self.continueAppBtn.pack(side=RIGHT, anchor=E,ipadx=40)

        self.bottomframe.pack(side=BOTTOM, expand=True, fill=BOTH)

        # updating and inserting the error information in the scrolledtext widget that holds them. 
        updateErrorInfoWidget()



if __name__ == '__main__':
    # test = ErrorWindow()
    # test.mainloop()
    # raise SystemExit(0)
    pass