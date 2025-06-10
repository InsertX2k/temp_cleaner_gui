"""
The module that contains all the frames to be displayed as stages of the OOBE (Out Of Box Experience) Window

Licensed under the same license as Temp_Cleaner GUI
"""
from tkinter import *
from customtkinter import *
import os, sys
from PIL import IcoImagePlugin, ImageTk, Image
# ConfigParser object
from configparser import ConfigParser

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
sys.path.append(f"{application_path}\\..")
sys.path.append(f"{application_path}")

# necessary for exception handling.
import error
from translations import *

WHITE_COLOR = '#f1f1f1'

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
    cfg_file.read(f"{application_path}\\..\\Config.ini")
    
    if str(cfg_file["ProgConfig"]["appearancemode"]) == "1": # LIGHT MODE
        # syntax is (bg_color, fg_color)
        return (WHITE_COLOR, 'black')
    else: # we are definitely in dark mode
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
        cfg_file.read(f"{application_path}\\..\\Config.ini")
    except Exception as __curErr:
        __window = error.ErrorWindow(f"""An Exception has occured while attempting to open the program configuration file.
Current execution stage is: frames.retrieveCurrentLanguage() - at reading config file.
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


class FirstStage(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        """
        This is the frame that is supposed to appear to the user as the first stage of the OOBE Screen

        It is supposed to welcome the user, then ask them to choose a display language for Temp_Cleaner GUI

        Takes the same args, and kwargs as a CTkFrame

        Requires master argument, which represents the window or parent that holds the frame
        """
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.configure(bg_color=WHITE_COLOR)
        self.configure(fg_color=WHITE_COLOR)
        try:
            # will attempt to load style.json from application_path
            set_appearance_mode("light")
            set_default_color_theme(f"{application_path}\\..\\style.json")
        except Exception as __errorLoadingStyle:
            print(f"[DEBUG] firststageframe: an error has occured while attempting to load style file: {__errorLoadingStyle}")


        # =================================================================
        # reserved for welcome header.
        self.welcomeHeader = CTkFrame(self, bg_color='black', fg_color=WHITE_COLOR, corner_radius=15, border_width=0.755)

        # loading tcg icon into memory.
        self.tcgicon_ico = IcoImagePlugin.IcoImageFile(f"{application_path}\\..\\icon0.ico").resize((40, 40))
        self.tcgicon_tk = ImageTk.PhotoImage(self.tcgicon_ico)

        self.tcglogo = Label(self.welcomeHeader, image=self.tcgicon_tk , font=("Arial Bold", 10), bg=WHITE_COLOR, fg=WHITE_COLOR, width=40, height=40)
        self.tcglogo.pack(side=LEFT, anchor=W, padx=3)

        self.welcomeLabel = Label(self.welcomeHeader, text="Welcome!", font=("Arial Bold", 25), bg=WHITE_COLOR, fg='black', borderwidth=2)
        self.welcomeLabel.pack(side=LEFT, anchor=NE, fill=X, expand=True, padx=10, pady=20)

        self.welcomeHeader.pack(fill=X, expand=False)
        # =================================================================

        self.welcomeFrameDescription = Label(self, text=en.oobe_first_stage_info, font=("Arial", 13), bg=WHITE_COLOR, fg='black', justify=LEFT, wraplength=780)
        self.welcomeFrameDescription.pack(pady=35)

        self.language_chooser_combobox = CTkComboBox(self, width=145, height=33, fg_color=WHITE_COLOR, text_color='black', text_color_disabled='red', button_color=WHITE_COLOR, border_color=WHITE_COLOR, justify=CENTER, values=['English', 'العربية'],dropdown_fg_color='grey35', command=self.__changeTextToTargetLanguage,dropdown_text_color='white')
        self.language_chooser_combobox.pack(expand=False)

        self.continueBtn = CTkButton(self, command=self.__destroyFrameAndSaveChanges, text=self._getChosenLanguage().oobe_continue_btn)
        self.continueBtn.pack()
    

    def __destroyFrameAndSaveChanges(self) -> None:
        """
        The function to be binded to the 'Continue' button.

        Changes the language mode in 'Config.ini' file (opens the file then saves changes to it then closes the file).
        """
        FUNC_NAME = "OOBEWindow.FirstStage.__destroyFrameAndSaveChanges()"
        # IMPLEMENT ACTUAL FUNCTIONALITY
        # open config.ini file
        # check if chosen language is 'العربية' or 'English' and write the appropriate lines to config.ini
        #    as follows:                ar          en     
        # then close the file, delete the variables used from memory using 'del' keyword.
        # FINALLY, destroy the frame, and return None (just type return)
        try:
            try:
                configFile: ConfigParser = ConfigParser()
                configFile.read(f"{application_path}\\..\\Config.ini")
            except Exception as __errorReadingCFG: 
                __errwindow = error.ErrorWindow(f"An error has occured during the execution of the function {FUNC_NAME}\nCouldn't read from {application_path}\\..\\Config.ini\nError details are:\n{__errorReadingCFG}\nPress any button to close the OOBE Window")
                __errwindow.wait_window()
                try: self.master.destroy(); raise SystemExit(255)
                except: raise SystemExit(255) # will raise SystemExit 255 both ways.
        
            # print(configFile) -> configparser object
            # for key in configFile['ProgConfig']:
                # print(f"{key}={configFile['ProgConfig'][key]}")
            
            print(f"[DEBUG] __destroyFrameAndSaveChanges, stage-1: current language setting in configuration file is: {configFile['ProgConfig']['languagesetting']}")
            # now lets get the currently selected language setting.
            __usrChosenLang: str = str(self.language_chooser_combobox.get())
            print(f"[DEBUG] __destroyFrameAndSaveChanges, stage-1: current user selected language is: {str(self.language_chooser_combobox.get())}")
            if __usrChosenLang == 'العربية':
                # user has selected arabic language.
                print(f"[DEBUG] __destroyFrameAndSaveChanges, stage-1: user has selected arabic language.")
                configFile['ProgConfig']['languagesetting'] = 'ar'
            else:
                # user has selected english language.
                print(f"[DEBUG] __destroyFrameAndSaveChanges, stage-1: user has selected english language or may not have selected a supported language.")
                configFile['ProgConfig']['languagesetting'] = 'en'
            try:
                # now let's finalize writing things to the configuration file.
                with open(f"{application_path}\\..\\Config.ini", 'w') as configFileWriter:
                    configFile.write(configFileWriter)
                configFileWriter.close() # freeing up resources.
                print(f"[DEBUG] __destroyFrameAndSaveChanges, stage-1: successfully wrote changes to the configuration file.")
                # free up some memory.
                del configFile 
                self.destroy() # destroy the frame.
                return None
            except Exception as __errorWritingCFG:
                __errwindow = error.ErrorWindow(f"An exception has occured during the execution of the function '{FUNC_NAME}'\nThis error occured while attempting to save data into the Config file\nError details are: {__errorWritingCFG}\nPress any of the two buttons to close the OOBE Window!")
                __errwindow.wait_window()
                try: self.master.destroy();raise SystemExit(355)
                except: raise SystemExit(355)
        except Exception as __generalErrorInContinueBtnFunc: # an exception occurs in other states except in reading and writing to the CFG file.
            print(f"[DEBUG] __destroyFrameAndSaveChanges, stage-1: an error has occured during the execution of this function.\nError details are:\n{__generalErrorInContinueBtnFunc}")
            # now lets show the user an error message.
            error.ErrorWindow(f"An error has occured during the execution of the function '{FUNC_NAME}'\nError details are:\n{__generalErrorInContinueBtnFunc}\nPress any button to close the OOBE Window")
            # will give destroying master a try.
            try: self.master.destroy()
            except: pass
            return None


    def _getChosenLanguage(self):
        """
        Returns the appropriate class for strings based on the selected language on the chooser widget

        Returns a class
        """
        if str(self.language_chooser_combobox.get()) == 'العربية':
            return ar
        else:
            return en

    def __changeTextToTargetLanguage(self, *args):
        """
        Changes the display language of all text elements in the frame to the target language specified in the language chooser combobox widget

        Must be strictly binded to the function of the language chooser combobox widget 
        """
        print(f"[DEBUG] firststageframe: changing display language for all text widgets to: {self.language_chooser_combobox.get()}")
        # changing the text of the welcome label
        if str(self.language_chooser_combobox.get()) == 'العربية':
            self.welcomeLabel.config(text="مرحباً!")
        else:
            self.welcomeLabel.config(text="Welcome!")
        
        # changing the text of the welcome frame description
        self.welcomeFrameDescription.config(text=self._getChosenLanguage().oobe_first_stage_info)
        self.continueBtn.configure(text=self._getChosenLanguage().oobe_continue_btn)
        print(f"[DEBUG] firststageframe: changed display language for all text widgets to: {self.language_chooser_combobox.get()}, FUNCTION FINISHED EXECUTION.")
        return


class SecondStage(CTkFrame):
    # initialize it by using def __init__(self, parent, *args, **kwargs)
    # then add functions to retrieve current language and appearance mode from Config.ini in application_path
    # then add widgets (including a good looking screenshot to show the user how the program looks like on every
    # appearance mode), then add a button to continue to the next stage.
    # it should then save the changes to the Config.ini file.
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.args = args
        self.kwargs = kwargs

        def __updateSwitchesAccordingToAppMode() -> None:
            """
            A Function to be called at the spawn/declare of this frame to update the switches
            to represent the currently saved appearance mode, and to update the CTK theme mode.
            """
            try:
                # will deselect both switches first.
                self.lightmode_switch.deselect()
                self.darkmode_switch.deselect()
                # now lets read the current appearance mode from the configuration file.
                __cfgparserobj: ConfigParser = ConfigParser()
                __cfgparserobj.read(f"{application_path}\\..\\Config.ini")
                # now to the actual checks.
                if str(__cfgparserobj["ProgConfig"]["appearancemode"]) == "1":
                    # we are currently in light mode.
                    # therefore, we gotta toggle ONLY the light mode switch.
                    self.lightmode_switch.select()
                    # now let's change the appearance mode in CTk Framework.
                    set_appearance_mode("light")
                elif str(__cfgparserobj["ProgConfig"]["appearancemode"]) == "2":
                    # we are currently in dark mode.
                    # therefore, we gotta toggle ONLY the dark mode switch.
                    self.darkmode_switch.select()
                    # now let's change the appearance mode in CTk Framework.
                    set_appearance_mode("dark")
                else:
                    # we will fall back to defaults, which is dark mode of course.
                    self.darkmode_switch.select()
                    # now it's CTk framework's turn.
                    set_appearance_mode("dark")
            except Exception as __errUpdatingSwitches:
                __errWindow: error.ErrorWindow = error.ErrorWindow(f"""An exception has occured while trying to update the theme switches.
Current function/program stage is: frames.SecondStage.__init__.__updateSwitchesAccordingToAppMode()
More error details available below:
{__errUpdatingSwitches}

Click any of the two buttons below to close the app with exit code 267
""")
                __errWindow.wait_window()
                try: self.destroy()
                except: pass
                raise SystemExit(267)
            
            return None



        def __changeThemeModeAndSaveChanges(currentSwitch: CTkSwitch) -> None:
            """
            A function linked to the switches (light mode and dark mode) that should do all the following: 

            1-Disable one switch if another is enabled (like the light mode switch will be disabled if dark mode is enabled and vice versa)

            2-Change the current appearance mode according to the currently enabled switch

            3-Save the currently selected appearance mode to the configuration file

            **THIS FUNCTION MUST BE STRICTLY LINKED TO THE command= PARAMETER OF BOTH OF THE THEME MODE SWITCHES**
            """
            # task num 1 - disable one switch if another is enabled!
            # =======================================================
            print(f"[DEBUG] __changeThemeModeAndSaveChanges @ SecondStage: current light mode switch state is: {self.lightmode_switch.get()} and dark mode switch is: {self.darkmode_switch.get()}, Current clicked switch ID is: {currentSwitch.__str__}")
            # disable the current switch.
            # print(currentSwitch.__str__)
            if currentSwitch.__str__ == "<DARKSWITCH>":
                # the dark switch is the one clicked right now
                currentSwitch.deselect()
                self.lightmode_switch.deselect()
                currentSwitch.select()
                # we gotta make sure others are deselected.
            elif currentSwitch.__str__ == "<LIGHTSWITCH>":
                # the light switch is the one clicked right now
                currentSwitch.deselect()
                self.darkmode_switch.deselect()
                currentSwitch.select()
                # we gotta make sure, again, that others are clicked rn.
            else:
                # we don't currently know what switch is clicked right now.
                currentSwitch.deselect()
                self.lightmode_switch.deselect()
                self.darkmode_switch.deselect()
                self.darkmode_switch.select()
            # =======================================================
            # now after this, im thinking of saving appearance mode to the 
            # configuration file first, then attempt to apply it to the
            # OOBE second stage frame (aka. this frame).
            # HOW TO implement this?: well, if the clicked toggle is dark mode, then save
            # appearance mode, dark to the configuration file, then update everything, and vice versa.
            # =======================================================
            # now let's attempt to get the currently selected appearance mode first.
            if currentSwitch.__str__ == "<DARKSWITCH>":
                # user has selected the dark mode switch
                # which means that the dark mode switch is the currently enabled one
                # which means to save the current appearance mode as dark mode.
                # and then change the current display mode to be dark mode.
                set_appearance_mode("dark")
                try:
                    __cfgparserobj: ConfigParser = ConfigParser()
                    __cfgparserobj.read(f"{application_path}\\..\\Config.ini")
                    # will change appearance mode to 2 since it represents the dark theme mode.
                    __cfgparserobj["ProgConfig"]["appearancemode"] = "2"
                    # now let's commit changes to the actual config file.
                    with open(f"{application_path}\\..\\Config.ini", 'w') as __cfgfileopenobj:
                        __cfgparserobj.write(__cfgfileopenobj)
                    # freeing up some memory.
                    __cfgfileopenobj.close()
                    del __cfgfileopenobj;del __cfgparserobj
                except Exception as __errSavingChgsToCfgFile:
                    __errWindow: error.ErrorWindow = error.ErrorWindow(f"""An exception has occured while attempting to save changes to the configuration file.
Current function is: frames.SecondStage.__init__.__changeThemeModeAndSaveChanges() @ writing changes to configuration file.
More error details available below:
{__errSavingChgsToCfgFile}

Click any button below to close this window, and exit this program with exit code 257
""")
                    __errWindow.wait_window()
                    # now after the window has been destroyed.
                    try: self.destroy()
                    except: pass
                    raise SystemExit(257)
                # we gotta right now possibly redraw all widgets again.
            elif currentSwitch.__str__ == "<LIGHTSWITCH>":
                # user has clicked on the light mode switch, therefore it is enabled
                # therefore we gotta save the current appearance mode as 1 (in the config file)
                set_appearance_mode("light")
                try:
                    __cfgparserobj: ConfigParser = ConfigParser()
                    __cfgparserobj.read(f"{application_path}\\..\\Config.ini")
                    # will change appearance mode to 1 since it represents the light theme mode.
                    __cfgparserobj["ProgConfig"]["appearancemode"] = "1"
                    # now let's commit changes to the actual config file.
                    with open(f"{application_path}\\..\\Config.ini", 'w') as __cfgfileopenobj:
                        __cfgparserobj.write(__cfgfileopenobj)
                    # freeing up some memory.
                    __cfgfileopenobj.close()
                    del __cfgfileopenobj;del __cfgparserobj
                except Exception as __errSavingChgsToCfgFile:
                    __errWindow: error.ErrorWindow = error.ErrorWindow(f"""An exception has occured while attempting to save changes to the configuration file.
Current function is: frames.SecondStage.__init__.__changeThemeModeAndSaveChanges() @ writing changes to configuration file.
More error details available below:
{__errSavingChgsToCfgFile}

Click any button below to close this window, and exit this program with exit code 257
""")
                    __errWindow.wait_window()
                    # now after the window has been destroyed.
                    try: self.destroy()
                    except: pass
                    raise SystemExit(257)
                # right now we gotta redraw all stuff.
            else:
                # it is possible that some exception occurs and we don't know how to 
                # deal with it.
                # will fall back to defaults then (saving to config file as dark mode)
                set_appearance_mode("dark")
                try:
                    __cfgparserobj: ConfigParser = ConfigParser()
                    __cfgparserobj.read(f"{application_path}\\..\\Config.ini")
                    # will change appearance mode to 2 since we are falling back to defaults.
                    __cfgparserobj["ProgConfig"]["appearancemode"] = "2"
                    # now let's commit changes to the actual config file.
                    with open(f"{application_path}\\..\\Config.ini", 'w') as __cfgfileopenobj:
                        __cfgparserobj.write(__cfgfileopenobj)
                    # freeing up some memory.
                    __cfgfileopenobj.close()
                    del __cfgfileopenobj;del __cfgparserobj
                except Exception as __errSavingChgsToCfgFile:
                    __errWindow: error.ErrorWindow = error.ErrorWindow(f"""An exception has occured while attempting to save changes to the configuration file.
Current function is: frames.SecondStage.__init__.__changeThemeModeAndSaveChanges() @ writing changes to configuration file.
More error details available below:
{__errSavingChgsToCfgFile}

Click any button below to close this window, and exit this program with exit code 257
""")
                    __errWindow.wait_window()
                    # now after the window has been destroyed.
                    try: self.destroy()
                    except: pass
                    raise SystemExit(257)

            # right now, we gotta call to redraw all widgets again.
            self.configure(bg_color=self.getCurrentAppearanceMode()[0], fg_color=self.getCurrentAppearanceMode()[0])
            self.welcomeHeader.configure(fg_color=self.getCurrentAppearanceMode()[0])
            self.tcglogo.configure(bg=self.getCurrentAppearanceMode()[0], fg=self.getCurrentAppearanceMode()[1])
            self.welcomeLabel.configure(bg=self.getCurrentAppearanceMode()[0], fg=self.getCurrentAppearanceMode()[1])
            self.informationLabel.configure(bg=self.getCurrentAppearanceMode()[0], fg=self.getCurrentAppearanceMode()[1])
            self.appearance_modes_frame.configure(bg_color=self.getCurrentAppearanceMode()[0], fg_color=self.getCurrentAppearanceMode()[0])
            self.lightmode_previewImg_display.configure(bg=self.getCurrentAppearanceMode()[0])
            self.darkmode_previewImg_display.configure(bg=self.getCurrentAppearanceMode()[0])
            return None

        # processing background color
        self.configure(bg_color=self.getCurrentAppearanceMode()[0], fg_color=self.getCurrentAppearanceMode()[0])
        # declaring other widgets
        # copying the main header.
        # =================================================================
        # reserved for welcome header.
        self.welcomeHeader = CTkFrame(self, bg_color='black', fg_color=self.getCurrentAppearanceMode()[0], corner_radius=15, border_width=0.755)

        # loading tcg icon into memory.
        self.tcgicon_ico = IcoImagePlugin.IcoImageFile(f"{application_path}\\..\\icon0.ico").resize((40, 40))
        self.tcgicon_tk = ImageTk.PhotoImage(self.tcgicon_ico)

        self.tcglogo = Label(self.welcomeHeader, image=self.tcgicon_tk , font=("Arial Bold", 10), bg=self.getCurrentAppearanceMode()[0], fg=self.getCurrentAppearanceMode()[1], width=40, height=40)
        self.tcglogo.pack(side=LEFT, anchor=W, padx=3)

        self.welcomeLabel = Label(self.welcomeHeader, text=retrieveCurrentLanguage().oobe_choose_theme_mode, font=("Arial Bold", 22), bg=self.getCurrentAppearanceMode()[0], fg=self.getCurrentAppearanceMode()[1], borderwidth=2)
        self.welcomeLabel.pack(side=LEFT, anchor=NE, fill=X, expand=True, padx=10, pady=20)

        self.welcomeHeader.pack(fill=X, expand=False)
        # =================================================================
        self.informationLabel = Label(self, text=retrieveCurrentLanguage().oobe_second_stage_info, font=("Arial", 13), bg=self.getCurrentAppearanceMode()[0], fg=self.getCurrentAppearanceMode()[1], justify=(RIGHT if retrieveCurrentLanguage().__str__ == "ar" else LEFT), wraplength=760)
        self.informationLabel.pack(pady=6)

        # =======================================================
        # let's declare a holder frame that will hold both frames for dark mode UI
        # preview and light mode UI previews and their selection CTkSwitch widgets too.
        self.appearance_modes_frame = CTkFrame(self, bg_color=self.getCurrentAppearanceMode()[0], fg_color=self.getCurrentAppearanceMode()[0])
        # =======================================================
        # let's declare a frame that will hold the elements of the light mode UI preview
        # and selection CTkSwitch widget
        self.lightmode_frame = CTkFrame(self.appearance_modes_frame)
        self.lightmode_previewImg_display = Label(self.lightmode_frame, text='', image=None, bg=self.getCurrentAppearanceMode()[0])
        self.lightmode_previewImg_pimg = PhotoImage(file=f"{application_path}\\tcg_lightmode_ss.png").subsample(2,2)
        self.lightmode_previewImg_display.configure(image=self.lightmode_previewImg_pimg)
        self.lightmode_previewImg_display.pack()
        self.lightmode_switch = CTkSwitch(self.lightmode_frame, fg_color='red', text=retrieveCurrentLanguage().light_mode, onvalue=1, offvalue=0, command=lambda: __changeThemeModeAndSaveChanges(self.lightmode_switch))
        self.lightmode_switch.__str__ = "<LIGHTSWITCH>"
        self.lightmode_switch.deselect()
        self.lightmode_switch.pack()
        self.lightmode_frame.pack(side=LEFT, anchor=N, expand=True)
        self.lightmode_frame.pack_propagate(False)
        # =======================================================
        # =======================================================
        # let's declare a frame that will hold the elements of the dark mode UI preview
        # and selection CTkSwitch widget
        self.darkmode_frame = CTkFrame(self.appearance_modes_frame)
        # let's declare all the inside widgets.
        self.darkmode_previewImg_display = Label(self.darkmode_frame, text='', image=None, bg=self.getCurrentAppearanceMode()[0])
        self.darkmode_previewImg_pimg = PhotoImage(file=f"{application_path}\\tcg_darkmode_ss.png").subsample(2,2)
        self.darkmode_previewImg_display.configure(image=self.darkmode_previewImg_pimg)
        self.darkmode_previewImg_display.pack()
        self.darkmode_switch = CTkSwitch(self.darkmode_frame, fg_color='red', text=retrieveCurrentLanguage().dark_mode, onvalue=1, offvalue=0, command=lambda: __changeThemeModeAndSaveChanges(self.darkmode_switch))
        self.darkmode_switch.__str__ = "<DARKSWITCH>"
        self.darkmode_switch.deselect()
        self.darkmode_switch.pack()
        self.darkmode_frame.pack(side=LEFT, anchor=N, expand=True)
        self.darkmode_frame.pack_propagate(False)
        # =======================================================
        self.appearance_modes_frame.pack(expand=False, fill=X, anchor=N)
        self.appearance_modes_frame.pack_propagate(False)
        # =======================================================
        # =======================================================
        # let's declare a button for continuing
        self.continue_btn = CTkButton(self, text=retrieveCurrentLanguage().oobe_continue_btn, command=lambda: self.destroy())
        self.continue_btn.pack(anchor=N, pady=5, ipady=9, ipadx=25)
        # =======================================================
        # now we gotta call this function to get the current theme mode.
        __updateSwitchesAccordingToAppMode()


    def getCurrentAppearanceMode(self):
        global retrieveCurrentAppearanceMode
        """
        Make use of retrieveCurrentAppearanceMode() function to retrieve the current appearance mode
        stored in the application's configuration file.

        This returns in the same syntax as the original function: (bg_color, fg_color)
        """
        try:
            curr_mode = retrieveCurrentAppearanceMode()
        except Exception as __curErr:
            __window = error.ErrorWindow(f"""An exception has occured while attempting to retrieve/get the current appearance mode in the configuration file.
Current program stage is: frames.SecondStage.getCurrentAppearanceMode() - on calling function: retrieveCurrentAppearanceMode()
More error details:
{__curErr}

Press any button below to close the program with exit code 257
""")
            __window.wait_window()
            try:
                del __window;del __curErr
                self.master.destroy();self.destroy()
            except:
                pass
            raise SystemExit(257)
        
        return curr_mode

    
    
    
class ThirdStage(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        global retrieveCurrentAppearanceMode, retrieveCurrentLanguage
        self.master = master
        self.args = args
        self.kwargs = kwargs
        def __saveConfigsToCfgFile(auto_update_switch_state: str, startup_tips_switch_state: str) -> bool:
            """
            Saves configuration for the auto update switch and the startup tips switch to the configuration file.

            arguments:
            auto_update_switch_state: str - the state of the auto update switch ("1" or "0")
            startup_tips_switch_state: str - the state of the startup tips switch ("1" or "0")

            **MUST BE STRICTLY CALLED FROM THE BINDED FUNCTION TO THE SWITCHES ONLY**
            """
            # this function has 2 goals
            # 1- is to check for the values of both switches (if they are true or false, 1 or 0)
            # 2- is to save the values as strings to the configuration file.

            # lets initialize a configparser object.
            try:
                __cfgparser: ConfigParser = ConfigParser()
                __cfgparser.read(f"{application_path}\\..\\Config.ini")
                print(f"[DEBUG]: frames.ThirdStage.__init__().__saveConfigsToCfgFile(): successfully accessed config file: Config.ini!")
            except Exception as __errorReadingCFG:
                __window: error.ErrorWindow = error.ErrorWindow(f"""An Exception has occured while attempting to access configuration file.
Current program stage is: frames.ThirdStage.__init__().__saveConfigsToCfgFile() @ reading from config file.
More error details are:
{__errorReadingCFG}

Press any button below to terminate this program's process...
""")
                __window.wait_window()
                try: del __window;self.destroy();self.master.destroy()
                except: pass
                raise SystemExit(768) # exit code 768 is another code for another failed stage.
            
            # lets check the values of the switches.
            print(f"[DEBUG]: frames.ThirdStage.__init__().__saveConfigsToCfgFile(): auto_update_switch_state={auto_update_switch_state}")
            print(f"[DEBUG]: frames.ThirdStage.__init__().__saveConfigsToCfgFile(): startup_tips_switch_state={startup_tips_switch_state}")
            if str(auto_update_switch_state) == "0": # will write "0" in the configuration file.
                                                     # to the configuration key 'autocheckforupdates'
                __cfgparser["ProgConfig"]["autocheckforupdates"] = "0"
            else: # whether user has explicitly enabled the auto updates check switch
                  # or the program had an error that prevented that from happening
                  # will fall back to defaults.
                __cfgparser["ProgConfig"]["autocheckforupdates"] = "1"
            
            if str(startup_tips_switch_state) == "0": # will write "0" in the configuration file.
                __cfgparser["ProgConfig"]["showstartuptips"] = "0"
            else:
                __cfgparser["ProgConfig"]["showstartuptips"] = "1"
            
            # lets write the changes to the configuration file.
            try:
                with open(f"{application_path}\\..\\Config.ini", 'w') as __cfgfileopenobj:
                    __cfgparser.write(__cfgfileopenobj)
                __cfgfileopenobj.close() # freeing up resources.
                del __cfgfileopenobj;del __cfgparser
                print(f"[DEBUG]: frames.ThirdStage.__init__().__saveConfigsToCfgFile(): successfully saved configuration to file Config.ini!!!")
            except Exception as __errorWritingCFG:
                __window: error.ErrorWindow = error.ErrorWindow(f"""An Exception has occured while saving configuration to file.
Current program stage is: frames.ThirdStage.__init__().__saveConfigsToCfgFile() @ writing config to file.
Error details are:
{__errorWritingCFG}

Press any button below to terminate the program's process...
""")
                __window.wait_window()
                try: self.destroy();self.master.destroy();del __window
                except: pass
                raise SystemExit(769) # an error code for a failure while saving to config file.
            return True
        
        def __updateCheckBoxesWithCurValues() -> None:
            """
            Reads from configuration file, usually 'Config.ini' the current values for the checkboxes
            and changes the toggle state of them according to the respective values in the configuration file.

            arguments: None

            returns: None
            """
            print(f"[DEBUG]: frames.ThirdStage.__init__(): __updateCheckBoxesWithCurValues() called.")
            try:
                __cfgparser: ConfigParser = ConfigParser()
                __cfgparser.read(f"{application_path}\\..\\Config.ini")
                print(f"[DEBUG]: frames.ThirdStage.__init__().__updateCheckBoxesWithCurValues(): successfully accessed config file: Config.ini!")
            except Exception as __errorReadingFromCFG:
                __window: error.ErrorWindow = error.ErrorWindow(f"""An error has occured while accessing the configuration file.
Current program stage is: frames.ThirdStage.__init__().__updateCheckBoxesWithCurValues() @ reading from config file.
More error details are:
{__errorReadingFromCFG}

Press any button below to terminate the program's process...
""")
                __window.wait_window()
                try: self.destroy();self.master.destroy();del __window
                except: pass
                raise SystemExit(768) # exit error 768 is for a failure in accessing configuration file.
            
            # now lets do the actual change.
            try:
                # thats for the auto check for updates switch
                if str(__cfgparser["ProgConfig"]["autocheckforupdates"]) == "1":
                    # config file has auto update enabled, therefore we must show 
                    # the change to the user.
                    self.autoUpdateSwitch.select()
                else: # any other value, or is disabled in configuration file.
                    self.autoUpdateSwitch.deselect()
                
                # now, for the startup tips switch.
                if str(__cfgparser["ProgConfig"]["showstartuptips"]) == "1":
                    # config file has startup tips enabled, therefore we must show 
                    # the change to the user.
                    self.startupTipsSwitch.select()
                else: # any other value, or is disabled in configuration file.
                    self.startupTipsSwitch.deselect()
                # lets free up some memory.
                del __cfgparser
            except Exception as __errReadingCfgFile:
                __window: error.ErrorWindow = error.ErrorWindow(f"""An error has occured while reading values from configuration file!
Current program stage is: frames.ThirdStage.__init__().__updateCheckBoxesWithCurValues() @ reading values from config.ini
Error details available below:
{__errReadingCfgFile}

Press any button below to terminate this program's process...
""")
                __window.wait_window()
                try: self.destroy();self.master.destroy();del __window
                except: pass
                raise SystemExit(765) # exit code 765 is for a failure in reading from the config file.
            return None


        print(f"[DEBUG]: frames.ThirdStage.__init__(): self.getCurrentAppearanceMode() -> {self.getCurrentAppearanceMode()}")
        self.configure(bg_color=self.getCurrentAppearanceMode()[0], fg_color=self.getCurrentAppearanceMode()[0])
        # constructing widgets.
        # copying the main header.
        # =================================================================
        # reserved for welcome header.
        self.welcomeHeader = CTkFrame(self, bg_color='black', fg_color=self.getCurrentAppearanceMode()[0], corner_radius=15, border_width=0.755)

        # loading tcg icon into memory.
        self.tcgicon_ico = IcoImagePlugin.IcoImageFile(f"{application_path}\\..\\icon0.ico").resize((40, 40))
        self.tcgicon_tk = ImageTk.PhotoImage(self.tcgicon_ico)

        self.tcglogo = Label(self.welcomeHeader, image=self.tcgicon_tk , font=("Arial Bold", 10), bg=self.getCurrentAppearanceMode()[0], fg=self.getCurrentAppearanceMode()[1], width=40, height=40)
        self.tcglogo.pack(side=LEFT, anchor=W, padx=3)

        self.welcomeLabel = Label(self.welcomeHeader, text=retrieveCurrentLanguage().oobe_configure_other_settings, font=("Arial Bold", 22), bg=self.getCurrentAppearanceMode()[0], fg=self.getCurrentAppearanceMode()[1], borderwidth=2)
        self.welcomeLabel.pack(side=LEFT, anchor=NE, fill=X, expand=True, padx=10, pady=20)

        self.welcomeHeader.pack(fill=X, expand=False)
        # =================================================================
        self.informationLabel = Label(self, text=retrieveCurrentLanguage().oobe_change_settings, font=("Arial", 13), bg=self.getCurrentAppearanceMode()[0], fg=self.getCurrentAppearanceMode()[1], justify=(RIGHT if retrieveCurrentLanguage().__str__ == "ar" else LEFT), wraplength=760)
        self.informationLabel.pack(pady=6)

        # constructing/declaring a frame to hold necessary checkboxes (toggles)
        # for other settings.
        # =======================================================
        self.otherSettingsFrame = CTkFrame(self, bg_color=self.getCurrentAppearanceMode()[0], fg_color=self.getCurrentAppearanceMode()[0])
        # declaring inside widgets.
        # =======================================================
        self.autoUpdateSwitchHeaderLbl0 = Label(self.otherSettingsFrame, text=retrieveCurrentLanguage().checking_for_updates, justify=(RIGHT if retrieveCurrentLanguage().__str__ == "ar" else LEFT), font=("Arial", 13), bg=self.getCurrentAppearanceMode()[0], fg=self.getCurrentAppearanceMode()[1], wraplength=760)
        self.autoUpdateSwitchHeaderLbl0.grid(column=0, row=0, pady=6, padx=10, sticky=W)
        self.autoUpdateSwitchInfoLbl0 = Label(self.otherSettingsFrame, text=retrieveCurrentLanguage().oobe_autoupdate_text, justify=(RIGHT if retrieveCurrentLanguage().__str__ == "ar" else LEFT), font=("Arial", 11), bg=self.getCurrentAppearanceMode()[0], fg=self.getCurrentAppearanceMode()[1], wraplength=760)
        self.autoUpdateSwitchInfoLbl0.grid(column=0, row=1, pady=0, padx=10, sticky=W)
        self.autoUpdateSwitch = CTkCheckBox(self.otherSettingsFrame, text=retrieveCurrentLanguage().auto_check_for_updates, fg_color='#0dff00', onvalue="1", offvalue="0", command=lambda: __saveConfigsToCfgFile(self.autoUpdateSwitch.get(), self.startupTipsSwitch.get()))
        self.autoUpdateSwitch.grid(column=0, row=2, pady=0, padx=10, sticky=W)
        # declaring widgets for startup tips switch.
        self.startupTipsSwitchHeaderLbl0 = Label(self.otherSettingsFrame, text=retrieveCurrentLanguage().startup_tips_hint, justify=(RIGHT if retrieveCurrentLanguage().__str__ == "ar" else LEFT), font=("Arial", 13), bg=self.getCurrentAppearanceMode()[0], fg=self.getCurrentAppearanceMode()[1], wraplength=760)
        self.startupTipsSwitchHeaderLbl0.grid(column=0, row=3, pady=6, padx=10, sticky=W)
        self.startupTipsSwitchInfoLbl0 = Label(self.otherSettingsFrame, text=retrieveCurrentLanguage().oobe_startup_tips_text, justify=(RIGHT if retrieveCurrentLanguage().__str__ == "ar" else LEFT), font=("Arial", 11), bg=self.getCurrentAppearanceMode()[0], fg=self.getCurrentAppearanceMode()[1], wraplength=760)
        self.startupTipsSwitchInfoLbl0.grid(column=0, row=4, pady=0, padx=10, sticky=W)
        self.startupTipsSwitch = CTkCheckBox(self.otherSettingsFrame, text=retrieveCurrentLanguage().show_startup_tips, fg_color='#0dff00', onvalue="1", offvalue="0", command=lambda: __saveConfigsToCfgFile(self.autoUpdateSwitch.get(), self.startupTipsSwitch.get()))
        self.startupTipsSwitch.grid(column=0, row=5, pady=0, padx=10, sticky=W)
        # =======================================================
        self.otherSettingsFrame.pack(expand=False, fill=BOTH, anchor=N)
        # lets declare a continue button.
        self.continueBtn: CTkButton = CTkButton(self, text=retrieveCurrentLanguage().oobe_continue_btn, command=lambda: self.destroy(), anchor=CENTER)
        self.continueBtn.pack()
        # now, lets read for actual real values from configuration file.
        __updateCheckBoxesWithCurValues()



    def getCurrentAppearanceMode(self) -> tuple | None:
        global retrieveCurrentAppearanceMode
        """
        Makes use of the global function retrieveCurrentAppearanceMode() to return a tuple containing
        the current appearance mode for the program stored in the configuration file.

        This returns in the same syntax as the original function: (bg_color, fg_color)

        What makes it different than the original one is the use of exception handling.
        """
        try: return retrieveCurrentAppearanceMode()
        except Exception as __errRetrievingAppearanceMode:
            __window = error.ErrorWindow(f"""An Exception has occured while attempting to retrieve the current appearance mode from the configuration file!!!
Current program stage is: frames.ThirdStage.getCurrentAppearanceMode()
More error details available below...
{__errRetrievingAppearanceMode}

Press any keys of the two to terminate this program's process...
""")
            __window.wait_window()
            try: del __window;self.destroy();self.master.destroy()
            except: pass
            raise SystemExit(512) # exit code 512 is for unable to configure frame properties.
        return None
        

class LastStage(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        global retrieveCurrentAppearanceMode, retrieveCurrentLanguage
        self.master = master
        self.args = args
        self.kwargs = kwargs
        self.configure(bg_color=self.__getCurrentAppearanceMode()[0], fg_color=self.__getCurrentAppearanceMode()[0])
        # declaring the function for the continue button.
        # this function, should, set the value of the constant FirstRun to 0 in the configuration file.
        # and lastly, destroy the self and its master window.
        def __destroyMasterAndSaveToCfgFile() -> None:
            """
            This function has the purpose of doing all of the following:
            
            1-Change the value of the variable FirstRun to 0 in the configuration file ({application_path}\\..\\Config.ini)
            
            2-Destroy the current frame (self) and its parent window (self.parent)

            This function always returns None, and when an error (exception) occurs it will start the error window.
            """
            try:
                __cfgparser: ConfigParser = ConfigParser()
                __cfgparser.read(f"{application_path}\\..\\Config.ini")
            except Exception as __errorOpeningCfgFile:
                __window: error.ErrorWindow = error.ErrorWindow(f"""An error has occured while accessing the Configuration file.
Current program stage is: frames.LastStage.__init__().__destroyMasterAndSaveToCfgFile() @ reading from config file.
More error details are:
{__errorOpeningCfgFile}

Press any button below to terminate the program's process...
""")
                __window.wait_window()
                try: self.destroy();self.master.destroy();del __window
                except: pass
                raise SystemExit(522) # exit code 522 is for unable to access configuration file.
            
            try:
                # will change the value of FirstRun to 0 in the configuration file.
                __cfgparser["ProgConfig"]["FirstRun"] = "0"
                # now lets write the changes to the configuration file.
                with open(f"{application_path}\\..\\Config.ini", 'w') as __cfgfileopenobj:
                    __cfgparser.write(__cfgfileopenobj)
                # freeing up some memory.
                __cfgfileopenobj.close()
                del __cfgfileopenobj;del __cfgparser
            except Exception as __errorWritingToCfgFile:
                __window: error.ErrorWindow = error.ErrorWindow(f"""An error has occured while writing to the configuration file.
Current program stage is: frames.LastStage.__init__().__destroyMasterAndSaveToCfgFile() @ writing to config file.
More error details are:
{__errorWritingToCfgFile}

Press any button below to terminate the program's process...
""")
                __window.wait_window()
                try: self.destroy();self.master.destroy();del __window
                except: pass
                raise SystemExit(523) # an exit error for not being able to save OOBE status to the
                                      # configuration file.
            # now, we can destroy the current frame and its parent window.
            try: self.destroy();self.master.destroy()
            except Exception as __errDestroyingSelf:
                __window: error.ErrorWindow = error.ErrorWindow(f"""An error has occured while destroying the OOBE window and LastStage frame.
Current program stage is: frames.LastStage.__init__().__destroyMasterAndSaveToCfgFile() @ destroying the frame and its parent window.
More error details are:
{__errDestroyingSelf}

Press any button below to terminate the program's process...
""")
                __window.wait_window()
                raise SystemExit(566) # exit code 566 is for unable to destroy the frame and its parent window.
            return None
        
        
        # copying the main header.
        # =================================================================
        # reserved for welcome header.
        self.welcomeHeader = CTkFrame(self, bg_color='black', fg_color=self.__getCurrentAppearanceMode()[0], corner_radius=15, border_width=0.755)

        # loading tcg icon into memory.
        self.tcgicon_ico = IcoImagePlugin.IcoImageFile(f"{application_path}\\..\\icon0.ico").resize((40, 40))
        self.tcgicon_tk = ImageTk.PhotoImage(self.tcgicon_ico)

        self.tcglogo = Label(self.welcomeHeader, image=self.tcgicon_tk , font=("Arial Bold", 10), bg=self.__getCurrentAppearanceMode()[0], fg=self.__getCurrentAppearanceMode()[1], width=40, height=40)
        self.tcglogo.pack(side=LEFT, anchor=W, padx=3)

        self.welcomeLabel = Label(self.welcomeHeader, text=retrieveCurrentLanguage().oobe_all_done, font=("Arial Bold", 22), bg=self.__getCurrentAppearanceMode()[0], fg=self.__getCurrentAppearanceMode()[1], borderwidth=2)
        self.welcomeLabel.pack(side=LEFT, anchor=NE, fill=X, expand=True, padx=10, pady=20)

        self.welcomeHeader.pack(fill=X, expand=False)
        # =================================================================
        self.informationLabel = Label(self, text=retrieveCurrentLanguage().oobe_your_all_done, font=("Arial", 13), bg=self.__getCurrentAppearanceMode()[0], fg=self.__getCurrentAppearanceMode()[1], justify=(RIGHT if retrieveCurrentLanguage().__str__ == "ar" else LEFT), wraplength=760)
        self.informationLabel.pack(pady=6)

        # lets construct/declare a continue button that will close the OOBE window
        # and set the variable (should I say, a constant?) FirstRun to 0 in the configuration file!
        self.continueButton: CTkButton = CTkButton(self, text=retrieveCurrentLanguage().oobe_continue_btn, command=__destroyMasterAndSaveToCfgFile)
        self.continueButton.pack(expand=True)

    
    def __getCurrentAppearanceMode(self) -> tuple | None:
        global retrieveCurrentAppearanceMode
        """
        Makes use of the global function retrieveCurrentAppearanceMode() to return a tuple containing
        the current appearance mode for the program stored in the configuration file.

        This returns in the same syntax as the original function: (bg_color, fg_color)

        What makes it different than the original one is the use of exception handling.
        """
        try: return retrieveCurrentAppearanceMode()
        except Exception as __errRetrievingAppearanceMode:
            __window = error.ErrorWindow(f"""An Exception has occured while attempting to retrieve the current appearance mode from the configuration file!!!
Current program stage is: frames.LastStage.__getCurrentAppearanceMode()
More error details are:
{__errRetrievingAppearanceMode}

Press any key below to terminate the program's process!!
""")
            __window.wait_window()
            try: self.destroy();self.master.destroy();del __window
            except: pass
            raise SystemExit(256) # exit code 256 is for unable to access from current appearance mode!
        return None
        
