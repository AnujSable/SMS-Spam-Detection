import streamlit as st
import pandas as pd
import joblib

model = joblib.load("spam_detector_model.pkl")
print("Model loaded successfully!")

st.title("📩 SMS Spam Detection System")

text = st.text_area("Paste the received SMS here")

if st.button("Check Message"):
    if text.strip() == "":
        st.warning("Please enter a message!")
    else:
        msg = pd.DataFrame({'v2':[text]})
        result = model.predict(msg)[0]

        if result == 1:
            st.error("🚨 This message is SPAM!")
        else:
            st.success("✅ This message is HAM (Safe)")
            
            
            
                       