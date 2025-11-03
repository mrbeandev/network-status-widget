# Build Instructions - Network Status Widget

This guide will help you create an executable file and set it up to start automatically with Windows.

## Quick Start

1. **Build the executable:**

    ```cmd
    python build_exe.py
    ```

    Or simply double-click `build.bat`

2. **Add to Windows startup:**
    - Right-click `add_to_startup.bat` and select "Run as administrator"
    - This will add the widget to your Windows startup folder

## Detailed Steps

### Step 1: Install Dependencies

```cmd
pip install -r requirements.txt
```

### Step 2: Build Executable

Run the build script:

```cmd
python build_exe.py
```

This will:

-   Install PyInstaller if needed
-   Create a custom spec file for optimal build
-   Build the executable with all dependencies included
-   Create a startup script
-   Clean up temporary files

### Step 3: Test the Executable

```cmd
dist\NetworkStatusWidget.exe
```

The widget should appear in your system tray. Right-click the signal bars for options.

### Step 4: Add to Windows Startup

**Option A: Automatic (Recommended)**

1. Right-click `add_to_startup.bat`
2. Select "Run as administrator"
3. The script will create a shortcut in your Windows startup folder

**Option B: Manual**

1. Press `Win + R`, type `shell:startup`, press Enter
2. Copy `dist\NetworkStatusWidget.exe` to this folder
3. Or create a shortcut to the exe in this folder

## File Structure After Build

```
project/
├── dist/
│   └── NetworkStatusWidget.exe    # Main executable
├── taskbar_network_widget.py      # Source code
├── requirements.txt               # Dependencies
├── build_exe.py                  # Build script
├── build.bat                     # Build launcher
├── add_to_startup.bat            # Startup installer
└── BUILD_INSTRUCTIONS.md         # This file
```

## Troubleshooting

### Build Issues

-   **PyInstaller not found:** Run `pip install pyinstaller`
-   **Missing modules:** Run `pip install -r requirements.txt`
-   **Build fails:** Check Python version (3.7+ required)

### Runtime Issues

-   **Widget doesn't appear:** Check system tray (notification area)
-   **No internet detection:** Check firewall settings
-   **Startup doesn't work:** Run `add_to_startup.bat` as administrator

### Removing from Startup

1. Press `Win + R`, type `shell:startup`, press Enter
2. Delete the "Network Status Widget.lnk" shortcut

## Advanced Configuration

### Custom Icon

To add a custom icon to the executable:

1. Create or download a `.ico` file
2. Edit `build_exe.py` and change `icon=None` to `icon='your_icon.ico'`
3. Rebuild the executable

### Build Options

The build script creates a single-file executable with:

-   No console window
-   All dependencies included
-   Optimized with UPX compression
-   Hidden imports for all required modules

## Security Note

Some antivirus software may flag PyInstaller executables as suspicious. This is a false positive common with packaged Python applications. You can:

1. Add an exception in your antivirus software
2. Build on the target machine to avoid detection
3. Use code signing (requires a certificate)

## Distribution

The `NetworkStatusWidget.exe` file is completely standalone and can be:

-   Copied to other Windows machines
-   Shared with others
-   Run without Python installed
-   Added to any Windows startup folder
