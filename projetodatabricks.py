from pyspark.sql.functions import month, sum, col, expr, to_date

# Carregar o arquivo CSV de vendas
df_vendas = spark.read.csv("/FileStore/tables/vendas.csv", header=True, inferSchema=True)

# Exibir os dados 
df_vendas.show()

# Verificar o esquema original dos dados
df_vendas.printSchema()

# Converter a coluna 'date' para o formato de data (DateType) 
df_vendas = df_vendas.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))

# Verificar o esquema após a conversão da coluna 'date'
df_vendas.printSchema()

# Convertendo as colunas 'price' e 'quantity' para float e int, respectivamente
df_vendas = df_vendas.withColumn("price", col("price").cast("float"))
df_vendas = df_vendas.withColumn("quantity", col("quantity").cast("int"))

# Verificar o esquema após a conversão
df_vendas.printSchema()

# Exibir os dados novamente após as conversões
df_vendas.show()

# Criando a coluna 'total_sales' (preço * quantidade)
df_vendas = df_vendas.withColumn("total_sales", expr("price * quantity"))

# Exibir o DataFrame atualizado com a coluna 'total_sales'
df_vendas.show()

# Total de vendas por produto
df_total_produto = df_vendas.groupBy("product").agg(sum("total_sales").alias("total_revenue"))
df_total_produto.show()

# Extraindo o mês da coluna 'date' e calculando a receita total por mês
df_vendas = df_vendas.withColumn("month", month("date"))
df_receita_mensal = df_vendas.groupBy("month").agg(sum("total_sales").alias("monthly_revenue"))
df_receita_mensal.show()
