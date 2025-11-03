# Changelog

All notable changes to the Network Status Widget project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-11-03

### Added
- Initial release of Network Status Widget by mrbeandev
- System tray integration with signal bar icon
- 6-bar signal strength indicator
- Color-coded status (Green/Orange/Red)
- Real-time network monitoring
- Customizable ping intervals (1s, 3s, 5s, 10s, 30s, custom)
- Configurable ping URL (default: https://mrbean.dev/health)
- Context menu with settings and options
- Proper dialog windows for all settings
- Network connection testing functionality
- About dialog with project information
- Settings persistence between sessions
- PyInstaller build system for creating executables
- Windows startup integration script
- Comprehensive documentation and build instructions

### Features
- **Signal Bars**: Visual representation of connection quality
- **Color Coding**: 
  - Green: Good connection (< 400ms)
  - Orange: Slow connection (400ms - 3000ms)
  - Red: No connection or very slow (> 3000ms)
- **Customizable Monitoring**: User-defined ping intervals and URLs
- **System Integration**: Runs in system tray, minimal resource usage
- **Startup Support**: Easy integration with Windows startup
- **Standalone Executable**: No Python installation required for end users

### Technical Details
- Built with Python 3.7+
- Uses pystray for system tray integration
- PIL/Pillow for icon generation
- tkinter for settings dialogs
- requests for network connectivity testing
- PyInstaller for executable creation

### Documentation
- Complete README with installation and usage instructions
- Detailed build instructions for creating executables
- Contributing guidelines for developers
- MIT License for open source distribution
- Author: mrbeandev | Website: mrbean.dev

## [Unreleased]

### Changed
- Updated default ping URL to `https://mrbean.dev/health` for better reliability
- Improved error handling in all batch scripts
- Enhanced virtual environment management

### Planned Features
- Unit tests for core functionality
- Improved error handling and logging
- Additional network test methods
- Configuration import/export
- Multiple ping URL support
- Network adapter selection
- Bandwidth monitoring capabilities
- Custom themes and icon designs
- Sound notifications for status changes