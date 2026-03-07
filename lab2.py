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

partition_date = df.repartitionByRange(4, "Release date")

date_summary = partition_date.filter(df["Release date"] >= "2020").groupBy("Release date").count().orderBy("Release date")

print("Content by Release Date:")
date_summary.show()

#Transformations

tencent_data = df.filter(df["Publisher(s)"].contains("Tencent Games"))

print("Tencent Games:")
tencent_data.select("Game", "Release date", "Player count[a]").show(10)

sorted_date = df.orderBy("Release date", ascending=False)

print("Latest Games:")
sorted_date.select("Game", "Release date", "Publisher").show(10)

spark.stop()