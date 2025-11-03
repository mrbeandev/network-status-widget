# 📶 Network Status Widget

<div align="center">

![Network Status Widget](https://img.shields.io/badge/Platform-Windows-blue?style=for-the-badge&logo=windows)
![Python](https://img.shields.io/badge/Python-3.7+-green?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**A sleek Windows taskbar widget that displays real-time network connectivity status using colorful signal bars in your system tray.**

**Author:** [mrbeandev](https://github.com/mrbeandev) • **Website:** [mrbean.dev](https://mrbean.dev)

[📥 Download](#installation--usage) • [🚀 Quick Start](#quick-start) • [🔧 Build](#building-executable) • [🤝 Contribute](CONTRIBUTING.md)

</div>

---

## ✨ Features

🎯 **Visual Network Monitoring**
- 6-bar signal strength indicator in system tray
- Real-time connection quality assessment
- Color-coded status for instant recognition

🎨 **Smart Color Coding**
- 🟢 **Green**: Excellent connection (< 400ms response)
- 🟠 **Orange**: Slow connection (400ms - 3000ms response)  
- 🔴 **Red**: No connection or very poor (> 3000ms response)

⚙️ **Highly Customizable**
- Configurable ping intervals (1s, 3s, 5s, 10s, 30s, or custom)
- Custom ping URL support (default: `https://mrbean.dev/health`)
- Adjustable timeout settings
- Persistent settings storage

🖥️ **System Integration**
- Lightweight system tray application
- Windows startup integration
- Minimal resource usage
- No console window interference

📦 **Easy Distribution**
- Single executable file (no Python required)
- Portable - runs on any Windows machine
- Simple startup folder integration

## Features

- **6-bar signal strength indicator** in the taskbar
- **Color-coded status:**
  - 🟢 Green: Good connection (fast response times)
  - 🟠 Orange: Slow connection (moderate response times)
  - 🔴 Red: No connection or very slow
  
- **System tray integration:** Lives in your taskbar notification area
- **Customizable ping intervals:** 1s, 3s, 5s, 10s, 30s, or custom
- **Configurable ping URL:** Default uses `https://mrbean.dev/health`
- **Real-time monitoring:** Continuous network status updates
- **Context menu:** Right-click for settings and options

## 🚀 Quick Start

### Option 1: Download Executable (Recommended)
1. Download the latest `NetworkStatusWidget.exe` from [Releases](../../releases)
2. Run the executable - it will appear in your system tray
3. Right-click the signal bars for settings and options

### Option 2: Run from Source
1. **Clone the repository:**
   ```bash
   git clone https://github.com/mrbeandev/network-status-widget.git
   cd network-status-widget
   ```

2. **Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Run the widget:**
   ```cmd
   python taskbar_network_widget.py
   ```

## 📥 Installation & Usage

## How to Use

1. After starting, look for the signal bars icon in your system tray (taskbar notification area)
2. The bars will fill up based on connection quality:
   - More bars = better connection
   - Color indicates overall status
3. **Right-click** the icon for options:
   - View current status
   - Change ping intervals
   - Modify ping URL
   - Test connection
   - Exit application

## Signal Bar Meanings

- **6 bars (Green):** Excellent connection (< 100ms)
- **5 bars (Green):** Very good connection (< 200ms)
- **4 bars (Green):** Good connection (< 400ms)
- **3 bars (Orange):** Fair connection (< 800ms)
- **2 bars (Orange):** Slow connection (< 1500ms)
- **1 bar (Orange/Red):** Very slow connection (< 3000ms)
- **0 bars (Red):** No connection

## Customization

The widget automatically saves your preferences:
- Ping interval (how often to check)
- Custom ping URL (default: https://mrbean.dev/health)
- Request timeout settings

All settings are stored in `network_widget_settings.json` and persist between sessions.

## Building Executable

To create a standalone executable file:

1. **Build the exe:**
   ```cmd
   python build_exe.py
   ```
   Or double-click `build.bat`

2. **Add to Windows startup:**
   - Right-click `add_to_startup.bat` and "Run as administrator"
   - The widget will now start automatically with Windows

The executable will be created in the `dist/` folder as `NetworkStatusWidget.exe`.

For detailed build instructions, see [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md).

## 📸 Screenshots

### System Tray Integration
The widget appears as signal bars in your Windows system tray, showing connection status at a glance.

### Context Menu
Right-click the icon to access all settings and options:
- View current network status
- Change ping intervals
- Modify ping URL
- Test connection
- Access about information

## 🎯 Signal Bar Meanings

| Bars | Color | Status | Response Time |
|------|-------|--------|---------------|
| 6 bars | 🟢 Green | Excellent | < 100ms |
| 5 bars | 🟢 Green | Very Good | < 200ms |
| 4 bars | 🟢 Green | Good | < 400ms |
| 3 bars | 🟠 Orange | Fair | < 800ms |
| 2 bars | 🟠 Orange | Slow | < 1500ms |
| 1 bar | 🟠 Orange | Very Slow | < 3000ms |
| 0 bars | 🔴 Red | No Connection | No response |

## 🔧 Configuration

The widget automatically saves your preferences in `network_widget_settings.json`:

```json
{
  "ping_url": "https://mrbean.dev/health",
  "ping_interval": 5,
  "timeout": 3,
  "signal_bars": 6
}
```

### Customizable Settings
- **Ping URL**: Any HTTP/HTTPS endpoint for connectivity testing
- **Ping Interval**: How often to check connection (1-300 seconds)
- **Timeout**: Request timeout duration (1-30 seconds)
- **Signal Bars**: Number of bars to display (fixed at 6)

## 🚀 Adding to Windows Startup

### Automatic Method (Recommended)
1. Build or download the executable
2. Right-click `add_to_startup.bat` and select "Run as administrator"
3. The widget will now start automatically with Windows

### Manual Method
1. Press `Win + R`, type `shell:startup`, press Enter
2. Copy `NetworkStatusWidget.exe` to the startup folder
3. The widget will start with Windows

## 🛠️ Development

### Prerequisites
- Python 3.7 or higher
- Windows operating system
- Internet connection for testing

### Setting up Development Environment
```bash
# Clone the repository
git clone https://github.com/mrbeandev/network-status-widget.git
cd network-status-widget

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run from source
python taskbar_network_widget.py
```

### Project Structure
```
network-status-widget/
├── taskbar_network_widget.py    # Main application
├── build_exe.py                 # Build script
├── requirements.txt             # Dependencies
├── README.md                    # This file
├── BUILD_INSTRUCTIONS.md        # Build guide
├── CONTRIBUTING.md              # Contribution guidelines
├── CHANGELOG.md                 # Version history
├── LICENSE                      # MIT License
└── .gitignore                   # Git ignore rules
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute
- 🐛 Report bugs and issues
- 💡 Suggest new features
- 🔧 Submit code improvements
- 📚 Improve documentation
- 🎨 Design better icons or UI

## 📋 Roadmap

- [ ] Unit tests and automated testing
- [ ] Multiple ping URL support
- [ ] Network adapter selection
- [ ] Bandwidth monitoring
- [ ] Custom themes and icons
- [ ] Sound notifications
- [ ] Network statistics logging
- [ ] Configuration import/export

## 🐛 Troubleshooting

### Common Issues

**Widget doesn't appear in system tray**
- Check if the application is running in Task Manager
- Look in the hidden icons area (click the up arrow in system tray)

**No network detection**
- Check firewall settings
- Try changing the ping URL in settings
- Verify internet connection with browser

**Build fails**
- Ensure Python 3.7+ is installed
- Run `pip install -r requirements.txt`
- Check for antivirus interference

**Startup doesn't work**
- Run `add_to_startup.bat` as administrator
- Manually check the startup folder: `Win + R` → `shell:startup`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [pystray](https://github.com/moses-palmer/pystray) for system tray integration
- Uses [Pillow](https://python-pillow.org/) for icon generation
- Packaged with [PyInstaller](https://www.pyinstaller.org/) for distribution
- Network testing via [mrbean.dev](https://mrbean.dev) health endpoint

---

<div align="center">

**Made with ❤️ for Windows users who want to monitor their network connection**

**Author:** [mrbeandev](https://github.com/mrbeandev) • **Website:** [mrbean.dev](https://mrbean.dev)

[⭐ Star this repo](../../stargazers) • [🐛 Report Bug](../../issues) • [💡 Request Feature](../../issues)

</div>