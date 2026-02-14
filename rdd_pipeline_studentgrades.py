from pyspark import SparkContext

sc = SparkContext("local", "Student Grade Monitoring")

data = [
    "Alice,Math,85",
    "Bob,Math,78",
    "Alice,English,90",
    "Bob,English,88",
    "Charlie,Math,92",
    "Charlie,English,81",
    "Alice,Science,76",
    "Bob,Science,89"
]


rdd = sc.parallelize(data)

pipeline = (
    rdd
    .map(lambda x: x.split(","))                         
    .map(lambda x: (x[0], int(x[2])))                    
    .filter(lambda x: x[1] >= 80)                       
    .mapValues(lambda grade: (grade, 1))                 
    .reduceByKey(lambda a, b: (a[0]+b[0], a[1]+b[1]))   
    .mapValues(lambda x: round(x[0] / x[1], 2))          
)

result = pipeline.collect()

print("Student Average Grades (>=80 only):")
for student, avg in result:
    print(f"{student}: {avg}")

sc.stop()