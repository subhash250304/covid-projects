# covid-projects
Titanic EDA Project Analyzed the Titanic dataset to identify survival patterns using Python (Pandas, Seaborn). The study revealed that gender and socio-economic class were the primary drivers of survival, with females and 1st-class passengers having the highest survival rates. Completed as part of a Data Science Certification.
Project Report: Exploratory Data Analysis of the Titanic Dataset
1. Introduction & Objective The primary objective of this project was to analyze the famous Titanic dataset to identify the key factors that influenced passenger survival rates. By applying Data Science techniques using Python libraries such as Pandas, Matplotlib, and Seaborn, this analysis seeks to determine if survival was random or if it followed specific patterns related to socio-economic status, gender, and age. The dataset comprises 891 rows, representing a subset of the passengers on board, and includes features such as Passenger Class, Sex, Age, Fare, and Port of Embarkation.

2. Data Cleaning & Preparation Before analysis could begin, the raw data required significant preprocessing to ensure accuracy.

Missing Values: The 'Age' column contained nearly 20% missing values. To prevent data loss, these were imputed using the median age of the passengers. The 'Embarked' column had minor gaps, which were filled with the mode (the most common port).

Feature Selection: The 'Cabin' column was dropped entirely as it had too many missing values to be useful. Identifiers such as 'Name', 'Ticket', and 'PassengerId' were also removed, as they do not statistically contribute to survival probability.


Encoding: Categorical variables were examined to ensure they were ready for visualization.

3. Key Findings & Visualizations The Exploratory Data Analysis (EDA) revealed three major trends:

Gender: The most significant predictor of survival was gender. Visualization showed that approximately 74% of females survived, compared to only 18% of males. This strongly confirms that the "Women and Children First" maritime protocol was strictly enforced.

Socio-Economic Class: There was a clear correlation between wealth and safety. First-class passengers had a survival rate exceeding 60%, while third-class passengers (the largest group) had a survival rate below 25%. This suggests that physical proximity to the boat deck and higher status granted better access to lifeboats.

Age Distribution: A Kernel Density Estimate (KDE) plot highlighted that children (ages 0–10) had a higher probability of survival, whereas the highest death toll was observed among young adults aged 20–30.

4. Conclusion This analysis conclusively demonstrates that survival on the Titanic was not a matter of chance. It was heavily determined by gender, class, and age. The data proves that social hierarchy and emergency protocols played a definitive role in who survived the tragedy.
output: Dataset Loaded Successfully
Shape: (891, 12) (Rows, Columns)

First 5 Rows:
   PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked    
0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S    
1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C    
2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S    
3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S    
4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S    

Missing Values Check:
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64

 Data Cleaning Complete. Remaining columns:
['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

Overall Survival Rate: 38.38%
Overall Death Rate: 61.62%
C:\Users\Admin\Music\axcentra ds python\code 4.py:49: FutureWarning: 

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same 
effect.

  sns.countplot(data=df, x='Survived', palette='pastel')
