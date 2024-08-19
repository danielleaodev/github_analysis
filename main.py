import pandas as pd
from collectors.github_data_collector import GitHubDataCollector
from processors.data_processor import DataProcessor
from analyzers.data_analyzer import DataAnalyzer
from utils.utils import setup_logging, log_error
from utils.custom_exceptions import GitHubAPIError, DataProcessingError, DataAnalysisError

def main():
    setup_logging()
    
    try:
        token = "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"  # Substitua pelo seu token de acesso do GitHub
        collector = GitHubDataCollector(token)
        raw_data = collector.get_repositories(num_repos=100)

        processor = DataProcessor()
        processed_data = processor.process_raw_data(raw_data)
        processor.save_to_csv('processed_data.csv')
        
        # Calcular métricas individuais
        analyzer = DataAnalyzer(processed_data)
        general_analysis = analyzer.analyze_general()
        language_analysis = analyzer.analyze_by_language()

        # Convertendo as análises para DataFrames para salvar em CSV
        general_df = pd.DataFrame([general_analysis])
        language_df = pd.DataFrame.from_dict(language_analysis).reset_index()

        # Salvando as análises em CSV
        general_analysis_path = 'general_analysis.csv'
        language_analysis_path = 'language_analysis.csv'
        
        general_df.to_csv(general_analysis_path, index=False)
        language_df.to_csv(language_analysis_path, index=False)

        print("Análises salvas com sucesso!")
        print(f"Análise geral salva em: {general_analysis_path}")
        print(f"Análise por linguagem salva em: {language_analysis_path}")
        
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
