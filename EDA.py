import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the source data
source_data = pd.read_excel('/Users/komalb/MS/Math 448/Project/Final Songs.xlsx')

# Significant features identified from the p-values
significant_features = ['Danceability', 'Energy', 'Loudness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence']

# Perform EDA on the significant features

# Histogram for each significant feature
for feature in significant_features:
    plt.figure(figsize=(10, 6))
    sns.histplot(source_data[feature], kde=True)
    plt.title(f'Histogram of {feature}')
    plt.savefig(f'histogram_{feature}.png')
    plt.close()

# Pairplot for significant features
plt.figure(figsize=(12, 10))
sns.pairplot(source_data[significant_features])
plt.savefig('pairplot_significant_features.png')
plt.close()

# Correlation heatmap for significant features
plt.figure(figsize=(10, 8))
corr_matrix = source_data[significant_features].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Significant Features')
plt.savefig('correlation_heatmap_significant_features.png')
plt.close()
