# Gender Prediction AI

An interactive Streamlit application that predicts a gender label from selected preference categories such as favorite color, music genre, beverage, and soft drink. The repository also includes a separate script for training and saving a scikit-learn Logistic Regression model.

> **Project scope:** This is an educational/demo machine-learning project. Its output is a model prediction based on the selected categories, not a reliable way to determine a person's gender. Preferences do not establish or prove gender.

## Features

- Interactive dashboard built with Streamlit.
- Four categorical inputs:
  - Favorite Color
  - Favorite Music Genre
  - Favorite Beverage
  - Favorite Soft Drink
- Prediction output displayed in a styled result card.
- Separate training script using a scikit-learn pipeline with one-hot encoding and Logistic Regression.
- Serialized model artifact included in the repository (`gender_model.pkl`).

## Tech Stack

- **Python**
- **Streamlit** — interactive web interface
- **pandas** — dataset loading and tabular data handling in the training script
- **scikit-learn** — categorical preprocessing and Logistic Regression
- **joblib** — model serialization in the training script

## Repository Structure

```text
gender_pred/
├── app.py              # Streamlit dashboard and prediction logic
├── train.py            # Trains and saves a Logistic Regression pipeline
├── gender_model.pkl    # Serialized scikit-learn Logistic Regression artifact
└── requirements.txt    # Current application dependency declaration
```

## How It Works

### 1. Interactive application

Run `app.py` to open the Streamlit dashboard. The user selects one option from each of the four preference categories and clicks **Predict Gender**.

The current application code calculates a score by adding:
- A fixed intercept
- A coefficient associated with the selected color
- A coefficient associated with the selected music genre
- A coefficient associated with the selected beverage
- A coefficient associated with the selected soft drink

It then applies the sigmoid function to the score and assigns the label `M` when the resulting value is at least `0.5`, otherwise `F`.

**Implementation note:** `app.py` currently uses coefficients hard-coded in the application. It does not load or call `gender_model.pkl`. Therefore, the live dashboard prediction path is separate from the serialized model-training path described below.

### 2. Model training script

`train.py`:
1. Reads a CSV file named `Transformed Data Set - Sheet1.csv`.
2. Uses the `Gender` column as the target and the remaining columns as input features.
3. Applies `OneHotEncoder(handle_unknown="ignore")` to the four preference columns.
4. Fits a scikit-learn `LogisticRegression` classifier inside a `Pipeline`.
5. Saves the fitted pipeline as `model_pipeline.pkl`.

The CSV file expected by the script is **not included in the uploaded repository archive**. You will need to provide that dataset in the project directory before running the training script.

The included `gender_model.pkl` is a separate serialized Logistic Regression estimator. Its recorded feature names include the four preference columns and `Male_Count` and `Female_Count`. The current training script saves to `model_pipeline.pkl`, so it does not overwrite `gender_model.pkl`.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/kunj1674/Ml_Projects.git
cd Ml_Projects/gender_pred
```

### 2. Create and activate a virtual environment (recommended)

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

The current `requirements.txt` contains only Streamlit. The training script also imports pandas, scikit-learn, and joblib. Install all dependencies with:

```bash
pip install streamlit pandas scikit-learn joblib
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to use the dashboard.

## Training the model

To run the training script, place the expected dataset file in the same directory as `train.py`:

```text
Transformed Data Set - Sheet1.csv
```

Then install the training dependencies and run:

```bash
python train.py
```

On successful execution, the script writes:

```text
model_pipeline.pkl
```

The training script currently does not split the data into training and test sets or report evaluation metrics. No accuracy, precision, recall, F1-score, or test-set performance is therefore claimed in this README.

## Current Implementation Notes

- The Streamlit interface uses manually embedded coefficients rather than loading the serialized model.
- The training script expects a CSV dataset that is not present in this repository snapshot.
- `requirements.txt` currently lists only `streamlit`; pandas, scikit-learn, and joblib are additionally needed to execute `train.py`.
- The repository contains both `gender_model.pkl` and code that writes `model_pipeline.pkl`; these are distinct files/artifacts.

These details are documented transparently so that the setup and current behavior are clear. A future improvement would be to connect the dashboard to one consistently trained and evaluated pipeline, add a held-out test set and meaningful metrics, and update the dependency file.

## Disclaimer

This project demonstrates a simple classification workflow for learning purposes. Gender is a personal identity and cannot be reliably inferred from favorite colors, music, beverages, or other preferences. Predictions should not be used for decisions about real people.

## Author

**Kunj Gupta**

- GitHub: [kunj1674](https://github.com/kunj1674)
- LinkedIn: [Kunj Gupta](https://www.linkedin.com/in/kunj-gupta-633251296)
