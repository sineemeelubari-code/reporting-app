import logging, os, sys
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger("daily_summary")

def run():
    logger.info("Starting daily summary")
    # TODO: collect data, generate summary, send email
    logger.info("Daily summary completed")

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        logger.exception(f"Daily summary failed: {e}")
        sys.exit(1)
