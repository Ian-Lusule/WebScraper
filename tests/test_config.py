```python
# tests/test_config.py

import os
import pytest
from lusules_web_scraper_pro.config import Config

# Create a temporary config file for testing
TEST_CONFIG_YAML = """
output_format: csv
output_file: test_output.csv
proxies:
  provider: rotating_proxies  # Example provider, replace with your actual provider
  api_key: test_api_key
user_agents:
  - "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
  - "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
delays:
  min: 2
  max: 5
target_urls:
  - "https://www.example.com"
data_extraction_rules:
  - selector: "#my-element"
    attribute: "text"
    field_name: "example_data"

"""

@pytest.fixture
def temp_config_file(tmpdir):
    config_file = tmpdir.join("config.yaml")
    config_file.write(TEST_CONFIG_YAML)
    return str(config_file)


def test_config_loading(temp_config_file):
    config = Config(temp_config_file)
    assert config.output_format == "csv"
    assert config.output_file == "test_output.csv"
    assert config.proxies["provider"] == "rotating_proxies"
    assert config.proxies["api_key"] == "test_api_key"
    assert len(config.user_agents) == 2
    assert config.delays["min"] == 2
    assert config.delays["max"] == 5
    assert len(config.target_urls) == 1
    assert len(config.data_extraction_rules) == 1
    assert config.data_extraction_rules[0]["selector"] == "#my-element"


def test_config_missing_file():
    with pytest.raises(FileNotFoundError):
        Config("nonexistent_file.yaml")


def test_config_invalid_yaml():
    # Create a temporary file with invalid YAML
    temp_file = "invalid_config.yaml"
    with open(temp_file, "w") as f:
        f.write("invalid yaml")

    with pytest.raises(yaml.YAMLError):  #Import yaml library at the top
        Config(temp_file)

    os.remove(temp_file) #Clean up after test


def test_config_default_values():
    config = Config()  # Test with no config file
    # Assert default values (replace with your actual default values)
    assert config.output_format == "csv" #Example default
    assert config.output_file == "output.csv" #Example default


# Add more tests for specific aspects of the configuration, 
# such as handling different proxy providers, 
# validating data extraction rules, etc.

```

**To make this code runnable, you'll need to:**

1.  **Install necessary libraries:**  `pytest`, `PyYAML`
2.  **Create the `lusules_web_scraper_pro` package:**  This should contain the `config.py` file with the `Config` class implementation.  The `config.py` file should handle loading and validating the YAML configuration file.  It should also define default values for missing configuration options.
3.  **Implement the `Config` class:** This class should read the YAML configuration file, parse it, and provide methods to access the configuration parameters.  Handle potential errors during file reading and YAML parsing.


Remember to replace placeholder values like `"rotating_proxies"` and `"test_api_key"` with your actual proxy provider and API key (if applicable).  Also, adapt the default values in `test_config_default_values` to match your `Config` class's defaults.  Add more tests to cover edge cases and different configuration scenarios for thorough testing.  The `test_config_invalid_yaml` test requires the `yaml` library.  Add `import yaml` at the top of the file.
