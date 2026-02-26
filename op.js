function checkEmail() {
    let emailText = document.getElementById("emailInput").value.toLowerCase();
    let resultDiv = document.getElementById("result");

    let phishingKeywords = [
        "urgent",
        "verify",
        "click here",
        "account suspended",
        "bank details",
        "lottery",
        "winner",
        "update now"
    ];

    let isPhishing = false;

    for (let i = 0; i < phishingKeywords.length; i++) {
        if (emailText.includes(phishingKeywords[i])) {
            isPhishing = true;
            break;
        }
    }

    if (isPhishing) {
        resultDiv.innerHTML = "⚠ This is a Phishing Email";
        resultDiv.style.color = "red";
    } else {
        resultDiv.innerHTML = "✅ This is a Safe Email";
        resultDiv.style.color = "green";
    }
}