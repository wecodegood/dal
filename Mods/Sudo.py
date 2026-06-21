import subprocess
import platform
import getpass
import re
from colorama import init
from termcolor import colored

DANGEROUS_PATTERNS = [
    r'\brm\s+(-[a-zA-Z]*f[a-zA-Z]*\s+|.*--force)',
    r'\brm\s+-rf?\s+/',
    r'\bmkfs\b',
    r'\bdd\s+',
    r'>\s*/dev/sd',
    r'\bshutdown\b',
    r'\breboot\b',
    r'\binit\s+0',
    r'\bhalt\b',
    r'\bformat\b',
]

BLOCKED_COMMANDS = [
    'rm -rf /',
    'rm -rf /*',
    ':(){:|:&};:',
    'dd if=/dev/zero of=/dev/sda',
    'dd if=/dev/random of=/dev/sda',
    'mkfs.ext4 /dev/sda',
]


def is_root():
    import os
    return os.geteuid() == 0


def get_os_type():
    return platform.system().lower()


def detect_terminal():
    current_os = get_os_type()

    if current_os == "linux":
        return "linux", ["bash", "-c"]
    elif current_os == "windows":
        try:
            result = subprocess.run(
                ["wsl", "--list", "--quiet"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                return "wsl", ["wsl", "bash", "-c"]
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        return "windows", None
    return current_os, None


def validate_command(command):
    cmd = command.strip()

    for blocked in BLOCKED_COMMANDS:
        if cmd == blocked:
            return False, f"Blocked dangerous command: {blocked}"

    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, cmd, re.IGNORECASE):
            return False, f"Blocked command matching dangerous pattern: {pattern}"

    return True, None


MAX_SUDO_RETRIES = 3
SUDO_TIMEOUT = 10


def elevate_to_root():
    init()
    current_os, terminal_cmd = detect_terminal()

    if terminal_cmd is None:
        print(colored(f"[-] Unsupported OS: {current_os}. Cannot elevate to root.", "red"))
        return None, None

    if is_root():
        print(colored("[+] Already running as root", "green"))
        return current_os, terminal_cmd

    if current_os == "linux":
        print(colored("[*] Detected Linux OS - Using native terminal", "green"))
    elif current_os == "wsl":
        print(colored("[*] Detected Windows OS - Using WSL", "green"))

    for attempt in range(MAX_SUDO_RETRIES):
        sudo_password = getpass.getpass("[?] Enter sudo password: ")

        print(colored(f"[*] Elevating to root privileges... (attempt {attempt + 1}/{MAX_SUDO_RETRIES})", "yellow"))
        try:
            if current_os == "linux":
                process = subprocess.Popen(
                    ["sudo", "-S", "su", "-c", "echo root_ok"],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
            else:
                process = subprocess.Popen(
                    ["wsl", "bash", "-c", "sudo -S su -c 'echo root_ok'"],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )

            stdout, stderr = process.communicate(
                input=sudo_password + "\n",
                timeout=SUDO_TIMEOUT,
            )

            if process.returncode == 0 and "root_ok" in stdout:
                print(colored("[+] Successfully elevated to root privileges", "green"))
                return current_os, terminal_cmd
            else:
                print(colored("[-] Failed to elevate to root privileges", "red"))
                if stderr:
                    print(colored(f"[-] Error: {stderr.strip()}", "red"))

        except subprocess.TimeoutExpired:
            print(colored(f"[!] sudo su timed out after {SUDO_TIMEOUT} seconds", "red"))
        except Exception as e:
            print(colored(f"[-] Error elevating privileges: {str(e)}", "red"))

        if attempt < MAX_SUDO_RETRIES - 1:
            print(colored("[*] Try again...", "yellow"))

    print(colored("[-] Max sudo attempts reached. Cannot elevate to root.", "red"))
    return None, None


def execute_command(command, current_os, terminal_cmd):
    is_valid, error_msg = validate_command(command)
    if not is_valid:
        print(colored(f"[-] Command rejected: {error_msg}", "red"))
        return None

    try:
        print(colored(f"[>] Executing: {command}", "cyan"))
        print(colored("=" * 60, "blue"))

        if current_os == "linux":
            result = subprocess.run(
                command.strip(),
                shell=True,
                text=True,
                capture_output=True,
                timeout=120,
            )
        else:
            result = subprocess.run(
                terminal_cmd + [command.strip()],
                text=True,
                capture_output=True,
                timeout=120,
            )

        if result.stdout:
            print(colored("[STDOUT]", "green"))
            print(result.stdout)
        if result.stderr:
            print(colored("[STDERR]", "red"))
            print(result.stderr)

        print(colored("=" * 60, "blue"))
        print(colored(f"[=] Exit code: {result.returncode}", "blue"))

        return result

    except subprocess.TimeoutExpired:
        print(colored("[!] Command timed out after 120 seconds", "red"))
        return None
    except Exception as e:
        print(colored(f"[-] Error executing command: {str(e)}", "red"))
        return None
