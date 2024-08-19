import pandas as pd
from datetime import datetime
from utils.utils import log_error, save_to_json
from utils.custom_exceptions import DataProcessingError

class DataProcessor:
    def __init__(self):
        self.data = pd.DataFrame()

    def process_raw_data(self, raw_data):
        try:
            data = {
                "name": [],
                "createdAt": [],
                "primaryLanguage": [],
                "stargazers": [],
                "pullRequests": [],
                "releases": [],
                "updatedAt": [],
                "total_issues": [],
                "closed_issues": [],
                "issue_closure_ratio": []
            }

            if isinstance(raw_data, list):
                for repo in raw_data:
                    if not isinstance(repo, dict):
                        print(f"Skipping invalid repo structure: {repo}")
                        continue

                    name = repo.get("name", "N/A")
                    created_at = repo.get("createdAt", "N/A")
                    primary_language = repo.get("primaryLanguage")
                    language_name = primary_language.get("name", "Unknown") if primary_language and isinstance(primary_language, dict) else "Unknown"
                    
                    stargazers_count = repo.get("stargazers", {}).get("totalCount", 0)
                    pull_requests_count = repo.get("pullRequests", {}).get("totalCount", 0)
                    releases_count = repo.get("releases", {}).get("totalCount", 0)
                    updated_at = repo.get("updatedAt", "N/A")
                    total_issues_count = repo.get("issues", {}).get("totalCount", 0)
                    closed_issues_count = repo.get("closedIssues", {}).get("totalCount", 0)

                    closure_ratio = closed_issues_count / total_issues_count if total_issues_count > 0 else None

                    data["name"].append(name)
                    data["createdAt"].append(created_at)
                    data["primaryLanguage"].append(language_name)
                    data["stargazers"].append(stargazers_count)
                    data["pullRequests"].append(pull_requests_count)
                    data["releases"].append(releases_count)
                    data["updatedAt"].append(updated_at)
                    data["total_issues"].append(total_issues_count)
                    data["closed_issues"].append(closed_issues_count)
                    data["issue_closure_ratio"].append(closure_ratio)

            df = pd.DataFrame(data)

            df['age'] = pd.to_numeric(df['createdAt'].apply(lambda x: datetime.now().year - datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ").year), errors='coerce')
            df['last_update'] = pd.to_numeric((pd.to_datetime('now') - pd.to_datetime(df['updatedAt']).dt.tz_localize(None)).dt.days, errors='coerce')

            self.data = df
            return df

        except Exception as e:
            log_error(f"Unexpected error during data processing: {e}")
            raise DataProcessingError(message=str(e))

    def save_to_csv(self, filename='processed_data.csv'):
        try:
            self.data.to_csv(filename, index=False)
            print(f"Data saved to {filename}")
        except Exception as e:
            log_error(f"Failed to save data to CSV: {e}")
            raise

# Exemplo de uso no main.py
if __name__ == "__main__":
    processor = DataProcessor()
    processed_data = processor.process_raw_data(raw_data)  # Suponha que raw_data já tenha sido coletado
    processor.save_to_csv('processed_data.csv')

    general_analysis = {
        "median_age": processor.calculate_maturity(),
        "median_pull_requests": processor.calculate_contribution(),
        "median_releases": processor.calculate_releases(),
        "median_update_frequency": processor.calculate_update_frequency(),
        "median_issue_closure_ratio": processor.calculate_issue_closure()
    }

    save_to_json(general_analysis, 'general_analysis.json')
