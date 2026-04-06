import streamlit as st
import pickle
import time
import sys
import os
import pandas as pd

# Fix imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from simulation.data_simulator import stream_data
from edge.feature_extraction import extract_features

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(layout="wide")

# ---------- HEADER ----------
st.markdown("""
<style>
.big-title {
    font-size:40px !important;
    font-weight:700;
}
.metric-box {
    background-color: #111;
    padding: 15px;
    border-radius: 10px;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🚗 Smart Driver Monitoring System</div>', unsafe_allow_html=True)
st.markdown("### 🧠 Real-time AI Fatigue Detection (HRV + Motion)")

# ---------- SIDEBAR ----------
st.sidebar.title("⚙️ Control Panel")
run = st.sidebar.button("▶ Start Simulation")

# ---------- SESSION ----------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------- LAYOUT ----------
top1, top2, top3 = st.columns(3)

score_box = top1.empty()
hr_box = top2.empty()
jerk_box = top3.empty()

status_box = st.empty()
chart_box = st.empty()
insight_box = st.empty()

# ---------- RUN ----------
if run:
    for _ in range(30):
        data, _ = stream_data()
        features = extract_features(data)

        rmssd, jerk, hr_mean = features
        score = model.predict_proba([features])[0][1]

        st.session_state.history.append({
            "score": score,
            "hr": hr_mean,
            "jerk": jerk
        })

        df = pd.DataFrame(st.session_state.history)

        # STATUS
        if score < 0.4:
            status = "SAFE"
            color = "green"
        elif score < 0.7:
            status = "FATIGUE"
            color = "orange"
        else:
            status = "DROWSY"
            color = "red"

        # ---------- METRICS ----------
        score_box.metric("🧠 Drowsiness Score", f"{score:.2f}")
        hr_box.metric("❤️ Heart Rate", f"{hr_mean:.1f} bpm")
        jerk_box.metric("🎯 Motion Stability", f"{jerk:.3f}")

        # ---------- STATUS ----------
        status_box.markdown(f"""
        ## 🚨 Status: <span style='color:{color}'>{status}</span>
        """, unsafe_allow_html=True)

        # ---------- CHARTS ----------
        with chart_box.container():
            st.subheader("📊 Live System Monitoring")

            c1, c2, c3 = st.columns(3)
            c1.line_chart(df["score"])
            c2.line_chart(df["hr"])
            c3.line_chart(df["jerk"])

        # ---------- INSIGHTS ----------
        with insight_box.container():
            st.subheader("🧠 AI Interpretation")

            st.markdown(f"""
            - RMSSD: **{rmssd:.2f}** → {'⚠ Low HRV (Fatigue)' if rmssd < 30 else '✅ Normal'}
            - Jerk: **{jerk:.3f}** → {'⚠ Low motion (Sleep risk)' if jerk < 0.1 else '✅ Active'}
            - HR: **{hr_mean:.1f} bpm**
            """)

        time.sleep(0.8)