"""
Provides the classes and functions related to the 'Donators list' window of Temp_Cleaner GUI

This file (as it is) belongs to Temp_Cleaner GUI and is a part of it and shouldn't be redistributed outside of it.
"""
# imports
from tkinter import *
from tkinter import ttk, scrolledtext, messagebox
from customtkinter import *
import configparser
from translations import *
from awesometkinter import DEFAULT_COLOR
from PIL import ImageTk, Image
import urllib.request
import threading
import webbrowser


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


# declaring other variables that are important to the functionality of this module.
donators_list_mrx_server = "https://raw.githubusercontent.com/InsertX2k/software-versions/main/donators.txt"
donators_list_file_local_path = f"{application_path}\\donators.txt"

try:
    # Defining the function that will get the current values of an configparser values.
    GetConfig = configparser.ConfigParser()
    GetConfig.read(f'{application_path}\\Config.ini')
except Exception as _errorReadingCFGParser:
    print(f"[ERROR]: from donators module: couldn't load from configparser:error details are\n{_errorReadingCFGParser}")
    raise SystemExit(255)

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




class DonatorsWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title(getCurrentLanguage().donators)
        width = 672
        height = 310
        self.geometry(f'{width}x{height}')
        self.minsize(width, height)
        self.maxsize(width, height)
        self.resizable(False, False) # window isn't resizable
        self.wm_resizable(False, False) # instructing wm that window isn't resizable.
        # disabling HiDPi awareness (see <https://sourceforge.net/p/temp-cleaner-gui/tickets/1/>)
        deactivate_automatic_dpi_awareness()
        self.attributes('-topmost',True)
        # set_appearance_mode("dark") # theme mode is always dark.

        try:
            self.iconbitmap(f"{application_path}\\donators.ico")
        except Exception as errorLoadingIconBitmap:
            messagebox.showerror("ERROR in Mainloop thread", f"Couldn't load the iconbitmap for this window due to the exception:\n{errorLoadingIconBitmap}\nPress OK to acknowledge this event and continue running the program.")
            pass


        def downloadDonatorsListFileFromServer(serverURL=donators_list_mrx_server, textWidgetToShowDataIn=None):
            """
            Downloads the donators list file from Github Server and shows it in the scrolledtext widget specified in textWidgetToShowDataIn.

            This function can return two values and in two different cases:
            
            False -> when an error occurs while trying to retrieve the list from the server.

            True -> when it successfully inserts the text of the list to the widget specified.
            """
            textWidgetToShowDataIn = self.donators_list
            try:
                with urllib.request.urlopen(serverURL) as fileFromServer:
                    donatorsList = fileFromServer.read().decode('utf-8')
                    textWidgetToShowDataIn.configure(state='normal')
                    textWidgetToShowDataIn.delete(1.0, END)
                    textWidgetToShowDataIn.insert(END, f"{donatorsList}")
                    textWidgetToShowDataIn.configure(state='disabled')
                return True
            except Exception:
                textWidgetToShowDataIn.configure(state='normal')
                textWidgetToShowDataIn.delete(1.0, END)
                textWidgetToShowDataIn.insert(END, f"{getCurrentLanguage().couldnt_download_donators_list}")
                textWidgetToShowDataIn.configure(state='disabled')
                return False

        def multithreadingRunDownloadFromServerFunction():
            """
            Uses the multi-threading capability to run the downloadDonatorsListFileFromServer function

            USE THIS INSTEAD OF THE FUNCTION downloadDonatorsListFileFromServer WHEN IN USE WITH MAIN GUI FUNCTIONS.
            """
            threading.Thread(target=downloadDonatorsListFileFromServer).start()
            pass
        

        def closeWindow():
            """
            A function for the button "OK"
            """
            self.destroy()
            return
        
        def openBrowserAndDonate():
            """
            A function used for the "Donate..." button in this window.
            """
            webbrowser.open("https://insertx2k.github.io/temp_cleaner_gui/downloads.html")
            return

        

        self.configure(bg=DEFAULT_COLOR)
        try:
            set_default_color_theme(f"{application_path}\\style.json")
        except Exception as errorLoadingCustomThemeFile:
            print(f"couldn't load the default theme file 'style.json' due to an exception:{errorLoadingCustomThemeFile}")
            messagebox.showerror("ERROR in Mainloop thread", f"Couldn't load theme file 'style.json' due to an exception\nException details are:\n{errorLoadingCustomThemeFile}\n\nPlease press OK to close this window.")
            self.destroy()
        
        self.godonate_btn = CTkButton(self, text=getCurrentLanguage().donate, command=openBrowserAndDonate, width=180, height=30)
        self.godonate_btn.place(x=207, y=270)

        self.ok_btn = CTkButton(self, text=getCurrentLanguage().ok, command=closeWindow, width=180, height=30)
        self.ok_btn.place(y=270, x=480)
        
        self.image_processor = Image.open(f"{application_path}\\donators.png")
        self.image_processor = self.image_processor.resize((200, 400))
        self.imagetk_processor = ImageTk.PhotoImage(self.image_processor)

        self.bgLbl = Label(self, text='', image=self.imagetk_processor, bg='#333')
        self.bgLbl.place(x=0, y=0)

        # declaring other widgets.
        self.lbl0 = Label(self, text=getCurrentLanguage().donators, bg='#333', fg='white', font=("Arial Bold", 15))
        self.lbl0.place(x=207, y=5)
        self.lbl1 = Label(self, text=getCurrentLanguage().thx_donators, bg='#333', fg='white', font=("Arial", 11), justify=LEFT)
        self.lbl1.place(x=207, y=33)

        # declaring the scrolledtext widget used to show the data from server.
        self.donators_list = scrolledtext.ScrolledText(self, background='#333', highlightcolor='orange', foreground='white', font=("Arial", 10))
        self.donators_list.place(x=207, y=75, relwidth=0.68, relheight=0.60)
        self.donators_list.configure(state='normal')
        self.donators_list.delete(1.0, END)
        self.donators_list.insert(END, f"{getCurrentLanguage().list_of_donators_is_loading}")
        self.donators_list.configure(state='disabled')

        multithreadingRunDownloadFromServerFunction()
        







if __name__ == '__main__':
    # process = DonatorsWindow()
    # process.mainloop()
    raise Exception("This file isn't a standalone executable, it is a module that is intended to be used in Temp_Cleaner GUI's main executable.")