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
from creds import get_credentials


email, password = get_credentials()

installed, chromium_path = check_chromium_installed()
if not installed:
    print("Error: Chromium browser not found.")
    print("Please install Chromium:")
    print("  Ubuntu/Debian: sudo apt install chromium-browser")
    print("  Fedora: sudo dnf install chromium")
    print("  Arch: sudo pacman -S chromium")
    sys.exit(1)

print(f"Found Chromium at: {chromium_path}")

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
            '--remote-debugging-port=9222'
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
        'Upgrade-Insecure-Requests': '1'
    })

    LoginToDeepSeek(email, password, page)
    InitLinuxMessage(browser, page)

    current_os, terminal_cmd = elevate_to_root()
    chatLoop(page, use=2, current_os=current_os, terminal_cmd=terminal_cmd)

    browser.close()
