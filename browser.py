#!/usr/bin/env python3
"""Run the right internet browser."""
from datetime import datetime

from pywinauto.application import Application
from pywinauto.findwindows import find_windows
from pywinauto.win32functions import SetForegroundWindow


FIREFOX_CLASS = "MozillaWindowClass"
CHROME_CLASS = "Chrome_WidgetWin_1"
BROWSER_PATHS = {
    FIREFOX_CLASS: "C:/Program Files (x86)/Mozilla Firefox/firefox.exe",
    CHROME_CLASS: "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
}


def run_or_raise(class_name, path):
    """Launch a program or focus it if already running."""
    try:
        windows = find_windows(class_name=class_name)
        # XXX: Finds most recent instance, not current workspace's one.
        last_window = windows[-1]
    except IndexError:
        Application().start(path)
    else:
        SetForegroundWindow(last_window)


def is_during_school(time):
    """Return whether a time is during school times."""
    is_weekday = time.isoweekday() in range(1, 6)
    is_school_time = time.hour in range(8, 16)
    return is_weekday and is_school_time


def main():
    """Launch Firefox or Chrome depending on whether I'm at school."""
    today = datetime.now()
    at_school = is_during_school(today)
    browser_class = CHROME_CLASS if at_school else FIREFOX_CLASS
    path = BROWSER_PATHS[browser_class]
    run_or_raise(browser_class, path)


if __name__ == "__main__":
    main()
