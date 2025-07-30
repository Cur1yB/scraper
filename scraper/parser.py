import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Login in site and get data from database")
    parser.add_argument("--login", required=True, help="Your login")
    parser.add_argument("--password", required=True, help="Your password")
    parser.add_argument("--db", required=False, help="Name of database")
    parser.add_argument("--table", required=False, help="Name of table")
    args = parser.parse_args()
    return args