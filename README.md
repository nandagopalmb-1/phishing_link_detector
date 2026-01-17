# 🛡️ PhishGuard – URL Phishing Detection Tool

PhishGuard is a **Flask-based web application** designed to detect potentially malicious or phishing URLs using **heuristic-based analysis**.  
The tool evaluates URLs against common phishing indicators and provides a **risk score and verdict** through an interactive web interface.

🔗 **Live Deployment:**  
https://phishinglinkdetector-production.up.railway.app

---

## 📌 Project Objective

The primary goal of this project is to:
- Understand how phishing URLs are structured
- Detect common phishing patterns programmatically
- Demonstrate how security logic can be integrated into a web application
- Gain hands-on experience with Flask and cloud deployment

---

## ⚙️ How the Tool Works

The application analyzes a given URL using multiple **security heuristics**, assigns a **risk score**, and classifies the URL as either **Safe** or **Suspicious**.

### 🔍 Phishing Indicators Used

- **IP Address in URL**  
  Phishing URLs often use raw IP addresses instead of domain names.

- **Excessive URL Length**  
  Very long URLs are commonly used to hide malicious intent.

- **Presence of `@` Symbol**  
  Used to mislead users by masking the actual destination.

- **Hyphen in Domain Name**  
  Attackers imitate trusted brands using hyphenated domains.

- **Multiple Subdomains**  
  Fake subdomains are used to impersonate legitimate websites.

- **Lack of HTTPS**  
  Absence of HTTPS may indicate insecure or malicious sources.

Each detected indicator increases the **risk score**.

---

## 🧠 Decision Logic

- The tool uses a **threshold-based scoring system**
- URLs exceeding the defined threshold are flagged as **Suspicious**
- Final verdict is determined **only in the backend**, ensuring consistency

---

## 🎨 User Interface Features

- Dynamic background color changes based on verdict:
  - 🟢 Green for Safe URLs
  - 🔴 Red for Suspicious URLs
- Risk score visualization bar
- Clear verdict labels and threat indicators
- Minimal, security-themed UI design

---

## ☁️ Deployment

The application is deployed on **Railway Cloud Platform** using:
- Flask as the backend framework
- Gunicorn as the WSGI server
- GitHub-based continuous deployment

This ensures public accessibility and production-grade hosting.

---

## 🚀 Technologies Used

- **Python**
- **Flask**
- **HTML & CSS**
- **Regular Expressions (`re`)**
- **Railway Cloud**
- **Gunicorn**

---

## ⚠️ Disclaimer

This tool is based on **heuristic analysis** and is intended for **educational purposes only**.  
It is **not a replacement for enterprise-grade security solutions** or real-time threat intelligence systems.

---

## 👤 Author

Developed by **Nandagopal M B**  
Cybersecurity & Python Enthusiast

---

## ⭐ Future Enhancements

- Rule-wise threat breakdown
- Machine learning-based detection
- URL reputation APIs
- Logging and analytics dashboard
