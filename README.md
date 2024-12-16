# Algerian Forest Fire Predictor

## Project Overview
This project predicts the **Forest Weather Index (FWI)** for Algerian forest fire data. The FWI is a numeric value that indicates the severity and spread potential of forest fires based on environmental parameters such as temperature, humidity, wind speed, and more. 

The model achieves an **R² score of 0.9842** after extensive experimentation with various regression techniques, providing highly accurate predictions.

---
## Features
- **Input Parameters:**
  - **Temperature**: Air temperature in Celsius.
  - **RH**: Relative Humidity in percentage.
  - **Ws**: Wind speed in km/h.
  - **Rain**: Rainfall in mm.
  - **FFMC**: Fine Fuel Moisture Code.
  - **DMC**: Duff Moisture Code.
  - **ISI**: Initial Spread Index.
  - **Classes**: Fire severity class.
  - **Region**: Location-based forest fire region.
- **Output**: Predicted **FWI** (Forest Weather Index).
- **Model Used**: Linear Regression ( Ridge , Lasso, ElasticNet).
- **Data Preprocessing**: StandardScaler is used to scale input features for model training and prediction.

---
## Model Performance
- **R² Score**: 0.9842
- **Techniques Tried**: Various linear regression models, including Ridge , Lasso , ElasticNet regression, were applied to optimize prediction accuracy.

---
## Tech Stack
- **Backend**: Python (Flask Framework)
- **Machine Learning**: Scikit-Learn
- **Frontend**: HTML, CSS
- **Model Storage**: Pickle file (.pkl)

---
## Installation Guide
Follow these steps to set up the project:

### 1. Clone the Repository
```bash
git clone https://github.com/Suman991/Fire-predictor.git
cd Fire-predictor
```

### 2. Install Dependencies
Make sure Python is installed. Install required libraries:
```bash
pip install -r requirements.txt
```
*Requirements include Flask, scikit-learn, and numpy.*

### 3. Run the Flask Application
Start the application server:
```bash
python app.py
```
The application will run on `http://127.0.0.1:5500/`.

---
## File Structure
```
project-root/
├── templates/
│   └── index.html          # Frontend UI (form and results)
├── model/
│   ├── ridge.pkl     # Trained regression model
│   └── scaler.pkl          # StandardScaler for input features
├── app.py                  # Flask backend logic
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---
## How to Use
1. Open the application in your browser at `http://127.0.0.1:5500/`.
2. Enter the following input parameters:
   - Temperature, RH, Wind Speed, Rain, FFMC, DMC, ISI, Classes, and Region.
3. Submit the form to get the predicted **FWI** value.

---
## Model and Preprocessing
- **Model**: Ridge Regression (trained using Scikit-learn).
- **Scaler**: `StandardScaler` is used for feature scaling to improve model performance.
- **Serialization**: The trained model and scaler are saved using the `pickle` module.

---
## Example Prediction
**Inputs:**
- Temperature: 28°C  
- RH: 58%  
- Ws: 18 km/h  
- Rain: 2.2 mm  
- FFMC: 63.7  
- DMC: 3.2  
- ISI: 1.2  
- Classes: 0  
- Region: 1

**Output:**
- **FWI**: 0.5

---
## Future Enhancements
- Improve the UI for better user experience.
- Implement additional ML models for comparison.
  

---
## Author
[Suman Moni]  
Contact: [sumanmoni27@gmail.com]  
GitHub: [https://github.com/Suman991](https://github.com/Suman991)

---
## License
This project is licensed under the MIT License.
