import os
import shutil


def get_chromium_path():
    paths = [
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
    ]

    for path in paths:
        if os.path.exists(path):
            return path

    chromium = shutil.which("chromium") or shutil.which("chromium-browser")
    if chromium:
        return chromium

    return None


def check_chromium_installed():
    path = get_chromium_path()
    if path:
        return True, path
    return False, None


def getBrowser():
    installed, path = check_chromium_installed()
    if installed:
        return [path]
    return []
