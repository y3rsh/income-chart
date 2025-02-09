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
    "Experienced\nCustomer Service,\nFactory Worker",
    "Technician,\nSkilled Trades\nUseful College Degree",
    "Senior Engineer, Small Business Owner",
]

lifestyle_labels = [
    "Basic needs are met,\nlimited savings,\nhard to travel and save\nowning a reliable car is hard\nmust have roommates\nalways hard trade offs",
    "More stability and less trade offs,\ntravel and save occasionally",
    "Comfortable home,\nsavings,\nquality healthcare",
]

# Adjust colors
colors = ["#f4cccc", "#f6b26b", "#ffe599", "#6fa8dc"]

fig, ax = plt.subplots(figsize=(10, 6))

# Create bars for income bands
y_positions = np.arange(len(income_bands))
hourly_rates = [rate for rate, _ in income_bands]

bars = ax.barh(y_positions, hourly_rates, color=colors, edgecolor='black')

# Add job labels inside bars (adjust for better fit)
for i, bar in enumerate(bars):
    ax.text(bar.get_width() * 0.5, bar.get_y() + bar.get_height() / 2, job_labels[i],
            va='center', ha='center', fontsize=10, color='black', fontweight='bold')

# Add lifestyle labels outside bars
for i, (rate, label) in enumerate(income_bands):
    ax.text(rate + 5, y_positions[i], lifestyle_labels[i],
            va='center', ha='left', fontsize=10, color='black')

# Labels and title
ax.set_xlabel("Hourly Rate or if Small Business Owner hourly rate/2 ($)")
ax.set_ylabel("Income Levels")
ax.set_title("Income Levels and Lifestyle Affect in the US\nBands are imprecise and vary by location")
ax.set_yticks(y_positions)
ax.set_yticklabels([label for _, label in income_bands])
ax.set_xlim(0, 120)  # Adjust x-axis limit for better label fit
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Save the figure
plt.savefig("income_chart.png", dpi=300, bbox_inches='tight')

# Create README.md with embedded image
with open("README.md", "w") as f:
    f.write("""# Income Levels and Lifestyle Choices\n\n"""
            "![Income Chart](income_chart.png)\n\n"
            "This chart represents different income levels, their associated job roles, "
            "and the lifestyle choices available at each income bracket.")

# Create an HTML page with embedded image
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Income Levels and Lifestyle Choices</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 20px;
            background-color: #f4f4f4;
        }
        img {
            max-width: 100%;
            height: auto;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 5px;
            background: white;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Income Levels and Lifestyle Choices</h1>
        <img src="income_chart.png" alt="Income Chart">
        <p>This chart represents different income levels, their associated job roles, and the lifestyle choices available at each income bracket.</p>
    </div>
</body>
</html>"""

# Save the HTML file
with open("index.html", "w") as f:
    f.write(html_content)

print("Files generated: income_chart.png, README.md, index.html")
