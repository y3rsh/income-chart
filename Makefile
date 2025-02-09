.PHONY: gen publish

gen:
	uv run zchart.py

define COMMIT_MSG
📊 Update charts 📈 $(shell date '+%Y-%m-%d %H:%M:%S') ✏️
endef

publish:
	git add .
	git commit -m "$(COMMIT_MSG)"
	git push
