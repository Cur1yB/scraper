import requests
from bs4 import BeautifulSoup
from scraper.constants import BASE


def login(login: str, password: str) -> requests.Session:
    '''
    Login to the site and return the session

    :param login: username
    :param password: password
    
    :return: session
    '''
    session = requests.Session()

    response = session.get(f"{BASE}/index.php", params={"route": "/"})
    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.select_one('input[name="token"]')["value"]

    session.post(
        f"{BASE}/index.php?route=/",
        data={"pma_username": login, "pma_password": password, "token": token},
    )

    if not any(k.startswith("pmaAuth") for k in session.cookies.keys()):
        raise RuntimeError("Login failed")

    return session
