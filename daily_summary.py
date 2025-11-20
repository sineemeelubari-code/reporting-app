import os

os.makedirs("output", exist_ok=True)

# Save main report
with open("output/daily_report.txt", "w") as f:
    f.write("Daily summary report content...")

# Save log file
with open("output/daily_log.txt", "w") as f:
    f.write("Log: Daily run completed successfully.")

# Save chart (example placeholder)
with open("output/daily_chart.csv", "w") as f:
    f.write("date,value\n2025-11-20,100\n")
