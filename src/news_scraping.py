from RPA.Browser.Selenium import Selenium


browser_lib = Selenium()


def open_the_website(url):
    browser_lib.open_available_browser(url)


def dismiss_terms():
    terms_button = "class:css-1fzhd9j"
    browser_lib.click_button(terms_button)


def dismiss_cookies():
    cookies_button = "data:testid:GDPR-reject"
    browser_lib.click_button(cookies_button)


def open_navigation_menu():
    menu_button = "data:testid:nav-button"
    browser_lib.click_button(menu_button)


def end_task():
    browser_lib.close_all_browsers()