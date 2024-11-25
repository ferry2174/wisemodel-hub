.PHONY: contrib quality style test


check_dirs := src utils setup.py


quality:
	ruff check $(check_dirs)  # linter
	ruff format --check $(check_dirs) # formatter
	python utils/check_static_imports.py

	mypy src  # type checker

style:
	ruff format $(check_dirs) # formatter
	ruff check --fix $(check_dirs) # linter
	python utils/check_static_imports.py --update