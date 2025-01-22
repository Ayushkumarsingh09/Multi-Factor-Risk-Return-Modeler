import pandas as pd

class DataIngestion:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        """Loads CSV data into a Pandas DataFrame."""
        try:
            data = pd.read_csv(self.file_path)
            print(f"Data loaded successfully from {self.file_path}")
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            raise
