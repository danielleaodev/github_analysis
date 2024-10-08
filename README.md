# GitHub Analysis

Este projeto coleta e analisa dados dos 1000 repositórios mais populares do GitHub (baseado no número de estrelas).

## Estrutura do Projeto

- `collectors/`: Contém o código para coletar dados do GitHub.
- `processors/`: Contém o código para processar os dados brutos.
- `analyzers/`: Contém o código para analisar os dados processados.
- `utils/`: Contém funções utilitárias para gerar e salvar logs.
- `main.py`: Script principal que orquestra a coleta, processamento e análise de dados.

## Como Executar

1. Clone este repositório.
2. Instale as dependências* necessárias.
3. Obtenha um token de acesso do GitHub.
4. Execute o script `main.py`.
    
    Os resultados da análise serão salvos nos arquivos general_analysis.json e language_analysis.json.
## * Dependências/Versão
- Python 3.x
- requests 2.32.3
- pandas 2.2.2
- python-dotenv 1.0.1
- matplotlib 3.9.2
- seaborn 0.13.2
   
## Relatório

- O relatório com as analises dos dados encontrados se encontra no arquivo `Relatório.md`. Nele, estão contempladas algumas hipóteses de respostas às perguntas levantadas no enunciado juntamente à uma discussão dos resultados obtidos.
    


