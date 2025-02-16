"""
A module file for informative banners that will appear on top of TCG's banner

Copyright (C) 2025 - Ziad (Mr.X) - Licensed under the same license as TCG

Icons used in this module are created by icons8.com (see icons8.com)
"""
from customtkinter import *
from tkinter import *
from PIL import ImageTk, Image

# attempting to retrieve module full path
# initializing a variable containing the path where application files are stored.
application_path = ''

# attempting to get where the program files are stored, and appending it to python syspath.
if getattr(sys, 'frozen', False): 
    # if program was frozen (compiled) using pyinstaller, the pyinstaller bootloader creates a sys attribute
    # frozen=True to indicate that the script file was compiled using pyinstaller, then it creates a
    # constant in sys that points to the directory where program executable is (where program files are).
    application_path = sys._MEIPASS
else: 
    # if program is not frozen (compiled) using pyinstaller and is running normally like a Python 3.x.x file.
    application_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(f"{application_path}")


# GLOBALS
FULLRES = "full res"
LOWRES = "low res"
FULL_RES = FULLRES
LOW_RES = LOWRES
FULLRESWIDTH = 1200
FULLRESHEIGHT = 125
FULL_RES_WIDTH = FULLRESWIDTH
FULL_RES_HEIGHT = FULLRESHEIGHT
LOWRESWIDTH = 775
LOWRESHEIGHT = 125
LOW_RES_WIDTH = LOWRESWIDTH
LOW_RES_HEIGHT = LOWRESHEIGHT
DEFAULTBANNERFGCOLOR = '#ffd800'
DEFAULT_BANNER_FG_COLOR = DEFAULTBANNERFGCOLOR
GREENFGCOLOR = '#0daf00'
GREEN_FG_COLOR = GREENFGCOLOR


