"""
The module for the window that asks user to connect their Android (7.0+) to PC via USB Cable
"""

# imports
from tkinter import *
from tkinter import ttk, messagebox
from customtkinter import *
import os, sys, configparser
from PIL import Image, ImageTk
import time
import threading
from subprocess import getoutput
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

print(f"[DEBUG]: connection_window module located at: {application_path}")
# fixes for translations module outside of cwd.
sys.path.append(f"{application_path}\\..")
from translations import *

try:
    # opening a configparser session for reading from the file 'Config.ini'
    GetConfig = configparser.ConfigParser()
    GetConfig.read(f"{application_path}\\..\\Config.ini")
    # ------------------------
except Exception as errorReadingConfigFile:
    messagebox.showerror("Runtime error", f"It seems like one of the necessary files to make Temp_Cleaner GUI work are missing, double check that the file 'Config.ini' exists in the directory where this program exists and try again\n\nError details for technical support:\n{errorReadingConfigFile}")
    raise SystemExit(255)

adb_exe_path = f"{application_path}\\adb\\adb.exe"

def requestADBConnection():
    """
    Requests an ADB Connection to the currently connected Android smartphone.
    
    Returns the output of the ADB connection command.
    """
    global adb_exe_path
    adb_connection_cmd_out = getoutput(f"{adb_exe_path} usb")
    return adb_connection_cmd_out

def killADBDaemon():
    """
    Requests to kill the currently running ADB Daemon
    
    Returns the output of the kill ADB Daemon command
    """
    global adb_exe_path
    adb_kill_daemon_cmd = getoutput(f"{adb_exe_path} kill-server")
    return adb_kill_daemon_cmd




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

def getTextJustification(currentLanguageStr=GetConfig["ProgConfig"]["languagesetting"]):
    """
    Returns the appropriate text direction according to current UI Language.
    """
    try:
        if str(currentLanguageStr) == "en":
            return 'left'
        elif str(currentLanguageStr) == "ar":
            return 'right'
        else:
            return 'left'
    except Exception as exception_reading_config_file:
        messagebox.showerror("An ERROR has occured",f"Couldn't read from 'Config.ini'\nException details:\n{exception_reading_config_file}\nPress OK to close this program")
        return None



class ConnectPhoneToPCWindow(Tk):
    global getTextJustification, killADBDaemon, requestADBConnection
    def __init__(self):
        super().__init__()
        self.title(f"{getCurrentLanguage().connect_phone_to_pc}")
        self.appwidth = 605
        self.appheight = 617
        self.spawn_x = (int(self.winfo_screenwidth()) / 2) - (self.appwidth / 2)
        self.spawn_y = (int(self.winfo_screenheight()) / 2) - (self.appheight / 2)
        self.geometry(f'{self.appwidth}x{self.appheight}+{int(self.spawn_x)}+{int(self.spawn_y)}') # spawns in the middle of the screen.
        self.resizable(False, False)
        self.wm_resizable(False, False)
        try:
            set_default_color_theme(f"{application_path}\\..\\style.json")
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
            self.iconbitmap(f"{application_path}\\connect_usb.ico")
        except Exception as errorLoadingIconBitmap:
            print(f"An exception has occured while attempting to load iconbitmap for the 'Connect Phone to PC Window'\nError details are:\n\n{errorLoadingIconBitmap}")
            messagebox.showerror("Error", f"An exception has occured while attempting to load iconbitmap for 'connectphonetopc' window\nError details are:\n\n{errorLoadingIconBitmap}")
            pass
        
        self.configure(bg=getCurrentAppearanceMode()[0])
        
        self.lbl0 = Label(self, text=getCurrentLanguage().connect_phone_via_cable, font=("Arial Bold", 18), bg=getCurrentAppearanceMode()[0], fg=getCurrentAppearanceMode()[1], justify=getTextJustification())
        self.lbl0.pack(expand=False)
        
        self.lbl1 = Label(self, text=getCurrentLanguage().adb_instructions_header, font=("Arial", 11), bg=getCurrentAppearanceMode()[0], fg=getCurrentAppearanceMode()[1], justify=getTextJustification())
        self.lbl1.pack(expand=False)
        
        self.instructions_list = Label(self, text=getCurrentLanguage().instructions_for_adb_connection, font=("Arial", 11), bg=getCurrentAppearanceMode()[0], fg=getCurrentAppearanceMode()[1], justify=getTextJustification())
        self.instructions_list.pack(expand=False, anchor=NW)
        
        self.instructions_gif = Label(self, bg=getCurrentAppearanceMode()[0], border=0, highlightthickness=0, height=340)
        self.instructions_gif.pack(anchor='center')
        self.instructions_gif_frames = self._getframes(f"{application_path}\\instructions.gif")
        
        def continueBtnFunction():
            self.destroy()
        
        def onWindowSpawnCommands():
            """
            Runs the commands that has to be executed upon a successful window spawn.
            Must be ran under a separate thread.
            """
            _tmp = killADBDaemon()
            print(_tmp)
            _tmp = requestADBConnection()
            print(_tmp)
            del _tmp
            return
        
        
        self.continue_btn = CTkButton(self, text=getCurrentLanguage().continue_connection_window_btn, command=continueBtnFunction)
        self.continue_btn.pack(ipadx=70)
        
        def changeGifFramesThreaded(frames=self.instructions_gif_frames):
            """
            This is a threaded function that loops over every frame and then changes the instructions label to contain each new frame.
            
            THIS MUST RUN AS A SEPARATE THREAD ASIDE FROM THE MAINLOOP THREAD.
            """
            err = 0
            while True:
                for frame in frames:
                    try:
                        self.instructions_gif.config(image=frame)
                    except:
                        err = 1
                        break
                    time.sleep(0.085)
                if err == 1:
                    break
                else:
                    pass
            return None
        
        threading.Thread(target=changeGifFramesThreaded, name="GIFPLAYERTHREAD0").start()
        threading.Thread(target=onWindowSpawnCommands, name="OnWindowSpawnADBShellCmds").start()
        

    def _getframes(self, img):
        global Image, ImageTk
        with Image.open(img) as gif:
            index = 0
            frames = []
            while True: # idk how many frames my gif is
                try:
                    gif.seek(index)
                    frame = ImageTk.PhotoImage(gif)
                    frames.append(frame)
                except EOFError:
                    break
                
                index +=1
            return frames
    
    def getCurThread(self):
        """
        Returns the current thread as a Thread object
        """
        return threading.current_thread()



if __name__ == '__main__':
    # ConnectPhoneToPCWindow().mainloop()
    # raise SystemExit(0)
    pass