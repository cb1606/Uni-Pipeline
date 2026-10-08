import pandas as pd

# Load raw student data
df = pd.read_csv("data/students.csv")

# Classify student performance
def classify_mark(mark):
    if mark >= 70:
        return "Distinction"
    elif mark >= 50:
        return "Pass"
    else:
        return "Fail"

df["performance"] = df["mark"].apply(classify_mark)

# Save transformed data
df.to_csv("data/student_performance.csv", index=False)

print("Transformation complete.")
print(df.head())
