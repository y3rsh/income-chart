# /// script
# requires-python = "==3.13.*"
# dependencies = [
#     "matplotlib",
#     "numpy",
# ]
# ///

from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


disclaimer = """Disclaimer:
This is a "Dad" picture, to help folks visualize the impact of income on lifestyle choices.
This chart is a broad generalization and does not account for the many variables that can affect lifestyle choices, such as;
location, family/family of origin, dependents, personal preferences, culture, religion, and economic conditions.
"""
year = datetime.now().year
header = f"US Income Levels and Lifestyle Choices {year}"


def gen_image():
    # Apply fivethirtyeight style
    plt.style.use("fivethirtyeight")

    income_bands = [
        (30, "Entry-Level\nService"),
        (60, "Skilled\nLabor"),
        (100, "Professional"),
    ]

    job_labels = [
        "Experienced\nCustomer Service,\nWarehouse\nAssembly\nManufacturing",
        "Technician,\nSkilled Trades\nUseful College Degree",
        "Senior Engineer, Small Business Owner",
    ]

    lifestyle_labels = [
        "Basic needs are met.\nLimited savings.\nLimited play\nOwning a reliable car is hard\nMust have roommates\nAlways hard trade offs 😓",
        "More stability with less trade offs\nTravel and save occasionally\nEmergencies are rough,\nbut more manageable.",
        "Richer\nthan 99%\nof humans",
    ]

    # Adjust colors to match fivethirtyeight aesthetic
    colors = ["#E24A33", "#348ABD", "#988ED5"]  # Muted red, blue, and purple

    fig, ax = plt.subplots(figsize=(10, 6))

    # Create bars for income bands
    y_positions = np.arange(len(income_bands))
    hourly_rates = [rate for rate, _ in income_bands]

    bars = ax.barh(y_positions, hourly_rates, color=colors, edgecolor="black")

    # Add job labels inside bars (adjusted for better readability)
    for i, bar in enumerate(bars):
        ax.text(
            bar.get_width() * 0.5,
            bar.get_y() + bar.get_height() / 2,
            job_labels[i],
            va="center",
            ha="center",
            fontsize=12,
            color="white",
            fontweight="bold",
        )

    # Add lifestyle labels to the right of the bars
    for i, (rate, label) in enumerate(income_bands):
        ax.text(
            rate + 5,  # Offset for better readability
            y_positions[i],
            lifestyle_labels[i],
            va="center",
            ha="left",
            fontsize=12,
            color="black",
        )

    # Set labels and title
    ax.set_xlabel(
        "Hourly Rate ($)\nIf Small Business Owner hourly rate divided by 2",
        fontsize=14,
        fontweight="bold",
    )
    ax.set_ylabel("Income Levels", fontsize=14, fontweight="bold")
    ax.set_title(
        "Income Levels and Lifestyle in the US\n(Bands are imprecise and only for visualization)",
        fontsize=16,
        fontweight="bold",
    )

    # Set y-axis labels
    ax.set_yticks(y_positions)
    ax.set_yticklabels([label for _, label in income_bands])

    # Set x-axis limits for better spacing
    ax.set_xlim(0, 120)

    # Improve grid styling
    ax.grid(axis="x", linestyle="--", alpha=0.5, color="gray")

    return plt


def gen_readme():
    with open("README.md", "w") as f:
        f.write(
            f"""# {header}

![Income Chart](income_chart.png)

[View Interactive Version](https://y3rsh.github.io/income-chart/)

## Disclaimer  
> {disclaimer}

## Other Tools  
- **[How Rich Am I?](https://www.givingwhatwecan.org/how-rich-am-i?income=100000&countryCode=USA&numAdults=1&numChildren=0)**  
"""
        )
    print("README file generated successfully.")


def gen_html():
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
    with open("index.html", "w") as f:
        f.write(html_content)
    print("HTML file generated successfully.")


if __name__ == "__main__":
    fig = gen_image()
    fig.savefig("income_chart.png", dpi=300, bbox_inches="tight")
    gen_readme()
    gen_html()
