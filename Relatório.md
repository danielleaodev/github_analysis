# Características de Repositórios Populares no GitHub

Este relatório analisa as características dos 1.000 repositórios com maior número de estrelas no GitHub, explorando questões relacionadas à maturidade, contribuição externa, frequência de lançamentos, frequência de atualizações, linguagens de programação, e o percentual de issues fechadas.

## Introdução

A análise é guiada pelas seguintes questões de pesquisa:

1. **Sistemas populares são maduros/antigos?**  
   *Hipótese:* Espera-se que sistemas populares sejam relativamente antigos, devido ao tempo necessário para atrair uma grande base de usuários e colaboradores.

2. **Sistemas populares recebem muita contribuição externa?**  
   *Hipótese:* É provável que sistemas populares tenham uma alta quantidade de pull requests aceitas, refletindo uma comunidade ativa e colaborativa.

3. **Sistemas populares lançam releases com frequência?**  
   *Hipótese:* Sistemas populares devem lançar releases frequentemente para manter o interesse dos usuários e fornecer atualizações regulares.

4. **Sistemas populares são atualizados com frequência?**  
   *Hipótese:* Espera-se que esses sistemas sejam atualizados regularmente para corrigir bugs, implementar novas funcionalidades e responder às necessidades da comunidade.

5. **Sistemas populares são escritos nas linguagens mais populares?**  
   *Hipótese:* A maioria dos sistemas populares deve ser escrita em linguagens de programação amplamente utilizadas e populares, como Python e JavaScript.

6. **Sistemas populares possuem um alto percentual de issues fechadas?**  
   *Hipótese:* É esperado que esses sistemas tenham uma alta taxa de fechamento de issues, indicando uma manutenção ativa e uma comunidade engajada na resolução de problemas.

7. **Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?**  
   *Hipótese:* Espera-se que sistemas escritos em linguagens populares atraiam mais contribuições, lancem mais releases e sejam atualizados com mais frequência devido à maior adoção e suporte da comunidade.

## Metodologia

Para responder às questões de pesquisa, foram coletados dados dos 1.000 repositórios com maior número de estrelas no GitHub. As métricas principais analisadas incluem:

- **Idade do repositório:** Calculada a partir da data de criação.
- **Total de pull requests aceitas.**
- **Total de releases.**
- **Tempo até a última atualização:** Calculado a partir da data de última atualização.
- **Linguagem primária:** Identificação da linguagem principal do repositório.
- **Razão de fechamento de issues:** Proporção entre o número de issues fechadas e o total de issues.

Os dados foram sumarizados utilizando valores medianos para representar as distribuições.

## Resultados

Para cada uma das questões de pesquisa, os seguintes resultados foram obtidos:

1. **Maturidade dos Sistemas Populares:**
   - *Métrica:* Idade mediana do repositório.
   - *Resultado:* A idade mediana dos repositórios é de **8 anos**.

2. **Contribuição Externa:**
   - *Métrica:* Total de pull requests aceitas.
   - *Resultado:* A mediana de pull requests aceitas é de **577,5**.

3. **Frequência de Lançamentos:**
   - *Métrica:* Total de releases.
   - *Resultado:* A mediana do número de releases é de **30**.

4. **Frequência de Atualizações:**
   - *Métrica:* Tempo até a última atualização.
   - *Resultado:* A mediana do tempo desde a última atualização é de **0 dias** (indicando atualizações frequentes).

5. **Linguagens de Programação:**
   - *Métrica:* Linguagem primária de cada repositório.
   - *Resultado:* As principais linguagens usadas são:
     - Python: 163 repositórios
     - JavaScript: 156 repositórios
     - TypeScript: 132 repositórios
     - Go: 75 repositórios
     - Java: 59 repositórios

6. **Percentual de Issues Fechadas:**
   - *Métrica:* Razão entre número de issues fechadas e o total de issues.
   - *Resultado:* A mediana do percentual de issues fechadas é de **86%**.

7. **Sistemas escritos em linguagens mais populares recebem mais contribuição externa, lançam mais releases e são atualizados com mais frequência?**
   - *Métrica 1:* Mediana de pull requests aceitas.
     - *Resultado:* A mediana de pull requests aceitas para sistemas escritos em linguagens populares é de **722**, enquanto para sistemas em linguagens não populares é de **305**.
   - *Métrica 2:* Mediana de releases.
     - *Resultado:* A mediana de releases para sistemas em linguagens populares é de **46**, enquanto para sistemas em linguagens não populares é de **0**.
   - *Métrica 3:* Mediana de dias desde a última atualização.
     - *Resultado:* A mediana de dias desde a última atualização é de **0** tanto para sistemas em linguagens populares quanto para sistemas em linguagens não populares.
       
# Data Viz e Análise dos Resultados

## Visuais
![Análise Geral](Dashboard%20de%20Análise%20de%20Repositórios%20Populares%20no%20Github.png)

![Análise Requisito extra](Análise%20requisito%20extra.png)


## Discussão

Os resultados confirmam parcialmente as hipóteses iniciais. Os sistemas populares tendem a ser maduros, com uma idade mediana de 8 anos, e possuem uma comunidade ativa, como evidenciado pelos 577,5 pull requests aceitos na mediana. A frequência de releases e atualizações é alta, o que é coerente com a hipótese de que sistemas populares são mantidos ativamente. Quanto às linguagens de programação, as mais populares (como Python e JavaScript) dominam, o que também estava dentro do esperado. Finalmente, o alto percentual de issues fechadas reflete uma boa manutenção e uma comunidade engajada.

Além disso, sistemas escritos em linguagens populares, como Python, JavaScript, TypeScript, Go e Java, tendem a receber mais contribuição externa, com uma mediana de **722** pull requests aceitas, em comparação com **305** para sistemas em linguagens menos populares. Esses sistemas também lançam mais releases (mediana de **42**) em comparação com sistemas em linguagens menos populares (mediana de **0** releases). No entanto, a frequência de atualizações (mediana de **0 dias**) não difere entre sistemas escritos em linguagens populares e não populares, sugerindo que esse fator pode estar mais relacionado a outros aspectos dos projetos.

Esses resultados destacam a importância das linguagens populares na atração de contribuições e lançamento de releases, enquanto a frequência de atualizações pode depender de outras variáveis, como o tipo de projeto ou a estrutura da equipe de manutenção.
