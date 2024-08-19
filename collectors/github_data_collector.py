import requests
from utils.custom_exceptions import GitHubAPIError
from utils.utils import log_error

class GitHubDataCollector:
    def __init__(self, token):
        self.api_url = "https://api.github.com/graphql"
        self.headers = {"Authorization": f"Bearer {token}"}
    
    def execute_query(self, query):
        try:
            response = requests.post(self.api_url, json={'query': query}, headers=self.headers)
            if response.status_code == 200:
                result = response.json()
                if 'errors' in result:
                    log_error(f"GraphQL errors: {result['errors']}")
                    raise GitHubAPIError(status_code=response.status_code, message="API returned errors")
                return result
            else:
                log_error(f"Failed request with status code: {response.status_code}")
                raise GitHubAPIError(status_code=response.status_code)
        except requests.exceptions.RequestException as e:
            log_error(f"RequestException: {e}")
            raise GitHubAPIError(status_code=response.status_code, message=str(e))

    def get_repositories(self, num_repos, batch_size=20):
        all_repositories = []
        cursor = None  # Cursor inicial é None

        while len(all_repositories) < num_repos:
            # Construção da string de consulta
            after_cursor = f', after: "{cursor}"' if cursor else ""
                
            query = f"""
            {{
            search(query: "stars:>1", type: REPOSITORY, first: {batch_size}{after_cursor}) {{
                nodes {{
                ... on Repository {{
                    name
                    createdAt
                    pullRequests(states: MERGED) {{
                    totalCount
                    }}
                    releases {{
                    totalCount
                    }}
                    updatedAt
                    primaryLanguage {{
                    name
                    }}
                    issues {{
                        totalCount
                    }}
                    closedIssues: issues(states: CLOSED) {{
                    totalCount
                    }}
                    stargazers {{
                    totalCount
                    }}
                }}
                }}
                pageInfo {{
                endCursor
                hasNextPage
                }}
            }}
            }}
            """
            result = self.execute_query(query)

            # Adicione os repositórios retornados à lista geral
            all_repositories.extend(result['data']['search']['nodes'])

            # Verifique se há mais páginas
            page_info = result['data']['search']['pageInfo']
            cursor = page_info['endCursor']

            if not page_info['hasNextPage']:
                break  # Se não houver mais páginas, sair do loop

        return all_repositories