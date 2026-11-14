# Web Scraper to Google Sheets

A Python bot that scrapes data from a website (all pages, automatically) and exports it to **CSV** and **Google Sheets**.

This project is a demo of the kind of data automation I build for clients: collecting data from the web and delivering it in a clean, ready-to-use format.

## Features

- Scrapes data across multiple pages automatically
- Exports results to a CSV file (Excel-compatible, UTF-8)
- Sends results to Google Sheets automatically
- Polite scraping with a delay between requests
- Error handling, so the bot stops cleanly if a page fails

## Demo

The demo scrapes [quotes.toscrape.com](https://quotes.toscrape.com), a sandbox website built for practicing web scraping. It collects the quote, author, and tags from all 10 pages (100 entries).

| quote | author | tags |
|-------|--------|------|
| "The world as we have created it is a process of our thinking..." | Albert Einstein | change, deep-thoughts, thinking, world |

## Tech Stack

- Python 3
- requests
- BeautifulSoup4
- gspread (Google Sheets API)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/RizkiMaulanaUnper/web-scraper-to-google-sheets.git
   cd web-scraper-to-google-sheets
   ```

2. Create a virtual environment and install dependencies:
   ```
   python -m venv venv
   venv\Scripts\activate
   pip install requests beautifulsoup4 gspread
   ```

3. Set up Google Sheets access:
   - Create a project in Google Cloud Console
   - Enable the **Google Sheets API** and **Google Drive API**
   - Create a **Service Account** and download its JSON key
   - Save the key as `credentials.json` in the project folder
   - Create a Google Sheet named `Hasil Scraping` and share it with the service account's `client_email` (Editor access)

4. Run the bot:
   ```
   python scraper.py
   ```

## Output

- `hasil.csv` is created in the project folder
- The same data appears in your Google Sheet

## Customization

This bot can be adapted to other websites: product prices, job listings, public business directories, and more. Only the selectors in `scrape_page()` need to change.

## Notes

- `credentials.json` is private and is excluded from this repository via `.gitignore`
- Only scrape publicly available data, and respect each website's `robots.txt` and terms of service

## Need a custom scraper or automation?

I build custom Python bots for data collection, reporting, and notifications. Contact me on Fiverr: **[add your Fiverr profile link here]**

---

Built by [Rizki Maulana](https://github.com/RizkiMaulanaUnper)
