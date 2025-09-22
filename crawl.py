import requests
import random
import pandas as pd
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from typing import List, Tuple

HEADERS_POOL = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.0 Safari/605.1.15",
]
YEARS_TO_SCRAPE = 5

def clean_number(x):
    if x is None or x == "":
        return None
    return float(x.replace(".", "").replace(",", "."))

def generate_months(start_month: int, start_year: int):
    today = date.today()
    end_month, end_year = today.month - 1, today.year
    months = []
    y, m = start_year, start_month
    while(y <= end_year):
        months.append((m, y))
        m += 1
        if(m > 12):
            y+=1
            m=1
        if(m > end_month and y == end_year):
            break

    return months


def get_data(month: int, year: int):
    print(month, year)
    rq = requests.Session()
    response = rq.get(
            url="https://vietnamtourism.gov.vn/StatisticGen/international?param=%7B%22code%22:%221205%22,%22year%22:%22"
             + str(year) + 
            "%22,%22period%22:%22t"
            + str(month) +
            "%22,%22lang%22:%22vi%22%7D",
            headers={'User-Agent': random.choice(HEADERS_POOL)}
        )
    return response.text

def scrape_months(times: List[Tuple[int, int]]):
    results = []
    for month, year in times:
        html = get_data(month=month, year=year)
        soup = BeautifulSoup(html, 'html.parser')
        total_rows = soup.find("tr", class_=["total-row"])
        total_data = 0
        rows = total_rows.find_all("td")
        cols = [row.get_text(strip=True) for row in rows]
        if(month == 1):
            total_data = clean_number(cols[month + 1])
        else:
            total_data = clean_number(cols[1])
        
        print(f"time: {month}/{year}, tourists: {total_data}")
        results.append({"time": f"{month}/{year}", "tourists": total_data})
    
    df = pd.DataFrame(results)
    df.to_csv("tourists.csv", index=False, encoding="utf-8-sig")
        
def main():
    months = generate_months(1, 2018)
    scrape_months(months)


    
main()