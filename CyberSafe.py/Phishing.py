import re


def welcome():
    print(" WELCOME TO CYBERSAFE " )
    print("Your personal cybersecurity awareness assistant.") 
    print("I can help you detect scams, phishing and other ")
    print("common cybersecurity risks. ")
    print()
def menu():
    print("\nWhat would you like to do? ")
    print("1.Chat with Cybersafe ")
    print("2.Check a suspiciuos message ")
    print("3.Check a suspicious link ")
    print("4.Cybersecurity risk assessment ")
    print("5.Get cybersecurity advice ")
def cybersecurity_advice():
    print("\nCYBERSECURITY ADVICE ")
    advice = [
        "Use strong and unique passwords for your accounts.",
        "Enable two-factor authentication(2FA) whenever possible",
        "Never share your password,PIN or OTP with anyone",
        "Be careful when clicking links in unexpected messages",
        "Keep your operating system and applications updated",
        "Do not download files from unknown or suspicious sources."
    ] 
    for tip in advice:
        print (".", tip)
def suspicious_message_checker():
    print ("\nSUSPICIOUS MESSAGE CHECKER")
    message = input ("Paste the suspicious message here:\n> ")
    message_lower = message.lower()
    risk_score = 0
    warnings = []

    suspicious_words = [
        "urgent",
        "verify your account",
        "click here",
        "you have won",
        "claim your prize",
        "limited time",
        "password"
    ]
    for word in suspicious_words:
        if word in message_lower:
            risk_score += 10

    urls = re.findall(r"(https?://\S+|www\.\S+)", message_lower)
    if urls:
        risk_score += 20
        warnings.append("Contains a link")

    sensitive_words = ["password", "otp", "pin", "bank", "card"]
    if any(word in message_lower for word in sensitive_words):
        risk_score += 20
        warnings.append("Requests or mentions sensitive information")

    risk_score = min(risk_score, 100)
    if risk_score >= 70:
        risk_level = "High"
    elif risk_score >= 40:
        risk_level = "Medium"
    else:
        risk_level = "Low"
    print(f"Risk Level: {risk_level}")
    if warnings:
        print("Warning signs detected:")
        for warning in warnings:
            print(f"-{warning}")
    if risk_score >= 70:
        print("This message is likely a scam or phishing attempt. Do not click any links or verify the sender through an official source.")
    elif risk_score >= 40:
        print("This message may be suspicious and could be a scam or phishing attempt.end=Be cautious and verify the sender through an official source befoore taking any action.")
    else:
        print("This message appears to be low risk, but always exercise caution and verify the sender if you are unsure.")
def risk_assessment():
    print("\nCYBERSECURITY RISK ASSESSMENT")
    print("Please answer the following questions to assess your cybersecurity risk:")
    # Add questions and logic for risk assessment
while True:
    answer = input("Do you want to continue? (yes/no): ").lower()
    if answer == "yes":
        welcome()
        menu()
        choice = input("Enter your choice (1-5)")
        print("\n Thank you for using Cybersafe. Stay safe online!")
    else:
        print("Goodbye!")
        break
    if __name__ == "__main__":
        cybersafe()