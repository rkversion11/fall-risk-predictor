# 🏥 Fall Risk Prediction App
### Based on LASI Wave 1 Data (2017-18)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.55-red)
![XGBoost](https://img.shields.io/badge/XGBoost-88.3%25-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📌 Overview
This app predicts the **fall risk** of elderly individuals (aged 45+) 
as **Low, Medium, or High** using biomarker data from the 
Longitudinal Ageing Study in India (LASI) Wave 1.

## 🌐 Live App
👉 [Click here to open the app](https://rkversion11-fall-risk-predictor-fall-risk-app.streamlit.app)

---

## 📊 Dataset
| Detail | Value |
|--------|-------|
| Source | LASI Wave 1, 2017-18 |
| Conducted by | IIPS Mumbai + Harvard + USC |
| Total individuals | 73,396 |
| Age group | 45 years and above |
| Coverage | All Indian states and UTs |
| Data format | STATA (.dta) |

---

## 🔬 Features Used
| Variable | Description | Clinical Relevance |
|----------|-------------|-------------------|
| bm028 | Grip strength reading 1 (kg) | Weak grip = fall risk |
| bm029 | Grip strength reading 2 (kg) | Weak grip = fall risk |
| bm030 | Grip strength reading 3 (kg) | Weak grip = fall risk |
| bmi | Body Mass Index | Underweight/Obese = fall risk |
| height | Height in metres | Anthropometric measure |
| highsyst | High systolic blood pressure | BP instability = fall risk |
| highdiast | High diastolic blood pressure | BP instability = fall risk |
| hyper | Hypertension (Yes/No) | Strongest predictor |
| bm060a | Right eye vision | Poor vision = fall risk |
| bm060b | Left eye vision | Poor vision = fall risk |

---

## 🎯 Target Variable
Fall risk is classified into 3 categories based on a 
composite clinical score:

| Class | Label | Risk Factors |
|-------|-------|-------------|
| 0 | 🟢 Low Risk | Score 0-1 |
| 1 | 🟡 Medium Risk | Score 2 |
| 2 | 🔴 High Risk | Score 3-5 |

The risk score is computed from:
- Weak grip strength (< 16 kg)
- Poor balance test performance
- Abnormal BMI (< 18.5 or > 27.5)
- Hypertension
- Poor vision

---

## 🤖 Models Trained
| Model | Accuracy | Notes |
|-------|----------|-------|
| Logistic Regression | 64.1% | Baseline model |
| Random Forest | 88.0% | Strong performance |
| **XGBoost** | **88.3%** | **Best model** ✅ |

---

## 📈 Model Performance (XGBoost)
| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| Low Risk | 0.98 | 0.85 | 0.92 |
| Medium Risk | 0.83 | 0.89 | 0.86 |
| High Risk | 0.81 | 0.94 | 0.87 |
| **Overall** | | | **88.3%** |

---

## 🏗️ Project Structure
```
fall-risk-predictor/
│
├── fall_risk_app.py              # Streamlit web app
├── fall_risk_xgboost_model.pkl   # Trained XGBoost model
├── fall_risk_scaler.pkl          # StandardScaler
├── fall_risk_imputer.pkl         # SimpleImputer
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 🚀 Run Locally
1. Clone the repository:
```bash
git clone https://github.com/rkversion11/fall-risk-predictor.git
cd fall-risk-predictor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run fall_risk_app.py
```

---

## 📦 Dependencies
```
streamlit
pandas
numpy
scikit-learn
xgboost
joblib
pyreadstat
imbalanced-learn
```

---

## 🔍 How It Works
1. User enters patient biomarker values
2. App feeds data into trained XGBoost model
3. Model predicts fall risk class
4. App displays result with probability breakdown

---

## ⚠️ Disclaimer
This tool is built for **research purposes only** and should 
not be used as a substitute for professional medical advice. 
Always consult a qualified healthcare provider for medical decisions.

---

## 👨‍💻 Author
- **Name:** Jaikar
- **Data:** LASI Wave 1 (IIPS Mumbai)
- **Tools:** Python, Streamlit, XGBoost, Scikit-learn

---

## 📚 References
- International Institute for Population Sciences (IIPS) (2020). 
  Longitudinal Ageing Study in India (LASI) Wave 1, 2017-18, 
  India Report, IIPS, Mumbai.
- LASI Website: https://www.iipsindia.ac.in/lasi
