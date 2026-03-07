from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Lab2").getOrCreate()

df = spark.read.csv("most_played_mobile_games.csv", header=True, inferSchema=True)

df.printSchema()

# Strategy 1: Repartitioning by Publisher

partition_publisher = df.repartition("Publisher(s)")   

publisher_summary = partition_publisher.filter(df["Publisher(s)"]== "Tencent Games")

print("Summary of Tencent Games:")
publisher_summary.show()

# Strategy 2: Repartitioning by Release Date
<<<<<<< HEAD
=======

partition_date = df.repartitionByRange(4, "Release date")

date_summary = partition_date.filter(df["Release date"] >= "2020").groupBy("Release date").count().orderBy("Release date")

print("Content by Release Date:")
date_summary.show()

#Transformations
>>>>>>> gestiada

partition_date = df.repartitionByRange(4, "Release Date")

date_summary = partition_date.filter(df["Release date"] >= "2020").groupBy("Release date").count().orderBy("Release date")

print("Content by Relase Date ")
date_summary.show()

