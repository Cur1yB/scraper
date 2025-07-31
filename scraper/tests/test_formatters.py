import pytest
from bs4 import BeautifulSoup
from scraper.formatters import get_table, create_table, create_json


@pytest.mark.parametrize(
    "row_data,expected_headers,expected_rows",
    [
        (
            [{"id": 1, "name": "Alice", "email": "alice@example.com"}],
            ["id", "name", "email"],
            [["1", "Alice", "alice@example.com"]],
        ),
        (
            [
                {"id": 1, "name": "A", "email": "a@x.com"},
                {"id": 2, "name": "B", "email": "b@x.com"},
            ],
            ["id", "name", "email"],
            [["1", "A", "a@x.com"], ["2", "B", "b@x.com"]],
        ),
    ],
)
def test_get_table(row_data, expected_headers, expected_rows, html_template, html_row):
    body_html = "\n".join([html_row.format(**row) for row in row_data])
    full_html = html_template.format(rows=body_html)

    soup = BeautifulSoup(full_html, "html.parser")
    table_tag = soup.select_one("table.table_results")

    rows, headers = get_table(table_tag)
    assert headers == expected_headers
    assert rows == expected_rows


def test_create_json_output(html_template, html_row):
    row = html_row.format(id=99, name="Test", email="t@example.com")
    html = html_template.format(rows=row)

    soup = BeautifulSoup(html, "html.parser")
    table_tag = soup.select_one("table.table_results")

    json_data = create_json(table_tag)
    assert '"id": "99"' in json_data
    assert '"name": "Test"' in json_data
    assert '"email": "t@example.com"' in json_data


def test_create_table_output(html_template, html_row):
    row = html_row.format(id=3, name="C", email="c@x.com")
    html = html_template.format(rows=row)

    soup = BeautifulSoup(html, "html.parser")
    table_tag = soup.select_one("table.table_results")

    table = create_table(table_tag)
    output = table.get_string()

    assert "id" in output
    assert "name" in output
    assert "C" in output
    assert "c@x.com" in output
