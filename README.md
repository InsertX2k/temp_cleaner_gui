# Temp_Cleaner GUI Project
A free (and of course an **Open-Source**) alternative to all Temp Cleaning Software available for all Windows Versions that can be expanded by you!<br/>
## Requirements : <br/>
* A little knowledge in Python (Specially the if statements usage) <br/>
* The Python module **WINTCMD** <br/>
* A Windows 10 PC <br/>
* A working human brain <br/>
* Pyinstaller or auto-py-to-exe (this one is recommended) <br/>
* Python installed <br/>
* Notepad++ or Visual Studio Code <br/>
**If Python knowledge doesn't exist**, don't worry, as I must be trying to explain to you how do you modify it by yourself! <br/>
## Inside of the program <br/>
![A screenshot of the inside of the program Temp_Cleaner GUI](https://github.com/InsertX2k/temp_cleaner_gui/blob/main/.readme.files/temp_cleaner_gui.inside_ss.jpg?raw=true) <br/>
<br/>
## Recompiling guide <br/>
This program usually comes as an executable ONLY for 64-bit based PCs, but there is a problem ONLY if your PC is a 32-bit one, but don't worry, You don't have to open an issue, all what you have to do is just following this guide step by step so you can recompile a 32-bit version of this program. <br/>
**Please before doing this make sure you have all of the requirements** <br/>
Download and install **pyinstaller** <br/>
Open **Windows Command Prompt** as **Administrator** and then execute the following command : <br/>
```
pip install pyinstaller
``` 
<br/>
Once done, please make sure to install auto-py-to-exe too, execute the following command to do so : <br/>
```
pip install auto-py-to-exe
```
<br/>
Then you should wait for the installation to be done. <br/>
<br/>
Once done, You should then be sure to make some changes to the source code file of the program (at least to make it appear like a 32-bit program) <br/>
Simply, all what you have to do is just replacing all words that are between quotes `" "` that says the program is 64-bit with the appropriate ones that says the program is a 32-bit one <br/>
Once you are done, be sure to save your changes and make sure that you edited everything properly/correctly. <br/>
Open ` auto-py-to-exe ` using **Windows Command Prompt** and then choose the program's source code file (that **.py** file you've been editing) as the script <br/>
and then choose all of the following configurations for the program : <br/>
* The program must be recompiled in One directory mode (--ondir) <br/>
* The icon file (icon0.ico) must be set as the program icon <br/>
* The files **icon0.ico** and the source code of the program (that **.py** file you've been editing) and the file **WINTCMD.py** must be added to the integrate files option, and BE SURE to keep their extraction directory as in the current directory (Simply don't modify anything after you add those files and everything is gonna be fine) <br/>
* The program must ask for UAC Admin privileges, Which means you will of course have to enable the option UAC-Access or something similar to it <br/>
* IMPORTANT : You must choose the **Console Window** as **Window based (Hide the console)** <br/>
If a GUI seems hard for you to use, then type the following command into a **Command Prompt Window** that is not elevated. <br/>
```
pyinstaller --noconfirm --onedir --windowed --icon "path\to\program\temp_cleaner_gui\icon0.ico" --name "temp-cleaner-v1.1-gui-foss" --clean --uac-admin --add-data "path\to\program\temp_cleaner_gui\icon0.ico;." --add-data "path\to\program\temp_cleaner_gui\temp_cleaner_gui_console0.py;." --add-data "path\to\program\temp_cleaner_gui\WINTCMD.py;."  "path\to\program\temp_cleaner_gui\temp_cleaner_gui_console0.py"
```
<br/>
And of course, do not forget to replace ` path\to\program\temp_cleaner_gui\ ` with the correct path of where did you store the program Temp_Cleaner GUI in  <br/>
<br/>
## Adding new features : <br/>
That's the main adventage of Temp_Cleaner GUI is that it can be manually expanded by **you** <br/>
All what you will have to do is just downloading the file that says the ``recompiling-guide`` and then extract it and then read it, and you are going to be ready to go! <br/>
<br/>
**Please note :** that you shouldn't post your modified version of **Temp_Cleaner GUI** here, please keep it for yourself, however, if you want to give us some paths to where should we look for temporary files, feel free to create an issue, and I will reply you as fast as possible! <br/>
And thanks for everyone who had supported me all this time <br/>
<br/>
## Known problems : <br/>
* The current release of the project (**v1.3**) is known to have compiling problems, but don't worry as I will be trying to resolve all of them as fast as possible.
<br/>
## Copyrights <br/>
The icon of the program, and the file **icon0.ico** is just a modified icon image that is originally owned by the **Numix Icon pack** author
<br/>
## Download an already compiled version <br/>
If recompiling the program is hard for you, feel free to download the executable of the program from [here](https://drive.google.com/file/d/10XCWXAyhNL5lygi5qeCEOQJEwzXAibfQ/view?usp=sharing) <br/>
**Please note that this version is only available for 64-bit based PCs** <br/>
-Insert
