.PHONY: gen publish

gen:
	uv run zchart.py

publish:
	git add .
	git commit -m "📊 Update charts 📈 $(shell date '+%Y-%m-%d %H:%M:%S') ✏️"
	git push
