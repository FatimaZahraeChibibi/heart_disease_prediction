from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load the trained model
model_path = 'C:/Users/fatim/heart_disease_prediction/best_model.pkl'
if os.path.exists(model_path):
    model = joblib.load(model_path)
    print("Model loaded successfully.")
else:
    print(f"No model found at '{model_path}'")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extracting features from the form
            sex = float(request.form['sex'])
            age = float(request.form['age'])
            cp = float(request.form['cp'])
            trestbps = float(request.form['trestbps'])
            chol = float(request.form['chol'])
            fbs = float(request.form['fbs'])
            restecg = float(request.form['restecg'])
            thalach = float(request.form['thalach'])
            exang = float(request.form['exang'])
            oldpeak = float(request.form['oldpeak'])
            slope = float(request.form['slope'])
            ca = float(request.form['ca'])
            thal = float(request.form['thal'])

            # Making prediction
            prediction = model.predict([[sex, age, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            
            # Returning the result
            return render_template('result.html', prediction=prediction[0])
        except Exception as e:
            print(f"Error during prediction: {e}")
            return render_template('result.html', prediction="Error during prediction")

if __name__ == '__main__':
    app.run(debug=True)
