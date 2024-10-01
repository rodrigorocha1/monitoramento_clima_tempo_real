from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructField, StructType, StringType, DoubleType
import os
from dotenv import load_dotenv
load_dotenv()

# Configuração do Spark com o conector Kafka
spark = SparkSession.builder \
    .appName('TesteStreaming') \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0") \
    .getOrCreate()

# Definindo o schema dos dados de clima
schema_clima = StructType([
    StructField("coord", StructType([
        StructField("lon", DoubleType(), True),
        StructField("lat", DoubleType(), True)
    ]), True),
    StructField("main", StructType([
        StructField("temp", DoubleType(), True),
        StructField("feels_like", DoubleType(), True),
        StructField("temp_min", DoubleType(), True),
        StructField("temp_max", DoubleType(), True),
        StructField("pressure", DoubleType(), True),
        StructField("humidity", DoubleType(), True),
        StructField("sea_level", DoubleType(), True),
        StructField("grnd_level", DoubleType(), True)
    ]), True),
    StructField("visibility", DoubleType(), True),
    StructField("wind", StructType([
        StructField("speed", DoubleType(), True),
        StructField("deg", DoubleType(), True)
    ]), True),
    StructField("clouds", StructType([
        StructField("all", DoubleType(), True)
    ]), True),
    StructField("dt", DoubleType(), True),
    StructField("sys", StructType([
        StructField("country", StringType(), True),
        StructField("sunrise", DoubleType(), True),
        StructField("sunset", DoubleType(), True)
    ]), True),
    StructField("timezone", DoubleType(), True),
    StructField("id", DoubleType(), True),
    StructField("name", StringType(), True),  # Campo do município
    StructField("cod", DoubleType(), True)
])

# Leitura do stream do Kafka
clima_stream_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", os.environ['URL_KAFKA']) \
    .option("subscribe", "topico_app_tempo_real") \
    .option("startingOffsets", "latest") \
    .load()


# Seleciona e converte a coluna de valor para string
clima_valores = clima_stream_df.selectExpr("CAST(value AS STRING)")


print(clima_valores.show())
# Aplica o parsing da coluna de valor utilizando o schema definido
# clima_json = clima_valores.select(
#     from_json(col("value"), schema_clima).alias("data"))

# # Seleciona os campos de interesse da estrutura `main` e o nome do município
# clima_main = clima_json.select(
#     col("data.name").alias("municipio"),  # Nome do município
#     col("data.main.temp").alias("temperatura"),
#     col("data.main.feels_like").alias("sensacao_termica"),
#     col("data.main.temp_min").alias("temp_min"),
#     col("data.main.temp_max").alias("temp_max"),
#     col("data.main.pressure").alias("pressao"),
#     col("data.main.humidity").alias("umidade"),
#     col("data.main.sea_level").alias("nivel_do_mar"),
#     col("data.main.grnd_level").alias("nivel_do_solo")
# )

# # Exibe os dados no console
# query = clima_main.writeStream \
#     .outputMode("append") \
#     .format("console") \
#     .option("truncate", False) \
#     .start()

# # Aguarda a finalização do stream
# query.awaitTermination()
