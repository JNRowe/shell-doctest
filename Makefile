.PHONY: help test

help:
	@echo "  test   to run all tests."

test:
	./Shell-doctest test test.py
	@echo
	@echo "Done."

