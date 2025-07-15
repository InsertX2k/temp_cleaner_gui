"""
The window module that contains the class for displaying the OOBE (Out Of Box Experience) window to the user

This file/module is a part of the OOBE module
"""
from tkinter import *
from customtkinter import *
import os, sys
# initializing a variable containing the path where program executable is stored.
application_path = ''

# a quick check whether if program is a compiled bundle by pyinstaller or a simple python file.
if getattr(sys, 'frozen', False):
    # pyinstaller creates a sys attribute frozen=True during startup of pyinstaller bootloader to indicate
    # that pyinstaller has compiled (frozen) this program, then it creates a sys constant _MEIPASS containing the path
    # where the executable is found.
    application_path = f"{sys._MEIPASS}\\oobe"
else: # if program is running as a python script via python terminal
    application_path = os.path.dirname(os.path.abspath(__file__))
# fixes for searching for external modules.
os.chdir(application_path)
sys.path.append(f"{application_path}\\..")
sys.path.append(f"{application_path}")

from oobe import frames

import error



class OOBEWindow(CTk):
    def __init__(self):
        """
        A Class for the CTk window representing the OOBE Window.
        """
        super().__init__()
        # self.stageFrame = stageFrame
        self.title("Temp_Cleaner GUI")
        # storing window geometry in variables
        self.window_width: int = int(800)
        self.window_height: int = int(400)
        # retrieving screen width and height
        self.__screenwidth = self.winfo_screenwidth()
        self.__screenheight = self.winfo_screenheight()
        print(f"[DEBUG] oobewindow: screen width is: {self.__screenwidth}, screen height is: {self.__screenheight}")
        # storing window spawn location into variables
        self._window_spawn_x = (self.__screenwidth / 2) - (self.window_width / 2)
        self._window_spawn_y = (self.__screenheight / 2) - (self.window_height / 2)
        self.geometry(f"{self.window_width}x{self.window_height}+{int(self._window_spawn_x)}+{int(self._window_spawn_y)}")
        self.resizable(False, False)
        # declaring a function for changing the currently displayed frame.
        def __changeDisplayedFrame():
            """
            Changes the currently displayed frame to the next stage frame.

            This modifies the variable self.stageFrame and repacks it to fill the entire window again.

            **THIS MUST NOT BE CALLED OUTSIDE OF THE DESTROY EVENT BINDED TO THE self.stageFrame WIDGET**
            """
            # check if the stageframe is an instance of the firststage or not.
            if self.stageFrame.__class__ == frames.FirstStage:
                # we are running an instance of the firststage, therefore the frame to display after then is the second stage frame.
                print(f"[DEBUG] oobewindowchangedisplayedframe: self.stageFrame is an instance of FirstStage\nTherefore the frame to display is the SecondStage")
                # now lets change the currently displayed frame widget (self.stageFrame) to be the SecondStage.
                self.stageFrame.destroy()
                self.stageFrame = frames.SecondStage(self)
                self.stageFrame.pack(fill=BOTH, expand=True)
            elif self.stageFrame.__class__ == frames.SecondStage:
                # we are right now running the secondstage frame, therefore we will go into the third stage
                print(f"[DEBUG] oobewindowchangedisplayedframe: self.stageFrame is an instance of SecondStage\nTherefore the frame to display is the ThirdStage")
                self.stageFrame.destroy()
                # del self.stageFrame
                self.stageFrame = frames.ThirdStage(self)
                self.stageFrame.pack(fill=BOTH, expand=True)
                # now we have to change it to be the third stage.
            elif self.stageFrame.__class__ == frames.ThirdStage: # now this is the time for the last stage of the OOBE!
                print(f"[DEBUG] oobewindowchangedisplayedframe: self.stageFrame is an instance of ThirdStage\nTherefore the frame to display is the LastStage")
                self.stageFrame.destroy()
                self.stageFrame = frames.LastStage(self)
                self.stageFrame.pack(fill=BOTH, expand=True)
            elif self.stageFrame.__class__ == frames.LastStage:
                # we are right now on the last stage, we don't need anything else!
                print(f"[DEBUG] oobewindowchangedisplayedframe: self.stageFrame is an instance of LastStage")
                return True
            else: # some rare special case where the __class__ property can't be used to determine
                  # what is the current class of the self.stageFrame widget.
                print("[DEBUG] oobewindowchangedisplayedframe: self.stageFrame is not an instance of any known stages.!!!..")
                __window: error.ErrorWindow = error.ErrorWindow(f"""A rare yet critical error has occured on the OOBE window!
Technical details: 
stageFrame.__class__ = {self.stageFrame.__class__}
stageFrame.__str__ = {self.stageFrame.__str__()}
type of stageFrame = {type(self.stageFrame)}
application_path = {application_path}
config file path = {application_path}\\..\\Config.ini
os type: {os.name}
login name: {os.getlogin()}
dev null: {os.devnull}

The OOBE program can't continue...
""")
                __window.wait_window()
                try:self.destroy();del __window
                except: pass
                raise SystemExit(789) # this exit code is super rare!
                # we will return False to avoid executing other lines.
                return False
            # we have to bind this function to the destroy even of the current stageframe widget.
            # this will apply irrespective of the current stageframe class.
            self.stageFrame.bind("<Destroy>", lambda e: __changeDisplayedFrame())
            # this function returns True whenever it successes to change the currently displayed frame.
            return True


        # apply code for centering the window.
        try:
            self.iconbitmap(f"{application_path}\\..\\icon0.ico")
        except Exception as __errorLoadingIconbitmap:
            error.ErrorWindow(f"An error has occured while attempting to load the iconbitmap for the OOBE window\nError details are:\n{__errorLoadingIconbitmap}\nPress Continue to load the window without any iconbitmap")

        # displaying first stage
        self.stageFrame = frames.FirstStage(self)
        # of course it has to fill the entire window.
        self.stageFrame.pack(fill=BOTH, expand=True)
        # binding destroy event to the change displayed frame function
        self.stageFrame.bind("<Destroy>", lambda e: __changeDisplayedFrame())
        # setting window attributes to be topmost
        self.attributes("-topmost", True)


if __name__ == '__main__':
    OOBEWindow().mainloop()
    print("End of OOBE Window mainloop!")
    raise SystemExit(0)
