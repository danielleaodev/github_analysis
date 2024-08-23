import pandas as pd
from datetime import datetime
from utils.utils import log_error
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

                    closure_ratio = closed_issues_count / total_issues_count if total_issues_count > 0 else 0


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

            self.data = pd.DataFrame(data)

             # Adicionar e processar colunas derivadas
            self.data['age'] = pd.to_numeric(self.data['createdAt'].apply(lambda x: datetime.now().year - datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ").year), errors='coerce')
            
            # Corrigir a diferença de tempo para last_update
            self.data['last_update'] = (pd.Timestamp.now(tz='UTC') - pd.to_datetime(self.data['updatedAt'], utc=True)).dt.days

            return self.data

        except Exception as e:
            log_error(f"Unexpected error during data processing: {e}")
            raise DataProcessingError(message=str(e))

    def save_to_csv(self, file_path):
        try:
            self.data.to_csv(file_path, index=False)
            print(f"Data saved to {file_path}")
        except Exception as e:
            log_error(f"Error saving data to CSV: {e}")
            raise
