from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Lab2").getOrCreate()

df = spark.read.csv("most_played_mobile_games.csv", header=True, inferSchema=True)

df.printSchema()

# Strategy 1: Repartitioning by Publisher

partition_publisher = df.repartition("Publisher")   

publisher_summary = partition_publisher.filter(df["Publisher"]== "Tencent Games")

print("Summary of Tencent Games:")
publisher_summary.show()

#Transformations

tencent_data = df.filter(df["Publisher"].contains("Tencent Games"))

print("Tencent Games:")
tencent_data.select()

sorted_date = df.orderBy("Release date", ascending=False)

print("Latest Games:")
sorted_date.select("Game", "Release date", "Publisher").show(10)