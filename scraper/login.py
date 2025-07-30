import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
from scraper.constants import BASE
from scraper.query import run_sql_query

load_dotenv()

def get_data(login, password, db, table):
    session = requests.Session()

    response = session.get(f"{BASE}/index.php", params={"route": "/"})
    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.select_one('input[name="token"]')['value']

    session.post(f"{BASE}/index.php?route=/", data={
        "pma_username": login,
        "pma_password": password,
        "token": token
    })

    run_sql_query(session)
