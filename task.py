from src import news_scraping as ns

# Define a main() function that calls the other functions in order:
def main():
    try:
        ns.set_directories()
        ns.open_the_website("https://nytimes.com")
        ns.dismiss_terms()
        ns.open_navigation_menu()
        ns.search_for("ChatGPT")
        ns.filter_date_range(1)
        ns.filter_categories(["Arts", "The Learning Network", "World"])
        ns.sort_results()
    finally:
        ns.end_task()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()