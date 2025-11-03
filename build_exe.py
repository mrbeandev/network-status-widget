#!/usr/bin/env python3
"""
Build script to create an executable for the Network Status Widget
Author: mrbeandev
Website: mrbean.dev
GitHub: github.com/mrbeandev
"""

import subprocess
import sys
import os
import shutil
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("✓ PyInstaller is already installed")
        return True
    except ImportError:
        print("Installing PyInstaller...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("✓ PyInstaller installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to install PyInstaller: {e}")
            return False

def create_spec_file():
    """Create a custom spec file for better executable configuration"""
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['taskbar_network_widget.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PIL._tkinter_finder',
        'tkinter',
        'tkinter.messagebox',
        'tkinter.simpledialog',
        'pystray._win32',
        'requests.packages.urllib3',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='NetworkStatusWidget',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # You can add an .ico file path here if you have one
)
'''
    
    with open('network_widget.spec', 'w') as f:
        f.write(spec_content)
    print("✓ Created custom spec file")

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building executable...")
    
    try:
        # Use the custom spec file
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--clean",
            "--noconfirm",
            "network_widget.spec"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✓ Executable built successfully!")
            return True
        else:
            print(f"✗ Build failed:")
            print(result.stdout)
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"✗ Error during build: {e}")
        return False

def cleanup_build_files():
    """Clean up temporary build files"""
    print("Cleaning up build files...")
    
    # Remove build directories
    for dir_name in ['build', '__pycache__']:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"✓ Removed {dir_name} directory")
    
    # Remove spec file
    if os.path.exists('network_widget.spec'):
        os.remove('network_widget.spec')
        print("✓ Removed spec file")

def create_startup_script():
    """Create a script to add the exe to Windows startup"""
    startup_script = '''@echo off
setlocal enabledelayedexpansion

echo ========================================
echo Network Status Widget - Startup Setup
echo Author: mrbeandev ^| Website: mrbean.dev
echo ========================================
echo.

set "exe_path=%~dp0dist\\NetworkStatusWidget.exe"
set "startup_folder=%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

if not exist "!exe_path!" (
    echo ❌ ERROR: NetworkStatusWidget.exe not found!
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
powershell -Command "try { $WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('!startup_folder!\\Network Status Widget.lnk'); $Shortcut.TargetPath = '!exe_path!'; $Shortcut.WorkingDirectory = '%~dp0dist'; $Shortcut.Description = 'Network Status Widget by mrbeandev - Shows network connectivity in system tray'; $Shortcut.Save(); exit 0 } catch { exit 1 }"

if !errorlevel! equ 0 (
    echo ✅ Successfully added to Windows startup!
    echo.
    echo The widget will now start automatically when Windows boots.
    echo You can find the shortcut at:
    echo !startup_folder!\\Network Status Widget.lnk
    echo.
    echo To remove from startup:
    echo 1. Press Win+R, type: shell:startup
    echo 2. Delete "Network Status Widget.lnk"
) else (
    echo ❌ Failed to create startup shortcut
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
'''
    
    with open('add_to_startup.bat', 'w') as f:
        f.write(startup_script)
    print("✓ Created startup script: add_to_startup.bat")

def main():
    """Main build process"""
    print("Network Status Widget - Build Script")
    print("Author: mrbeandev | Website: mrbean.dev")
    print("====================================")
    print()
    
    try:
        # Check if main file exists
        if not os.path.exists('taskbar_network_widget.py'):
            print("✗ taskbar_network_widget.py not found!")
            print("Make sure you're running this script from the project directory.")
            return False
        
        # Install PyInstaller
        if not install_pyinstaller():
            return False
        
        # Install requirements
        print("Installing requirements...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--quiet"
            ])
            print("✓ Requirements installed")
        except subprocess.CalledProcessError as e:
            print(f"✗ Failed to install requirements: {e}")
            print("Make sure you have an active internet connection.")
            return False
        except FileNotFoundError:
            print("✗ requirements.txt not found!")
            return False
        
        # Create spec file
        create_spec_file()
        
        # Build executable
        if not build_executable():
            return False
        
        # Verify executable was created
        if not os.path.exists('dist/NetworkStatusWidget.exe'):
            print("✗ Executable was not created successfully!")
            return False
        
        # Create startup script
        create_startup_script()
        
        # Clean up
        cleanup_build_files()
        
        print()
        print("🎉 Build completed successfully!")
        print()
        print("Files created:")
        print("  📁 dist/NetworkStatusWidget.exe - The main executable")
        print("  📄 add_to_startup.bat - Script to add to Windows startup")
        print()
        print("Next steps:")
        print("1. Test the executable: dist/NetworkStatusWidget.exe")
        print("2. Add to startup: Run add_to_startup.bat as administrator")
        print("3. Or use ONE_CLICK_SETUP.bat for automatic setup")
        print()
        print("Author: mrbeandev | Website: mrbean.dev")
        print()
        
        return True
        
    except KeyboardInterrupt:
        print("\n✗ Build cancelled by user")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected error during build: {e}")
        print("For help, visit: mrbean.dev")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        print("Build failed!")
        sys.exit(1)