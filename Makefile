.PHONY: help test

help:
	@echo "  test   to run all tests."

test:
	./shell-doctest test test.py
	@echo
	@echo "Done."

release:
	python setup.py register sdist upload

