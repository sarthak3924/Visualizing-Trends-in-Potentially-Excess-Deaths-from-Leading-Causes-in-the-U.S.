import pandas as pd

# Update the path to the CSV file
file_path = r"C:\Users\Sarthak Chubey\Downloads\NCHS_-_Potentially_Excess_Deaths_from_the_Five_Leading_Causes_of_Death.csv"

# Load the CSV file
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found. Please check the path and try again.")
    exit()

# Drop rows with missing values in key columns
df_clean = df.dropna(subset=[
    'Observed Deaths', 'Expected Deaths', 'Potentially Excess Deaths', 'Percent Potentially Excess Deaths'
])

# 1. Most Common Cause of Death
most_common_cause = df_clean['Cause of Death'].value_counts().idxmax()
print("1. Most Common Cause of Death:", most_common_cause)

# 2. State with Highest Avg % Excess Deaths
state_highest_excess_pct = df_clean.groupby('State')['Percent Potentially Excess Deaths'].mean().idxmax()
print("2. State with Highest Avg % Excess Deaths:", state_highest_excess_pct)

# 3. Year with Highest Total Excess Deaths
year_highest_excess = df_clean.groupby('Year')['Potentially Excess Deaths'].sum().idxmax()
print("3. Year with Highest Total Excess Deaths:", year_highest_excess)

# 4. Age Group with Highest Avg % Excess Deaths
agegroup_highest_pct = df_clean.groupby('Age Range')['Percent Potentially Excess Deaths'].mean().idxmax()
print("4. Age Group with Highest Avg % Excess Deaths:", agegroup_highest_pct)

# 5. Average % Excess Deaths from Heart Disease
avg_pct_heart_disease = df_clean[df_clean['Cause of Death'] == 'Heart Disease']['Percent Potentially Excess Deaths'].mean()
print("5. Average % Excess Deaths from Heart Disease:", round(avg_pct_heart_disease, 2))

# 6. Total Excess Deaths from Cancer
total_cancer_excess = df_clean[df_clean['Cause of Death'] == 'Cancer']['Potentially Excess Deaths'].sum()
print("6. Total Excess Deaths from Cancer:", int(total_cancer_excess))

# 7. State with Lowest Avg Expected Deaths
state_lowest_expected = df_clean.groupby('State')['Expected Deaths'].mean().idxmin()
print("7. State with Lowest Avg Expected Deaths:", state_lowest_expected)

# 8. Entries where Observed > Expected Deaths
count_excess_observed = (df_clean['Observed Deaths'] > df_clean['Expected Deaths']).sum()
print("8. Entries where Observed > Expected Deaths:", int(count_excess_observed))

# 9. Top 5 States by Total Excess Deaths
top5_states_excess = df_clean.groupby('State')['Potentially Excess Deaths'].sum().nlargest(5)
print("9. Top 5 States by Total Excess Deaths:")
print(top5_states_excess)

# 10. Correlation between Population and Excess Deaths
correlation_pop_excess = df_clean['Population'].corr(df_clean['Potentially Excess Deaths'])
print("10. Correlation between Population and Excess Deaths:", round(correlation_pop_excess, 3))