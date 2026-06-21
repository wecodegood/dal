def LoginToDeepSeek(page, url="https://chat.deepseek.com", timeout_ms=300000):
    from colorama import init
    from termcolor import colored
    import time

    init()

    print(colored("Opening DeepSeek...", "yellow"))
    page.goto(url, wait_until="networkidle")

    try:
        page.wait_for_selector('textarea[placeholder*="Message"]', timeout=timeout_ms)
        print(colored("Login detected! Continuing...", "green"))
        return True
    except Exception:
        print(colored("Timed out waiting for login.", "red"))
        return False
