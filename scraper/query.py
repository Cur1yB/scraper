from bs4 import BeautifulSoup
from scraper.constants import BASE
from requests import Session


def run_sql_query(session: Session, db: str, table: str, cols: str) -> str:
    """
    Imitates the SQL query functionality in the admin panel

    :param session: Requests session
    :param db: Database name
    :param table: Table name
    :param cols: Columns to select

    :return: Table as HTML string
    """
    query = f"SELECT {cols} FROM {table};"
    sql_page = session.get(
        f"{BASE}/index.php",
        params={
            "route": "/database/sql",
            "db": db,
        },
    )

    soup = BeautifulSoup(sql_page.text, "html.parser")
    token_el = soup.select_one('input[name="token"]')
    token = token_el["value"]

    resp = session.post(
        f"{BASE}/index.php?route=/import",
        data={
            "token": token,
            "db": db,
            "sql_query": query,
        },
    )

    soup = BeautifulSoup(resp.text, "html.parser")
    table = soup.select_one("table.table_results")
    if not table:
        raise RuntimeError("Table not found")
    return table
