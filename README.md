# Temp_Cleaner GUI Project
A free (and of course an **Open-Source**) alternative to all Temp Cleaning Software available for all Windows Versions that can be expanded by you!<br/>
<br/>
## Download a compiled version : <br/>
OK, I know you won't be even trying to recompile the program, exactly like most people on GitHub, However, If you are, feel free to continue reading, if you just want to download a compiled version of the program, simply scroll down until the end, you should find some download links for compiled versions with installers for this program. <br/>
<br/>
**Yes, I used Inno setup for the installer, thanks for the creator/developer of Inno setup installers.** <br/>
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
![A screenshot of the inside of the program Temp_Cleaner GUI](https://raw.githubusercontent.com/InsertX2k/temp_cleaner_gui/main/.readme.files/temp_cleaner_gui_project_v1.52_update2_default_banner_ss.jpg) <br/>
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
**Please keep in mind this recompiling guide doesn't work for the version 1.53, and I won't be doing a new recompiling guide, feel free to read the source code so you can learn how do you add new features to the program.**
<br/>
**Please note :** that you shouldn't post your modified version of **Temp_Cleaner GUI** here, please keep it for yourself, however, if you want to give us some paths to where should we look for temporary files, feel free to create an issue, and I will reply you as fast as possible! <br/>
And thanks for everyone who had supported me all this time <br/>
<br/>
## What happened to version 1.3? <br/>
I have actually canceled it's release due to compiling problems, but don't worry, someday I might be able to make a new update for that project like this one and without any compiling problems. <br/>
<br/>
## Version 1.52 : <br/>
### What's new in version 1.52? <br/>
In this version, you will only have to make a selection from the list of checkboxes shown in your screen, each checkbox of them are a cleaning action, then you press the "Execute" button to start cleaning using the given selections. <br/>
**Please note : this version also uses the same environment variables as the version 1.32, the GUI is just what has got changed.**
<br/>
## Copyrights <br/>
The icon of the program, and the file **icon0.ico** is just a modified icon image that is originally owned by the **Numix Icon pack** author
<br/>
## Version 1.32 of Temp_Cleaner GUI (End of Support) <br/>
In this version you no longer need to recompile the program to resolve path issues, all what you will have to do is just creating the environment variable that redirectes to the correct path of the operation (e.g. when trying to resolve issues with **RAMMap.exe** by **Sysinternals**, all what you have to do is just creating a new environment variable or overwriting an existing environment variable which contains the **RAMMap.exe** full path) <br/>
**Environment variables needed by the program :** <br/>
`rammappath` - It's value must be the full path of the program **RAMMap.exe** (incl. it's name too) (e.g. C:\Users\Insert\Desktop\RAMMap\RAMMap.exe) <br/>
`winxpepath` - It's value must be the full path of where the **WinXPE** program is installed in (excl. it's name) (e.g. D:\WinXPE) <br/>
`adwclrpath` - When a custom path is defined for the program **ADWCleaner** to store it's data in, You will have to specify it in the value of this variable <br/>
**Please keep in mind the variable `adwclrpath` is optional, and the program will function properly without it.** <br/>
`cdpccpath` - When the **ConnectedDevicesPlatform** cache cleaner doesn't function properly, simply create this variable with the name of the folder inside of the folder `%localappdata%\ConnectedDevicesPlatform`, it can be a random numbers or words. <br/>
**Please keep in mind that I no longer support this version**, Consider downloading **v1.52** if you want to get support.
<br/>
## Version 1.52 Update 2 : <br/>
In this update of the project **Temp_Cleaner GUI** I just have replaced the word that says `Welcome to The Temp_Cleaner GUI Project, the renewed version` or whatever it was, with an awesome and a customizable banner, Which allows for better customization (And of course, without any programming knowledge) <br/>
<br/>
## How to change the banner in Update 2? : <br/>
The best feature of Update 2 in Version 1.52 of **Temp_Cleaner GUI**, is that it allows for a better customization for the banner image, if you really want to change the banner image of the program, please first install it on your computer, then go to the path where you installed it in, then go to the file `banner.png` and make the changes you wish to it. <br/>
If you would consider replacing it with a new file, Feel free to do, I won't prevent you so, but before you go, please keep in mind the new picture must be with the *following properties :* <br/>
**Resolution :** 1200x300 (Don't go higher than this, or even lower than this) <br/>
**File extension :** it must be a png file (Portable Network Picture or whatever is it called) <br/>
**Bit Depth :** 32 (Don't go lower than this, or even higher than this) <br/>
<br/>
## Download an already compiled version with installer (Only Windows 10) (64-bit Only) <br/>
If you just want to download an already compiled version alongwith an installer for it (If you are just too lazy to compile the program), and if you are running Windows 10 (Any version) 64-bit edition only, Simply click [here](https://drive.google.com/file/d/1yolD8q6-GZzO3WPWlewmhEvE9HAZV0F7/view?usp=sharing) <br/>
**This is a download link to the latest version of the program, v1.52 Update 2 for Windows 10 64-bit** <br/>
If you can't download it for any reason, feel free to create an issue, and I must be trying my best to resolve your problem. <br/>
<br/>
## Download an already compiled version with installer, but for 32-bit based PCs (Version 1.32 only) <br/>
If you want to download an already compiled version of **Temp_Cleaner GUI v1.32** for **32-bit based PCs**, then this is your lucky day! <br/>
You can get it by clicking [here](https://drive.google.com/file/d/1TPJcLnxAGz-yo5NFUwcRND8PzA9Oyfp4/view?usp=sharing) <br/>
<br/>
## Download an edition for older OSes (Windows 7) (64-bit ONLY!) (Version 1.32 only) <br/>
You can download it by clicking [here](https://drive.google.com/file/d/1NufB2brpUdX-Bg0CdGuhInThyIV71t0e/view?usp=sharing) <br/>
There you go with the link, I can not guarantee it will even work on your computer, it worked for me, but however that doesn't mean it will work for you, as it requires at least a Computer with Windows 7 Service Pack 1 with the latest Windows Updates (basically the IE11 update), and of course **that is 64-bit compatible.** <br/>
Regardless of everything, feel free to try it, as you are losing nothing if it didn't work. <br/>
<br/>
**Please note** : This is only the download link for the version 1.32 of **The Temp_Cleaner GUI Project**, which means it is outdated, Please come here later, when the compiled release of version 1.52 update 2 is published if you want to download it. <br/>
**Download a 32-bit compatible version of Temp_Cleaner GUI for Windows 7** - Click here (Currently Unavailable) <br/>
I will be working on a 32-bit compile of this program, this shouldn't take so long... <br/>
<br/>
-Insert
