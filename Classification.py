import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

# Load and preprocess data
def load_classification_data():
    df = pd.read_excel('Datasets/Final Songs.xlsx')
    df.dropna(inplace=True)

    features_to_scale = ['Danceability', 'Energy', 'Loudness', 'Speechiness',
                         'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo']

    scaler = StandardScaler()
    df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

    # Ensure the 'popularity_class' column exists
    df["popularity_class"] = df['Popularity'].apply(lambda x: "Popular" if x >= 50 else "Not Popular")

    significant_features = ['Danceability', 'Energy', 'Loudness', 'Acousticness',
                            'Instrumentalness', 'Liveness', 'Valence']

    return df, significant_features, 'popularity_class'


# Train classification models and return predictions as a Pandas Series
def train_classification_models():
    df, significant_features, target = load_classification_data()

    X = df[significant_features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=29)

    models = {
        "Logistic Regression": LogisticRegression(class_weight='balanced', random_state=29),
        "SVM": SVC(class_weight='balanced', random_state=29),
        "Random Forest Classifier": RandomForestClassifier(n_estimators=400, class_weight='balanced', random_state=29)
    }

    results = {}
    predictions_dict = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X)

        results[name] = {
            "Accuracy": round(accuracy_score(y_test, model.predict(X_test)), 3),
            "Recall": round(recall_score(y_test, model.predict(X_test), pos_label="Popular"), 3),
            "Precision": round(precision_score(y_test, model.predict(X_test), pos_label="Popular"), 3)
        }

        predictions_dict[name] = pd.Series(predictions, index=df.index)  # Convert predictions to Pandas Series

    # Return classification results and predictions correctly
    return results, predictions_dict
