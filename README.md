# 🛡️ AI Network Intrusion Detection System

An AI-powered Network Intrusion Detection System that detects malicious network traffic using a **Random Forest Machine Learning model** trained on the **NSL-KDD dataset**.

## 🚀 Features

- 🛡️ Detects Normal and Malicious Network Traffic
- 🤖 Random Forest Machine Learning Model
- 📊 Interactive Streamlit Dashboard
- 🌧️ Cyber-themed HTML Landing Page
- 📈 Confidence Score & Risk Level
- ⚡ Loading Animation
- 📋 Traffic Summary
- 🎯 79.6% Detection Accuracy

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- Joblib
- HTML
- CSS
- JavaScript
- NSL-KDD Dataset

---

## 📂 Project Structure

```
Network-Anomaly-Detection/
│
├── landing/
│   ├── index.html
│   ├── style.css
│   ├── matrix.js
│   ├── loading.js
│
├── models/
├── dataset/
├── app.py
├── dashboard.py
├── train.py
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Mathu-z/Network-Anomaly-Detection.git
```

Move into the project folder

```bash
cd Network-Anomaly-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit dashboard

```bash
streamlit run app.py
```

Open the landing page

```
landing/index.html
```

---

## 🤖 Machine Learning Model

- Algorithm: Random Forest Classifier
- Dataset: NSL-KDD
- Accuracy: **79.6%**

Input Features:

- Duration
- Protocol
- Service
- Flag
- Source Bytes
- Destination Bytes
- Count
- Server Count
- Logged In
- Serror Rate

---


## 🔮 Future Improvements

- Real-time packet capture using Wireshark
- Live network monitoring
- Attack history
- Interactive charts
- World attack map
- Threat severity levels
- Advanced Machine Learning models

---

## 👨‍💻 Author

**Mathew Varghese**

Computer Science Engineering Student

GitHub: https://github.com/Mathu-z
