@echo off
setlocal enabledelayedexpansion

echo ========================================
echo Network Status Widget - Build Script
echo Author: mrbeandev ^| Website: mrbean.dev
echo ========================================
echo.
echo This will create an executable file.
echo.
pause

:: Check if virtual environment exists and activate it
if exist ".venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
    if errorlevel 1 (
        echo ❌ Failed to activate virtual environment
        echo Continuing with global Python...
    ) else (
        echo ✅ Virtual environment activated
    )
)

echo.
echo Starting build process...
python build_exe.py

if errorlevel 1 (
    echo.
    echo ❌ Build failed!
    echo Check the error messages above.
    echo.
    echo For help:
    echo • Run install.bat first
    echo • Visit mrbean.dev
    echo • Check README.md
    echo.
) else (
    echo.
    echo ✅ Build completed successfully!
    echo.
    echo Files created:
    if exist "dist\NetworkStatusWidget.exe" (
        echo ✅ dist\NetworkStatusWidget.exe
    )
    if exist "add_to_startup.bat" (
        echo ✅ add_to_startup.bat
    )
    echo.
)

pause