```python
# src/lusules_web_scraper_pro/data_outputter.py

import csv
import json
import sqlite3
from typing import List, Dict, Any

class DataOutputter:
    """
    Handles the output of scraped data to various formats (CSV, JSON, SQLite).
    """

    def __init__(self, output_format: str = "csv", output_file: str = "output.csv", db_name: str = "scraper_data.db"):
        self.output_format = output_format.lower()
        self.output_file = output_file
        self.db_name = db_name
        self.db_connection = None

        if self.output_format not in ["csv", "json", "sqlite"]:
            raise ValueError("Invalid output format. Choose from 'csv', 'json', or 'sqlite'.")

        if self.output_format == "sqlite":
            self.create_db_table()


    def create_db_table(self):
        """Creates the SQLite table if it doesn't exist."""
        self.db_connection = sqlite3.connect(self.db_name)
        cursor = self.db_connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS scraped_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT
            )
        """)
        self.db_connection.commit()


    def output_data(self, data: List[Dict[str, Any]]):
        """Outputs the scraped data to the specified format."""
        if self.output_format == "csv":
            self._output_csv(data)
        elif self.output_format == "json":
            self._output_json(data)
        elif self.output_format == "sqlite":
            self._output_sqlite(data)


    def _output_csv(self, data: List[Dict[str, Any]]):
        """Outputs data to a CSV file."""
        if not data:
            print("No data to output.")
            return

        keys = data[0].keys()
        with open(self.output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)


    def _output_json(self, data: List[Dict[str, Any]]):
        """Outputs data to a JSON file."""
        with open(self.output_file, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)


    def _output_sqlite(self, data: List[Dict[str, Any]]):
        """Outputs data to an SQLite database."""
        cursor = self.db_connection.cursor()
        for item in data:
            try:
                cursor.execute("INSERT INTO scraped_data (data) VALUES (?)", (json.dumps(item),))
            except sqlite3.IntegrityError as e:
                print(f"Error inserting data into SQLite: {e}")
        self.db_connection.commit()

    def close_db_connection(self):
        """Closes the database connection if open."""
        if self.db_connection:
            self.db_connection.close()


#Example Usage
#data_outputter = DataOutputter(output_format="sqlite", output_file="output.db")
#data_outputter.output_data([{"name": "Lusule", "age": 30}, {"name": "Ian", "age": 30}])
#data_outputter.close_db_connection()

#data_outputter = DataOutputter(output_format="json", output_file="output.json")
#data_outputter.output_data([{"name": "Lusule", "age": 30}, {"name": "Ian", "age": 30}])

#data_outputter = DataOutputter(output_format="csv", output_file="output.csv")
#data_outputter.output_data([{"name": "Lusule", "age": 30}, {"name": "Ian", "age": 30}])

```