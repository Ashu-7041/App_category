import structlog

from logger import configure_logging

configure_logging()

logger = structlog.get_logger(__name__)

from services.app_scraper.playstore_appstore_scraper import AppScraper

logger.info("Initializing app_scraper service")
app_scraper = AppScraper()

file_name = "/Users/ashutoshtiwari/Downloads/app_testing.csv"
logger.info("Starting app_scraper service")
app_scraper.app_data_scraper(csv_file=file_name)

logger.info("Completed app_scraper service")
