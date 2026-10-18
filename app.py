import os
import joblib
import streamlit as st

st.set_page_config(page_title="Email Spam Detector", page_icon="📧")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def find_file(name):
    for folder in [BASE_DIR, os.path.join(BASE_DIR, "email_spam_detection")]:
        path = os.path.join(folder, name)
        if os.path.exists(path):
            return path
    raise FileNotFoundError(f"Could not find {name}")

@st.cache_resource
def load_model():
    model = joblib.load(find_file("spam_model.pkl"))
    vectorizer = joblib.load(find_file("vectorizer.pkl"))
    return model, vectorizer

model, vectorizer = load_model()

st.title("📧 Email Spam Detector")
st.write("Paste a message below and the model will tell you if it is spam or not.")

message = st.text_area("Enter your message here:", height=180)

if st.button("Check Message"):
    if message.strip() == "":
        st.warning("Please type or paste a message first.")
    else:
        features = vectorizer.transform([message])
        prediction = model.predict(features)[0]
        spam_probability = model.predict_proba(features)[0][1] * 100

        if prediction == 1:
            st.error(f"🚨 This looks like SPAM (spam probability: {spam_probability:.1f}%)")
        else:
            st.success(f"✅ This looks like a normal message, HAM (spam probability: {spam_probability:.1f}%)")

st.caption("Built with Python, scikit-learn (TF-IDF + Naive Bayes) and Streamlit.")
