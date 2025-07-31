rmcache:
	find . -name "__pycache__" -exec rm -rf {} +

install:
	uv sync

demo_version:
	uv run asciinema play demo/demo.cast

demo_tests:
	uv run asciinema play demo/demo_tests.cast

test:
	uv run pytest -vv

cov:
	uv run pytest --cov -vv