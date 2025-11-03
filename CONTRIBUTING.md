# Contributing to Network Status Widget

Thank you for your interest in contributing to the Network Status Widget! This document provides guidelines for contributing to this project.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/network-status-widget.git
   cd network-status-widget
   ```
   
   Original repository: https://github.com/mrbeandev/network-status-widget
3. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Development Setup

### Running from Source
```bash
python taskbar_network_widget.py
```

### Building Executable
```bash
python build_exe.py
```

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small

## 📝 How to Contribute

### Reporting Bugs
1. Check if the bug has already been reported in [Issues](../../issues)
2. If not, create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (Windows version, Python version)
   - Screenshots if applicable

### Suggesting Features
1. Check [Issues](../../issues) for existing feature requests
2. Create a new issue with:
   - Clear description of the feature
   - Use case and benefits
   - Possible implementation approach

### Submitting Code Changes

1. **Create a branch** for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Write clean, readable code
   - Add comments for complex logic
   - Test your changes thoroughly

3. **Test your changes**:
   - Run the application and test all functionality
   - Test the build process
   - Verify the executable works correctly

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: brief description of your changes"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**:
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your branch
   - Provide a clear description of your changes

## 🧪 Testing Guidelines

### Manual Testing Checklist
- [ ] Widget appears in system tray
- [ ] Signal bars display correctly
- [ ] Colors change based on connection quality
- [ ] Context menu works properly
- [ ] Settings dialogs open and close correctly
- [ ] Settings are saved and loaded properly
- [ ] Custom ping URL works
- [ ] Custom intervals work
- [ ] Executable builds without errors
- [ ] Executable runs on clean Windows system

### Test Scenarios
1. **Network Conditions**:
   - Good internet connection
   - Slow internet connection
   - No internet connection
   - Intermittent connection

2. **Settings**:
   - Change ping intervals
   - Change ping URL
   - Change timeout values
   - Invalid inputs

3. **System Integration**:
   - System tray functionality
   - Windows startup integration
   - Multiple monitor setups

## 📋 Code Review Process

1. All submissions require review before merging
2. Reviewers will check for:
   - Code quality and style
   - Functionality and testing
   - Documentation updates
   - Backward compatibility

## 🎯 Areas for Contribution

### High Priority
- [ ] Add unit tests
- [ ] Improve error handling
- [ ] Add logging functionality
- [ ] Performance optimizations
- [ ] Better icon design

### Medium Priority
- [ ] Additional network test methods
- [ ] Configuration import/export
- [ ] Multiple ping URL support
- [ ] Network adapter selection
- [ ] Bandwidth monitoring

### Low Priority
- [ ] Themes and customization
- [ ] Sound notifications
- [ ] Network statistics logging
- [ ] Integration with other tools

## 📚 Resources

- [Python Style Guide (PEP 8)](https://pep8.org/)
- [PyInstaller Documentation](https://pyinstaller.readthedocs.io/)
- [Pystray Documentation](https://pystray.readthedocs.io/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

## 🤝 Community Guidelines

- Be respectful and inclusive
- Help others learn and grow
- Provide constructive feedback
- Follow the code of conduct
- Have fun and be creative!

## 📞 Getting Help

If you need help or have questions:
1. Check the [README.md](README.md) and [BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md)
2. Visit [mrbean.dev](https://mrbean.dev) for additional resources
3. Search existing [Issues](../../issues)
4. Create a new issue with the "question" label
5. Be specific about what you're trying to do and what's not working

## 👨‍💻 Author

**mrbeandev**
- Website: [mrbean.dev](https://mrbean.dev)
- GitHub: [@mrbeandev](https://github.com/mrbeandev)

Thank you for contributing to make this project better! 🎉