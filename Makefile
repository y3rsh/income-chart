.PHONY: gen publish

gen:
	uv run zchart.py

# Cross-platform timestamp generation (Bash & PowerShell compatible)
publish:
	git add .
	git commit -m "📊 Update charts 📈 $(shell bash -c 'date +\"%Y-%m-%d %H:%M:%S\" 2>/dev/null || powershell -Command \"Get-Date -Format \\\"yyyy-MM-dd HH:mm:ss\\\"\"') ✏️"
	git push
