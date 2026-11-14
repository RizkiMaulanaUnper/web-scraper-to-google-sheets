import csv
import time
import requests
import gspread
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"


def scrape_page(page):
    url = f"{BASE_URL}/page/{page}/"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.select(".quote")
    data = []
    for item in items:
        data.append({
            "quote": item.select_one(".text").get_text(strip=True),
            "author": item.select_one(".author").get_text(strip=True),
            "tags": ", ".join(t.get_text() for t in item.select(".tag")),
        })
    return data


def scrape_all():
    all_data = []
    page = 1
    while True:
        try:
            data = scrape_page(page)
        except requests.RequestException as e:
            print(f"Gagal di halaman {page}: {e}")
            break
        if not data:
            break
        all_data.extend(data)
        print(f"Halaman {page}: {len(data)} data")
        page += 1
        time.sleep(1)  # jeda 1 detik antar halaman
    return all_data


def save_csv(data, filename="hasil.csv"):
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=["quote", "author", "tags"])
        writer.writeheader()
        writer.writerows(data)


def save_to_sheets(data, sheet_name="Hasil Scraping"):
    gc = gspread.service_account(filename="credentials.json")
    sheet = gc.open(sheet_name).sheet1
    sheet.clear()
    rows = [["quote", "author", "tags"]]
    for d in data:
        rows.append([d["quote"], d["author"], d["tags"]])
    sheet.update(rows, "A1")
    print(f"{len(data)} data terkirim ke Google Sheets")


if __name__ == "__main__":
    hasil = scrape_all()
    save_csv(hasil)
    save_to_sheets(hasil)
    print(f"Selesai: {len(hasil)} data tersimpan")