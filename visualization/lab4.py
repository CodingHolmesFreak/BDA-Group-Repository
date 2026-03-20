import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#Datasets

#lab 1 dataset
students = ['Alice', 'Bob', 'Charlie']
grades = [87.5, 88.5, 87.0]

#lab 2 dataset
games = ['PUBG Mobile', 'Honor of Kings', 'QQ Speed', 'Tiao Yi Tiao', 'Love Nikki']
players = [300, 200, 200, 100, 100]

release_years = ['2010', '2011', '2012', '2014', '2016', '2017', '2018']
release_counts = [1, 1, 3, 2, 3, 4, 1]

#lab 3 dataset
categories = ['<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND']
house_counts = [9034, 6496, 2628, 2270, 5]

income = [8.3252, 8.3014, 7.2574, 5.6431, 6.1183]
house_value = [452600, 358500, 352100, 341300, 75000]
population = [322, 2401, 496, 558, 86]

#MATPLOTLIB VISUALIZATIONS

#1 BAR CHART - LAB 3
plt.figure()
plt.bar(categories, house_counts)
plt.title("Ocean Proximity Distribution")
plt.xlabel('Category')
plt.ylabel('Number of Houses')
plt.show()

#2 Scatter Plot - LAB 3
plt.figure()
plt.scatter(income, house_value)
plt.title("Median Income vs House Value")
plt.xlabel("Median Income")
plt.ylabel("House Value")
plt.show()

#3 Line Graph - LAB 2
plt.figure()
plt.plot(release_years, release_counts, marker='o')
plt.title("Game Releases Over Time")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

#4 Histogram - LAB 3
plt.figure()
sns.histplot(population, bins=5)
plt.title("Population Distribution")
plt.xlabel("Population")          
plt.ylabel("Frequency")
plt.show()

#5 Pie Chart - Lab 2
plt.figure()
plt.pie(players, labels=games, autopct='%1.1f%%')
plt.title('Tencent Game Player Distribution')
plt.show()

#6 Bar Chart - Lab 1
plt.figure()
plt.bar(students, grades)
plt.title("Student Average Grades (>=80)")
plt.xlabel("Student")
plt.ylabel("Average Grade")
plt.ylim(80, 90)
plt.show()

#SEABORN VISUALIZATIONS

