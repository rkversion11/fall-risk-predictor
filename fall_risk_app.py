
import streamlit as st
import joblib
import pandas as pd
import numpy as np

# ── PAGE CONFIG ───────────────────────────────────────────
st.set_page_config(
    page_title="Fall Risk Predictor",
    page_icon="🏥",
    layout="centered"
)

# ── LOAD MODEL ────────────────────────────────────────────
@st.cache_resource
def load_model():
    model   = joblib.load("fall_risk_xgboost_model.pkl")
    scaler  = joblib.load("fall_risk_scaler.pkl")
    imputer = joblib.load("fall_risk_imputer.pkl")
    return model, scaler, imputer

model, scaler, imputer = load_model()

# ── HEADER ────────────────────────────────────────────────
st.title("🏥 Fall Risk Prediction App")
st.markdown("### Based on LASI Wave 1 Data (73,396 Indians aged 45+)")
st.markdown("---")

# ── INPUT FORM ────────────────────────────────────────────
st.subheader("📋 Enter Patient Details")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**💪 Grip Strength (kg)**")
    bm028 = st.slider("Reading 1", 0.0, 60.0, 20.0, 0.5)
    bm029 = st.slider("Reading 2", 0.0, 60.0, 20.0, 0.5)
    bm030 = st.slider("Reading 3", 0.0, 60.0, 20.0, 0.5)
    
    st.markdown("**📏 Anthropometrics**")
    height = st.slider("Height (m)", 1.0, 2.0, 1.55, 0.01)
    bmi    = st.slider("BMI", 10.0, 50.0, 22.0, 0.1)

with col2:
    st.markdown("**🫀 Blood Pressure**")
    highsyst  = st.selectbox("High Systolic BP",  
                             [0, 1], 
                             format_func=lambda x: "Yes" if x==1 else "No")
    highdiast = st.selectbox("High Diastolic BP", 
                             [0, 1], 
                             format_func=lambda x: "Yes" if x==1 else "No")
    hyper     = st.selectbox("Hypertension",      
                             [0, 1], 
                             format_func=lambda x: "Yes" if x==1 else "No")

    st.markdown("**👁️ Vision**")
    bm060a = st.selectbox("Right Eye Vision", 
                          [1, 2], 
                          format_func=lambda x: "Good" if x==1 else "Poor")
    bm060b = st.selectbox("Left Eye Vision",  
                          [1, 2], 
                          format_func=lambda x: "Good" if x==1 else "Poor")

st.markdown("---")

# ── PREDICT BUTTON ────────────────────────────────────────
if st.button("🔍 Predict Fall Risk", use_container_width=True):
    
    patient = pd.DataFrame({
        "bm028":    [bm028],
        "bm029":    [bm029],
        "bm030":    [bm030],
        "bmi":      [bmi],
        "height":   [height],
        "highsyst": [highsyst],
        "highdiast":[highdiast],
        "hyper":    [hyper],
        "bm060a":   [bm060a],
        "bm060b":   [bm060b],
    })

    imputed    = imputer.transform(patient)
    prediction = model.predict(imputed)[0]
    proba      = model.predict_proba(imputed)[0]

    st.markdown("---")
    st.subheader("📊 Prediction Result")

    if prediction == 0:
        st.success("## 🟢 LOW RISK")
        st.markdown("This patient has a **low risk** of falling.")
    elif prediction == 1:
        st.warning("## 🟡 MEDIUM RISK")
        st.markdown("This patient has a **moderate risk** of falling. Consider preventive measures.")
    else:
        st.error("## 🔴 HIGH RISK")
        st.markdown("This patient has a **high risk** of falling. Immediate intervention recommended!")

    st.markdown("### Probability Breakdown")
    col1, col2, col3 = st.columns(3)
    col1.metric("🟢 Low Risk",    f"{proba[0]*100:.1f}%")
    col2.metric("🟡 Medium Risk", f"{proba[1]*100:.1f}%")
    col3.metric("🔴 High Risk",   f"{proba[2]*100:.1f}%")

    st.markdown("---")
    st.markdown("**⚠️ Disclaimer:** This tool is for research purposes only.")

# ── FOOTER ────────────────────────────────────────────────
st.markdown("---")
st.markdown("Built using LASI Wave 1 Data | Model: XGBoost (88.3% accuracy)")
