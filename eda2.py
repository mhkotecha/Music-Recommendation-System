import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the source data
source_data = pd.read_excel('/Users/komalb/MS/Math 448/Project/Final Songs.xlsx')
significant_features = ['Danceability', 'Energy', 'Loudness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence']

# Histogram for 'Popularity'
plt.figure(figsize=(10, 6))
sns.histplot(source_data['Popularity'], kde=True)
plt.title('Histogram of Popularity')
plt.savefig('histogram_popularity.png')
plt.close()

# Boxplot for 'Popularity'
plt.figure(figsize=(10, 6))
sns.boxplot(y=source_data['Popularity'])
plt.title('Boxplot of Popularity')
plt.savefig('boxplot_popularity.png')
plt.close()

# Scatter plot of 'Popularity' vs significant features
for feature in significant_features:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=source_data[feature], y=source_data['Popularity'])
    plt.title(f'Scatter Plot of Popularity vs {feature}')
    plt.xlabel(feature)
    plt.ylabel('Popularity')
    plt.savefig(f'scatter_popularity_{feature}.png')
    plt.close()

# Correlation heatmap for 'Popularity' with significant features
plt.figure(figsize=(10, 8))
corr_matrix_popularity = source_data[significant_features + ['Popularity']].corr()
sns.heatmap(corr_matrix_popularity, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Popularity with Significant Features')
plt.savefig('correlation_heatmap_popularity.png')
plt.close()
