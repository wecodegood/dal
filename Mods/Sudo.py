import subprocess
import platform
import getpass
from colorama import init
from termcolor import colored


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


MAX_SUDO_RETRIES = 3
SUDO_TIMEOUT = 10


def elevate_to_root():
    init()
    current_os, terminal_cmd = detect_terminal()

    if terminal_cmd is None:
        print(colored(f"Unsupported OS: {current_os}. Cannot elevate to root.", "red"))
        return None, None

    if current_os == "linux":
        print(colored("Detected Linux OS - Using native terminal", "green"))
    elif current_os == "wsl":
        print(colored("Detected Windows OS - Using WSL", "green"))

    for attempt in range(MAX_SUDO_RETRIES):
        sudo_password = getpass.getpass("Enter sudo password: ")

        print(colored(f"Elevating to root privileges... (attempt {attempt + 1}/{MAX_SUDO_RETRIES})", "yellow"))
        try:
            if current_os == "linux":
                process = subprocess.Popen(
                    "sudo su",
                    shell=True,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
            else:
                process = subprocess.Popen(
                    ["wsl", "bash", "-c", "sudo su"],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )

            stdout, stderr = process.communicate(
                input=sudo_password + "\n",
                timeout=SUDO_TIMEOUT,
            )

            if process.returncode == 0:
                print(colored("Successfully elevated to root privileges", "green"))
                return current_os, terminal_cmd
            else:
                print(colored("Failed to elevate to root privileges", "red"))
                if stderr:
                    print(colored(f"Error: {stderr.strip()}", "red"))

        except subprocess.TimeoutExpired:
            print(colored(f"sudo su timed out after {SUDO_TIMEOUT} seconds", "red"))
        except Exception as e:
            print(colored(f"Error elevating privileges: {str(e)}", "red"))

        if attempt < MAX_SUDO_RETRIES - 1:
            print(colored("Try again...", "yellow"))

    print(colored("Max sudo attempts reached. Cannot elevate to root.", "red"))
    return None, None


def execute_command(command, current_os, terminal_cmd):
    try:
        print(colored(f"Executing: {command}", "cyan"))
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
            print(colored("STDOUT:", "green"))
            print(result.stdout)
        if result.stderr:
            print(colored("STDERR:", "red"))
            print(result.stderr)

        print(colored("=" * 60, "blue"))
        print(colored(f"Command completed with exit code: {result.returncode}", "blue"))

        return result

    except subprocess.TimeoutExpired:
        print(colored("Command timed out after 120 seconds", "red"))
        return None
    except Exception as e:
        print(colored(f"Error executing command: {str(e)}", "red"))
        return None
