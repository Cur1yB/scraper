from scraper.formatters import create_table, create_json

FORMAT_MAPPER = {
    "table": create_table,
    "json": create_json,
    # You can add more formatters here
}
