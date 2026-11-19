import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

def train_and_save_model():
    print("Loading dataset...")
    # Load the specific dataset file 
    df = pd.read_csv("Transformed Data Set - Sheet1.csv")

    X = df.drop("Gender", axis=1)
    y = df["Gender"]

    categorical_features = ['Favorite Color', 'Favorite Music Genre', 'Favorite Beverage', 'Favorite Soft Drink']

    # Encode categorical text into numerical data for Logistic Regression
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])

    # Build the model pipeline
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(random_state=42, max_iter=1000))
    ])

    print("Training the Logistic Regression model...")
    model_pipeline.fit(X, y)
    
    model_filename = "model_pipeline.pkl"
    joblib.dump(model_pipeline, model_filename)
    print(f"Model saved successfully as '{model_filename}'.")

if __name__ == "__main__":
    train_and_save_model()