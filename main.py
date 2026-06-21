#framework
from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth


# moduals:
    #main moduals:
from initMods.Loginer import LoginToDeepSeek
from initMods.GetLastResponse import GetLastResponse
from useExamples.chatWithModel import chatLoop
from Mods.Message import SendGetMessage, SendMessage
from Mods.Setup import getBrowser
#moduals:
    #init prompt moduals:
from initMods.initMessages import InitChatMessage
from initMods.initMessages import InitLinuxMessage

# moduals: 
    #creds moduals:
from creds import *


#moduals:
    # simple moduals:
from Mods.Message import SendMessage
import time
import os
import subprocess
import sys


ubr = sys.argv[1]
br_list = getBrowser()

if ubr[1] == "chrome":
    ubr[1] = "chromium"

with sync_playwright() as p:

    br_type = getattr(p, ubr)



    browser = br_type.launch_persistent_context(
        executable_path=br_list[0],
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

    chatLoop(page, use=2, sudo_password=8088)
    
    browser.close()
