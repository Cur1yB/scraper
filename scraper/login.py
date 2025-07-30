import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

def login():
    BASE = "http://185.244.219.162/phpmyadmin"
    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')

    session = requests.Session()

    response = session.get(f"{BASE}/index.php", params={"route": "/"})
    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.select_one('input[name="token"]')['value']

    session.post(f"{BASE}/index.php?route=/", data={
        "pma_username": LOGIN,
        "pma_password": PASSWORD,
        "token": token
    })

    if any(k.startswith("pmaAuth") for k in session.cookies.keys()):
        print("OK")
