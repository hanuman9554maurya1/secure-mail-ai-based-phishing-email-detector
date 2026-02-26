import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Sample dataset (You can replace with real dataset later)
data = {
    'email': [
        'Congratulations! You won a free iPhone. Click here.',
        'Your bank account has been suspended. Verify now.',
        'Meeting scheduled at 10 AM tomorrow.',
        'Project report attached. Please review.',
        'Urgent! Update your password immediately.'
    ],
    'label': [1, 1, 0, 0, 1]  # 1 = Phishing, 0 = Safe
}

df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(
    df['email'], df['label'], test_size=0.2, random_state=42
)

vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

# Save model
pickle.dump(model, open("phishing_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved successfully!")