import os

os.makedirs("output", exist_ok=True)

report_content = "Monthly report content goes here..."

with open("output/monthly_report.txt", "w") as f:
    f.write(report_content)

print("✅ Monthly report saved to output/monthly_report.txt")
