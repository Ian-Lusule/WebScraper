```python
# src/lusules_web_scraper_pro/exceptions.py

class LusulesWebScraperProException(Exception):
    """Base exception for all exceptions raised by Lusules Web Scraper Pro."""
    pass

class ConfigurationError(LusulesWebScraperProException):
    """Raised when there's an error in the configuration file."""
    pass

class ProxyError(LusulesWebScraperProException):
    """Raised when there's an issue with proxies (e.g., connection failure, invalid proxy)."""
    pass

class RequestError(LusulesWebScraperProException):
    """Raised when there's an error during an HTTP request (e.g., connection timeout, HTTP error)."""
    pass

class ScraperError(LusulesWebScraperProException):
    """Raised when there's an error during the scraping process (e.g., element not found, parsing error)."""
    pass

class CaptchaError(LusulesWebScraperProException):
    """Raised when a CAPTCHA is encountered and cannot be solved."""
    pass

class DataOutputError(LusulesWebScraperProException):
    """Raised when there's an error writing the scraped data to the output (e.g., file write error, database error)."""
    pass

class SeleniumError(LusulesWebScraperProException):
    """Raised when there's an error using Selenium (e.g., WebDriver exception)."""
    pass

class InvalidSelectorError(LusulesWebScraperProException):
    """Raised when an invalid CSS selector or XPath expression is used."""
    pass


class WebsiteStructureError(LusulesWebScraperProException):
    """Raised when the website structure changes unexpectedly, breaking the scraper."""
    pass

```

This file defines a set of custom exceptions for the `lusules-web-scraper-pro` project.  Each exception inherits from a base `LusulesWebScraperProException` class, making it easy to handle all exceptions related to the scraper in a unified way.  The specific exceptions cover various scenarios, from configuration problems to errors during data extraction and output.  This improves error handling and makes debugging easier.  The comments clearly explain the purpose of each exception.
