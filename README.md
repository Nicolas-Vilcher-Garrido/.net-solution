# Analise de dados de vendas com Databricks e PySpark

## Descrição do Projeto

Este projeto visa realizar uma análise de dados de vendas utilizando Databricks e PySpark. Através do carregamento de um arquivo CSV contendo informações de vendas, o projeto aplica transformações e agregações para obter insights valiosos sobre o desempenho dos produtos e a receita mensal. Ele demonstra como o Spark pode ser usado para processar grandes volumes de dados de forma eficiente em um ambiente distribuído.

## Estrutura do Projeto

1. **Carregamento de Dados**:
   - O arquivo `vendas.csv` contendo informações de vendas, como produto, preço, quantidade e data, é carregado no ambiente do Databricks.
   - O CSV é lido utilizando o Spark com as opções `header=True` para reconhecer o cabeçalho e `inferSchema=True` para inferir automaticamente os tipos de dados.

2. **Manipulação de Dados**:
   - As colunas `price` e `quantity` são convertidas para os tipos `float` e `int`, respectivamente, para garantir cálculos precisos.
   - A coluna `date` é convertida para o tipo de data (`DateType`), garantindo a correta manipulação das datas no Spark.

3. **Cálculos e Agregações**:
   - Criamos uma nova coluna chamada `total_sales`, que é o resultado da multiplicação entre o preço e a quantidade para cada venda.
   - Calculamos o **total de vendas por produto** usando a função de agregação `groupBy()` e `sum()`, obtendo o valor total vendido para cada produto.
   - Extraímos o mês da coluna de data e calculamos a **receita mensal** agrupando os dados por mês.

4. **Visualização dos Dados**:
   - O projeto exibe os resultados intermediários e finais em tabelas, permitindo uma análise visual das vendas totais por produto e das variações de receita ao longo dos meses.

## Tecnologias Utilizadas

- **Databricks**: Ambiente de processamento distribuído otimizado para grandes volumes de dados.
- **PySpark**: Interface Python para o Apache Spark, usada para manipulação e agregação de dados.
- **CSV**: Formato de arquivo utilizado para armazenar os dados de entrada.

## Como Rodar o Projeto

1. **Carregar os Dados**:
   - Faça upload do arquivo `vendas.csv` para o Databricks, no diretório `/FileStore/tables/`.
   
2. **Executar o Notebook**:
   - O código está estruturado para rodar diretamente no Databricks.

3. **Explorar os Resultados**:
   - O notebook exibe os resultados de vendas totais por produto e receita mensal. Explore os dados e faça modificações no código para gerar novas análises.

## Conclusão

Este projeto mostra como o Databricks e PySpark podem ser utilizados para analisar dados de vendas em um ambiente distribuído. Com o uso de funções de agregação e manipulação de dados, é possível obter insights importantes de forma eficiente e escalável.
