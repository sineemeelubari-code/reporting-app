import logging, os, sys
from datetime import datetime
from dotenv import load_dotenv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("monthly_report")

def run():
    logger.info("Starting monthly report")
    reports_path = os.getenv("REPORTS_PATH","reports")
    os.makedirs(reports_path, exist_ok=True)
    pdf_file = os.path.join(reports_path,"monthly_report.pdf")
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.setFont("Helvetica",12)
    c.drawString(100,750,"Monthly Report")
    c.drawString(100,730,f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawString(100,710,"Summary of engagement, growth, and performance metrics...")
    c.save()
    logger.info(f"Monthly PDF saved to {pdf_file}")
    logger.info("Monthly report completed")

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        logger.exception(f"Monthly report failed: {e}")
        sys.exit(1)
