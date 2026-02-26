from flask import Flask, render_template, request


app = Flask(__name__)

# Suspicious keywords list
suspicious_keywords = [
    "urgent", "verify", "click here",
    "password", "bank", "otp",
    "lottery", "winner",
    "free money", "account suspended"
]

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    score = 0

    if request.method == "POST":
        email_text = request.form["email"]
        email_text = email_text.lower()

        # Count suspicious words
        for word in suspicious_keywords:
            if word in email_text:
                score += 1

        # Decision logic
        if score >= 3:
            result = "⚠️ This Email is Likely PHISHING!"
        else:
            result = "✅ This Email Looks SAFE."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)