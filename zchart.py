# /// script
# requires-python = "==3.13.*"
# dependencies = [
#     "matplotlib",
#     "numpy",
# ]
# ///

import matplotlib.pyplot as plt
import numpy as np

# Update income bands to remove the highest level
income_bands = [
    (30, "Entry-Level\nService"),
    (60, "Skilled\nLabor"),
    (100, "Professional"),
]

# Update job examples and lifestyle descriptions accordingly
job_labels = [
    "Experienced\nCustomer Service,\nWarehouse\nAssembly\nManufacturing",
    "Technician,\nSkilled Trades\nUseful College Degree",
    "Senior Engineer, Small Business Owner",
]

lifestyle_labels = [
    "Basic needs are met.\nLimited savings.\nLimited play\nOwning a reliable car is hard\nMust have roommates\nAlways hard trade offs 😓",
    "More stability and less trade offs,\ntravel and save occasionally\nEmergencies are rough but more manageable",
    "Richer than 99% of the worlds population"
]

# Adjust colors
colors = ["#f4cccc", "#f6b26b", "#ffe599", "#6fa8dc"]

fig, ax = plt.subplots(figsize=(10, 6))

# Create bars for income bands
y_positions = np.arange(len(income_bands))
hourly_rates = [rate for rate, _ in income_bands]

bars = ax.barh(y_positions, hourly_rates, color=colors, edgecolor="black")

# Add job labels inside bars (adjust for better fit)
for i, bar in enumerate(bars):
    ax.text(
        bar.get_width() * 0.5,
        bar.get_y() + bar.get_height() / 2,
        job_labels[i],
        va="center",
        ha="center",
        fontsize=12,
        color="black",
        fontweight="bold",
    )

# Add lifestyle labels outside bars
for i, (rate, label) in enumerate(income_bands):
    ax.text(
        rate + 5,
        y_positions[i],
        lifestyle_labels[i],
        va="center",
        ha="left",
        fontsize=12,
        color="black",
    )

# Labels and title
ax.set_xlabel("Hourly Rate ($)\nOR if Small Business Owner/Salaried, hourly rate divided by 2")
ax.set_ylabel("Income Levels")
ax.set_title("Income Levels and Lifestyle in the US\nBands are imprecise and only for visualization")
ax.set_yticks(y_positions)
ax.set_yticklabels([label for _, label in income_bands])
ax.set_xlim(0, 120)  # Adjust x-axis limit for better label fit
ax.grid(axis="x", linestyle="--", alpha=0.7)

# Save the figure
plt.savefig("income_chart.png", dpi=300, bbox_inches="tight")

disclaimer = """Disclaimer:
This is a "Dad" picture, to help folks visualize the impact of income on lifestyle choices.
This chart is a broad generalization and does not account for the many variables that can affect lifestyle choices, such as;
location, family/family of origin, dependents, personal preferences, culture, religion, and economic conditions.
"""
header = "US Income Levels and Lifestyle Choices 2025"

# Create README.md with embedded image
with open("README.md", "w") as f:
    f.write(f"""# {header}\n![Income Chart](income_chart.png)\n<https://y3rsh.github.io/income-chart/>\n{disclaimer}
## Other tools
- [How Rich am I](https://www.givingwhatwecan.org/how-rich-am-i?income=100000&countryCode=USA&numAdults=1&numChildren=0)
""")

# Create an HTML page with embedded image
html_content = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>{header}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
            background-color: #f4f4f4;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 5px;
            background: white;
        }}
        .container {{
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }}
    </style>
</head>
<body>
    <div class=\"container\">
        <h1>{header}</h1>
        <img src=\"income_chart.png\" alt=\"Income Chart\">
        <p>{disclaimer}</p>
    </div>
    <div class=\"container\">
    <h2>Other tools</h2>
    <a href="https://www.givingwhatwecan.org/how-rich-am-i?income=100000&countryCode=USA&numAdults=1&numChildren=0" target="_blank" rel="noopener noreferrer">How Rich am I</a>
    </div>
</body>
</html>"""


# Save the HTML file
with open("index.html", "w") as f:
    f.write(html_content)

print("Files generated: income_chart.png, README.md, index.html")
