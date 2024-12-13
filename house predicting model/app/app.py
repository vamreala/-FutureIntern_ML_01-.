from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model_path = 'app/model/house_price_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        square_feet = float(request.form['square_feet'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        garage = int(request.form['garage'])

        # Prepare input for prediction
        input_features = np.array([[square_feet, bedrooms, bathrooms, garage]])
        prediction = model.predict(input_features)[0]

        return jsonify({'prediction': f"The estimated price is ${prediction:,.2f}"})
    except Exception as e:
        return jsonify({'error': f"Error during prediction: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
