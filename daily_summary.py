import os

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# Generate your report content
report_content = "Daily summary report content goes here..."

# Save to file
with open("output/daily_report.txt", "w") as f:
    f.write(report_content)

print("✅ Daily report saved to output/daily_report.txt")
