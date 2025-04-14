import sys
from Regression import train_regression_models
from Classification import train_classification_models
from Recommendation import load_recommendation_data, recommend_songs


# Function for user to select regression model
def choose_regressor():
    print("\nHi! I am your Music Recommender System. Before proceeding with recommendations, I will guide you through some options to get relevant predictions.\n")

    while True:
        print("\nWhich Regression Model would you like to use?")
        print("1. Linear Regression")
        print("2. Ridge Regression")
        print("3. Polynomial Linear Regression")
        print("4. Polynomial Ridge Regression")
        print("5. Random Forest Regressor (Best Model)")

        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice not in [1, 2, 3, 4, 5]:
                print("\nInvalid choice! Please enter a number between 1 and 5.\n")
                continue

            # If user selects anything other than Random Forest Regressor (5), show disclaimer
            if choice in [1, 2, 3, 4]:
                print("\nThe model you selected is not the best regressor (Random Forest had the highest performance).")
                print("Do you wish to continue or choose another?")
                print("1. Yes, continue with my choice")
                print("2. No, let me choose again")

                sub_choice = int(input("Enter your choice (1-2): "))
                if sub_choice == 2:
                    continue  # Restart the selection process

            print("\nYou have selected a regression model. Training now...\n")
            return choice  # Return selected model

        except ValueError:
            print("\nInvalid input! Please enter a valid number.\n")


# Function for user to select classification model
def choose_classifier():
    print("\nWhich Classification Model would you like to use?")
    print("1. Logistic Regression")
    print("2. Support Vector Machine (SVM)")
    print("3. Random Forest Classifier (Best Model)")

    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice not in [1, 2, 3]:
                print("\nInvalid choice! Please enter a number between 1 and 3.\n")
                continue

            # If user selects anything other than Random Forest Classifier (3), show disclaimer
            if choice in [1, 2]:
                print("\nThe model you selected is not the best classifier (Random Forest had the highest performance).")
                print("Do you wish to continue or choose another?")
                print("1. Yes, continue with my choice")
                print("2. No, let me choose again")

                sub_choice = int(input("Enter your choice (1-2): "))
                if sub_choice == 2:
                    continue  # Restart the selection process

            print("\nYou have selected a classification model. Training now...\n")
            return choice  # Return selected model

        except ValueError:
            print("\nInvalid input! Please enter a valid number.\n")


# Function to run regression model and return predictions
def run_regression():
    regressor_choice = choose_regressor()
    r2_score, predicted_popularity = train_regression_models(regressor_choice)
    print(f"\nRegression Model Trained! R² Score: {r2_score}\n")
    return predicted_popularity, regressor_choice


# Function to run classification model and return predictions
def run_classification():
    classifier_choice = choose_classifier()
    classification_results, classification_predictions = train_classification_models()

    # Extract predictions for the chosen model
    selected_model = (
        "Logistic Regression" if classifier_choice == 1 else
        "SVM" if classifier_choice == 2 else
        "Random Forest Classifier"
    )

    if selected_model not in classification_predictions:
        raise ValueError(f"Error: '{selected_model}' not found in classification predictions!")

    selected_predictions = classification_predictions[selected_model]  # Get predictions as Pandas Series

    # Display performance metrics of the selected classifier
    metrics = classification_results[selected_model]
    print(f"\n {selected_model} Model Trained!")
    print(f"   - Accuracy: {metrics['Accuracy']}")
    print(f"   - Recall: {metrics['Recall']}")
    print(f"   - Precision: {metrics['Precision']}")

    return selected_predictions, classifier_choice




# Function to run recommendation system with user options
def run_recommendation(predicted_popularity, classification_predictions, regressor_choice, classifier_choice):
    df, features = load_recommendation_data()
    user_id = input("\nEnter your Spotify User ID: ")

    print("\nWould you like to filter recommendations to show only 'Popular' songs?")
    print("1. Yes, only recommend popular songs")
    print("2. No, recommend all songs")

    try:
        filter_choice = int(input("Enter your choice (1-2): "))
        filter_popular = True if filter_choice == 1 else False

        num_recommendations = int(input("\nHow many recommendations would you like? (Default: 5): ") or 5)

        print("\nGenerating song recommendations...")
        recommended_songs = recommend_songs(user_id, df, features, predicted_popularity, classification_predictions,
                                            num_recommendations, filter_popular)

        if recommended_songs.empty:
            print("\nNo recommendations found. Please check your user ID or try again.")
        else:
            print("\n**Your Personalized Song Recommendations:**")
            print(recommended_songs[['Song Name', 'Artist(s)', 'Similarity Score']].to_string(index=False))

    except ValueError:
        print("\nInvalid input! Please enter a valid number.")


# Main function to run the interactive system
def main():
    predicted_popularity, regressor_choice = run_regression()
    classification_predictions, classifier_choice = run_classification()
    run_recommendation(predicted_popularity, classification_predictions, regressor_choice, classifier_choice)

    print("\nThank you for using the Music Recommender System! Enjoy your personalized recommendations.")


# Run the interactive system
if __name__ == "__main__":
    main()