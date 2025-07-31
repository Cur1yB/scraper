import pytest
from scraper.query import run_sql_query
from scraper.tests.supports.constants import (
    TOKEN_HTML,
    NO_TABLE_HTML,
    RESULT_HTML_TEMPLATE,
    NO_TOKEN_HTML,
)


class FakeResponse:
    def __init__(self, text: str):
        self.text = text


class CapturingSession:
    def __init__(self, token_html: str, result_html: str):
        self._token_html = token_html
        self._result_html = result_html
        self.last_get = None
        self.last_get_params = None
        self.last_post_url = None
        self.last_post_data = None
        self.last_post_headers = None

    def get(self, url, params=None, **kwargs):
        self.last_get = url
        self.last_get_params = params or {}
        return FakeResponse(self._token_html)

    def post(self, url, data=None, headers=None, **kwargs):
        self.last_post_url = url
        self.last_post_data = data or {}
        self.last_post_headers = headers or {}
        return FakeResponse(self._result_html)


@pytest.mark.parametrize(
    "db,table,cols,expected_sql",
    [
        ("testDB", "users", "id, name, email", "SELECT id, name, email FROM users;"),
        ("testDB", "users", "*", "SELECT * FROM users;"),
    ],
)
def test_run_sql_query_success(db, table, cols, expected_sql):
    sess = CapturingSession(token_html=TOKEN_HTML, result_html=RESULT_HTML_TEMPLATE)

    table_tag = run_sql_query(sess, db=db, table=table, cols=cols)

    assert table_tag.name == "table"
    assert "table_results" in table_tag.get("class", [])

    head_cells = [th.get_text(strip=True) for th in table_tag.select("thead th")]
    assert head_cells == ["id", "name", "email"]
    first_row = [
        td.get_text(strip=True)
        for td in table_tag.select("tbody tr")[0].select("td[data-type]")
    ]
    assert first_row == ["1", "pupa&lupa", "pupa@lupa.com"]

    assert sess.last_post_url.endswith("/index.php?route=/import")
    assert sess.last_post_data["db"] == db
    assert sess.last_post_data["token"] == "test-token"
    assert sess.last_post_data["sql_query"] == expected_sql

    assert sess.last_get_params.get("route") == "/database/sql"
    assert sess.last_get_params.get("db") == db


def test_run_sql_query_raises_when_no_table():
    sess = CapturingSession(token_html=TOKEN_HTML, result_html=NO_TABLE_HTML)
    with pytest.raises(RuntimeError, match="Table not found"):
        run_sql_query(sess, db="testDB", table="users", cols="*")


def test_run_sql_query_missing_token_raises():
    sess = CapturingSession(token_html=NO_TOKEN_HTML, result_html=RESULT_HTML_TEMPLATE)
    with pytest.raises((TypeError, KeyError, AttributeError)):
        run_sql_query(sess, db="testDB", table="users", cols="*")
