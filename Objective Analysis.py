import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load your local file
file_path = r"C:\Users\Sarthak Chubey\Downloads\NCHS_-_Potentially_Excess_Deaths_from_the_Five_Leading_Causes_of_Death.csv"
df = pd.read_csv(file_path)

# Drop rows with important missing values
df_cleaned = df.dropna(subset=[
    'Year', 'Cause of Death', 'State', 'Potentially Excess Deaths',
    'Percent Potentially Excess Deaths', 'Locality',
    'Observed Deaths', 'Expected Deaths', 'Age Range'
])

# Fix warning by using .loc
df_cleaned.loc[:, 'Year'] = df_cleaned['Year'].astype(int)

# Plot settings
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

#1)

top_causes = df_cleaned['Cause of Death'].value_counts().index[:5]
trend_data = df_cleaned[df_cleaned['Cause of Death'].isin(top_causes)]

plt.figure()
sns.lineplot(data=trend_data, x='Year', y='Potentially Excess Deaths',
             hue='Cause of Death', estimator='sum', errorbar=None)
plt.title('Trend of Potentially Excess Deaths Over Time by Cause')
plt.xlabel('Year')
plt.ylabel('Total Excess Deaths')
plt.legend(title='Cause of Death')
plt.tight_layout()
plt.show()


#2)
plt.figure()
cause_totals = df_cleaned.groupby('Cause of Death')['Potentially Excess Deaths'].sum().sort_values(ascending=False)
sns.barplot(x=cause_totals.index, y=cause_totals.values)
plt.title('Total Potentially Excess Deaths by Cause of Death')
plt.xlabel('Cause of Death')
plt.ylabel('Total Excess Deaths')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#3)
plt.figure()
state_risk = df_cleaned.groupby('State')['Percent Potentially Excess Deaths'].mean().sort_values(ascending=False).head(20)
sns.barplot(x=state_risk.values, y=state_risk.index, hue=state_risk.index, palette="Reds_r", legend=False)
plt.title('Top 20 States by Avg Percent Potentially Excess Deaths')
plt.xlabel('Average Percent Excess Deaths')
plt.ylabel('State')
plt.tight_layout()
plt.show()

#4)
plt.figure()
sns.boxplot(data=df_cleaned, x='Locality', y='Percent Potentially Excess Deaths')
plt.title('Percent Excess Deaths by Locality')
plt.xlabel('Locality')
plt.ylabel('Percent Excess Deaths')
plt.tight_layout()
plt.show()


#5)
heatmap_data = df_cleaned.pivot_table(
    values='Percent Potentially Excess Deaths',
    index='Age Range',
    columns='Cause of Death',
    aggfunc='mean'
)

plt.figure()
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap='coolwarm')
plt.title('Avg Percent Excess Deaths by Age Range and Cause of Death')
plt.xlabel('Cause of Death')
plt.ylabel('Age Range')
plt.tight_layout()
plt.show()


#6)
death_stats = df_cleaned.groupby('Year')[['Observed Deaths', 'Expected Deaths']].sum().reset_index()

plt.figure()
plt.plot(death_stats['Year'], death_stats['Observed Deaths'], marker='o', label='Observed Deaths')
plt.plot(death_stats['Year'], death_stats['Expected Deaths'], marker='o', label='Expected Deaths')
plt.title('Observed vs Expected Deaths Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.legend()
plt.tight_layout()
plt.show()

