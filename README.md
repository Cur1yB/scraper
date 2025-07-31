## Scraper

This script log in in site with requered `login` and `password` and get data from `table` (default: `users`) which inside `db` (default: `testDB`), you can also select cols by `cols` (default: `*`)

# Install

Your system must have installed `uv` [Documetation astral-uv](https://docs.astral.sh/uv/)

```
pipx install uv
```

## Install environment

You can install all dependencies from `uv.lock` by command:

```
uv sync
```

Also you can use command from Makefile:

```
make install
```

Done!

## Usage

```bash
usage: scraper [-h] --login LOGIN --password PASSWORD [--db DB] [--table TABLE] [--formatter FORMATTER] [--cols COLS]

Login in site and get data from database

options:
  -h, --help            show this help message and exit
  --login LOGIN         Your login
  --password PASSWORD   Your password
  --db DB               Name of database
  --table TABLE         Name of table
  --formatter FORMATTER
                        Formatter of output
  --cols COLS           Columns to show
```

# Demo version

You can run demo-verson **Asciinema powered** by command:

```
make demo_version
```

[![asciicast](https://asciinema.org/a/jDNSTLSHVc6igu3QBcQzUIwGh.svg)](https://asciinema.org/a/jDNSTLSHVc6igu3QBcQzUIwGh)

## Tests

You can run tests by command:

```
make test
```

You can watch test coverage by command

```
make cov
```

And finally you can watch demo_version of test by

```
make demo_tests
```


[![asciicast](https://asciinema.org/a/JFPPbCrli8CDnCo7yN8t5V1aS.svg)](https://asciinema.org/a/JFPPbCrli8CDnCo7yN8t5V1aS)