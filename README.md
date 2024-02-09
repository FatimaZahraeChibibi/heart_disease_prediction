# Heart Disease Prediction

## Overview

This project aims to predict the likelihood of heart disease in patients using machine learning algorithms. It involves collecting and preprocessing data related to various medical attributes, training multiple machine learning models, and building a web application for users to interactively predict heart disease risk.

## Project Components

1. **Data Collection and Preprocessing:**
   - Utilized the Cleveland Heart Disease dataset containing various medical attributes.
   - Preprocessed the data by handling missing values, encoding categorical variables, and scaling numerical features.

2. **Model Training and Evaluation:**
   - Trained and evaluated multiple machine learning algorithms, including Logistic Regression, Decision Trees, Random Forest, and Support Vector Machines (SVM).
   - Used metrics such as accuracy, precision, recall, F1-score, and ROC AUC to evaluate model performance.

3. **Flask Web Application:**
   - Developed a user-friendly web application using Flask framework.
   - Implemented HTML/CSS components for the user interface, allowing users to input medical data and receive predictions regarding heart disease risk.

## Usage

To use the heart disease prediction web application:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the Flask application using `python app.py`.
5. Access the application through a web browser by visiting `http://localhost:5000`.

## File Structure

- `app.py`: Main Flask application file containing route definitions and model prediction logic.
- `templates/`: Directory containing HTML templates for the web application.
- `static/`: Directory containing static files such as CSS stylesheets and JavaScript files.
- `heart_disease_prediction.ipynb`: Jupyter Notebook containing the data preprocessing, model training, and evaluation steps.

## Technologies Used

- Python
- Flask
- scikit-learn
- HTML
- CSS
