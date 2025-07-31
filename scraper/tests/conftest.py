import pytest

HTML_TEMPLATE = """
<table class="table_results">
  <thead>
    <tr><th>id</th><th>name</th><th>email</th></tr>
  </thead>
  <tbody>
    {rows}
  </tbody>
</table>
"""

ROW_TEMPLATE = """
<tr>
  <td data-type="int">{id}</td>
  <td data-type="string">{name}</td>
  <td data-type="string">{email}</td>
</tr>
"""

TOKEN_HTML = """<html><body>
<input type="hidden" name="token" value="test-token">
</body></html>"""


@pytest.fixture
def html_row():
    return ROW_TEMPLATE


@pytest.fixture
def html_template():
    return HTML_TEMPLATE


@pytest.fixture
def token_html():
    return TOKEN_HTML
