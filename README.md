# 🔐 Challenge-Based Liveness Detection System

A real-time **challenge-based liveness detection web application** that verifies whether a user is a **real live person or a spoof (photo/video attack)** by requiring users to perform **random facial and hand gesture challenges** using a webcam.

This project demonstrates how **active user interaction** can effectively prevent replay attacks in biometric authentication systems.

---

## 🚀 Features

- Real-time webcam-based verification
- Randomized facial and hand gesture challenges
- Eye blink detection (left / right)
- Head movement verification
- Hand gesture detection (thumbs up, palm open)
- Finger counting (1–5 using left or right hand)
- Time-limited tasks with restricted attempts
- Clear success and failure result screens
- Restartable verification flow

---

## 🧠 Technologies Used

- Python
- Streamlit
- OpenCV
- MediaPipe
- NumPy

---

## 🏗️ How It Works

1. User clicks **Start Verification**
2. System generates random liveness challenges
3. User performs the required facial and hand gestures
4. Successful completion of tasks → **REAL**
5. Exceeding mistake or time limits → **SPOOF**
6. Final result is displayed with an option to restart

---

## 📁 Project Structure

```text
.
├── app.py
├── app_components/
│   ├── engine.py
│   ├── detectors.py
│   └── tasks.py
├── requirements.txt
└── README.md


⚙️ Installation & Run
1️⃣ Clone the repository

git clone https://github.com/Umangghatbandhe06012001/liveness_detection_app.git
cd liveness_detection_app

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the application
streamlit run app.py

📦 Dependencies

All required libraries and their exact versions are specified in requirements.txt


🎯 Use Cases

=> Online exam proctoring
=> Secure login systems
=> Identity verification (KYC)
=> Attendance systems
=> Biometric anti-spoofing research

⚠️ Disclaimer

This project is intended for educational and research purposes only.
Production-level liveness detection systems require additional security layers such as depth sensing, hardware validation, and continuous verification.


🔮 Future Improvements

=> Compound multi-gesture challenges
=> Micro-motion consistency analysis
=> Multi-modal liveness (voice + face)
=> Continuous background liveness verification


