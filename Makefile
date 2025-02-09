.PHONY: gen publish

gen:
	uv run zchart.py

publish:
	uv run publish.py
