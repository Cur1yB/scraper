from scraper.login import login
from scraper.parser import parse_args
from scraper.query import run_sql_query
from scraper.mappers import FORMAT_MAPPER


def main():
    args = parse_args()
    session = login(login=args.login, password=args.password)
    table = run_sql_query(
        session, db=args.db, table=args.table, cols=args.cols
    )  # Mmm... SQL Injection
    if args.formatter not in FORMAT_MAPPER.keys():
        raise RuntimeError(f"Formatter {args.formatter} not supported")
    format_view = FORMAT_MAPPER[args.formatter](table)
    print(format_view)


if __name__ == "__main__":
    main()
