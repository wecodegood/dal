import os

def getBrowser():
    """--- based on the OS, finds out where our browser is."""
    browserNames = ["chromium", "firefox"]

    path = "/usr/bin/"
    brList = []

    for i in browserNames:
        if os.path.exists(path+i):
            brList.append(path+i)
    return brList
