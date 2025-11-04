@echo off
setlocal enabledelayedexpansion

echo ========================================
echo Network Status Widget - Startup Setup
echo Author: mrbeandev ^| Website: mrbean.dev
echo ========================================
echo.

set "exe_path=%~dp0dist\NetworkStatusWidget.exe"
set "startup_folder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

if not exist "!exe_path!" (
    echo [ERROR] NetworkStatusWidget.exe not found!
    echo.
    echo Please build the executable first:
    echo 1. Run build_exe.py, or
    echo 2. Run ONE_CLICK_SETUP.bat
    echo.
    pause
    exit /b 1
)

echo Adding Network Status Widget to Windows startup...
echo.
echo Executable: !exe_path!
echo Startup folder: !startup_folder!
echo.

echo Creating startup shortcut...
powershell -Command "try { $WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('!startup_folder!\Network Status Widget.lnk'); $Shortcut.TargetPath = '!exe_path!'; $Shortcut.WorkingDirectory = '%~dp0dist'; $Shortcut.Description = 'Network Status Widget by mrbeandev - Shows network connectivity in system tray'; $Shortcut.Save(); exit 0 } catch { exit 1 }"

if !errorlevel! equ 0 (
    echo [OK] Successfully added to Windows startup!
    echo.
    echo The widget will now start automatically when Windows boots.
    echo You can find the shortcut at:
    echo !startup_folder!\Network Status Widget.lnk
    echo.
    echo To remove from startup:
    echo 1. Press Win+R, type: shell:startup
    echo 2. Delete "Network Status Widget.lnk"
) else (
    echo [ERROR] Failed to create startup shortcut
    echo.
    echo Manual setup:
    echo 1. Press Win+R, type: shell:startup
    echo 2. Copy NetworkStatusWidget.exe to that folder
    echo.
    echo For help visit: mrbean.dev
)

echo.
echo Author: mrbeandev ^| Website: mrbean.dev
echo.
pause
