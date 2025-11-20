import os

os.makedirs("output", exist_ok=True)

report_content = "Weekly report content goes here..."

with open("output/weekly_report.txt", "w") as f:
    f.write(report_content)

print("✅ Weekly report saved to output/weekly_report.txt")
