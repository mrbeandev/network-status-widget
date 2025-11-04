@echo off
setlocal enabledelayedexpansion

echo ========================================
echo Network Status Widget
echo Author: mrbeandev ^| Website: mrbean.dev
echo ========================================
echo.

:: Check if virtual environment exists
if exist ".venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
    if errorlevel 1 (
        echo [ERROR] Failed to activate virtual environment
        goto :run_global
    )
    echo [OK] Virtual environment activated
) else (
    echo No virtual environment found, using global Python...
)

:run_global
echo Starting Network Status Widget...
echo The widget will appear in your system tray.
echo Right-click the signal bars icon for options.
echo.

python taskbar_network_widget.py
if errorlevel 1 (
    echo.
    echo [ERROR] Error starting widget!
    echo.
    echo Possible solutions:
    echo 1. Run install.bat to install dependencies
    echo 2. Run ONE_CLICK_SETUP.bat for complete setup
    echo 3. Check if Python is installed correctly
    echo.
    echo For help visit: mrbean.dev
    echo.
    pause
    exit /b 1
)

echo Widget closed normally.
pause