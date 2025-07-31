import pandas as pd

data = pd.read_csv("Salary_Data.csv")
data["YearsExperience"] += 3
data.to_csv("Salary_Data.csv", index=False)