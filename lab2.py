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

partition_date = df.repartitionByRange(4, "Release Date")

date_summary = partition_date.filter(df["Release date"] >= "2020").groupBy("Release date").count().orderBy("Release date")

print("Content by Relase Date ")
date_summary.show()

#Transformations

#filter publisher
tencent_date = df.filter(df["Publisher(s)"].contains("Tencent Games"))

print("Tencent Games:")
tencent_date.select("Game", "Release date", "Player count[a]").show()

#sort release date
sorted_date = df.orderBy("Release date", ascending=False)

print("Latest Games:")
sorted_date.select("Game", "Release date", "Publisher(s)").show(10)

spark.stop()