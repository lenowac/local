:: Batch Script
@echo off
echo.
echo.
echo.

:: Header
echo leo's quickinstaller
echo.
echo @lenowac, 2019
echo.
echo.
echo this set of scripts will run the choco installer and install some essential apps with it.
timeout 3

:: Make some room
echo.
echo.
echo.
echo.
echo.

:: get privileges
echo getting privileges...
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )

cd setup

:: install choco 
echo next up: chocolatery
echo.
call "install-choco.bat"

echo.

:: install dependencies
echo next up: installing dependencies
echo.
call "install-dependencies.bat"
call "setup-vscode.bat"

echo.

:: move files
echo next up: moving files
echo.
python "setup-files.py"

echo next up: set up mamp
echo.
call "setup-mamp.bat"

echo done :)

echo.
timeout 10
EXIT