import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.style.use('dark_background')
sns.set_theme(style="darkgrid")

# DATASETS

categories = ['<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND']
house_counts = [9034, 6496, 2628, 2270, 5]

income = [8.3252, 8.3014, 7.2574, 5.6431, 6.1183]
house_value = [452600, 358500, 352100, 341300, 75000]
population = [322, 2401, 496, 558, 86]

games = ['PUBG Mobile', 'Honor of Kings', 'QQ Speed', 'Tiao Yi Tiao', 'Love Nikki']
players = [300, 200, 200, 100, 100]

release_years = ['2010','2011','2012','2014','2016','2017','2018']
release_counts = [1,1,3,2,3,4,1]

students = ['Alice', 'Bob', 'Charlie']
grades = [87.5, 88.5, 87.0]

blue_palette = ['#27374D', '#526D82', '#9DB2BF', '#DDE6ED']

# MATPLOTLIB VISUALIZATIONS

# 1. Bar Chart – Lab 3
plt.figure(figsize=(8,5))
plt.bar(categories, house_counts, color=blue_palette)
plt.title('Ocean Proximity Distribution', fontsize=14, weight='bold')
plt.xlabel('Category')
plt.ylabel('Number of Houses')
plt.xticks(rotation=25)
plt.tight_layout()
plt.show()

# 2. Scatter Plot – Lab 3
plt.figure(figsize=(8,5))
plt.scatter(income, house_value, color='#526D82')
plt.title('Median Income vs House Value', fontsize=14, weight='bold')
plt.xlabel('Median Income')
plt.ylabel('House Value')
plt.tight_layout()
plt.show()

# 3. Line Graph – Lab 2
plt.figure(figsize=(8,5))
plt.plot(release_years, release_counts, marker='o', color='#526D82', linewidth=2)
plt.title('Game Releases Over Time', fontsize=14, weight='bold')
plt.xlabel('Year')
plt.ylabel('Count')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# 4. Histogram – Lab 3
plt.figure(figsize=(8,5))
plt.hist(population, bins=5, color='#9DB2BF', edgecolor='white')
plt.title('Population Distribution', fontsize=14, weight='bold')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 5. Pie Chart – Lab 2
plt.figure(figsize=(6,6))
plt.pie(players, labels=games, autopct='%1.1f%%', colors=blue_palette)
plt.title('Tencent Game Player Distribution', fontsize=14, weight='bold')
plt.tight_layout()
plt.show()

# 6. Bar Chart – Lab 1
plt.figure(figsize=(6,4))
plt.bar(students, grades, color=blue_palette)
plt.title('Student Average Grades (>=80)', fontsize=14, weight='bold')
plt.xlabel('Students')
plt.ylabel('Average Grade')
plt.ylim(80, 90)
plt.tight_layout()
plt.show()

# SEABORN VISUALIZATIONS

# DataFrames

df_ocean = pd.DataFrame({'Category': categories, 'Count': house_counts})
df_income = pd.DataFrame({'Income': income, 'HouseValue': house_value, 'Population': population})
df_students = pd.DataFrame({'Student': students, 'Grade': grades})
df_release = pd.DataFrame({'Year': release_years, 'Count': release_counts})

# 7. Seaborn Bar Plot – Lab 3
plt.figure(figsize=(8,5))
sns.barplot(data=df_ocean, x='Category', y='Count', palette=blue_palette)
plt.title('Ocean Proximity Distribution', fontsize=14, weight='bold')
plt.xticks(rotation=25)
plt.tight_layout()
plt.show()

# 8. Regression Plot – Lab 3
plt.figure(figsize=(8,5))
sns.regplot(data=df_income, x='Income', y='HouseValue', scatter_kws={'color':'#526D82', 's':90},
line_kws={'color':'#27374D'})
plt.title('Income vs House Value', fontsize=14, weight='bold')
plt.tight_layout()
plt.show()

# 9. Box Plot – Lab 3
plt.figure(figsize=(6,4))
sns.boxplot(y=df_income['Population'], color='#526D82')
plt.title('Population Distribution', fontsize=14, weight='bold')
plt.tight_layout()
plt.show()

# 10. Heatmap – Lab 3
plt.figure(figsize=(6,5))
sns.heatmap(df_income.corr(), annot=True, cmap=blue_palette, linewidths=0.5)
plt.title('Correlation Heatmap', fontsize=14, weight='bold')
plt.tight_layout()
plt.show()

# 11. Count Plot – Lab 2
plt.figure(figsize=(8,5))
sns.countplot(data=df_release, x='Year', palette=blue_palette)
plt.title('Game Release Frequency', fontsize=14, weight='bold')
plt.xticks(rotation=25)
plt.tight_layout()
plt.show()

# 12. Seaborn Bar Plot – Lab 1
plt.figure(figsize=(6,4))
sns.barplot(data=df_students, x='Student', y='Grade', palette=blue_palette)
plt.title('Student Grades', fontsize=14, weight='bold')
plt.tight_layout()
plt.show()

# 13. Box Plot – Lab 1
plt.figure(figsize=(6,4))
blue_palette = ['#27374D', '#526D82', '#9DB2BF', '#DDE6ED']
sns.boxplot(y=df_students['Grade'], color=blue_palette[0])
plt.title('Student Grade Distribution', fontsize=14, weight='bold')
plt.tight_layout()
plt.show()