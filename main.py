import pandas as pd
from collectors.github_data_collector import GitHubDataCollector
from processors.data_processor import DataProcessor
from analyzers.data_analyzer import DataAnalyzer
from utils.utils import setup_logging, log_error
from utils.custom_exceptions import GitHubAPIError, DataProcessingError, DataAnalysisError
from utils.generate_graphs import generate_graphs

def main():
    setup_logging()
    
    try:
        token = "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"  # Substitua pelo seu token de acesso do GitHub
        collector = GitHubDataCollector(token)
        raw_data = collector.get_repositories(num_repos=1000)

        processor = DataProcessor()
        processed_data = processor.process_raw_data(raw_data)
        processor.save_to_csv('processed_data.csv')

        analyzer = DataAnalyzer(processed_data)
        general_analysis = analyzer.analyze_general()
        language_analysis = analyzer.analyze_by_language()

        # Gerar gráficos diretamente a partir dos dados processados
        generate_graphs(general_analysis, language_analysis)

    except GitHubAPIError as e:
        log_error(f"GitHub API error: {e}")
        print("Erro na API do GitHub. Verifique os logs para mais detalhes.")
    except DataProcessingError as e:
        log_error(f"Data processing error: {e}")
        print("Erro no processamento dos dados. Verifique os logs para mais detalhes.")
    except DataAnalysisError as e:
        log_error(f"Data analysis error: {e}")
        print("Erro na análise dos dados. Verifique os logs para mais detalhes.")
    except Exception as e:
        log_error(f"Unexpected error: {e}")
        print("Ocorreu um erro inesperado. Verifique os logs para mais detalhes.")

if __name__ == "__main__":
    main()
