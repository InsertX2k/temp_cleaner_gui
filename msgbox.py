"""
Alternative MessageBox Implementation for Temp_Cleaner GUI

Provides necessary classes to deploy a messagebox with timeout and default selection after the timeout.

Copyright (C) 2025 - Ziad (Mr.X) for Temp_Cleaner GUI, Licensed under the same license as Temp_Cleaner GUI
"""
# imports
from tkinter import *
from customtkinter import *
import os, sys, ctypes, threading
from configparser import ConfigParser
import error
from translations import *
from time import sleep

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
# fixes for searching for external modules.
os.chdir(application_path)
# appending Application path to sys.path, necessary for solving imports.
sys.path.append(f"{application_path}")

# some constants
WHITE_COLOR = '#f1f1f1'

# reserved for a custom terminatable thread.
def _async_raise(tid, exctype=error.UserInitiatedThreadStop):
    """
    Raises an exception in the threads with ID using ExceptionType defined

    `tid` -> is the ID (identification number) of the thread you want to raise the Exception in

    `exctype` -> Is the class/object of the Exception you want to raise in the thread.
    """
    # if not threading.inspect.isclass(exctype):
    #     raise TypeError("Only types can be raised (not instances)")
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid),
                                                    ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # "if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


class ControllableThread(threading.Thread):
    def __init__(self, *args, **kwargs) -> None:
        """
        A class for a thread that can be stopped manually (or automatically) within any parts of the program

        It has all the following functions:
        
        `_get_my_tid()` -> Returns the current Thread ID (Identification Number)

        `raiseExc()` -> Used to raise an Exception in the current thread.

        Used primarly in the cleaning thread but may be later used in any parts of the program
        """
        super(__class__, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()
    
    def _get_my_tid(self):
        """determines this (self's) thread id

        CAREFUL: this function is executed in the context of the caller
        thread, to get the identity of the thread represented by this
        instance.
        """
        if not self.is_alive():
            raise threading.ThreadError("the thread is not active")

        # do we have it cached?
        if hasattr(self, "_thread_id"):
            return self._thread_id

        # no, look for it in the _active dict
        for tid, tobj in threading._active.items():
            if tobj is self:
                self._thread_id = tid
                return tid

        # TODO: in python 2.6, there's a simpler way to do: self.ident

        raise AssertionError("could not determine the thread's id")

    def raiseExc(self):
        """Raises the default exception type `UserInitiatedThreadStop` in the context of this thread.

        If the thread is busy in a system call (time.sleep(),
        socket.accept(), ...), the exception is simply ignored until the another command is executed

        If you are sure that your exception should terminate the thread,
        one way to ensure that it works is:

            t = ThreadWithExc( ... )
            ...
            t.raiseExc( SomeException )
            while t.isAlive():
                time.sleep( 0.1 )
                t.raiseExc( SomeException )

        If the exception is to be caught by the thread, you need a way to
        check that your thread has caught it.

        CAREFUL: this function is executed in the context of the
        caller thread, to raise an exception in the context of the
        thread represented by this instance.
        """
        _async_raise(self._get_my_tid())



# getting the default appearance mode.
def retrieveCurrentAppearanceMode():
    """
    Retrieves the current appearance mode from the configuration file stored in 
    the program's configuration file (named Config.ini)

    Returns a tuple of two values, the first value represents the background color, and the 
    second value represents the foreground color, in this syntax (bg_color, fg_color)

    **!!!NEVER USE WITHOUT IMPLEMENTING EXCEPTION HANDLING TO IT!!!**
    """
    # make configparser access the configuration file.
    cfg_file: ConfigParser = ConfigParser()
    cfg_file.read(f"{application_path}\\Config.ini")
    
    if str(cfg_file["ProgConfig"]["appearancemode"]) == "1": # LIGHT MODE
        # syntax is (bg_color, fg_color)
        # configuring CTk Framework's appearance mode.
        set_appearance_mode("light")
        return (WHITE_COLOR, 'black')
    else: # we are definitely in dark mode
        set_appearance_mode("dark")
        return ('#333', 'white')
    
    return (None, None)

def retrieveCurrentLanguage():
    """
    Returns the current class according to the display language selected in the configuration file.
    
    This returns a class (like en, ar) or whenever an exception occurs it will return the en class

    **!!!NEVER USE WITH EXCEPTION HANDLING, IT ALREADY HAS AN IN-BUILT ONE!!!**
    """
    try:
        cfg_file: ConfigParser = ConfigParser()
        cfg_file.read(f"{application_path}\\Config.ini")
    except Exception as __curErr:
        __window = error.ErrorWindow(f"""An Exception has occured while attempting to open the program configuration file.
Current execution stage is: msgbox.retrieveCurrentLanguage() - at reading config file.
More error details are:
{__curErr}

Click any button of the two below to exit this program with code 258.
""")
        __window.wait_window()
        del __window;del __curErr
        raise SystemExit(258)
    
    try:
        if str(cfg_file["ProgConfig"]["languagesetting"]) == "ar":
            return ar
        else:
            return en
    except:
        pass
    return en


class YesNoMsgBox(Toplevel):
    """
    A custom messagebox of type CTkToplevel that supports a timeout feature and
    a default action to be done after the timeout.

    Attributes:
        title (str): The title of the messagebox.
        message (str): The message to be displayed in the messagebox.
        default (str): The default button after the timeout, must be either "yes" or "no"
        timeout (int): The duration in seconds before the default button is selected.

    Supports the same args and keyword arguments of the CTkToplevel widget.
    """
    def __init__(self, title: str, message: str, timeout:int, default: str="yes", *args, **kwargs):
        global retrieveCurrentAppearanceMode
        super().__init__(*args, **kwargs)
        # configure window title.
        self.title(title)
        # linking arguments to self
        self.message = str(message)
        self.timeout = int(timeout)
        self.default = str(default).lower()
        # a variable that will be modified and will have to be accessed when the msgbox is destroyed
        # this, holds the actual selection value, like "yes" or "no", because we can't really return
        # a value from the __init__ function.
        # NOTE: "none" means the window hasn't started yet, or is currently waiting for a user prompt.
        self.selection: str = "none"
        # let's load some icon bitmap
        def processTimeOut():
            """
            Waits for the specified timeout, then return the default value and modify 
            the selection variable to contain it, finally, destroy the messagebox.
            """

            __default_value: str = self.default
            __timeout: int = self.timeout
            # wait for the specified timeout.
            sleep(__timeout)
            # we need to check after the timeout if the user has already pressed any of the buttons (yes or no)
            # because if they did, we won't need to continue executing this function already.
            # otherwise, we can continue.
            if self.selection != "none":
                return
            # modify the selection variable to the default value.
            self.selection = __default_value
            # print(self)
            try: self.after(0, self.destroy)
            except: pass
            # except: pass
            return __default_value

        try:
            self.iconbitmap(f"{application_path}\\icon0.ico")
        except Exception as __errLoadingIcoBitmap:
            error.ErrorWindow(f"An Exception has occured while attempting to load the iconbitmap for this window!\nError details are:\n{__errLoadingIcoBitmap}\nPress Continue to close this window")
            pass
        # setting the window size and position
        self.window_width = 600
        self.window_height = 200
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.window_spawnx = (self.screen_width / 2) - (self.window_width / 2)
        self.window_spawny = (self.screen_height / 2) - (self.window_height / 2)
        self.geometry(f"{self.window_width}x{self.window_height}+{int(self.window_spawnx)}+{int(self.window_spawny)}")
        self.resizable(False, False)
        # setting the window as always on top.
        self.attributes("-topmost", True)
        # configuring window background color
        try:
            self.configure(bg=retrieveCurrentAppearanceMode()[0])
        except Exception as __errLoadingColorMode:
            __window = error.ErrorWindow(f"""An Exception has occured while attempting to load the current appearance mode from the configuration file.
Current stage is: msgbox.YesNoMsgBox.configure() @ changing background.

Error details are:
{__errLoadingColorMode}

Click any buttons below to close this application with exit code 620!
""")
            try: __window.wait_window()
            except: pass
            raise SystemExit(620)

        # lets load the color theme
        try:
            set_default_color_theme(f"{application_path}\\style.json")
        except Exception as __errLoadingColorTheme:
            __window = error.ErrorWindow(f"""An error has occured while attempting to load the color theme for this window.
Current stage is: msgbox.YesNoMsgBox.__init__() @ set_default_color_theme()
Error details are:
{__errLoadingColorTheme}

Click any buttons below to close this application with exit code 269.
""")
            try: __window.wait_window();del __window
            except: pass
            raise SystemExit(269)

        # we need to construct widgets.
        # storing all widgets (like the label to show question mark and the question text) in a frame
        self.mainFrame = Frame(self, bg=retrieveCurrentAppearanceMode()[0])
        # declaring necessary frames to show the question mark to the user.
        self.qMarkShowLabel = Label(self.mainFrame, bg=retrieveCurrentAppearanceMode()[0], text='')
        # lets load the image 'question.png' onto it
        self.qMarkShowImg = PhotoImage(file=f"{application_path}\\question.png").subsample(2,2)
        # self.qMarkShowImg = self.qMarkShowImg.subsample(1,1)
        self.qMarkShowLabel.configure(image=self.qMarkShowImg)
        self.qMarkShowLabel.pack(side=LEFT, padx=15, pady=15, anchor=N)
        # declaring text showing label.
        self.msgShowLabel = Label(self.mainFrame, text=self.message, bg=retrieveCurrentAppearanceMode()[0], fg=retrieveCurrentAppearanceMode()[1], font=("Arial", 13), wraplength=508, justify=LEFT)
        self.msgShowLabel.pack(side=LEFT, anchor=N, padx=0, pady=15)
        self.mainFrame.pack(anchor=N)
        # self.mainFrame.pack_propagate(False)
        # declaring a frame to hold the action buttons (yes or no)
        self.actionButtonsFrame = Frame(self, bg=retrieveCurrentAppearanceMode()[0], width=600, height=50)
        # appending some buttons
        self.yes_btn = CTkButton(self.actionButtonsFrame, text=retrieveCurrentLanguage().yes, command=lambda: self.closeMsgBox("yes"))
        self.yes_btn.pack(side=LEFT, padx=100)
        self.no_btn = CTkButton(self.actionButtonsFrame, text=retrieveCurrentLanguage().no, command=lambda: self.closeMsgBox("no"))
        self.no_btn.pack(side=LEFT, padx=20)
        self.actionButtonsFrame.pack(anchor=S, side=BOTTOM, fill=X, pady=15)
        # self.actionButtonsFrame.pack(fill=X, expand=True, side=BOTTOM, anchor=N)
        self.actionButtonsFrame.pack_propagate(False)
        self.timeOutProcessingThd = ControllableThread(target=processTimeOut, daemon=True, name="MSGBOXTIMEOUTTHD0")
        self.timeOutProcessingThd.start()
    
    def closeMsgBox(self, value: str):
        """
        Closes the displayed messagebox and modify the variable that stores the current selection.

        Arguments:

            value (str): is the value to be returned and stored into the selection variable
        
        Returns the value given as an argument/parameter.
        """
        # modify the selection variable to the given value in the parameter.
        self.selection = str(value)
        try: self.destroy()
        except: pass
        return value



if __name__ == '__main__':
    pass
