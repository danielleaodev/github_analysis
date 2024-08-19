import pandas as pd
from utils.utils import log_error

class DataAnalyzer:
    def __init__(self, processed_data):
        self.processed_data = processed_data

    def analyze_general(self):
        try:
            general_analysis = {
                "median_age": self.processed_data['age'].median(),
                "median_pull_requests": self.processed_data['pullRequests'].median(),
                "median_releases": self.processed_data['releases'].median(),
                "median_update_frequency": self.processed_data['last_update'].median(),
                "median_issue_closure_ratio": self.processed_data['issue_closure_ratio'].median()
            }
            return general_analysis

        except Exception as e:
            log_error(f"Error during general analysis: {e}")
            raise

    def analyze_by_language(self):
        try:
            numeric_columns = ['age', 'pullRequests', 'releases', 'last_update', 'issue_closure_ratio']

            # Verifique se as colunas estão presentes e são numéricas
            for column in numeric_columns:
                if column not in self.processed_data.columns:
                    raise ValueError(f"Column {column} is missing in the processed data.")

            for column in numeric_columns:
                self.processed_data[column] = pd.to_numeric(self.processed_data[column], errors='coerce')

            language_analysis = self.processed_data.groupby('primaryLanguage')[numeric_columns].median()

            if language_analysis.empty:
                raise ValueError("The result of the language analysis is empty. Check the data processing steps.")

            return language_analysis

        except Exception as e:
            log_error(f"Error during language analysis: {e}")
            raise
