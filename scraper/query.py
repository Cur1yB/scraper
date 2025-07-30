from bs4 import BeautifulSoup
from scraper.constants import BASE

def run_sql_query(session,  db="testDB", query="SELECT * FROM users;"):
    sql_page = session.get(f"{BASE}/index.php", params={
        "route": "/database/sql",
        "db": db,
    })

    soup = BeautifulSoup(sql_page.text, "html.parser")
    token_el = soup.select_one('input[name="token"]')
    token = token_el["value"]

    resp = session.post(f"{BASE}/index.php?route=/import", data={
        "token": token,
        "db": db,
        "sql_query": query,
    })

    soup = BeautifulSoup(resp.text, "html.parser")
    table = soup.select_one("table.table_results")

    for row in table.select("tbody tr"):
        cells = [td.get_text() for td in row.select("td[data-type]")]
        print(" ".join(cells))
