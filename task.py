from src import news_scraping as ns

from RPA.Robocorp.WorkItems import WorkItems

# Define a main() function that calls the other functions in order:
def main(URL, QUERY, TIMESPAN, CATEGORIES):
    try:
        ns.set_directories()
        ns.open_the_website(URL)
        ns.dismiss_terms()
        ns.dismiss_cookies()
        ns.search_for(QUERY)
        ns.filter_date_range(TIMESPAN)
        ns.filter_categories(CATEGORIES)
        ns.sort_results()
        article_results = ns.extract_article_results(QUERY)
        ns.save_results_in_excel(article_results)
    finally:
        ns.end_task()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    library = WorkItems()
    library.get_input_work_item()
    variables = library.get_work_item_variables()

    URL = "http://nytimes.com"
    QUERY = variables["search_phrase"]
    TIMESPAN = variables["months"]
    CATEGORIES = variables["sections"]

    main(URL, QUERY, TIMESPAN, CATEGORIES)
