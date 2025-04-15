#Data missing value handling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load CSV File
df = pd.read_csv('Customer Churn.csv')

#Display the output
df.head()
print("\nFirst 5 Rows:")
print(df.head())
df.info()
print(df.info())


#replacing blanks with 0 as tenure is 0 and no total charges are recorded
df["TotalCharges"] = df["TotalCharges"].replace(" ","0")
df["TotalCharges"] = df["TotalCharges"].astype("float")
df.info()
print(df.info())





#Data visulization(Graphs & charts)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Convert 'TotalCharges' to numeric if needed
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

#Selecting only numeric columns
numeric_df = df[['tenure', 'MonthlyCharges', 'TotalCharges']]

plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap - Customer Churn')
plt.show()




#Scatter Plot – Tenure vs Monthly Charges colored by Churn
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='tenure', y='MonthlyCharges', hue='Churn', palette='Set1', alpha=0.6)
plt.title('Tenure vs Monthly Charges (Churn Status)')
plt.xlabel('Tenure (months)')
plt.ylabel('Monthly Charges ($)')
plt.legend(title='Churn')
plt.show()




#Bar Plot – Churn by Contract Type
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='Contract', hue='Churn', palette='Set2')
plt.title('Churn by Contract Type')
plt.xlabel('Contract')
plt.ylabel('Customer Count')
plt.xticks(rotation=15)
plt.legend(title='Churn')
plt.show()




#Pie Chart – Churn Distribution
churn_counts = df['Churn'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(churn_counts.values, labels=churn_counts.index, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'salmon'])
plt.title('Customer Churn Distribution')
plt.axis('equal')
plt.show()



#Violin Plot – Monthly Charges Distribution by Churn
plt.figure(figsize=(8, 5))
sns.violinplot(data=df, x='Churn', y='MonthlyCharges', hue='Churn', palette='pastel', legend=False)
plt.title('Monthly Charges Distribution by Churn')
plt.xlabel('Churn')
plt.ylabel('Monthly Charges ($)')
plt.show()




#count of customers by senior citizen
plt.figure(figsize = (4,4))
ax = sns.countplot(x = "SeniorCitizen", data = df)
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Senior Citizen")
plt.show()


#churn by gender
plt.figure(figsize = (3,3))
sns.countplot(x = "gender", data = df, hue = "Churn")
plt.title("Churn by Gender")
plt.show()

#people who have used our services for a long time have stayed and people who have used our sevices 
#1 or 2 months  have churned
plt.figure(figsize = (4,4))
ax = sns.countplot(x = "Contract", data = df, hue = "Churn")
ax.bar_label(ax.containers[0])
plt.title("Count of Customers by Contract")
plt.show()


#Query Section for Customer Churn Dataset
import pandas as pd

#1 Total Rows and Columns
print("Total Rows and Columns:", df.shape)


#2 Top & Bottom 5 Records
print("Top 5 Records:\n", df.head())
print("\nBottom 5 Records:\n", df.tail())

#3 Missing Values Count
print("Missing Values in Each Column:\n", df.isnull().sum())

#4 Maximum & Minimum Monthly Charges
print("Maximum Monthly Charges:", df['MonthlyCharges'].max())
print("Minimum Monthly Charges:", df['MonthlyCharges'].min())

#5 Average Monthly Charges
print("Average Monthly Charges:", df['MonthlyCharges'].mean())

#6 Churn Rate by Contract Type
churn_by_contract = df.groupby('Contract')['Churn'].value_counts(normalize=True).unstack()
print("Churn Rate by Contract Type:\n", churn_by_contract)


#7 Customer Segment with Most Churn (e.g., Payment Method)
churn_by_payment = df[df['Churn'] == 'Yes']['PaymentMethod'].value_counts()
print("Most Churned Payment Method:\n", churn_by_payment.head(1))

#8 Monthly Charges by Gender
charges_by_gender = df.groupby('gender')['MonthlyCharges'].mean()
print("Average Monthly Charges by Gender:\n", charges_by_gender)


#9 Senior Citizen Churn Count
senior_churn = df[df['SeniorCitizen'] == 1]['Churn'].value_counts()
print("Churn Count among Senior Citizens:\n", senior_churn)

#10 Filter Customers Using Fiber Optic Internet Who Churned
fiber_churn = df[(df['InternetService'] == 'Fiber optic') & (df['Churn'] == 'Yes')]
print("Fiber Optic Users Who Churned:\n", fiber_churn[['customerID', 'InternetService', 'Churn']])




