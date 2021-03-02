:: Batch Script
:: requires choco
@echo off
echo.

:: get privileges
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )

echo.
echo.
echo jetzt ist sehr guter zeitpunkt um tee zu machen, 
echo denn die downloads sind insgesamt etwa 800mb grosz.
echo.
timeout 4

:: Set up choco with PS (deactivated)
:: Set-ExecutionPolicy AllSigned
:: Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

:::: ab hier kann alles problemlos angepasst werden. ::::

:: Tools
choco install git -y
choco install vscode -y
choco install firefox -y
choco install mamp -y

:: Python
choco install python3 -y
python -m pip install --upgrade pip
pip install pywin32

:: Update
choco upgrade all -y