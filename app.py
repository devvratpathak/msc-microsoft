from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from catboost import CatBoostClassifier
from sklearn.preprocessing import LabelEncoder

# Create a Flask application
app = Flask(__name__)

# Load the data
df = pd.read_csv("he.csv")
df3 = pd.read_csv("he.csv")

# Preprocess the data
a = LabelEncoder()
df['Gender'] = a.fit_transform(df['Gender'])
df['Blood_Type'] = a.fit_transform(df['Blood Type'])
df['Test_Results'] = a.fit_transform(df['Test Results'])
df.drop(['Blood Type', 'Medication', 'Test Results'], axis=1, inplace=True)
df.drop(['Name', 'Date of Admission', 'Doctor', 'Hospital', 'Insurance Provider', 'Billing Amount',
         'Room Number', 'Admission Type', 'Discharge Date'], axis=1, inplace=True)

target = df3['Medical Condition']
X = df.drop(['Medical Condition'], axis=1)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, target, test_size=0.2, random_state=42)

# Create classifiers
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
catboost_classifier = CatBoostClassifier(iterations=100, learning_rate=0.1, verbose=False)

# Train the classifiers
rf_classifier.fit(X_train, y_train)
catboost_classifier.fit(X_train, y_train)

# Create the ensemble model
ensemble_model1 = VotingClassifier(estimators=[('Random Forest', rf_classifier), ('CatBoost', catboost_classifier)], voting='soft')
ensemble_model1.fit(X_train, y_train)

# Define routes
@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/medcond", methods=['GET', 'POST'])
def medcond():
    if request.method == 'POST':
        # Get user input
        user_input = []
        column_names = ['Age', 'Gender', 'Blood_Type', 'Test_Results']
        for column in column_names:
            user_input.append(float(request.form[column]))

        input_df = pd.DataFrame([user_input], columns=column_names)
        input_values = input_df.values.reshape(1, -1)

        # Make prediction
        ensemble_model100 = ensemble_model1.predict(input_values)

        # Return the result as a string
        return f"Medical Condition: {ensemble_model100[0]}"

    # If the method is GET, render the template
    return render_template("medicalcondition.html")


if __name__ == "__main__":
    # Run the Flask application
    app.run(port=8080, debug=True)
