from prettytable import PrettyTable
import json
from typing import Tuple, List


def create_table(table: str) -> str:
    """
    Get table html-view and return table-view string

    :param table: html table

    :return: table-view as a string
    """
    rows, headers = get_table(table)
    pretty_table = PrettyTable()
    if headers:
        pretty_table.field_names = headers
    pretty_table.add_rows(rows)
    return pretty_table


def create_json(table: str) -> str:
    """
    Get table html-view and return it as a stringify json

    :param table: html table
    :return: table-view as a json
    """
    rows, headers = get_table(table)
    data = [dict(zip(headers, row)) for row in rows]
    return json.dumps(data, indent=2, ensure_ascii=False)


def get_table(table: str) -> Tuple[List[str]]:
    """
    Get table html-view and return rows and headers

    :param table: html table
    :return: rows List[str] and headers List[str]
    """
    headers = [
        header
        for header in [th.get_text(strip=True) for th in table.select("thead tr th")]
        if header
    ]
    rows = []
    for row in table.select("tbody tr"):
        cells = [td.get_text() for td in row.select("td[data-type]")]
        rows.append(cells)
    return rows, headers
