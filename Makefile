.PHONY: help test

help:
	@echo "  test   to run all tests."

test:
	./shell-doctest test test.py
	@echo
	@echo "Done."

