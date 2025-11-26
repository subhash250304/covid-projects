import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# ==========================================
# 1. DATA LOADING & OVERVIEW
# ==========================================
# Load the uploaded dataset
df = pd.read_csv(r'C:\Users\Admin\Downloads\Titanic-Dataset.csv')

print(" Dataset Loaded Successfully")
print(f"Shape: {df.shape} (Rows, Columns)")
print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values Check:")
print(df.isnull().sum())

# ==========================================
# 2. DATA CLEANING
# ==========================================
# 'Age' has missing values. We fill them with the median age.
df['Age'] = df['Age'].fillna(df['Age'].median())

# 'Embarked' has 2 missing values. Fill with the mode (most common port).
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop 'Cabin' (too many missing) and 'Ticket'/'Name' (not useful for stats)
df.drop(columns=['Cabin', 'Ticket', 'Name', 'PassengerId'], inplace=True, errors='ignore')

print("\n Data Cleaning Complete. Remaining columns:")
print(df.columns.tolist())

# ==========================================
# 3. EXPLORATORY DATA ANALYSIS (EDA)
# ==========================================

# --- A. Overall Survival Rate ---
survival_rate = df['Survived'].value_counts(normalize=True) * 100
print(f"\nOverall Survival Rate: {survival_rate[1]:.2f}%")
print(f"Overall Death Rate: {survival_rate[0]:.2f}%")

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Survived', palette='pastel')
plt.title('Overall Survival Count (0 = Died, 1 = Survived)')
plt.xticks([0, 1], ['Died', 'Survived'])
plt.show()

# --- B. Survival by Gender ---
# Hypothesis: Women were given priority.
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Sex', y='Survived', palette='coolwarm', errorbar=None)
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Probability')
plt.show()

# --- C. Survival by Passenger Class ---
# Hypothesis: 1st Class passengers had better access to lifeboats.
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='Pclass', y='Survived', palette='viridis', errorbar=None)
plt.title('Survival Rate by Passenger Class')
plt.ylabel('Survival Probability')
plt.xlabel('Passenger Class (1 = 1st, 3 = 3rd)')
plt.show()

# --- D. Age Distribution (Survived vs. Died) ---
# Hypothesis: Children were saved first.
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df[df['Survived'] == 1], x='Age', fill=True, label='Survived', color='green')
sns.kdeplot(data=df[df['Survived'] == 0], x='Age', fill=True, label='Died', color='red')
plt.title('Age Distribution: Survived vs. Died')
plt.legend()
plt.show()

# --- E. Correlation Heatmap ---
# See how numerical variables relate to survival
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include=[np.number]) # Select only numbers for correlation
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Feature Correlation Heatmap')
plt.show()