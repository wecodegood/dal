import subprocess
import sys
from Mods.Setup import check_chromium_installed
from art import BANNER
from colorama import init
from termcolor import colored

init()


def main():
    print(BANNER)
    print(colored("Opening Chrome for manual login...", "yellow"))
    print(colored("Log in to DeepSeek, then close this window.", "cyan"))
    print(colored("The session will be saved for the main app.", "cyan"))
    print()

    installed, chromium_path = check_chromium_installed()
    if not installed:
        print(colored("Error: Chromium not found.", "red"))
        sys.exit(1)

    args = [
        chromium_path,
        '--user-data-dir=./config',
        '--disable-blink-features=AutomationControlled',
        '--no-sandbox',
        '--disable-dev-shm-usage',
        '--disable-web-security',
        '--disable-features=IsolateOrigins,site-per-process',
        '--disable-gpu',
        '--disable-software-rasterizer',
        '--disable-extensions',
        '--disable-setuid-sandbox',
        '--disable-background-networking',
        '--disable-default-apps',
        '--disable-sync',
        '--disable-translate',
        '--no-first-run',
        '--disable-popup-blocking',
        '--disable-notifications',
        '--disable-background-timer-throttling',
        '--disable-backgrounding-occluded-windows',
        '--disable-renderer-backgrounding',
        '--password-store=basic',
        '--use-fake-ui-for-media-stream',
        '--disable-hang-monitor',
        '--disable-prompt-on-repost',
        '--disable-domain-reliability',
        '--disable-component-update',
        '--disable-client-side-phishing-detection',
        'https://chat.deepseek.com',
    ]

    try:
        subprocess.run(args)
        print()
        print(colored("Session saved. You can now run: python main.py", "green"))
    except KeyboardInterrupt:
        print()
        print(colored("Session saved. You can now run: python main.py", "green"))


if __name__ == "__main__":
    main()
