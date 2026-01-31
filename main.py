from config import BASE_URL, START_PAGE, END_PAGE
from scraper import scrape_page
from cleaner import clean_data
from saver import save_to_csv

all_data = []

for page in range(START_PAGE, END_PAGE + 1):
    url = BASE_URL.format(page)
    print("Scraping:", url)

    page_data = scrape_page(url)
    print("Items on page:", len(page_data))
    all_data.extend(page_data)

  

cleaned_data = clean_data(all_data)
save_to_csv(cleaned_data)

print("Done! Data saved in output.csv")

print(len(page_data))