# Security Policy

## Supported Versions

We actively support the following versions of Network Status Widget:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability in Network Status Widget, please report it responsibly.

### How to Report

1. **Do NOT create a public GitHub issue** for security vulnerabilities
2. Send an email to the maintainers with details about the vulnerability
3. Include as much information as possible:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if you have one)

### What to Expect

- **Acknowledgment**: We'll acknowledge receipt of your report within 48 hours
- **Investigation**: We'll investigate and validate the vulnerability
- **Timeline**: We aim to provide a fix within 30 days for critical issues
- **Credit**: We'll credit you in the security advisory (unless you prefer to remain anonymous)

### Security Considerations

#### Network Requests
- The application makes HTTP/HTTPS requests to test connectivity
- Default URL is `https://mrbean.dev/health` (author's reliable health check endpoint)
- Users can configure custom URLs - ensure they use trusted endpoints
- The default endpoint is maintained by the project author for optimal reliability

#### System Integration
- The application integrates with Windows system tray
- No elevated privileges required
- Settings are stored locally in JSON format

#### Executable Distribution
- Executables are built using PyInstaller
- No code signing currently implemented
- Antivirus software may flag as suspicious (false positive)

### Best Practices for Users

1. **Download from trusted sources**: Only download executables from official GitHub releases
2. **Verify checksums**: Check file hashes when available
3. **Use HTTPS URLs**: When configuring custom ping URLs, prefer HTTPS
4. **Firewall settings**: Ensure your firewall allows the application to make network requests
5. **Regular updates**: Keep the application updated to the latest version

### Scope

This security policy covers:
- The main application (`taskbar_network_widget.py`)
- Build scripts and processes
- Documentation and configuration

Out of scope:
- Third-party dependencies (report to respective projects)
- User system configuration issues
- Network infrastructure problems

### Security Features

- **No data collection**: The application doesn't collect or transmit personal data
- **Local storage only**: Settings are stored locally on the user's machine
- **Minimal permissions**: Runs with standard user privileges
- **Open source**: All code is publicly available for review

Thank you for helping keep Network Status Widget secure!