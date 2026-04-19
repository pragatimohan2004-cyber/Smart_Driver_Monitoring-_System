# 🚗 Smart Drowsiness Detection System

### 🧠 AI-powered Multimodal Driver Monitoring (HRV + Motion Analysis)

---

## 📌 Overview

Driver drowsiness is a major cause of road accidents worldwide. Traditional detection systems rely on single-modal inputs such as cameras or steering patterns, which are often unreliable in real-world scenarios.

This project presents a **multimodal drowsiness detection system** that combines:

* Physiological signals (Heart Rate Variability)
* Motion behavior (acceleration-based jerk)
* Machine Learning-based classification

The system simulates real-time sensor data, extracts meaningful features, and predicts driver drowsiness through an interactive dashboard.

---

## ⚙️ System Architecture

```text
Simulation Layer → Feature Extraction → ML Model → Dashboard (Streamlit)
```

### 🔹 Components

* **Simulation Layer**

  * Generates synthetic physiological and motion data
  * Mimics real-world driver states (alert vs drowsy)

* **Feature Extraction**

  * RMSSD (HRV metric)
  * Motion jerk (driver control stability)
  * Mean heart rate

* **Machine Learning Model**

  * Random Forest Classifier
  * Predicts drowsiness probability

* **Dashboard**

  * Real-time visualization
  * Multi-metric monitoring
  * Trend analysis and insights

---

## 🧠 Features

* 📊 Real-time simulation of driver state
* 📈 Live visualization of trends (HR, jerk, drowsiness score)
* 🎯 Multi-modal sensor fusion
* 🚨 Alert system (Safe / Fatigue / Drowsy)
* 🧠 Explainable feature insights (HRV & motion interpretation)
* 🎛 Interactive dashboard (Streamlit)

---

## 🖥️ Demo

The system dashboard displays:

* Drowsiness score (0–1 probability)
* Heart rate trends
* Motion stability (jerk)
* Real-time status classification
* Feature-level insights

---

## 📁 Project Structure

```
Smart_Drowsiness/
│
├── dashboard/
│   └── app.py                # Streamlit UI
│
├── edge/
│   ├── feature_extraction.py
│   └── inference.py
│
├── simulation/
│   ├── data_simulator.py
│   └── __init__.py
│
├── train_model.py            # Model training script
├── model.pkl                 # Trained model
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/smart-drowsiness-detector.git
cd smart-drowsiness-detector
```

### 2️⃣ Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Train the model

```bash
python train_model.py
```

### 5️⃣ Run the dashboard

```bash
streamlit run dashboard/app.py
```

---

## 🧪 How It Works

1. Synthetic sensor data is generated (HR, motion)
2. Data is processed into time-window features:

   * RMSSD (HRV)
   * Jerk (motion)
3. Features are fed into a trained ML model
4. Model outputs drowsiness probability
5. Dashboard visualizes results in real-time

---

## 📊 Key Concepts Used

* Time-series feature extraction
* Heart Rate Variability (HRV)
* Sensor fusion
* Machine Learning (Random Forest)
* Real-time visualization (Streamlit)

---

## 🔮 Future Improvements

* Integration with real sensors (PPG, IMU)
* Personalization per driver baseline
* Edge deployment (ESP32 / Raspberry Pi)
* Deep learning-based temporal models (LSTM/Transformer)
* Camera-based eye tracking integration

---

## 🎯 Applications

* Automotive driver safety systems
* Fleet monitoring solutions
* Wearable fatigue detection systems
* Smart transportation systems

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Pragati Mohan**
B.Tech Computer Science
Manipal University Jaipur

---

⭐ If you found this project useful, please consider starring the repository!
