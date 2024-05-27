from flask import Flask, request, jsonify
from flasgger import Swagger
import mlflow.pyfunc
import pandas as pd
import pickle

# Load the model from the pickle file
def load_model_from_pickle(file_path):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Specify the path to the pickle file
model_file_path = "linear_regression_model.pkl"
loaded_model = load_model_from_pickle(model_file_path)

# Create Flask application
app = Flask(__name__)
swagger = Swagger(app)

# Define Swagger specification
@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint for predicting wine quality.
    ---
    parameters:
      - name: fixed_acidity
        in: formData
        type: number
        required: true
      - name: volatile_acidity
        in: formData
        type: number
        required: true
      - name: citric_acid
        in: formData
        type: number
        required: true
      - name: residual_sugar
        in: formData
        type: number
        required: true
      - name: chlorides
        in: formData
        type: number
        required: true
      - name: free_sulfur_dioxide
        in: formData
        type: number
        required: true
      - name: total_sulfur_dioxide
        in: formData
        type: number
        required: true
      - name: density
        in: formData
        type: number
        required: true
      - name: pH
        in: formData
        type: number
        required: true
      - name: sulphates
        in: formData
        type: number
        required: true
      - name: alcohol
        in: formData
        type: number
        required: true
    responses:
      200:
        description: OK
    """
    # Extract input features from request
    fixed_acidity = float(request.form['fixed_acidity'])
    volatile_acidity = float(request.form['volatile_acidity'])
    citric_acid = float(request.form['citric_acid'])
    residual_sugar = float(request.form['residual_sugar'])
    chlorides = float(request.form['chlorides'])
    free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
    total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
    density = float(request.form['density'])
    pH = float(request.form['pH'])
    sulphates = float(request.form['sulphates'])
    alcohol = float(request.form['alcohol'])

    # Create DataFrame with input features
    input_data = pd.DataFrame({
        'fixed_acidity': [fixed_acidity],
        'volatile_acidity': [volatile_acidity],
        'citric_acid': [citric_acid],
        'residual_sugar': [residual_sugar],
        'chlorides': [chlorides],
        'free_sulfur_dioxide': [free_sulfur_dioxide],
        'total_sulfur_dioxide': [total_sulfur_dioxide],
        'density': [density],
        'pH': [pH],
        'sulphates': [sulphates],
        'alcohol': [alcohol]
    })

    # Predict wine quality using the loaded model
    predicted_quality = loaded_model.predict(input_data)

    # Return the predicted quality as JSON response
    return jsonify({'predicted_quality': predicted_quality[0]})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Run Flask on port 5001
