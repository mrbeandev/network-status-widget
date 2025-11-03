@echo off
setlocal enabledelayedexpansion

echo ========================================
echo Network Status Widget - ONE CLICK SETUP
echo Author: mrbeandev
echo Website: mrbean.dev
echo ========================================
echo.
echo This will:
echo 1. Install all dependencies
echo 2. Build the executable
echo 3. Add to Windows startup
echo.
echo Press any key to continue or Ctrl+C to cancel...
pause >nul

:: Check if Python is installed
echo [1/6] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    goto :error_exit
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python !PYTHON_VERSION! found

:: Create virtual environment
echo.
echo [2/6] Setting up virtual environment...
if exist ".venv" (
    echo ✅ Virtual environment already exists
) else (
    python -m venv .venv
    if errorlevel 1 (
        echo ❌ ERROR: Failed to create virtual environment
        goto :error_exit
    )
    echo ✅ Virtual environment created
)

:: Activate virtual environment
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ ERROR: Failed to activate virtual environment
    goto :error_exit
)
echo ✅ Virtual environment activated

:: Install requirements
echo.
echo [3/6] Installing dependencies...
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo ❌ ERROR: Failed to install dependencies
    echo Check your internet connection and try again
    goto :error_exit
)
echo ✅ Dependencies installed

:: Build executable
echo.
echo [4/6] Building executable...
python build_exe.py
if errorlevel 1 (
    echo ❌ ERROR: Failed to build executable
    goto :error_exit
)

:: Check if executable was created
if not exist "dist\NetworkStatusWidget.exe" (
    echo ❌ ERROR: Executable not found after build
    goto :error_exit
)
echo ✅ Executable built successfully

:: Test the executable briefly
echo.
echo [5/6] Testing executable...
start /wait /min dist\NetworkStatusWidget.exe
timeout /t 2 /nobreak >nul
taskkill /f /im NetworkStatusWidget.exe >nul 2>&1
echo ✅ Executable test completed

:: Add to startup
echo.
echo [6/6] Adding to Windows startup...
set "exe_path=%~dp0dist\NetworkStatusWidget.exe"
set "startup_folder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

if not exist "!exe_path!" (
    echo ❌ ERROR: Executable not found at !exe_path!
    goto :error_exit
)

echo Creating startup shortcut...
powershell -Command "try { $WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('!startup_folder!\Network Status Widget.lnk'); $Shortcut.TargetPath = '!exe_path!'; $Shortcut.WorkingDirectory = '%~dp0dist'; $Shortcut.Description = 'Network Status Widget by mrbeandev - Shows network connectivity in system tray'; $Shortcut.Save(); exit 0 } catch { exit 1 }"

if errorlevel 1 (
    echo ❌ ERROR: Failed to create startup shortcut
    echo You can manually copy the exe to the startup folder:
    echo !startup_folder!
    goto :error_exit
)

echo ✅ Added to Windows startup successfully

echo.
echo ========================================
echo 🎉 ONE CLICK SETUP COMPLETE! 🎉
echo ========================================
echo.
echo ✅ Dependencies installed
echo ✅ Executable built: dist\NetworkStatusWidget.exe
echo ✅ Added to Windows startup
echo.
echo The widget will now:
echo • Start automatically when Windows boots
echo • Show network status in your system tray
echo • Display colorful signal bars for connection quality
echo.
echo To start now: Double-click dist\NetworkStatusWidget.exe
echo To remove from startup: Delete shortcut from startup folder
echo.
echo Author: mrbeandev
echo Website: mrbean.dev
echo GitHub: github.com/mrbeandev
echo.
echo Thank you for using Network Status Widget! 🚀
echo.
pause
exit /b 0

:error_exit
echo.
echo ========================================
echo ❌ SETUP FAILED
echo ========================================
echo.
echo Something went wrong during setup.
echo Please check the error messages above.
echo.
echo For help:
echo • Visit: mrbean.dev
echo • GitHub: github.com/mrbeandev
echo • Check the README.md file
echo.
pause
exit /b 1