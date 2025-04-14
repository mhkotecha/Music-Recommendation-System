# Music Recommendation System

This repository contains the implementation of a **Music Recommendation System** that predicts **song popularity** and generates **personalized recommendations** based on user preferences. The system leverages **machine learning models** and **audio feature analysis** to enhance the music streaming experience.

## Project Overview

With the rapid growth of music streaming platforms, **personalized recommendations** have become essential for user engagement. This project provides a **data-driven approach** to music recommendations by:

- **Extracting song data** from user playlists using the **Spotify API**.
- **Predicting song popularity** using **Regression models**.
- **Classifying songs** as "Popular" or "Not Popular" using **Classification models**.
- **Generating personalized song recommendations** using **Cosine Similarity-based filtering**.

**Dataset Limitations:**  
This dataset was **manually collected** by asking users to provide their **Spotify user IDs**. Due to **limited data availability** and necessary preprocessing (removing duplicates and incomplete entries), **model accuracy and similarity scores are relatively low**. Expanding the dataset will significantly improve performance.

## Key Features

- **Spotify API Integration**: Extracts **song metadata** and **audio features** from user playlists.
- **Machine Learning for Popularity Prediction**: Uses **multiple regression models** to estimate song popularity.
- **Automated Song Classification**: Categorizes tracks as **"Popular" or "Not Popular"** using **classification models**.
- **Content-Based Recommendation System**: Recommends songs **based on feature similarity** to the user's playlist.
- **Interactive User Experience**: Allows users to **choose ML models** and **filter recommendations**.

## Methodology

### **1. Data Collection & Preprocessing**
- Extracted **5,333 songs** from **Spotify user playlists** using the `spotipy` library.
- Retrieved **audio features**, **metadata**, and **popularity scores**.
- **Removed duplicates and incomplete data** for better model accuracy.
- Standardized **numerical features** using `StandardScaler`.

### **2. Machine Learning Models**

#### **Regression (Song Popularity Prediction)**
- **Goal:** Predicts a song’s **popularity score** based on audio features.
- **Models Implemented**:
  - **Linear Regression**
  - **Ridge Regression**
  - **Polynomial Linear Regression**
  - **Polynomial Ridge Regression**
  - **Random Forest Regressor** (Best Model)
- **Feature Selection**: Used **Ordinary Least Squares (OLS) Analysis** to find the most important attributes.
- **User Interaction**: Allows users to **select the regression model**.

#### **Classification (Popularity Categorization)**
- **Goal:** Classifies a song as **"Popular" or "Not Popular"**.
- **Models Implemented**:
  - **Logistic Regression**
  - **Support Vector Machine (SVM)**
  - **Random Forest Classifier** (Best Model)
- **User Interaction**: Users can **choose their classification model**.
  
#### **Recommendation System (Content-Based Filtering)**
- **Goal:** Recommends songs **based on feature similarity** to a user’s playlist.
- **Technique Used:** **Cosine Similarity**
- **Ranking Factors**:
  - **Audio Feature Similarity**
  - **Predicted Popularity (from regression model)**
  - **User’s "Popular Songs" Preference (from classification model)**

### **3. Evaluation Metrics**
- **Regression Models:** Evaluated using **R² score**.
- **Classification Models:** Evaluated using **Accuracy, Recall, and Precision**.
- **Recommendation System:** Evaluated using **Cosine Similarity Scores**.

## Interactive System Usage

The system allows users to **choose models** for regression and classification and then receive **personalized song recommendations**.

### **1. Choose a Regression Model**
Users can **select a regression model** to predict song popularity:

Which Regression Model would you like to use?

Linear Regression, 
Ridge Regression, 
Polynomial Linear Regression, 
Polynomial Ridge Regression, 
Random Forest Regressor (Best Model).


If a user selects a **non-optimal model**, they receive a **warning message** and can **reselect** or proceed.

### **2. Choose a Classification Model**
Users can **select a classification model** to categorize songs:

Which Classification Model would you like to use?

Logistic Regression, 
Support Vector Machine (SVM), 
Random Forest Classifier (Best Model).


Similarly, if a **suboptimal classifier is chosen**, the system **warns the user** and allows reselection.

### **3. Choose a Recommendation Type**
Users can filter recommendations to **only show popular songs**:

Would you like to filter recommendations to show only 'Popular' songs?

Yes, only recommend popular songs
No, recommend all songs


### **4. Generate Personalized Recommendations**
Once model selections are complete, the system generates **song recommendations** based on **user-selected models** and **playlist similarity**.

## Results

### **Regression Model Performance**
| Model                  | R² Score |
|------------------------|----------|
| Linear Regression      | 0.062    |
| Ridge Regression       | 0.062    |
| Polynomial Regression  | 0.101    |
| Random Forest Regressor| 0.269    |

### **Classification Model Performance**
| Model                  | Accuracy | Recall | Precision |
|------------------------|----------|--------|-----------|
| Logistic Regression    | 0.604    | 0.780  | 0.592     |
| SVM                    | 0.630    | 0.778  | 0.616     |
| Random Forest Classifier| 0.671   | 0.762  | 0.661     |

## Future Enhancements

- **Expand Dataset**: Increase song diversity by collecting more user playlists.
- **Hybrid Recommendation System**: Incorporate **collaborative filtering** with content-based filtering.
- **Real-Time Predictions**: Implement live playlist updates with **streaming data**.
- **Scalability**: Optimize for **larger user bases and high-volume requests**.

## Conclusion

This **Music Recommendation System** successfully:
- **Predicts song popularity** using **Regression Models**.
- **Classifies songs** as "Popular" or "Not Popular".
- **Generates personalized recommendations** using **Cosine Similarity**.




