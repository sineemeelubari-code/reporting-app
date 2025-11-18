import logging, os, sys
import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("weekly_report")

def run():
    logger.info("Starting weekly report")
    data = {"Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],"Engagement":[120,150,180,90,200,220,170]}
    df = pd.DataFrame(data)
    plt.plot(df["Day"], df["Engagement"], marker="o")
    plt.title("Weekly Engagement Trends")
    reports_path = os.getenv("REPORTS_PATH","reports")
    os.makedirs(reports_path, exist_ok=True)
    chart_file = os.path.join(reports_path,"weekly_trends.png")
    plt.savefig(chart_file)
    logger.info(f"Weekly chart saved to {chart_file}")
    logger.info("Weekly report completed")

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        logger.exception(f"Weekly report failed: {e}")
        sys.exit(1)
