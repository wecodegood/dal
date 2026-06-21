def LoginToDeepSeek(evar, pvar, page, url="https://chat.deepseek.com"):
    page.goto(url, wait_until="networkidle")
    
    email_field = page.get_by_placeholder("Phone number / email address")
    password_field = page.get_by_placeholder("Password")
    
    if email_field.is_visible() and password_field.is_visible():
        email_field.fill(evar)
        password_field.fill(pvar)
        page.get_by_role("button", name="Log in", exact=True).click()
        
        try:
            page.wait_for_selector('textarea[placeholder*="Message"]', timeout=15000)
            return True
        except:
            error = page.locator('[class*="error"]').first
            if error.is_visible():
                print(f"Login error: {error.text_content()}")
            return False
    return True