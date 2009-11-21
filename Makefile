.PHONY: help test

help:
	@echo "  test   to run all tests."

test:
	./shell-doctest --debug test test.py
	python test.py
	@echo
	@echo "Done."

manifest:
	python setup.py sdist --manifest-only

release:
	python setup.py register sdist upload

serve:
	cd doc; make serve

