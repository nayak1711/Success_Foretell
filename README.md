# Success Foretell 🎯

Success Foretell is a predictive web application built using **Flask** that forecasts the likelihood of business success based on city, type of business, and area. It uses a trained machine learning model (Linear Regression with polynomial features) to make predictions.

---

## 🚀 Features

- Secure login (hardcoded email + password hash)
- Dropdown forms for:
  - Business City (Bhopal, Indore)
  - Type of Business
  - Business Area (dynamically filtered based on city)
- ML-based success prediction (as a percentage)
- Clear result display

---

## 🧪 Tech Stack

- Python 3.10+
- Flask
- scikit-learn
- joblib
- HTML/CSS (with Tailwind styling)
- JavaScript (dynamic dropdowns)

---

## 📁 Project Structure

SUCCESS_FORETELL/
├── app.py
├── rating_poly_model.joblib
├── poly_converter.joblib
├── templates/
│   ├── login.html
│   ├── home.html
│   ├── prediction.html
│   └── result.html
└── static/         # (if exists)


---

## ⚙️ Setup Instructions (with Virtual Environment)

> ❗ Don't use the `venv/` from the ZIP — create your own clean environment.

1. **Open PowerShell (as Administrator)**  
2. **Navigate to your project folder:**
   ```powershell
   cd "C:\Users\hp\Desktop\Project2\SUCCESS_FORETELL"
3. Create a virtual environment:
   python -m venv venv
4. Enable script execution (only if needed):
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
5. Activate the virtual environment:
   venv\Scripts\activate

## ⚙️ Return to terminal on VScode and Install required libraries:
  - pip install flask scikit-learn joblib
 Run the app:
  - python app.py
    
## 🔐 Login Credentials
Use the following to access the prediction page:

Email: successfortell@gmail.com

Password: launch2025

## 🧠 Model Info
Model Type: Linear Regression with Polynomial Features
Framework Used: Scikit-learn v1.3.0
Model Files:
  - rating_poly_model.joblib  (The trained regression model)
  -poly_converter.joblib  (The polynomial feature transformer)
These files are saved using joblib, which is recommended for scikit-learn models because it's faster and more efficient for objects with large NumPy arrays.

## 💡 Future Improvements
-Replace hardcoded login with database authentication
-Add user registration
-Connect model training pipeline
-Deploy on Heroku, Render, or Railway

## 🧑‍💻 Author
 Suman Kumar Nayak

 
