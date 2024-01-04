import subprocess
import time

# Define the list of commands
commands = [
    "sudo apt update",
    "sudo DEBIAN_FRONTEND=nointeractive apt-get install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver",
    "sudo apt install screen",
    "wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb",
    "sudo dpkg -i chrome-remote-desktop_current_amd64.deb",
    "sudo apt --fix-broken install -y",
    "sudo dpkg -i chrome-remote-desktop_current_amd64.deb",
    "sudo apt install firefox"
]

# Execute commands one by one
for command in commands:
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error message: {e}")
        break
    time.sleep(1)  # Wait for a short time between commands
