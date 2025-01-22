import unittest
from src.data_ingestion import DataIngestion
import os

class TestDataIngestion(unittest.TestCase):
    def setUp(self):
        self.valid_file = "tests/sample_data/sample.csv"
        self.invalid_file = "tests/sample_data/invalid.csv"

    def test_load_data_success(self):
        ingestion = DataIngestion(self.valid_file)
        data = ingestion.load_data()
        self.assertFalse(data.empty, "Data should not be empty")

    def test_load_data_failure(self):
        ingestion = DataIngestion(self.invalid_file)
        with self.assertRaises(Exception):
            ingestion.load_data()

if __name__ == '__main__':
    unittest.main()
