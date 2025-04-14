import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess data
def load_recommendation_data():
    df = pd.read_excel('Datasets/Final Songs.xlsx')
    df.dropna(inplace=True)

    features_to_scale = ['Danceability', 'Energy', 'Loudness', 'Speechiness',
                         'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo']

    scaler = StandardScaler()
    df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

    return df, features_to_scale

# Recommendation function using direct model outputs
def recommend_songs(user_id, df, features, predicted_popularity, classification_predictions, num_recommendations=5,
                    filter_popular=False):
    df['Predicted Popularity'] = predicted_popularity

    # Ensure classification_predictions is correctly applied
    if isinstance(classification_predictions, pd.Series):  # If it's a Pandas Series, use it directly
        df['Popularity Class'] = classification_predictions
    else:
        raise TypeError(" Error: classification_predictions is not a valid Pandas Series!")

    user_songs = df[df['User id'] == user_id]
    user_playlist_songs = user_songs['Song id'].unique()

    valid_user_playlist_songs = df[df['Song id'].isin(user_playlist_songs)]
    user_song_indices = valid_user_playlist_songs.index

    if len(user_song_indices) == 0:
        print("No valid songs found in the user's playlist.")
        return pd.DataFrame()

    similarity_matrix = cosine_similarity(df[features])
    mean_similarity_scores = similarity_matrix[user_song_indices].mean(axis=0)

    similarity_scores_df = pd.DataFrame({
        'Song id': df['Song id'],
        'Similarity Score': mean_similarity_scores,
        'Predicted Popularity': df['Predicted Popularity'],
        'Popularity Class': df['Popularity Class']
    })

    similarity_scores_df = similarity_scores_df[~similarity_scores_df['Song id'].isin(user_playlist_songs)]

    if filter_popular:
        similarity_scores_df = similarity_scores_df[similarity_scores_df['Popularity Class'] == "Popular"]

    top_recommendations = similarity_scores_df.sort_values(by=['Similarity Score', 'Predicted Popularity'],
                                                           ascending=[False, False]).head(num_recommendations)

    recommended_songs = top_recommendations.merge(df[['Song id', 'Song Name', 'Artist(s)']],
                                                  on='Song id').drop_duplicates(subset='Song id')

    return recommended_songs
