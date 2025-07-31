import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Login in site and get data from database"
    )
    parser.add_argument("--login", required=True, help="Your login")
    parser.add_argument("--password", required=True, help="Your password")
    parser.add_argument(
        "--db", required=False, help="Name of database", default="testDB"
    )
    parser.add_argument(
        "--table", required=False, help="Name of table", default="users"
    )
    parser.add_argument(
        "--formatter", required=False, help="Formatter of output", default="table"
    )
    parser.add_argument("--cols", required=False, help="Columns to show", default="*")
    args = parser.parse_args()
    return args
