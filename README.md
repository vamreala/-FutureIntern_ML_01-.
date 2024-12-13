# -FutureIntern_ML_01-.

# House Price Prediction Web Application

## Overview
This web application predicts house prices based on user input for features such as square feet, number of bedrooms, bathrooms, and garages. The project utilizes a machine learning model to generate predictions and offers a sleek, modern user interface.

---

## Features
1. **Machine Learning Model**: Trained and saved using Python's `scikit-learn` library.
2. **Web Framework**: Built using Flask for a lightweight backend.
3. **Modern UI/UX**: Responsive, interactive, and visually appealing interface using Glassmorphism design principles.
4. **Live Predictions**: User inputs are processed and predictions are displayed instantly.

---

## Folder Structure
```
House Pricing Prediction/
├── app/
│   ├── app.py                 # Flask backend script
│   ├── model/
│   │   └── house_price_model.pkl  # Pre-trained machine learning model
│   ├── templates/
│   │   └── index.html         # Frontend HTML template
│   ├── static/
│   │   ├── styles.css         # Modern UI styling
│   │   ├── animations.js      # Optional animations (if needed)
```

---

## Requirements

### Python Libraries
- Flask
- scikit-learn
- numpy
- pandas

### Additional Tools
- Modern browser (Chrome, Firefox, etc.)

---

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-repo/house-price-prediction.git
cd house-price-prediction/app
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```
Ensure Python 3.7+ is installed.

### Step 3: Start the Flask Application
```bash
python app.py
```
Access the app at `http://127.0.0.1:5000/` in your browser.

---

## Usage
1. Enter the following details:
   - **Square Feet**: Total area of the house.
   - **Bedrooms**: Number of bedrooms.
   - **Bathrooms**: Number of bathrooms.
   - **Garage**: Number of garages.
2. Click the **Predict** button.
3. The predicted house price will be displayed dynamically.

---

## Model Details
- The model is trained on a dataset using the `LinearRegression` algorithm from `scikit-learn`.
- Saved in the `model/house_price_model.pkl` file for easy deployment.

---

## Credits
- **Frontend Design**: Responsive and modern design using custom CSS.
- **Machine Learning**: Pre-trained model created using Python.
- **Backend Development**: Flask framework for serving predictions.

---

## Future Improvements
- Add support for additional features like location and year built.
- Include data visualization for better insights.
- Improve prediction accuracy by training with a larger dataset.
- Add user authentication and history tracking.

---

## License
This project is licensed under the MIT License. Feel free to use and modify as needed.
