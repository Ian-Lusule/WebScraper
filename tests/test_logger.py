```python
# tests/test_logger.py

import logging
import unittest
from lusules_web_scraper_pro.logger import setup_logger


class TestLogger(unittest.TestCase):
    def test_setup_logger(self):
        """Test that the setup_logger function creates a logger with the correct configuration."""
        logger = setup_logger("test_logger", log_file="test.log", level=logging.DEBUG)
        self.assertIsInstance(logger, logging.Logger)
        self.assertEqual(logger.level, logging.DEBUG)
        self.assertTrue(logger.handlers)  # Check if handlers are attached

        # Check log file content (optional, more robust testing might involve file comparison)
        # with open("test.log", "r") as f:
        #     log_content = f.read()
        #     self.assertIn("Test message", log_content) #Example assertion


    def test_log_levels(self):
        """Test logging at different levels."""
        logger = setup_logger("test_logger_levels", log_file="test_levels.log", level=logging.DEBUG)

        logger.debug("This is a debug message.")
        logger.info("This is an info message.")
        logger.warning("This is a warning message.")
        logger.error("This is an error message.")
        logger.critical("This is a critical message.")

        #Similar file content check as above could be implemented here for more comprehensive testing


    def test_exception_handling(self):
        """Test exception handling within the logger."""
        logger = setup_logger("test_exception_logger", log_file="test_exception.log", level=logging.ERROR)

        try:
            raise ValueError("This is a test exception.")
        except ValueError as e:
            logger.exception(f"An exception occurred: {e}")

        #Check for exception details in log file.


if __name__ == "__main__":
    unittest.main()

```

**To make this code runnable, you'll need to create the following:**

1. **`lusules_web_scraper_pro/logger.py`:** This file should contain the `setup_logger` function.  Here's a possible implementation:

```python
# lusules_web_scraper_pro/logger.py
import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """
    Sets up a logger with the specified name, log file, and logging level.

    Args:
        name: The name of the logger.
        log_file: The path to the log file.
        level: The logging level (default is INFO).

    Returns:
        A configured logger object.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create handlers
    if not logger.handlers: #Avoid duplicate handlers
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(console_handler)

    return logger

```

2.  **Project Structure:** Ensure your project has the correct directory structure:

```
lusules-web-scraper-pro/
├── lusules_web_scraper_pro/
│   └── logger.py
└── tests/
    └── test_logger.py
```

Remember to install the `unittest` module (it's usually included with Python).  Run the tests using `python -m unittest tests/test_logger.py`.  The test will create log files in the same directory as the script is run.  Remember to adapt the assertions in the test methods to accurately check the content of the log files based on your `setup_logger` implementation.  The comments in `test_log_levels` and `test_exception_handling` indicate how to extend the tests to check the log file content more thoroughly.
