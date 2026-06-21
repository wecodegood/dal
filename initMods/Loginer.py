def LoginToDeepSeek(evar, pvar, page, url="https://chat.deepseek.com"):
    from colorama import init
    from termcolor import colored

    init()

    print(colored("Connecting to DeepSeek...", "yellow"))
    page.goto(url, wait_until="networkidle")

    email_field = page.get_by_placeholder("Phone number / email address")
    password_field = page.get_by_placeholder("Password")

    if email_field.is_visible() and password_field.is_visible():
        print(colored("Logging in...", "yellow"))
        email_field.fill(evar)
        password_field.fill(pvar)
        page.get_by_role("button", name="Log in", exact=True).click()

        try:
            page.wait_for_selector('textarea[placeholder*="Message"]', timeout=15000)
            print(colored("Login successful!", "green"))
            return True
        except Exception:
            error = page.locator('[class*="error"]').first
            if error.is_visible():
                print(colored(f"Login error: {error.text_content()}", "red"))
            else:
                print(colored("Login failed: Timed out waiting for chat interface", "red"))
            return False
    else:
        print(colored("Login failed: Could not find login form", "red"))
        return False