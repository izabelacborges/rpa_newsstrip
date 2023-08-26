import contextlib
import logging

from src.news_article import NewsArticle
from utils import excel_utils as excel
from utils import utils as u

from RPA.Browser.Selenium import Selenium


browser_lib = Selenium()


def set_directories():
    browser_lib.set_screenshot_directory("article-images")
    
    
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


def show_all_articles():
    show_more_locator = "data:testid:search-show-more-button"
    with contextlib.suppress(Exception):
        while browser_lib.is_element_visible(show_more_locator):
            browser_lib.click_button_when_visible(show_more_locator)


def extract_text_info(locator):
    date_locator = f"xpath://li[@data-testid = 'search-bodega-result'][{locator+1}]/div/span"
    date = browser_lib.get_text(date_locator)
    
    title_locator = f"xpath://li[@data-testid = 'search-bodega-result'][{locator+1}]/div/div/div/a/h4"
    title = browser_lib.get_text(title_locator)
    
    desc_locator = f"xpath://li[@data-testid = 'search-bodega-result'][{locator+1}]/div/div/div/a/p"
    description = browser_lib.get_text(desc_locator)

    return date, title, description


def save_image(locator):
    img_locator = f"xpath://li[@data-testid = 'search-bodega-result'][{locator+1}]/div/div/figure/div/img"
    
    return browser_lib.capture_element_screenshot(img_locator, f"article-{locator+1}.png")


def info_metrics(title, description, term):
    count_query = u.get_query_count(title, description, term)
    bool_contains_currency = u.contains_currency(title, description)
    
    return count_query, bool_contains_currency


def extract_article_results(term):
    articles = []

    results_header = "data:testid:SearchForm-status"
    results_returned = browser_lib.get_text(results_header).split("\n")[0]
    amount = u.get_number_from_sentence(results_returned)[0]

    show_all_articles()

    for i in range(amount):
        date, title, description = extract_text_info(i)
        
        img_filename = save_image(i)
        
        count_query, bool_contains_currency = info_metrics(title, description, term)
        
        articles.append(
            NewsArticle(
                title=title,
                date=date,
                description=description,
                imgage_file_path=img_filename,
                count_times_query_appears=count_query,
                contains_currency=bool_contains_currency
            )
        )

    return articles


def save_results_in_excel(articles, filename="articles.xlsx"):
    excel.setup_file(filename)
    excel.save_results(articles, filename)
    excel.teardown()


def end_task():
    browser_lib.close_all_browsers()