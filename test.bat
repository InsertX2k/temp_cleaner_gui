@echo off
cls
title Temp_Cleaner GUI Website - Run on Local Server
echo Running a test server on localhost...
echo.
py -m http.server 8000
echo.
echo Server stopped!
pause >nul
exit /b 0