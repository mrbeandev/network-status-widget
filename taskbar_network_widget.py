#!/usr/bin/env python3
"""
Network Status Widget - Windows Taskbar Network Connectivity Monitor
Author: mrbeandev
Website: mrbean.dev
GitHub: github.com/mrbeandev

A Windows taskbar widget that shows network connectivity status using signal bars.
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import time
import requests
import json
import os
import sys
from PIL import Image, ImageDraw
import pystray
from pystray import MenuItem as item
import io


class NetworkTaskbarWidget:
    def __init__(self):
        self.load_settings()
        self.setup_variables()
        self.create_tray_icon()
        self.start_monitoring()

    def load_settings(self):
        """Load settings from config file"""
        self.settings_file = "network_widget_settings.json"
        default_settings = {
            "ping_url": "https://mrbean.dev/health",
            "ping_interval": 3,  # seconds
            "timeout": 3,
            "signal_bars": 6,
        }

        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, "r") as f:
                    self.settings = {**default_settings, **json.load(f)}
            else:
                self.settings = default_settings
                self.save_settings()
        except Exception as e:
            print(f"Error loading settings: {e}")
            self.settings = default_settings

    def save_settings(self):
        """Save current settings to file"""
        try:
            with open(self.settings_file, "w") as f:
                json.dump(self.settings, f, indent=2)
        except Exception as e:
            print(f"Error saving settings: {e}")

    def setup_variables(self):
        """Initialize variables"""
        self.current_signal_strength = 0  # 0-6 bars
        self.current_status = "unknown"  # unknown, good, slow, no_connection
        self.monitoring = True
        self.last_response_time = 0

    def create_signal_icon(self, bars_filled, status_color):
        """Create a signal strength icon with specified bars and color"""
        # Create 48x48 icon (larger for better visibility)
        size = 48
        image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        # Define colors with better contrast
        colors = {
            "good": (0, 220, 0, 255),  # Bright Green
            "slow": (255, 140, 0, 255),  # Orange
            "no_connection": (220, 0, 0, 255),  # Red
            "unknown": (120, 120, 120, 255),  # Gray
        }

        active_color = colors.get(status_color, colors["unknown"])
        inactive_color = (80, 80, 80, 180)  # Darker gray, more visible

        # Draw signal bars (6 bars total) - larger and more spaced
        bar_width = 5  # Increased from 3
        bar_spacing = 2  # Increased from 1
        start_x = 3  # Adjusted for larger icon
        base_y = size - 3  # Adjusted for larger icon

        for i in range(self.settings["signal_bars"]):
            bar_height = 6 + (i * 5)  # Increased heights (was 4 + i*3)
            x = start_x + (i * (bar_width + bar_spacing))
            y = base_y - bar_height

            # Choose color based on whether this bar should be filled
            color = active_color if i < bars_filled else inactive_color

            # Draw the bar with rounded corners effect
            draw.rectangle([x, y, x + bar_width, base_y], fill=color)

            # Add a subtle border for better definition
            border_color = (
                (255, 255, 255, 100) if i < bars_filled else (60, 60, 60, 100)
            )
            draw.rectangle([x, y, x + bar_width, base_y], outline=border_color, width=1)

        return image

    def check_network_status(self):
        """Check network status by pinging the configured URL"""
        try:
            start_time = time.time()
            response = requests.get(
                self.settings["ping_url"], timeout=self.settings["timeout"]
            )
            end_time = time.time()

            if response.status_code == 200:
                response_time = (end_time - start_time) * 1000  # Convert to ms
                self.last_response_time = response_time

                # Determine signal strength and status based on response time
                if response_time < 400:
                    return 6, "good"  # All bars, green
                elif response_time < 600:
                    return 5, "good"  # 5 bars, green
                elif response_time < 800:
                    return 4, "good"  # 4 bars, green
                elif response_time < 1000:
                    return 3, "slow"  # 3 bars, orange
                elif response_time < 3000:
                    return 2, "slow"  # 2 bars, orange
                elif response_time < 6000:
                    return 1, "slow"  # 1 bar, orange
                else:
                    return 1, "no_connection"  # 1 bar, red
            else:
                return 0, "no_connection"

        except requests.RequestException as e:
            print(f"Network check failed: {e}")
            return 0, "no_connection"
        except Exception as e:
            print(f"Unexpected error: {e}")
            return 0, "unknown"

    def update_tray_icon(self):
        """Update the system tray icon with current network status"""
        icon_image = self.create_signal_icon(
            self.current_signal_strength, self.current_status
        )

        # Update tooltip text
        status_text = {
            "good": "Good Connection",
            "slow": "Slow Connection",
            "no_connection": "No Connection",
            "unknown": "Checking...",
        }

        tooltip = f"Network Status: {status_text[self.current_status]}"
        if self.last_response_time > 0:
            tooltip += f"\nResponse Time: {self.last_response_time:.0f}ms"
        tooltip += (
            f"\nBars: {self.current_signal_strength}/{self.settings['signal_bars']}"
        )

        # Update the tray icon
        if hasattr(self, "tray_icon"):
            self.tray_icon.icon = icon_image
            self.tray_icon.title = tooltip

    def create_tray_icon(self):
        """Create the system tray icon"""
        # Initial icon
        initial_icon = self.create_signal_icon(0, "unknown")

        # Create context menu
        menu = pystray.Menu(
            item("Network Status", self.show_status, default=True),
            pystray.Menu.SEPARATOR,
            item(
                "Ping Intervals",
                pystray.Menu(
                    item("1 second", lambda: self.set_ping_interval(1)),
                    item("3 seconds", lambda: self.set_ping_interval(3)),
                    item("5 seconds", lambda: self.set_ping_interval(5)),
                    item("10 seconds", lambda: self.set_ping_interval(10)),
                    item("30 seconds", lambda: self.set_ping_interval(30)),
                    item("Custom...", self.set_custom_interval),
                ),
            ),
            item(
                "Settings",
                pystray.Menu(
                    item("Change Ping URL...", self.change_ping_url),
                    item("Set Timeout...", self.set_timeout),
                    item("Test Connection", self.test_connection),
                ),
            ),
            pystray.Menu.SEPARATOR,
            item("About", self.show_about),
            item("Exit", self.exit_application),
        )

        # Create tray icon
        self.tray_icon = pystray.Icon(
            "network_status", initial_icon, "Network Status Widget", menu
        )

    def show_status(self, icon=None, item=None):
        """Show current network status in a message box"""

        def show_dialog():
            status_text = {
                "good": "Good Connection",
                "slow": "Slow Connection",
                "no_connection": "No Connection",
                "unknown": "Checking...",
            }

            message = f"Network Status: {status_text[self.current_status]}\n"
            message += f"Signal Bars: {self.current_signal_strength}/{self.settings['signal_bars']}\n"
            if self.last_response_time > 0:
                message += f"Response Time: {self.last_response_time:.0f}ms\n"
            message += f"Ping URL: {self.settings['ping_url']}\n"
            message += f"Check Interval: {self.settings['ping_interval']} seconds"

            # Create a proper dialog window
            root = tk.Tk()
            root.title("Network Status")
            root.geometry("400x200")
            root.resizable(False, False)

            # Center the window
            root.update_idletasks()
            x = (root.winfo_screenwidth() // 2) - (400 // 2)
            y = (root.winfo_screenheight() // 2) - (200 // 2)
            root.geometry(f"400x200+{x}+{y}")

            # Add message text
            text_widget = tk.Text(root, wrap=tk.WORD, padx=10, pady=10)
            text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            text_widget.insert(tk.END, message)
            text_widget.config(state=tk.DISABLED)

            # Add close button
            close_btn = tk.Button(root, text="Close", command=root.destroy, width=10)
            close_btn.pack(pady=10)

            root.focus_force()
            root.mainloop()

        # Run dialog in separate thread to avoid blocking
        threading.Thread(target=show_dialog, daemon=True).start()

    def set_ping_interval(self, interval):
        """Set the ping interval"""
        self.settings["ping_interval"] = interval
        self.save_settings()

    def set_custom_interval(self, icon=None, item=None):
        """Set a custom ping interval"""

        def show_dialog():
            root = tk.Tk()
            root.title("Custom Interval")
            root.geometry("300x150")
            root.resizable(False, False)

            # Center the window
            root.update_idletasks()
            x = (root.winfo_screenwidth() // 2) - (300 // 2)
            y = (root.winfo_screenheight() // 2) - (150 // 2)
            root.geometry(f"300x150+{x}+{y}")

            # Add label
            label = tk.Label(root, text="Enter ping interval in seconds (1-300):")
            label.pack(pady=10)

            # Add entry
            entry_var = tk.StringVar(value=str(self.settings["ping_interval"]))
            entry = tk.Entry(root, textvariable=entry_var, width=20)
            entry.pack(pady=5)
            entry.focus()

            # Add buttons
            button_frame = tk.Frame(root)
            button_frame.pack(pady=10)

            def save_interval():
                try:
                    interval = int(entry_var.get())
                    if 1 <= interval <= 300:
                        self.settings["ping_interval"] = interval
                        self.save_settings()
                        root.destroy()
                    else:
                        tk.messagebox.showerror(
                            "Error", "Please enter a value between 1 and 300"
                        )
                except ValueError:
                    tk.messagebox.showerror("Error", "Please enter a valid number")

            ok_btn = tk.Button(button_frame, text="OK", command=save_interval, width=8)
            ok_btn.pack(side=tk.LEFT, padx=5)

            cancel_btn = tk.Button(
                button_frame, text="Cancel", command=root.destroy, width=8
            )
            cancel_btn.pack(side=tk.LEFT, padx=5)

            # Bind Enter key to save
            root.bind("<Return>", lambda e: save_interval())

            root.focus_force()
            root.mainloop()

        threading.Thread(target=show_dialog, daemon=True).start()

    def change_ping_url(self, icon=None, item=None):
        """Change the ping URL"""

        def show_dialog():
            root = tk.Tk()
            root.title("Change Ping URL")
            root.geometry("500x150")
            root.resizable(False, False)

            # Center the window
            root.update_idletasks()
            x = (root.winfo_screenwidth() // 2) - (500 // 2)
            y = (root.winfo_screenheight() // 2) - (150 // 2)
            root.geometry(f"500x150+{x}+{y}")

            # Add label
            label = tk.Label(root, text="Enter new ping URL:")
            label.pack(pady=10)

            # Add entry
            entry_var = tk.StringVar(value=self.settings["ping_url"])
            entry = tk.Entry(root, textvariable=entry_var, width=60)
            entry.pack(pady=5, padx=10)
            entry.focus()
            entry.select_range(0, tk.END)

            # Add buttons
            button_frame = tk.Frame(root)
            button_frame.pack(pady=10)

            def save_url():
                new_url = entry_var.get().strip()
                if new_url:
                    if new_url.startswith(("http://", "https://")):
                        self.settings["ping_url"] = new_url
                        self.save_settings()
                        root.destroy()
                    else:
                        tk.messagebox.showerror(
                            "Error", "URL must start with http:// or https://"
                        )
                else:
                    tk.messagebox.showerror("Error", "Please enter a valid URL")

            ok_btn = tk.Button(button_frame, text="OK", command=save_url, width=8)
            ok_btn.pack(side=tk.LEFT, padx=5)

            cancel_btn = tk.Button(
                button_frame, text="Cancel", command=root.destroy, width=8
            )
            cancel_btn.pack(side=tk.LEFT, padx=5)

            # Bind Enter key to save
            root.bind("<Return>", lambda e: save_url())

            root.focus_force()
            root.mainloop()

        threading.Thread(target=show_dialog, daemon=True).start()

    def set_timeout(self, icon=None, item=None):
        """Set request timeout"""

        def show_dialog():
            root = tk.Tk()
            root.title("Set Timeout")
            root.geometry("300x150")
            root.resizable(False, False)

            # Center the window
            root.update_idletasks()
            x = (root.winfo_screenwidth() // 2) - (300 // 2)
            y = (root.winfo_screenheight() // 2) - (150 // 2)
            root.geometry(f"300x150+{x}+{y}")

            # Add label
            label = tk.Label(root, text="Enter request timeout in seconds (1-30):")
            label.pack(pady=10)

            # Add entry
            entry_var = tk.StringVar(value=str(self.settings["timeout"]))
            entry = tk.Entry(root, textvariable=entry_var, width=20)
            entry.pack(pady=5)
            entry.focus()

            # Add buttons
            button_frame = tk.Frame(root)
            button_frame.pack(pady=10)

            def save_timeout():
                try:
                    timeout = int(entry_var.get())
                    if 1 <= timeout <= 30:
                        self.settings["timeout"] = timeout
                        self.save_settings()
                        root.destroy()
                    else:
                        tk.messagebox.showerror(
                            "Error", "Please enter a value between 1 and 30"
                        )
                except ValueError:
                    tk.messagebox.showerror("Error", "Please enter a valid number")

            ok_btn = tk.Button(button_frame, text="OK", command=save_timeout, width=8)
            ok_btn.pack(side=tk.LEFT, padx=5)

            cancel_btn = tk.Button(
                button_frame, text="Cancel", command=root.destroy, width=8
            )
            cancel_btn.pack(side=tk.LEFT, padx=5)

            # Bind Enter key to save
            root.bind("<Return>", lambda e: save_timeout())

            root.focus_force()
            root.mainloop()

        threading.Thread(target=show_dialog, daemon=True).start()

    def test_connection(self, icon=None, item=None):
        """Test the current connection"""

        def show_test():
            root = tk.Tk()
            root.title("Connection Test")
            root.geometry("350x200")
            root.resizable(False, False)

            # Center the window
            root.update_idletasks()
            x = (root.winfo_screenwidth() // 2) - (350 // 2)
            y = (root.winfo_screenheight() // 2) - (200 // 2)
            root.geometry(f"350x200+{x}+{y}")

            # Add status label
            status_label = tk.Label(
                root, text="Testing connection... Please wait.", pady=20
            )
            status_label.pack()

            # Add progress indicator (simple text animation)
            progress_label = tk.Label(root, text="●", font=("Arial", 20))
            progress_label.pack()

            result_text = tk.Text(root, height=6, width=40, wrap=tk.WORD)
            result_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

            close_btn = tk.Button(root, text="Close", command=root.destroy, width=10)
            close_btn.pack(pady=5)

            def run_test():
                try:
                    # Animate progress
                    for i in range(3):
                        progress_label.config(text="●" * (i + 1))
                        root.update()
                        time.sleep(0.5)

                    signal_strength, status = self.check_network_status()

                    status_text = {
                        "good": "Good Connection",
                        "slow": "Slow Connection",
                        "no_connection": "No Connection",
                        "unknown": "Connection Test Failed",
                    }

                    message = f"Test Result: {status_text[status]}\n"
                    if self.last_response_time > 0:
                        message += f"Response Time: {self.last_response_time:.0f}ms\n"
                    message += f"Signal Bars: {signal_strength}/{self.settings['signal_bars']}\n"
                    message += f"URL Tested: {self.settings['ping_url']}"

                    status_label.config(text="Test Complete!")
                    progress_label.config(text="✓", fg="green")
                    result_text.insert(tk.END, message)
                    result_text.config(state=tk.DISABLED)

                except Exception as e:
                    status_label.config(text="Test Failed!")
                    progress_label.config(text="✗", fg="red")
                    result_text.insert(tk.END, f"Connection test failed: {str(e)}")
                    result_text.config(state=tk.DISABLED)

            # Run test in background
            threading.Thread(target=run_test, daemon=True).start()

            root.focus_force()
            root.mainloop()

        threading.Thread(target=show_test, daemon=True).start()

    def show_about(self, icon=None, item=None):
        """Show about dialog"""

        def show_dialog():
            root = tk.Tk()
            root.title("About Network Status Widget")
            root.geometry("450x300")
            root.resizable(False, False)

            # Center the window
            root.update_idletasks()
            x = (root.winfo_screenwidth() // 2) - (450 // 2)
            y = (root.winfo_screenheight() // 2) - (300 // 2)
            root.geometry(f"450x300+{x}+{y}")

            about_text = """Network Status Widget v1.0

