import matplotlib.pyplot as plt
import json

def generate_graphs(language_data_path, general_data_path, output_dir='graphs'):
    # Carregando os dados gerais
    with open(general_data_path, 'r') as f:
        general_data = json.load(f)

    # Gráfico para idade (RQ01)
    plt.figure(figsize=(8, 6))
    plt.bar(['Median Age'], [general_data['median_age']])
    plt.ylabel('Years')
    plt.title('Median Age of Popular Repositories (RQ01)')
    plt.savefig(f'{output_dir}/median_age.png')
    plt.close()

    # Gráfico para pull requests (RQ02)
    plt.figure(figsize=(8, 6))
    plt.bar(['Median Pull Requests'], [general_data['median_pull_requests']])
    plt.ylabel('Number of Pull Requests')
    plt.title('Median Pull Requests of Popular Repositories (RQ02)')
    plt.savefig(f'{output_dir}/median_pull_requests.png')
    plt.close()

    # Gráfico para releases (RQ03)
    plt.figure(figsize=(8, 6))
    plt.bar(['Median Releases'], [general_data['median_releases']])
    plt.ylabel('Number of Releases')
    plt.title('Median Releases of Popular Repositories (RQ03)')
    plt.savefig(f'{output_dir}/median_releases.png')
    plt.close()

    # Gráfico para frequência de atualização (RQ04)
    plt.figure(figsize=(8, 6))
    plt.bar(['Median Update Frequency'], [general_data['median_update_frequency']])
    plt.ylabel('Days Since Last Update')
    plt.title('Median Update Frequency of Popular Repositories (RQ04)')
    plt.savefig(f'{output_dir}/median_update_frequency.png')
    plt.close()

    # Gráfico para fechamento de issues (RQ06)
    plt.figure(figsize=(8, 6))
    plt.bar(['Median Issue Closure Ratio'], [general_data['median_issue_closure_ratio']])
    plt.ylabel('Closure Ratio')
    plt.title('Median Issue Closure Ratio of Popular Repositories (RQ06)')
    plt.savefig(f'{output_dir}/median_issue_closure_ratio.png')
    plt.close()

    # Carregando os dados de análise por linguagem
    with open(language_data_path, 'r') as f:
        language_data = json.load(f)

    # Gráfico para RQ05: Contagem de repositórios por linguagem popular
    languages = list(language_data['popular_language_counts'].keys())
    counts = list(language_data['popular_language_counts'].values())

    plt.figure(figsize=(10, 6))
    plt.barh(languages, counts, color='skyblue')
    plt.xlabel('Number of Repositories')
    plt.title('Repositories by Popular Language (RQ05)')
    plt.savefig(f'{output_dir}/repos_by_language.png')
    plt.close()

    print(f"All graphs saved in {output_dir}/")
