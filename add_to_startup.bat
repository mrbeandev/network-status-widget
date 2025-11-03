@echo off
echo Adding Network Status Widget to Windows Startup
echo ===============================================

set "exe_path=%~dp0dist\NetworkStatusWidget.exe"
set "startup_folder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

if not exist "%exe_path%" (
    echo ERROR: NetworkStatusWidget.exe not found!
    echo Please run build_exe.py first to create the executable.
    pause
    exit /b 1
)

echo Creating shortcut in startup folder...
powershell -Command "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%startup_folder%\Network Status Widget.lnk'); $Shortcut.TargetPath = '%exe_path%'; $Shortcut.WorkingDirectory = '%~dp0dist'; $Shortcut.Description = 'Network Status Widget - Shows network connectivity in system tray'; $Shortcut.Save()"

if %errorlevel% equ 0 (
    echo ✓ Successfully added to Windows startup!
    echo The widget will now start automatically when Windows boots.
    echo.
    echo To remove from startup, delete the shortcut from:
    echo %startup_folder%
) else (
    echo ✗ Failed to create startup shortcut
)

echo.
pause
