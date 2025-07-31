TOKEN_HTML = """<html><body>
<input type="hidden" name="token" value="test-token">
</body></html>"""

RESULT_HTML_TEMPLATE = """
<html><body>
<table class="table_results">
  <thead>
    <tr><th>id</th><th>name</th><th>email</th></tr>
  </thead>
  <tbody>
    <tr>
      <td data-type="int">1</td>
      <td data-type="string">pupa&lupa</td>
      <td data-type="string">pupa@lupa.com</td>
    </tr>
  </tbody>
</table>
</body></html>
"""

NO_TABLE_HTML = "<html><body><div>no results</div></body></html>"

NO_TOKEN_HTML = """<html><body></body></html>"""