A Windows taskbar widget that shows network connectivity status using signal bars.

Author: mrbeandev
Website: mrbean.dev
GitHub: github.com/mrbeandev

Features:
• 6-bar signal strength indicator
• Color-coded status (Green/Orange/Red)
• Customizable ping intervals
• Configurable ping URL
• System tray integration

Default URL: https://mrbean.dev/health

This widget monitors your internet connection by sending requests to the configured URL and displays the connection quality using colored signal bars in your system tray.

Made with ❤️ for Windows users"""

            # Add text widget
            text_widget = tk.Text(root, wrap=tk.WORD, padx=10, pady=10)
            text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            text_widget.insert(tk.END, about_text)
            text_widget.config(state=tk.DISABLED)

            # Add close button
            close_btn = tk.Button(root, text="Close", command=root.destroy, width=10)
            close_btn.pack(pady=10)

            root.focus_force()
            root.mainloop()

        threading.Thread(target=show_dialog, daemon=True).start()

    def monitor_network(self):
        """Background thread to monitor network status"""
        while self.monitoring:
            try:
                signal_strength, status = self.check_network_status()

                # Update current status
                self.current_signal_strength = signal_strength
                self.current_status = status

                # Update tray icon
                self.update_tray_icon()

                # Wait for next check
                time.sleep(self.settings["ping_interval"])

            except Exception as e:
                print(f"Error in network monitoring: {e}")
                time.sleep(5)  # Wait 5 seconds on error

    def start_monitoring(self):
        """Start the network monitoring thread"""
        self.monitor_thread = threading.Thread(target=self.monitor_network, daemon=True)
        self.monitor_thread.start()

    def exit_application(self, icon=None, item=None):
        """Exit the application"""
        self.monitoring = False
        if hasattr(self, "tray_icon"):
            self.tray_icon.stop()

    def run(self):
        """Run the application"""
        try:
            # Start the tray icon
            self.tray_icon.run()
        except KeyboardInterrupt:
            self.exit_application()


def main():
    """Main function to start the application"""
    # Check if required modules are available
    try:
        import pystray
        from PIL import Image, ImageDraw
    except ImportError as e:
        print(f"Missing required module: {e}")
        print("Installing required packages...")
        try:
            import subprocess

            subprocess.check_call(
                [
                    sys.executable,
                    "-m",
                    "pip",
                    "install",
                    "pystray",
                    "Pillow",
                    "requests",
                ]
            )
            print("Packages installed successfully. Please restart the application.")
            return
        except Exception as install_error:
            print(f"Failed to install packages: {install_error}")
            print("Please manually install: pip install pystray Pillow requests")
            return

    # Create and run the widget
    try:
        widget = NetworkTaskbarWidget()
        widget.run()
    except Exception as e:
        print(f"Error starting application: {e}")
        input("Press Enter to exit...")


if __name__ == "__main__":
    main()
