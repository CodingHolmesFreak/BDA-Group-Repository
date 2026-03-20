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

df_ocean = pd.DataFrame({
    'Category': categories,
    'Count': house_counts
})

df_income = pd.DataFrame({
    'Income': income,
    'HouseValue': house_value,
    'Population': population
})

df_students = pd.DataFrame({
    'Student': students,
    'Grade': grades
})

df_release = pd.DataFrame({
    'Year': release_years,
    'Count': release_counts
})

#7 Bar Plot - Lab 3
sns.barplot(x='Category', y='Count', data=df_ocean)
plt.title('Ocean Proximity')
plt.xticks(rotation=30)
plt.show()

#8 Regression Plot - Lab 3
sns.regplot(x='Income', y='HouseValue', data=df_income)
plt.title('Income vs House Value')
plt.show()

#9 Box Plot - Lab 3 
sns.boxplot(y=df_income['Population'])
plt.title('Population Distribution')
plt.show()

#10 Heatmap – Lab 3
sns.heatmap(df_income.corr(), annot=True)
plt.title('Correlation Heatmap')
plt.show()

#11 Count Plot – Lab 2
sns.countplot(x='Year', data=df_release)
plt.title('Game Release Frequency')
plt.xticks(rotation=30)
plt.show()

#12 Seaborn Bar Plot – Lab 1
sns.barplot(x='Student', y='Grade', data=df_students)
plt.title('Student Grades')
plt.show()

#13 Box Plot – Lab 1
sns.boxplot(y=df_students['Grade'])
plt.title('Student Grade Distribution')
plt.show()