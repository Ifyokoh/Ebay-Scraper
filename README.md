# Ebay-Scraper

This scraper is based on [Ebay]('https://www.ebay.com/') website. 

## Installation
- psycopg2
- pandas

You can scrape the page using any keyword you want by running the `scraper.py` file with list of interested keyword.

Example
- Run scraper.py
- Run `scrape_data(1000, ['bags', 'shoes', 'dress'])`

To connect to database and insert the scraped data
- Run database.py
- Run `database(scrape_data(1000, ['bags', 'shoes', 'dress']))`