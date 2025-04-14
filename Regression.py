import pandas as pd
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.ensemble import RandomForestRegressor

# Load and preprocess data
def load_regression_data():
    df = pd.read_excel('Datasets/Final Songs.xlsx')
    df.dropna(inplace=True)

    features_to_scale = ['Danceability', 'Energy', 'Loudness', 'Speechiness', 'Acousticness',
                         'Instrumentalness', 'Liveness', 'Valence', 'Tempo']

    scaler = StandardScaler()
    features_scaled_df = pd.DataFrame(scaler.fit_transform(df[features_to_scale]),
                                      columns=features_to_scale, index=df.index)
    df[features_to_scale] = features_scaled_df

    all_features = features_to_scale + ['Mode', 'Key']
    target = 'Popularity'

    return df, all_features, target

# Train regression models and return predictions
def train_regression_models(model_choice):
    df, all_features, target = load_regression_data()

    X_temp = sm.add_constant(df[all_features])
    y = df[target]

    # Feature selection using OLS
    ols_model = sm.OLS(y, X_temp).fit()
    significant_features = ols_model.pvalues[ols_model.pvalues < 0.05].index.tolist()

    if 'const' in significant_features:
        significant_features.remove('const')

    X = df[significant_features]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.12, random_state=29)

    models = {
        1: LinearRegression(),
        2: Ridge(alpha=1.0),
        3: PolynomialFeatures(degree=2, include_bias=False),  # Polynomial Linear Regression
        4: PolynomialFeatures(degree=2, include_bias=False),  # Polynomial Ridge Regression
        5: RandomForestRegressor(n_estimators=400, random_state=29)
    }

    if model_choice not in models:
        raise ValueError("Invalid model choice!")

    # Polynomial Regression Models
    if model_choice in [3, 4]:
        poly = models[model_choice]
        X_train_poly = poly.fit_transform(X_train)
        X_test_poly = poly.transform(X_test)

        if model_choice == 3:
            model = LinearRegression()
        else:
            model = Ridge(alpha=1.0)

        model.fit(X_train_poly, y_train)
        predictions = model.predict(X_test_poly).astype(int)
        predicted_popularity = model.predict(poly.transform(X))

    else:
        model = models[model_choice]
        model.fit(X_train, y_train)
        predictions = model.predict(X_test).astype(int)
        predicted_popularity = model.predict(X)

    r2 = r2_score(y_test, predictions)

    return round(r2, 3), predicted_popularity
