import pandas as pd

# Load the file
file_path = r"dad-hmdb-childbirth-2024-2025-data-tables-en.xlsx"

# Read Table 1 - National hospitalization trends
table1 = pd.read_excel(file_path, sheet_name="Table 1", header=2, nrows=5)
table1.columns = ["Fiscal Year", "Hospitalization Rate per 100k", "Avg Length of Stay (days)"]
table1 = table1.dropna(subset=["Fiscal Year"])
print("=== Table 1 ===")
print(table1)
print()

# Read Table 2 - Top diagnoses by province
table2 = pd.read_excel(file_path, sheet_name="Table 2", header=1, nrows=150)
table2.columns = ["Province", "Rank", "Diagnosis", "Number of Hospitalizations", "Percentage", "Avg Length of Stay (days)"]
table2["Province"] = table2["Province"].ffill()
table2 = table2.dropna(subset=["Diagnosis"])
print("=== Table 2 ===")
print(table2.head(20))
print()

# Read Table 6a - Newborns by province over time
table6 = pd.read_excel(file_path, sheet_name="Table 6", header=2, nrows=18)
print("=== Table 6 ===")
print(table6.iloc[:, 0:5])

# Clean Table 6 - remove note rows at the bottom
table6_clean = table6.iloc[:13].copy()  # Keep only actual province rows
print("=== Table 6 Cleaned ===")
print(table6_clean.iloc[:, 0:3])
print()

# Export all three tables to clean CSV files
# Add a sort order column
table1["Sort Order"] = [1, 2, 3, 4, 5]
table1.to_csv("table1_hospitalization_trends.csv", index=False)
table2.to_csv("table2_diagnoses_by_province.csv", index=False)
table6_clean.to_csv("table6_newborns_by_province.csv", index=False)

print("✅ All three tables exported successfully as CSV files!")

# Clean Table 6 - remove note rows at the bottom
table6_clean = table6.iloc[:13].copy()  # Keep only actual province rows
print("=== Table 6 Cleaned ===")
print(table6_clean.iloc[:, 0:3])
print()

# Export all three tables to clean CSV files
table1.to_csv("table1_hospitalization_trends.csv", index=False)
table2.to_csv("table2_diagnoses_by_province.csv", index=False)
table6_clean.to_csv("table6_newborns_by_province.csv", index=False)

print("✅ All three tables exported successfully as CSV files!")