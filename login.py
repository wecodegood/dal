import subprocess
import os
import sys
from art import BANNER
from colorama import init
from termcolor import colored

init()


def main():
    print(BANNER)
    print(colored("Opening your Chrome browser...", "yellow"))
    print(colored("Log in to DeepSeek, then close the tab.", "cyan"))
    print(colored("The session will be saved for the main app.", "cyan"))
    print()

    config_path = os.path.abspath("./config")

    chrome_paths = [
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
    ]

    chrome = None
    for path in chrome_paths:
        if os.path.exists(path):
            chrome = path
            break

    if not chrome:
        print(colored("Error: No Chrome/Chromium found on your system.", "red"))
        sys.exit(1)

    args = [
        chrome,
        f'--user-data-dir={config_path}',
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
        subprocess.Popen(args)
        print(colored(f"Opened {chrome}", "green"))
        print(colored("Log in, then run: python main.py", "green"))
    except Exception as e:
        print(colored(f"Error opening Chrome: {e}", "red"))


if __name__ == "__main__":
    main()
