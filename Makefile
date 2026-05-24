install:
	uv sync
build:
	uv build
package-install:
	uv tool install dist/*.whl
force-install:
	uv tool install --force dist/*.whl
lint:
	uv run ruff check gendiff
gendiff:
	uv run gendiff
test:
	uv run pytest
test-coverage:
	uv run pytest --cov=gendiff --cov-report xml tests/