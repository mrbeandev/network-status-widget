@echo off
setlocal enabledelayedexpansion

echo ========================================
echo Network Status Widget - Installation
echo Author: mrbeandev
echo Website: mrbean.dev
echo ========================================
echo.

:: Check if Python is installed
echo [1/4] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

:: Get Python version for display
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✓ Python !PYTHON_VERSION! found

:: Create virtual environment
echo.
echo [2/4] Creating virtual environment...
if exist ".venv" (
    echo ✓ Virtual environment already exists
) else (
    python -m venv .venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        echo Make sure you have the 'venv' module installed
        pause
        exit /b 1
    )
    echo ✓ Virtual environment created successfully
)

:: Activate virtual environment
echo.
echo [3/4] Activating virtual environment...
call .venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo ✓ Virtual environment activated

:: Install requirements
echo.
echo [4/4] Installing required packages...
pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install required packages
    echo Check your internet connection and try again
    pause
    exit /b 1
)
echo ✓ All packages installed successfully

echo.
echo ========================================
echo Installation Complete! 🎉
echo ========================================
echo.
echo Next steps:
echo 1. Run the widget: run_taskbar_widget.bat
echo 2. Or build executable: build.bat
echo 3. Or one-click setup: ONE_CLICK_SETUP.bat
echo.
echo The widget will appear in your system tray.
echo Right-click the signal bars for settings.
echo.
echo Author: mrbeandev ^| Website: mrbean.dev
echo.
pause