class InformationBanner(CTkFrame):
    def __init__(self, master, displayIcon, headerText: str, contentText: str, functionButtonText: str, funcToCallForFuncButton, displayFuncBtn: bool=True, fgcolor=DEFAULTBANNERFGCOLOR, bannerMode=FULLRES, textFgColor='black', *args, **kwargs):
        """
        This is the full width and height version of the Information Frame
        
        Used ONLY when running TCG on displays with resolution of 1024x768 or higher
        
        This function has no optional arguments, except of course *args, and **kwargs which are redirected immediately to the parent class when initializing the frame widget.

        Required arguments are:
        
        master: the master widget that will hold this frame into, for example, TCG's main window.
        
        displayIcon: must be of type `PhotoImage`, is the variable that stores the decoded image to be displayed.
        
        headerText: must be of type `str`, and holds the text to be displayed on the top header, supports up to 57 characters only.
        
        contentText: must be of type `str`, and holds the text to be displayed like a paragraph to the bottom of the header.
        
        functionButtonText: must be of type `str`, and holds the text that has to be displayed on the button that is displayed on this frame.
        
        funcToCallForFuncButton: the function that will be called when the user clicks the button.
        
        displayFuncBtn: must be of type `bool`, and is used to determine whether the function button should be displayed or not, default value is True.
        
        bannerMode: must be of type `str`, and is used to determine the mode of the banner, either "full res" or "low res", default value is "full res".
        
        textFgColor: must be of type `str`, and is used to determine the color of the text that is displayed on the banner, default value is 'black'.
        """
        # some initialization stuff.
        self.foreground_color = fgcolor
        self.textForegroundColor = textFgColor
        self.banner_mode = str(bannerMode)
        if self.banner_mode == "low res":
            super().__init__(master=master, width=LOWRESWIDTH, height=LOWRESHEIGHT, fg_color=self.foreground_color, corner_radius=20, *args, **kwargs)
        else: # we are in HIGH RES mode.
            super().__init__(master=master, width=FULLRESWIDTH, height=FULLRESHEIGHT, fg_color=self.foreground_color, corner_radius=20, *args, **kwargs)
        # linking arguments to self
        self.displayIcon = displayIcon
        self.headerText: str = str(headerText)
        self.contentText: str = str(contentText)
        self.functionButtonText: str = str(functionButtonText)
        self.funcToCallForFunctionButton = funcToCallForFuncButton
        self.displayFuncBtn = displayFuncBtn
        # setting up the label for displaying the icon
        self.iconDisplayLabel = Label(self, image=self.displayIcon, bg=self.foreground_color, width=17, height=7, border=45)
        self.iconDisplayLabel.pack(side=LEFT, padx=10)
        # self.iconDisplayLabel.pack_propagate(False)
        # setting up labels for displaying header
        self.headingTextLabel = Label(self, text=self.headerText, font=("Arial Bold", 25), fg=self.textForegroundColor, bg=self.foreground_color, anchor=W, justify=LEFT)
        self.headingTextLabel.pack(fill=X, after=self.iconDisplayLabel, padx=10, pady=7)
        # setting up label for displaying content text
        self.contentTextLabel = Label(self, text=self.contentText, font=("Arial", 11), fg=self.textForegroundColor, bg=self.foreground_color, anchor=NW, justify=LEFT, width=65, height=4, wraplength=881)
        self.contentTextLabel.pack(after=self.headingTextLabel, padx=10, pady=7, side=LEFT, ipadx=145)
        if self.displayFuncBtn == True: # there is some actual need for displaying the function button
            # setting up the button for the function
            self.functionBtn = CTkButton(self, text=self.functionButtonText, command=self.funcToCallForFunctionButton)
            self.functionBtn.pack(after=self.contentTextLabel, side=RIGHT, padx=10, expand=False)
        else: # no need to display function button
            pass
        # -----------------------------------------------
        # setting up properties of widgets for low-res banner mode
        if self.banner_mode == "low res": # we are in LOW-RES MODE
            # for iconDisplayLabel its always the same
            self.iconDisplayLabel.configure(width=17, height=7)
            self.headingTextLabel.configure(font=("Arial Bold", 14))
            self.contentTextLabel.configure(width=20, wraplength=470)
        # -----------------------------------------------
        
        # disabling pack_propagate, this is necessary for making sure the frame maintains a constant width & height.
        self.pack_propagate(False)
        
    def update_configuration(self, displayIcon, headerText: str, contentText: str, functionButtonText: str, funcToCallForFuncButton, displayFuncBtn: bool=True, fgcolor=DEFAULTBANNERFGCOLOR, bannerMode=FULLRES, textFgColor='black'):
        """
        Changes the Information Banner properties, this could be for example it's displayIcon or headerText.
        
        Required arguments are:
        
        displayIcon: must be of type `PhotoImage`, is the variable that stores the decoded image to be displayed.
        
        headerText: must be of type `str`, and holds the text to be displayed on the top header, supports up to 57 characters only.
        
        contentText: must be of type `str`, and holds the text to be displayed like a paragraph to the bottom of the header.
        
        functionButtonText: must be of type `str`, and holds the text that has to be displayed on the button that is displayed on this frame.
        
        funcToCallForFuncButton: the function that will be called when the user clicks the button.
        
        displayFuncBtn: must be of type `bool`, and is used to determine whether the function button should be displayed or not, default value is True.
        
        bannerMode: must be of type `str`, and is used to determine the mode of the banner, either "full res" or "low res", default value is "full res".
        
        textFgColor: must be of type `str`, and is used to determine the color of the text that is displayed on the banner, default value is 'black'.
        
        fgcolor: must be of type `str`, and is used to determine the color of the banner, default value is '#ffd800' (or DEFAULTBANNERFGCOLOR)
        
        returns True if successed in updating banner properties, otherwise returns False
        """
        def __functionBtnDestroyFunc():
            if self.functionBtn.winfo_exists() == True:
                try:
                    self.functionBtn.destroy()
                except:
                    pass
        try:
            _forecolor = fgcolor
            self.configure(fg_color=_forecolor, require_redraw=False)
            # self.configure(fg=_forecolor, require_redraw=True)
            self.iconDisplayLabel.configure(bg=_forecolor)
            self.iconDisplayLabel.configure(image=displayIcon)
            self.headingTextLabel.configure(text=headerText, fg=textFgColor, bg=_forecolor)
            self.contentTextLabel.configure(text=contentText, fg=textFgColor, bg=_forecolor)
            if displayFuncBtn == True: # there is some actual need for displaying the function button
                __functionBtnDestroyFunc() # to destroy first
                self.functionBtn = CTkButton(self, text=functionButtonText, command=funcToCallForFuncButton)
                self.functionBtn.pack(after=self.contentTextLabel, side=RIGHT, padx=10, expand=False)
            else: # no need to display function button
                __functionBtnDestroyFunc()
            if bannerMode == "low res":
                self.configure(width=LOWRESWIDTH, height=LOWRESHEIGHT, require_redraw=True)
                self.iconDisplayLabel.configure(width=17, height=7)
                self.headingTextLabel.configure(font=("Arial Bold", 14))
                self.contentTextLabel.configure(width=20, wraplength=470)
            else: # we are in HIGH RES mode.
                self.configure(width=FULLRESWIDTH, height=FULLRESHEIGHT, require_redraw=True)
            return True
        except:
            return False
        
        
        return True
        # except:
        #     return False
        
        
        
        
if __name__ == '__main__':
    # class testWindow(CTk):
    #     def __init__(self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         self.title("Test Window")
    #         self.geometry("1200x800")
    #         self.resizable(True, True)
    #         # declaring PhotoImage object for the icon
    #         # self.iconObjFile = Image.open(f"{application_path}\\updatefb.png")
    #         # self.iconObj = ImageTk.PhotoImage(self.iconObjFile)
    #         # self.iconObj = self.iconObj.subsample(1,1)
    #         # self.iconObj = self.iconObj.subsample(2, 2)
    #         self.iconObj = PhotoImage(file=f"{application_path}\\correctfb.png")
    #         # self.iconObj_edit = self.iconObj.configure(width=250, height=7)
    #         self.iconObj = self.iconObj.subsample(2, 2)
            
    #         # everything is done, only internal testing is what's required.
    #         self.show_banner = InformationBanner(self, self.iconObj, "You're all set!", "Your PC is probably clean and you may not need to run any cleaning functions, and your current installation of Temp_Cleaner GUI is up-to-date!", "Update Now!", None, displayFuncBtn=False, bannerMode=FULLRES, fgcolor=GREEN_FG_COLOR)
    #         self.show_banner.pack()
    
    # testWindow().mainloop()
    # raise SystemExit(0)
    pass