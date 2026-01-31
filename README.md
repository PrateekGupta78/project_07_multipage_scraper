# WS-7: Multi-Page Web Scraper (Python)

This is a beginner-friendly multi-page web scraping project using Python.  
It scrapes data from multiple pages, cleans the text, removes duplicates, and saves the final result into a CSV file.

This project is perfect for practicing:
- Web Scraping
- Data Cleaning
- Automation
- Python Projects for Freelancing

---

## 🔹 Website Used (Safe for Practice)
https://books.toscrape.com
---

## 🔹 Features
- Scrapes data from page 1 to page 10
- Uses Requests and BeautifulSoup
- Cleans text (spaces, symbols, formatting)
- Removes duplicate records
- Saves output in CSV file

---

## 🔹 Folder Structure

WS-7-MultiPage-Scraper/
│
├── main.py        # main runner file
├── scraper.py    # extracts data from website
├── cleaner.py    # cleans text & removes duplicates
├── saver.py      # saves data to CSV
├── config.py     # base URL & page settings
└── output.csv    # final scraped data
---

## 🔹 How the Program Works

config → main → scraper → cleaner → saver → output.csv
1. config.py stores the website URL and page range  
2. main.py loops through pages  
3. scraper.py extracts data  
4. cleaner.py cleans and removes duplicates  
5. saver.py saves everything into a CSV file  

---

## 🔹 Requirements

Install Python libraries:

pip install requests beautifulsoup4
---

## 🔹 How to Run

python main.py
After running, you will get:

output.csv
---

## 🔹 Sample Output

| Title | Price |
|--------|--------|
| a light in the attic | 51.77 |
| tipping the velvet | 53.74 |
| soumission | 50.10 |

---

## 🔹 Skills Used
- Python
- Requests
- BeautifulSoup
- Web Scraping
- Data Cleaning
- CSV Automation

---

## 👨‍💻 Author
Prateek Gupta  
India 🇮🇳

---

Happy Scraping 🚀