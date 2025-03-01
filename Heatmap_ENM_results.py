import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("/home/manueljara/Documents/ENMs/suitability_proportions_all.csv")

# Select numeric columns
numeric_columns = data.select_dtypes(include=['number']).columns

# Group by 'Continent' and compute means
continent_data = data.groupby('Continent')[numeric_columns].mean().reset_index()

# Set 'Continent' as the index for the heatmap
continent_data.set_index('Continent', inplace=True)

# Generate the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(continent_data, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Mean Suitability by Continent")
plt.show()