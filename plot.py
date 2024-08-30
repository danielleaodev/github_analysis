import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec

def plot_dashboard():
    # Caminho da pasta Extract Data
    input_dir = 'Extract Data'
    
    # Carregar os dados dos CSVs gerados
    processed_data = pd.read_csv(f'{input_dir}/processed_data_1000.csv')
    general_analysis = pd.read_csv(f'{input_dir}/general_analysis_1000.csv')
    language_analysis = pd.read_csv(f'{input_dir}/language_analysis_1000.csv')

    # Configurar o layout do dashboard
    fig = plt.figure(constrained_layout=True, figsize=(15, 10))
    gs = GridSpec(3, 2, figure=fig)  # Layout de 3 linhas e 2 colunas

    # 1. Idade Mediana dos Repositórios
    ax1 = fig.add_subplot(gs[0, 0])  # Primeira linha, primeira coluna
    ax1.hist(processed_data['age'], bins=20, edgecolor='black')
    ax1.axvline(general_analysis['median_age'][0], color='blue', linestyle='dashed', linewidth=2, label=f'Mediana: {general_analysis["median_age"][0]:.1f} anos')
    ax1.set_title('Distribuição da Idade dos Repositórios')
    ax1.set_xlabel('Idade (anos)')
    ax1.set_ylabel('Número de Repositórios')
    ax1.legend()

    # 2. Contribuição Externa (Boxplot)
    ax2 = fig.add_subplot(gs[0, 1])  # Primeira linha, segunda coluna
    sns.boxplot(x=processed_data['pullRequests'], ax=ax2)
    ax2.set_title('Distribuição de Pull Requests Aceitas')
    ax2.set_xlabel('Total de Pull Requests Aceitas')

    # 3. Frequência de Lançamentos (Histograma)
    ax3 = fig.add_subplot(gs[1, 0])  # Segunda linha, primeira coluna
    ax3.hist(processed_data['releases'], bins=20, edgecolor='black')
    ax3.axvline(general_analysis['median_releases'][0], color='blue', linestyle='dashed', linewidth=2, label=f'Mediana: {general_analysis["median_releases"][0]:.1f} releases')
    ax3.set_title('Distribuição do Número de Releases')
    ax3.set_xlabel('Total de Releases')
    ax3.set_ylabel('Número de Repositórios')
    ax3.legend()

    # 4. Frequência de Atualizações (Gráfico de Barras)
    ax4 = fig.add_subplot(gs[1, 1])  # Segunda linha, segunda coluna
    ax4.hist(processed_data['last_update'], bins=20, edgecolor='black')
    ax4.set_title('Tempo Até a Última Atualização')
    ax4.set_xlabel('Tempo (dias)')
    ax4.set_ylabel('Número de Repositórios')

    # 5. Linguagens de Programação Principais (Gráfico de Barras)
    ax5 = fig.add_subplot(gs[2, 0])  # Terceira linha, primeira coluna
    ax5.bar(language_analysis['index'], language_analysis['popular_language_counts'], color='skyblue', edgecolor='black')
    ax5.set_title('Linguagens de Programação mais Usadas')
    ax5.set_xlabel('Linguagem de Programação')
    ax5.set_ylabel('Número de Repositórios')

    # 6. Percentual de Issues Fechadas (Boxplot)
    ax6 = fig.add_subplot(gs[2, 1])  # Terceira linha, segunda coluna
    sns.boxplot(x=processed_data['issue_closure_ratio'], ax=ax6)
    ax6.set_title('Distribuição do Percentual de Issues Fechadas')
    ax6.set_xlabel('Percentual de Issues Fechadas (%)')

    # Exibir o dashboard
    plt.suptitle('Dashboard de Análise de Repositórios Populares no GitHub', fontsize=16)
    plt.show()

if __name__ == "__main__":
    plot_dashboard()
