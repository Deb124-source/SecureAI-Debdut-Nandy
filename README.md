# SecurePass AI - ML Powered Password Strength Analyzer

SecurePass AI is a machine learning based password security analyzer that evaluates password strength, identifies security risks, calculates entropy, and generates stronger password recommendations.

The application uses an XGBoost classification model trained on password patterns and complexity features to classify passwords into:

- Weak
- Medium
- Strong


## Live Demo

Streamlit Application:

https://secureai-debdut-nandy.streamlit.app/


## Project Overview

Weak passwords are one of the most common reasons behind account security breaches. SecurePass AI provides an intelligent way to analyze password complexity and guide users toward creating stronger credentials.

The system extracts important password characteristics such as:

- Password length
- Uppercase character count
- Lowercase character count
- Digit count
- Special character count
- Unique character count
- Character diversity

These features are used by a machine learning model to predict password strength.


## Machine Learning Workflow

The project follows an end-to-end ML pipeline:

1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Model Deployment


## Dataset

The model was trained using a password strength dataset containing:

- Password samples
- Strength labels

Target Classes:

| Label | Meaning |
|------|---------|
| 0 | Weak |
| 1 | Medium |
| 2 | Strong |


## Feature Engineering

The following features are generated from each password:

| Feature | Description |
|---------|-------------|
| Length | Total password characters |
| Uppercase | Number of uppercase letters |
| Lowercase | Number of lowercase letters |
| Digits | Number of numeric characters |
| Symbols | Special character count |
| Unique Characters | Number of different characters |
| Spaces | Presence of spaces |
| Has Uppercase | Binary feature |
| Has Digit | Binary feature |
| Has Symbol | Binary feature |


## Model Used

Algorithm:

XGBoost Classifier


Why XGBoost?

- High classification performance
- Handles structured features efficiently
- Fast prediction
- Suitable for deployment


## Application Features

### Password Strength Prediction

The model predicts:

- Weak Password
- Medium Password
- Strong Password


### Password Entropy Calculation

The application estimates password randomness using entropy calculation.


### Security Recommendations

The system provides suggestions such as:

- Increase password length
- Add uppercase characters
- Add numbers
- Add special characters


### Strong Password Generator

Users can generate secure random passwords directly from the application.


## Tech Stack

Programming Language:

- Python


Machine Learning:

- XGBoost
- Scikit-learn


Data Processing:

- Pandas
- NumPy


Deployment:

- Streamlit


Model Serialization:

- Joblib


## Project Structure

```

SecurePass_AI/

│
├── app.py
│
├── SecurePass_AI.pkl
│
├── requirements.txt
│
└── README.md

````


## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/SecurePass_AI.git
````

Navigate to the project folder:

```bash
cd SecurePass_AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Model Evaluation

The model was evaluated using:

* Accuracy Score
* Classification Report
* Confusion Matrix

Evaluation metrics help measure how accurately the model identifies weak, medium, and strong passwords.

## Future Improvements

* Add password leak detection using breach databases
* Add real-time security scoring
* Add explainable AI feature importance
* Integrate enterprise password policy checking
* Add browser extension support

## Author

Debdut Nandy

Machine Learning | Data Analytics | AI Projects

## License

This project is for educational and portfolio purposes.
