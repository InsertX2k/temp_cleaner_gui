import configparser
import os, sys
from tkinter import *
from tkinter import ttk

# initializing a variable containing the path where application files are stored.
application_path = ''

# attempting to get where the program files are stored
if getattr(sys, 'frozen', False): 
    # if program was frozen (compiled) using pyinstaller, the pyinstaller bootloader creates a sys attribute
    # frozen=True to indicate that the script file was compiled using pyinstaller, then it creates a
    # constant in sys that points to the directory where program executable is (where program files are).
    application_path = sys._MEIPASS
    os.chdir(application_path)
else: 
    # if program is not frozen (compiled) using pyinstaller and is running normally like a Python 3.x.x file.
    application_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(application_path)


Cfg = configparser.ConfigParser()
Cfg.read(f"{application_path}\\addsclean.ini")



class Window(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("custom cleaners test")
        self.geometry('1280x720')
        self.resizable(True, True)
        i = 0
        fileCreator = open(f"{application_path}\\temp.py", mode='w', encoding='utf-8')
        fileCreator.write("import os\n")
        fileCreator.close()
        print(f"[DEBUG]: Length of cfg.sections() is: {int(len(Cfg.sections()))}")

        for section in Cfg.sections():
            # VARIABLES = {"Cfg":Cfg, 
            #             'section':section,
            #             'self':self,
            #             'os':os,
            #             'i':i}
            setattr(self, f"{section}", ttk.LabelFrame(self, text=section))
            # CREATE_CMD_FUNCTION = open(f"{application_path}\\test.pycmd", encoding='utf-8').read()
            # exec(f"{CREATE_CMD_FUNCTION}", VARIABLES, VARIABLES)
            newFuncDeclare = f"""def func{i}():
    os.system("{Cfg[section]['CMD']}")
    return None
"""
            fileProcessor = open(f"{application_path}\\temp.py", mode='a', encoding='utf-8')
            fileProcessor.write(newFuncDeclare)
            fileProcessor.close()
            try:
                del temp
                os.rmdir(f"{application_path}\\__pycache__")
            except:
                pass
            import temp
            setattr(self, f"btn{i}", ttk.Button(getattr(self, f"{section}"), text=Cfg[section]['Name'], command=getattr(temp, f"func{i}")))
            # getattr(self, f"btn{i}").configure(command=getattr(temp, f"func{i}"))
            getattr(self, f"btn{i}").grid(column=0, row=i, sticky='w')
            getattr(self, f"{section}").grid(column=0, row=i, sticky='w')
            if i == (int(len(Cfg.sections())) - 1) or i > (int(len(Cfg.sections())) - 1):
                break
                pass
            else:
                try:
                    del temp
                    os.rmdir(f"{application_path}\\__pycache__")
                except:
                    pass
                i+=1
            




if __name__ == '__main__':
    print(f"{Cfg.sections()}")
    for section in Cfg.sections():
        print(f"{Cfg.options(section)}")
    test = Window()
    test.mainloop()
    raise SystemExit(0)