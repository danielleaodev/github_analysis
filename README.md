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

## * Dependências
Python 3.x
requests
pandas
python-dotenv

```bash
python main.py
