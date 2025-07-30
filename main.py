from scraper.login import get_data
from scraper.parser import parse_args

def main():
    args = parse_args()
    get_data(login=args.login, password=args.password, db=args.db, table=args.table)


if __name__ == "__main__":
    main()