# Temp_Cleaner GUI Project
A free (and of course an **Open-Source**) alternative to all Temp Cleaning Software available for all Windows Versions that can be expanded by you!<br/>
<br/>

## Inside of the program <br/>
**Might not always be up-to-date.**
<br/>
<br/>
![A screenshot of the inside of the program Temp_Cleaner GUI](https://raw.githubusercontent.com/InsertX2k/temp_cleaner_gui/gh-pages/ss0.jpg) <br/>
<br/>


## Download a compiled version: <br/>
**I've moved the official downloads section from this page to the better UI Github page, so feel free to go there to download the compiled version of such software.**
<br/>

## How to compile? <br/>
**In order to properly compile, You will need all of the following :** <br/>
* `Pyinstaller` or `auto-py-to-exe`; any of these software can be installed using Python PIP through any of the following appropriate commands : <br/>
```
pip install pyinstaller
```
Or:

```
python -m pip install pyinstaller
```

<br/>

```
pip install auto-py-to-exe
```
Or:
```
python -m pip install auto-py-to-exe
```
<br/>

* **Python Modules** `PIL/pillow` and `WINTCMD` <br/>
```
pip install pillow
```
Or:
```
python -m pip install pillow
```
Or:
```
pip install PIL
```
Or:
```
python -m pip install PIL
```
<br/>

About the module `WINTCMD`, you can download it from the source code files (**of course in this branch**), **and don't forget to include it in the `--hidden-import` option if you will use `Pyinstaller`**. <br/>

<br/>

**Of course [Python 3.9.x](https://www.python.org/downloads/) is a must have.**

<br/>

**Once you have all the requirements on your computer/workstation, do all of the following :**

1-**Choose the script file `temp_cleaner_gui_project_renewed_gui_sourcecode.py` as the script file you want to compile (If using `Pyinstaller` or `auto-py-to-exe`)** <br/>
2-Choose the **icon** file as `icon0.ico` <br/>
3-Choose the window mode as `Windowed` or to hide the console window. <br/>
4-**Do not choose the output file as a single file, instead choose one directory.** <br/>
5-**Choose to include all of the following files :** <br/>
```bat
banner.png
Config.ini
icon0.ico
nul'
```

<br/>

6-Enable the option to request Administrative privileges from the user `--uac-admin` <br/>
7-**If you want to**, Create a **version file** and include it with the compiled version. <br/>
8-**Choose all of the following modules to be imported using the `--hidden-import` option** <br/>
```py
re
WINTCMD
PIL
pillow
temp_cleaner_gui_project_renewed_gui_sourcecode
```

<br/>

9-**About the option `--name`, name it whatever you want, Here is a suggestion `UltimateProgrammerCodePy`.** <br/>

10-When you are done, choose to compile using `Pyinstaller` either by pressing the button `Convert py to exe` if using `auto-py-to-exe`, or by pressing the `enter` button in your keyboard if using the command line interface of `Pyinstaller` <br/>

11-**Wait for the compiling process to be done, ignore the warnings, and you are done, Enjoy!** <br/>



## Copyrights <br/>


The icon of the program, and the file **icon0.ico** is just a modified icon image that is originally owned by the **Numix Icon pack** author


<br/>

<br/>

## What's new in all updates?, Anyone? <br/>
Simply open the tags (or releases) in this repository, this should help you clearly understand every new update to this program and what it does. <br/>

<br/>

## Found a bug?, Got a suggestion for any new features? <br/>
Simply create a new issue, and be sure to properly describe the bug if you are reporting a bug, and if you are suggesting a new feature, clearly describe it in the issue you will create, and tell us why should we add this feature (basically why do you think this feature will be useful), and we will try to reply you as fast as possible. <br/>

## How to change the banner in Update 2? : <br/>


The best feature of Update 2 in Version 1.52 of **Temp_Cleaner GUI**, is that it allows for a better customization for the banner image, if you really want to change the banner image of the program, please first install it on your computer, then go to the path where you installed it in, then go to the file `banner.png` and make the changes you wish to it. <br/>


If you would consider replacing it with a new file, Feel free to do, I won't prevent you so, but before you go, please keep in mind the new picture must be with the *following properties :* <br/>


**Resolution :** **1200x300** (Don't go higher than this, or even lower than this) <br/>


**File extension :** it must be a **png** file (Portable Network Picture or whatever is it called) <br/>


**Bit Depth :** 32 (Don't go lower than this, or even higher than this) <br/>


<br/>

## Download an already compiled release with installer: <br/>
**This page is not where you are supposed to find any compiled releases of such software, consider going to [This link](https://insertx2k.github.io/temp_cleaner_gui) for official downloads.**

## Additional Downloadable banners for **The Temp_Cleaner GUI Project v1.52 Update 2 & 3 & 4** <br/>


If you feel bored of the default banner, and you don't have any suggestions for a new cool banner, or you even don't know how to create a new one for yourself, simply click [here](https://github.com/InsertX2k/temp_cleaner_gui/tree/main/additional-downloadable-banners), for some awesome additional downloadable banners for the program! <br/>



**Please keep in mind that it also includes the installation guide, simply in the README.md** <br/>


<br/>


**-Insert**
