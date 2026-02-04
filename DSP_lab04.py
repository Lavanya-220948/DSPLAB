
#1st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#2nd
file_path = input("Enter the path of the dataset (CSV file): ")
df = pd.read_csv(file_path)


#3rd rows=238 and columns=7

rows, columns = df.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")



#4column names Column names:


print("Column names:")
print(df.columns)


#display first five rows

print("First 5 rows of the dataset:")
print(df.head())


#data type of each column

print("Data types of each column:")
print(df.dtypes)



#identify missing numbers

print("Missing values in each column:")
print(df.isnull().sum())



#8. fill missing values using mean

numerical_columns = df.select_dtypes(include=np.number).columns

for col in numerical_columns:
    df[col].fillna(df[col].mean())


#9. fill missing values using mode
categorical_columns = df.select_dtypes(include=['object', 'string']).columns

for col in categorical_columns:
    df[col].fillna(df[col].mode()[0])


#10 verify there is no missing values

print("Missing values after filling:")
print(df.isnull().sum())

print(df.head())

#11 mean for numerical values

print("Mean of numerical columns:")
print(df[numerical_columns].mean())


#12 median for all numerical values

print("Median of numerical columns:")
print(df[numerical_columns].median())



#standard deviation

print("Standard deviation of numerical columns:")
print(df[numerical_columns].std())


#minimum and maximum values

print("Minimum values:")
print(df[numerical_columns].min())

print("Maximum values:")
print(df[numerical_columns].max())



#15 summary using describe()

print("Statistical summary:")
print(df.describe())


#16histogram for purchases amount

purchase_col = input("Enter the purchase amount column name: ")

plt.hist(df[purchase_col], bins=10)
plt.xlabel("Purchase Amount")
plt.ylabel("Frequency")
plt.title("Histogram of Purchase Amount")
plt.show()

#17 barchart showing the count of customers


category_col = input("Enter the product category column name: ")

df[category_col].value_counts().plot(kind='bar')
plt.xlabel("Product Category")
plt.ylabel("Customer Count")
plt.title("Customers by Product Category")
plt.show()




#18 box plot for purchase amount


plt.boxplot(df[purchase_col])
plt.ylabel("Purchase Amount")
plt.title("Box Plot of Purchase Amount")
plt.show()


#19 scatter plot between age and purchase

age_col = input("Enter the age column name: ")

plt.scatter(df[age_col], df[purchase_col])
plt.xlabel("Age")
plt.ylabel("Purchase Amount")
plt.title("Age vs Purchase Amount")
plt.show()


#20 correlation heatmap for numerical columns

correlation_matrix = df[numerical_columns].corr()

plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


















































