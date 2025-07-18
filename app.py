from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from joblib import load
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Hardcoded login credentials
VALID_EMAIL = "successfortell@gmail.com"
HASHED_PASSWORD = generate_password_hash("launch2025")

# Load ML model and polynomial converter
model = load("rating_poly_model.joblib")
poly = load("poly_converter.joblib")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == VALID_EMAIL and check_password_hash(HASHED_PASSWORD, password):
            return redirect(url_for('prediction_page'))
        else:
            flash('Invalid email or password')
            return redirect(url_for('login'))

    return render_template('login.html')

# Prediction input page
@app.route('/prediction')
def prediction_page():
    return render_template('prediction.html')  # Form to input location, area, tob

# Prediction processing route
@app.route('/predict', methods=['POST'], endpoint='prediction')
def predict():
    try:
        location = int(request.form['location'])
        area = int(request.form['area'])
        tob = int(request.form['tob'])

        input_data = [[location, tob, area]]
        transformed_data = poly.transform(input_data)
        prediction = model.predict(transformed_data)[0]
        percentage = round((prediction / 5) * 100, 2)

        return render_template('result.html', percentage=percentage)
    except Exception as e:
        flash(f"Error in prediction: {str(e)}")
        return redirect(url_for('prediction_page'))

# Home route
@app.route('/home')
def home():
    return render_template('home.html')

# Logout route
@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
