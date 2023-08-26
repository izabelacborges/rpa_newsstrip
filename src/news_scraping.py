import logging
from utils import utils as u

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


def search_for(term):
    input_field = "name:query"
    browser_lib.input_text(input_field, term)
    browser_lib.press_keys(input_field, "ENTER")


def filter_date_range(timespan):
    start_date, end_date = u.get_date_range(timespan)

    calendar_button = "data:testid:search-date-dropdown-a"
    browser_lib.click_button(calendar_button)

    choose_date_button = "xpath://button[@value='Specific Dates']"
    browser_lib.click_button(choose_date_button)

    start_date_input = "id:startDate"
    browser_lib.input_text(start_date_input, start_date)
    end_date_input = "id:endDate"
    browser_lib.input_text(end_date_input, end_date)

    browser_lib.click_button(calendar_button)


def filter_categories(categories):
    section_button = "data:testid:search-multiselect-button"
    browser_lib.click_button(section_button)

    for i in categories:
        try:
            section = f'xpath://input[contains(@value, "{i}")]'
            browser_lib.select_checkbox(section)
        except Exception:
            logging.exception(f'There is no {i} category for the searched term.')
    
    browser_lib.click_button(section_button)


def sort_results(sort_by="newest"):
    sortby_button = "data:testid:SearchForm-sortBy"
    browser_lib.select_from_list_by_value(sortby_button, sort_by)


def extract_article_results(term):
    results_header = "data:testid:SearchForm-status"
    results_returned = browser_lib.get_text(results_header).split("\n")[0]
    amount = u.get_number_from_sentence(results_returned)[0]


def end_task():
    browser_lib.close_all_browsers()