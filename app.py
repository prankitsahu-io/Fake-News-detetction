# app.py
import streamlit as st
import pickle

# Load saved model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# UI
st.title("📰 Fake News Detection App")
st.markdown("Enter a news article below to check whether it's **fake** or **real**.")

input_text = st.text_area("📝 News Article Text")

if st.button("Predict"):
    if input_text.strip() == "":
        st.warning("Please enter some text!")
    else:
        transformed = vectorizer.transform([input_text])
        prediction = model.predict(transformed)[0]
        st.success("✅ Real News" if prediction else "❌ Fake News")
