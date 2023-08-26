from RPA.Browser.Selenium import Selenium


browser_lib = Selenium()


def open_the_website(url):
    browser_lib.open_available_browser(url)


def end_task():
    browser_lib.close_all_browsers()