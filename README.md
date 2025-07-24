# lusules-web-scraper-pro

**By Ian Lusule**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


## Description

`lusules-web-scraper-pro` is a powerful and robust Python web scraper designed for extracting data from dynamic websites.  It incorporates advanced anti-detection techniques, proxy rotation, and flexible configuration options to ensure reliable and efficient scraping. This project prioritizes maintainability, extensibility, and ease of use.


## Features

* **Dynamic Website Handling:** Uses Selenium to interact with JavaScript-heavy websites, handling dynamic content loading, infinite scrolling, lazy loading, and AJAX requests.
* **Proxy Rotation:** Supports multiple proxy providers, intelligent proxy selection, and automatic retries for failed proxies.
* **Anti-Detection Mechanisms:** Employs randomized delays, user-agent rotation, header manipulation, CAPTCHA handling (with fallback to a CAPTCHA solving service), JavaScript rendering, and fingerprinting mitigation techniques.
* **Data Extraction:** Leverages BeautifulSoup for efficient parsing and extraction of data from various HTML formats (tables, lists, etc.) using CSS selectors and XPath expressions.
* **Data Output:** Offers flexible output options: CSV, JSON, and database integration (SQLite, PostgreSQL).
* **Error Handling and Logging:** Includes comprehensive error handling and detailed logging for monitoring scraper activity.
* **Modularity and Extensibility:** Designed with a modular architecture for easy maintenance and extension.
* **Configuration:** Uses a configuration file (YAML) for customizable settings (proxies, output format, URLs, extraction rules).


## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/[YourGitHubUsername]/lusules-web-scraper-pro.git
cd lusules-web-scraper-pro
```

2. **Create a virtual environment (recommended):**

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

**Note:** You'll need to install a suitable webdriver (e.g., ChromeDriver for Chrome) and place it in your system's PATH or specify its location in the code.  You may also need to configure a CAPTCHA solving service (e.g., 2captcha, Anti-Captcha) and obtain an API key.


## Usage

1. **Configure the scraper:**  Edit the `config.yaml` file to specify your target website URL(s), desired output format, proxy settings (if using), and data extraction rules.  See the `example_config.yaml` file for a template.

2. **Run the scraper:**

```bash
python main.py
```

The output will be saved to the location specified in the configuration file.


## Configuration (config.yaml)

```yaml
target_url: "https://www.example.com"  # Your target website URL
output_format: "csv"  # csv, json, sqlite, postgresql
output_file: "output.csv" # Output file path
proxy_provider: "rotating_proxies" # "rotating_proxies", "free_proxies" or "none" (specify provider details if needed)
user_agents: ["User-Agent 1", "User-Agent 2"] # List of user agents
# ... other settings ...
data_extraction_rules:
  - selector: "#product-list li" # CSS selector or XPath expression
    fields:
      - name: "title"
        selector: ".product-title"
      - name: "price"
        selector: ".product-price"
```


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.  Follow the standard contribution guidelines.


## Examples

The `examples` directory contains sample scripts demonstrating how to scrape different types of dynamic websites and extract specific data.


## Error Handling

The scraper includes comprehensive error handling and logging to help diagnose and resolve issues.  Check the log files for details on any errors encountered.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
