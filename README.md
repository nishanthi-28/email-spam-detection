# 📧 Email Spam Detection Using Machine Learning

A machine learning project that classifies messages as **spam** or **ham (not spam)** using **TF-IDF** and **Multinomial Naive Bayes**, with a web app built using **Streamlit**.

🔗 **Live App:** PASTE-YOUR-STREAMLIT-LINK-HERE

## 📌 Project Overview
Spam messages waste time and can be harmful (phishing, scams). This project trains a model that reads a message and predicts whether it is spam.

## 🛠️ Technologies Used
- Python
- Pandas, Matplotlib
- Scikit-learn (TF-IDF, Naive Bayes)
- Streamlit
- Google Colab and GitHub

## 📊 Dataset
- **SMS Spam Collection Dataset** (UCI / Kaggle)
- About 5,572 messages labeled `ham` or `spam`
- 5,169 messages remain after removing duplicates

## ⚙️ Methodology
1. Load and inspect the dataset
2. Clean data: remove duplicates, convert labels to numbers (ham = 0, spam = 1)
3. Split data: 80% training, 20% testing (stratified)
4. Convert text to numbers using TF-IDF
5. Train a Multinomial Naive Bayes classifier
6. Evaluate using accuracy, precision, recall, F1-score and a confusion matrix
7. Save the model with joblib and build a Streamlit web app

## ✅ Results
- Accuracy: **ADD-YOUR-ACCURACY %** (copy it from your Step 4 output)
- The model is very precise at catching spam, with few normal messages wrongly flagged.

## 📁 Project Structure
```
email-spam-detection/
├── app.py                  # Streamlit web app
├── requirements.txt        # Libraries needed
├── README.md
└── email_spam_detection/
    ├── spam_detection.ipynb   # Colab notebook
    ├── spam.csv               # Dataset
    ├── spam_model.pkl         # Trained model
    └── vectorizer.pkl         # TF-IDF vectorizer
```

## ▶️ How to Run
1. Open `spam_detection.ipynb` in Google Colab and upload `spam.csv`.
2. Run all cells to train and save the model.
3. To run the app locally:
```
pip install -r requirements.txt
streamlit run app.py
```

## ⚠️ Limitations
- Trained on SMS messages, so results on long or formal emails may be less accurate.
- The dataset is small and imbalanced (far more ham than spam).

## 🚀 Future Improvements
- Train on a real email dataset
- Try other models (Logistic Regression, SVM)
- Handle class imbalance

## 👤 Author
**YOUR NAME** | B.Tech Information Technology
