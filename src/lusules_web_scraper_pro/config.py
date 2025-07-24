```python
# src/lusules_web_scraper_pro/config.py

import os
from typing import Dict, List, Any
import yaml

DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.yaml")


class Config:
    """
    Configuration class for the web scraper. Loads settings from a YAML file.
    """

    def __init__(self, config_path: str = DEFAULT_CONFIG_PATH):
        self.config_path = config_path
        self.config: Dict[str, Any] = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Loads configuration from YAML file."""
        try:
            with open(self.config_path, "r") as f:
                config = yaml.safe_load(f)
                return config
        except FileNotFoundError:
            print(f"Warning: Config file not found at {self.config_path}. Using default settings.")
            return {}  # Return empty dict if file not found

    def get(self, key: str, default: Any = None) -> Any:
        """Gets a configuration value."""
        return self.config.get(key, default)

    @property
    def target_urls(self) -> List[str]:
        """Returns a list of target URLs."""
        return self.get("target_urls", [])

    @property
    def output_format(self) -> str:
        """Returns the desired output format (e.g., 'csv', 'json')."""
        return self.get("output_format", "csv").lower()

    @property
    def output_file(self) -> str:
        """Returns the output file path."""
        return self.get("output_file", "output.csv")

    @property
    def proxies(self) -> List[str]:
        """Returns a list of proxy URLs."""
        return self.get("proxies", [])

    @property
    def user_agents(self) -> List[str]:
        """Returns a list of user-agent strings."""
        return self.get("user_agents", [])

    @property
    def headers(self) -> Dict[str, str]:
        """Returns custom request headers."""
        return self.get("headers", {})

    @property
    def delays(self) -> Dict[str, int]:
        """Returns delays in seconds for different actions."""
        return self.get("delays", {"min": 1, "max": 5})

    @property
    def database(self) -> Dict[str, Any]:
        """Returns database connection settings."""
        return self.get("database", {})

    @property
    def selectors(self) -> Dict[str, str]:
        """Returns CSS selectors or XPath expressions for data extraction."""
        return self.get("selectors", {})

    @property
    def captcha_solver(self) -> Dict[str, Any]:
        """Returns CAPTCHA solver settings (e.g., API key)."""
        return self.get("captcha_solver", {})


# Example usage (in your main scraper script):

# config = Config("my_config.yaml") # Use a custom config file if needed.
# target_urls = config.target_urls
# output_format = config.output_format
# proxies = config.proxies
# ...and so on...

```

**src/lusules_web_scraper_pro/config.yaml (Example):**

```yaml
target_urls:
  - "https://www.example.com"
  - "https://www.another-example.com"

output_format: json
output_file: data.json

proxies:
  - "http://user:password@proxy.example.com:8080"
  - "http://another-proxy.com:8081"

user_agents:
  - "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
  - "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

headers:
  "Accept-Language": "en-US,en;q=0.9"
  "Referer": "https://www.google.com"

delays:
  min: 2
  max: 10

database:
  type: sqlite
  path: "scraper_data.db"

selectors:
  title: "#main-title"
  price: ".product-price"

captcha_solver:
  provider: "2captcha" # Or another provider
  api_key: "YOUR_API_KEY"

```

Remember to replace placeholder values like proxy URLs, API keys, and selectors with your actual data.  This `config.py` provides a robust and flexible way to manage your scraper's settings.  The use of YAML makes configuration easy to read and modify.  Error handling is included for missing config files, providing graceful degradation to default settings. Remember to install the `PyYAML` library: `pip install pyyaml`
