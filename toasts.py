"""
A simple module to emulate the toast notifications widget that exists in the Android Operating System.

Copyright (c) 2025 - Ziad (Mr.X)'s Software

Licensed under the same license as Temp_Cleaner GUI
"""
# imports
from tkinter import Label, Tk
from customtkinter import CTkFrame
import threading
from time import sleep

# toast class
class Toast(Tk):
    def __init__(self, width: int, height: int, textToDisplay: str, textFont: tuple, timeout: int = 15, bg_color: str = '#333', textColor: str = 'white', *args, **kwargs):
        """
        Constructs a Toast notification widget.

        This widget behaves similarily to the toast widget that exists in the Android OS.

        Parameters:

        width: an integer representing the width of the toast widget.
        height: an integer representing the height of the toast widget.
        textToDisplay: a string value representing the text to be displayed in the toast widget.
        textFont: a tuple of the syntax (font_name: str, font_size: int) representing the font of the text to be displayed in the toast widget.
        timeout: an integer representing the time in seconds after which the toast will automatically fade and destroy itself, defaults to 15 seconds (and CANNOT be less than that).
        bg_color: a string value representing the background color of the toast widget, defaults to '#333' if not specified manually.
        textColor: a string value representing the color of the text to be displayed in the toast widget, defaults to 'white' if not specified manually.
        *args: additional positional arguments to be passed to the Tk class.
        **kwargs: additional keyword arguments to be passed to the Tk class.
        """
        super().__init__(*args, **kwargs)
        self.textToDisplay = textToDisplay
        self.bg_color = bg_color
        self.width = width
        self.height = height
        self.textColor = textColor
        self.textFont: tuple = textFont
        self.timeout: int = int(timeout)
        if self.timeout < 15: 
            # we don't allow this
            raise ValueError("The timeout cannot be less than 15 seconds!")
        self.configure(bg=self.bg_color)
        # the function for the actual animation of the toast spawn process.
        def animate_toast_spawn():
            print("[DEBUG] animate_toast_spawn: begin...")
            for i in range(10):
                # we will animate the toast's transpareny from 0.0 to 0.9
                self.attributes('-alpha', (0.1 * i))
                print(f"[DEBUG] animate_toast_spawn: changing toast transparency to : {0.1 * i}")
                sleep(0.05)
        
        def animate_toast_despawn():
            print("[DEBUG] animate_toast_despawn: begin...\n[DEBUG] animate_toast_despawn: this will wait for the spawn animation to finish")
            self.__spawnAnimThd.join(timeout=1) # timeout of 1 second is obligatory.
            for i in range(9, -1, -1):
                # this will animate the toast's transpareny from 0.9 to 0.0
                self.attributes('-alpha', (0.1 * i))
                print(f"[DEBUG] animate_toast_despawn: changing toast transparency to : {0.1 * i}")
                sleep(0.05)
            # destroy the toast.
            print("[DEBUG] animate_toast_despawn: destroying the toast...")
            self.destroy()
        

        # we need to center it on the screen first
        # the logic for centering the toast on the screen goes like this:
        # we need to determine the screen width and height, store them in constant variables
        # then, we need to determine the width and height of the toast TopLevel object, we store them in constants too
        # then, we do this formula: (screen width / 2) - (toast width / 2), thats for the spawning x position
        # now, for the spawning y postition, we do the same but replacing width with height
        self.__SCREENWIDTH: int = self.winfo_screenwidth()
        self.__SCREENHEIGHT: int = self.winfo_screenheight()
        self.__TOASTWIDTH: int = int(self.width)
        self.__TOASTHEIGHT: int = int(self.height)
        self.__SPAWNXCORD: int = int((self.__SCREENWIDTH / 2) - (self.__TOASTWIDTH / 2))
        self.__SPAWNYCORD: int = int((self.__SCREENHEIGHT / 2) - (self.__TOASTHEIGHT / 2))
        self.geometry(f'{self.__TOASTWIDTH}x{self.__TOASTHEIGHT}+{self.__SPAWNXCORD}+{self.__SPAWNYCORD}')
        # now lets remove WM decorations
        self.overrideredirect(True)
        # lets declare a frame that will hold the widget
        self.textFrame: CTkFrame = CTkFrame(self, corner_radius=25, fg_color=self.bg_color, border_width=2, bg_color='black', border_color='black')
        # lets declare the widget that holds the text
        self.textDisplay: Label = Label(self.textFrame, text=self.textToDisplay, bg=self.bg_color, fg=self.textColor, font=textFont, wraplength=(self.__TOASTWIDTH - 35))
        self.textDisplay.pack(expand=True, fill='both', padx=20, pady=5)
        self.textFrame.pack(expand=True, fill='both', padx=0, pady=0)
        # lets make it topmost
        self.attributes('-topmost', True)
        self.attributes('-alpha', 0.0)
        # applying a color for transparency.
        self.attributes('-transparentcolor', 'black')
        # lets start the animation thread
        self.__spawnAnimThd: threading.Thread = threading.Thread(target=animate_toast_spawn, daemon=True, name="ToastSpawnAnimationThd0")
        # lets start the thread and run the animation (just ONCE)!
        self.__spawnAnimThd.start()
        # declaring a thread for the despawn animation, we will not start it yet!
        self.__despawnAnimThd: threading.Thread = threading.Thread(target=animate_toast_despawn, daemon=True, name="ToastDespawnAnimationThd0")
        # the logic to automatically close the toast after a certain time.
        self.after((self.timeout * 1000), lambda: self.__despawnAnimThd.start())

        



# test
if __name__ == '__main__':
    raise RuntimeError("This module is meant to be used as a module, a part of another program.")