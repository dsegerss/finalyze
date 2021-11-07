from bs4 import BeautifulSoup
import requests

URL = "https://companiesmarketcap.com/usa/largest-companies-in-the-usa-by-market-cap"


def get_ticker_symbols():
    html = requests.get(URL).text
    soup = BeautifulSoup(html, "html.parser")
    symbols = [e.text for e in soup.select("div.company-code")]
    return symbols


def insert_to_db():
    pass
