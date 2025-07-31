import pandas as pd

data = pd.read_csv("Salary_Data.csv")
data["YearsExperience"] += 2
data.to_csv("Salary_Data.csv", index=False)