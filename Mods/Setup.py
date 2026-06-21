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


def getBrowser():
    chromium_path = get_chromium_path()
    if chromium_path:
        return [chromium_path]
    return []
