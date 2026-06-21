from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth
import sys

from initMods.Loginer import LoginToDeepSeek
from initMods.GetLastResponse import GetLastResponse
from useExamples.chatWithModel import chatLoop
from Mods.Message import SendMessage
from Mods.Setup import check_chromium_installed
from Mods.Sudo import elevate_to_root
from initMods.initMessages import InitLinuxMessage
from art import BANNER
from colorama import init
from termcolor import colored

init()


def main():
    print(BANNER)

    installed, chromium_path = check_chromium_installed()
    if not installed:
        print(colored("Error: Chromium browser not found.", "red"))
        print("Please install Chromium:")
        print("  Ubuntu/Debian: sudo apt install chromium-browser")
        print("  Fedora: sudo dnf install chromium")
        print("  Arch: sudo pacman -S chromium")
        sys.exit(1)

    print(colored(f"Found Chromium at: {chromium_path}", "green"))

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch_persistent_context(
                executable_path=chromium_path,
                user_data_dir="./config",
                headless=False,
                args=[
                    '--disable-blink-features=AutomationControlled',
                    '--no-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-web-security',
                    '--disable-features=IsolateOrigins,site-per-process',
                    '--disable-gpu',
                    '--disable-software-rasterizer',
                    '--disable-extensions',
                    '--disable-setuid-sandbox',
                    '--remote-debugging-port=9222',
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
                ],
                viewport={'width': 720, 'height': 480}
            )

            page = browser.new_page()
            st = Stealth()
            st.apply_stealth_sync(page)

            page.set_extra_http_headers({
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '"Linux"',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
            })

            if not LoginToDeepSeek(page):
                print(colored("Failed to login to DeepSeek. Exiting.", "red"))
                browser.close()
                sys.exit(1)

            InitLinuxMessage(browser, page)

            current_os, terminal_cmd = elevate_to_root()
            chatLoop(page, use=2, current_os=current_os, terminal_cmd=terminal_cmd)

            browser.close()

    except KeyboardInterrupt:
        print(colored("\nShutting down...", "yellow"))
        sys.exit(0)
    except Exception as e:
        print(colored(f"Fatal error: {e}", "red"))
        sys.exit(1)


if __name__ == "__main__":
    main()
