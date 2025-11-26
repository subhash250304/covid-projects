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
