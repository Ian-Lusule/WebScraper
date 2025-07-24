```python
import logging
import os

# Define log levels and format
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s'
LOG_LEVEL = logging.DEBUG  # Set to logging.INFO for production

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

# Create file handler and set level
log_file = os.path.join(os.path.dirname(__file__), 'lusules_web_scraper_pro.log')
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(LOG_LEVEL)

# Create formatter and add it to the handler
formatter = logging.Formatter(LOG_FORMAT)
file_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(file_handler)

# Create console handler and set level
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def log_exception(e):
    """Logs exceptions with traceback."""
    logger.exception(f"An error occurred: {e}")


# Example usage within the scraper:
# try:
#     # Your scraping code here
#     result = scrape_website(url)
# except Exception as e:
#     log_exception(e)


# Add this to your main scraper file for easy access:
# from src.lusules_web_scraper_pro.logger import logger, log_exception

```

**To use this logger:**

1.  **Save:** Save the code above as `src/lusules_web_scraper_pro/logger.py`.
2.  **Import:** In your main scraper file (e.g., `scraper.py`), import the logger:

    ```python
    from src.lusules_web_scraper_pro.logger import logger, log_exception
    ```

3.  **Use:**  Use the `logger` object to log messages at different levels (debug, info, warning, error, critical):

    ```python
    logger.debug("Starting the scraping process...")
    logger.info("Successfully connected to the website.")
    logger.warning("Encountered a slow proxy. Switching...")
    try:
        # Your scraping code here
        data = extract_data(html)
    except Exception as e:
        log_exception(e)  # Logs the exception with traceback
    logger.info(f"Scraped data: {data}")
    logger.critical("Fatal error: Scraper failed completely.")

    ```

4.  **Log File:** The log messages will be written to `lusules_web_scraper_pro.log` in the same directory as `logger.py`.  You can adjust the `LOG_LEVEL` in `logger.py` to control the verbosity of the logs (e.g., set to `logging.INFO` for production to reduce log file size).


This improved logger provides better context (filename, function, line number) in log messages, handles exceptions more gracefully, and separates log levels for better organization.  Remember to handle exceptions appropriately in your scraping logic to prevent the scraper from crashing unexpectedly.  The `log_exception` function is particularly useful for capturing detailed error information.
