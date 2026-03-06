from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Lab2").getOrCreate()

df = spark.read.csv("most_played_mobile_games.csv", header=True, inferSchema=True)

df.printSchema()

