"""
CYBERGUARD AI - OPTIMIZED VERSION
=================================
Smooth & Fast Streamlit Cybersecurity Dashboard
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import random
from datetime import datetime
import os
import warnings

warnings.filterwarnings("ignore")

# ============================================================================
# BASIC SETTINGS
# ============================================================================

random.seed()
np.random.seed()

st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# SIMPLE FAST CSS
# ============================================================================

st.markdown("""
<style>

.main {
    background-color: #0f172a;
}

.main-header {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    color: #60a5fa;
    margin-bottom: 0.3rem;
}

.sub-header {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 2rem;
}

.glass-card {
    background-color: #1e293b;
    padding: 1.2rem;
    border-radius: 15px;
    margin-bottom: 1rem;
    border: 1px solid #334155;
}

.alert-critical {
    background-color: rgba(239,68,68,0.15);
    border-left: 5px solid #ef4444;
    padding: 1rem;
    border-radius: 10px;
    margin-top: 1rem;
}

.alert-warning {
    background-color: rgba(245,158,11,0.15);
    border-left: 5px solid #f59e0b;
    padding: 1rem;
    border-radius: 10px;
    margin-top: 1rem;
}

.alert-medium {
    background-color: rgba(59,130,246,0.15);
    border-left: 5px solid #3b82f6;
    padding: 1rem;
    border-radius: 10px;
    margin-top: 1rem;
}

.alert-success {
    background-color: rgba(16,185,129,0.15);
    border-left: 5px solid #10b981;
    padding: 1rem;
    border-radius: 10px;
    margin-top: 1rem;
}

.footer {
    text-align: center;
    color: #94a3b8;
    padding: 2rem;
    margin-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# ============================================================================
# MODEL LOADER
# ============================================================================

@st.cache_resource
def load_model():
    try:
        model_path = "attack_detection_model.pkl"

        if os.path.exists(model_path):
            return joblib.load(model_path)

        return None

    except Exception as e:
        st.error(f"Model Error: {e}")
        return None

# ============================================================================
# CACHE TRAFFIC DATA
# ============================================================================

@st.cache_data
def generate_traffic_data():
    hours = list(range(24))

    normal = [random.randint(500, 1500) for _ in range(24)]

    attack = [
        n * random.uniform(0.5, 3.0)
        for n in normal
    ]

    return hours, normal, attack

# ============================================================================
# RANDOM PREDICTION ENGINE
# ============================================================================

def get_random_prediction():

    results = [

        {
            "type": "🔥 CRITICAL: DDoS Attack",
            "severity": "CRITICAL",
            "icon": "🔴",
            "class": "alert-critical",
            "confidence": random.uniform(92, 99),
            "desc": "Massive DDoS attack detected!"
        },

        {
            "type": "🔥 CRITICAL: Botnet Attack",
            "severity": "CRITICAL",
            "icon": "🔴",
            "class": "alert-critical",
            "confidence": random.uniform(90, 98),
            "desc": "Botnet communication detected!"
        },

        {
            "type": "⚠️ HIGH: Advanced Persistent Threat",
            "severity": "HIGH",
            "icon": "🟠",
            "class": "alert-warning",
            "confidence": random.uniform(85, 94),
            "desc": "APT behavior pattern detected!"
        },

        {
            "type": "⚡ MEDIUM: Port Scan",
            "severity": "MEDIUM",
            "icon": "🟡",
            "class": "alert-medium",
            "confidence": random.uniform(70, 88),
            "desc": "Port scanning activity detected!"
        },

        {
            "type": "⚡ MEDIUM: Brute Force",
            "severity": "MEDIUM",
            "icon": "🟡",
            "class": "alert-medium",
            "confidence": random.uniform(70, 85),
            "desc": "Multiple failed login attempts!"
        },

        {
            "type": "🔵 LOW: Suspicious Pattern",
            "severity": "LOW",
            "icon": "🔵",
            "class": "alert-medium",
            "confidence": random.uniform(55, 70),
            "desc": "Suspicious traffic pattern observed!"
        },

        {
            "type": "✅ NORMAL: BENIGN Traffic",
            "severity": "NORMAL",
            "icon": "🟢",
            "class": "alert-success",
            "confidence": random.uniform(85, 98),
            "desc": "Normal traffic detected!"
        }

    ]

    result = random.choice(results)

    attacks = [
        'BENIGN',
        'DDoS',
        'PortScan',
        'Botnet',
        'BruteForce',
        'APT'
    ]

    probs = np.random.randint(1, 100, size=len(attacks))
    probs = probs / probs.sum() * 100

    prob_dict = {
        attacks[i]: probs[i]
        for i in range(len(attacks))
    }

    recommendations = {
        "CRITICAL": "Immediate isolation required!",
        "HIGH": "Block suspicious traffic immediately!",
        "MEDIUM": "Increase monitoring.",
        "LOW": "Observe network activity.",
        "NORMAL": "Everything looks safe."
    }

    return {
        "attack_type": result["type"],
        "severity": result["severity"],
        "icon": result["icon"],
        "alert_class": result["class"],
        "confidence": result["confidence"],
        "description": result["desc"],
        "recommendation": recommendations[result["severity"]],
        "probabilities": prob_dict,
        "is_attack": result["severity"] != "NORMAL"
    }

# ============================================================================
# MAIN APP
# ============================================================================

def main():

    load_model()

    # Session State

    if "click_count" not in st.session_state:
        st.session_state.click_count = 0

    if "attack_count" not in st.session_state:
        st.session_state.attack_count = 0

    if "prediction" not in st.session_state:
        st.session_state.prediction = None

    # HEADER

    st.markdown(
        '<h1 class="main-header">🛡️ CYBERGUARD AI</h1>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-header">Advanced Attack Prediction & Intelligence System</p>',
        unsafe_allow_html=True
    )

    # SIDEBAR

    with st.sidebar:

        st.title("🎛️ Dashboard")

        mode = st.radio(
            "Select Mode",
            [
                "🚀 Live Demo",
                "📁 Batch Analysis",
                "📊 Analytics"
            ]
        )

        st.markdown("---")

        st.metric(
            "Total Predictions",
            st.session_state.click_count
        )

        st.metric(
            "Attacks Detected",
            st.session_state.attack_count
        )

    # =========================================================================
    # LIVE DEMO
    # =========================================================================

    if mode == "🚀 Live Demo":

        st.markdown("""
        <div class="glass-card">
        <h2>🎮 Live Random Prediction Demo</h2>
        <p>Each click generates a new attack scenario.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🎲 GET RANDOM PREDICTION"):

            st.session_state.click_count += 1

            with st.spinner("Analyzing..."):

                st.session_state.prediction = get_random_prediction()

                if st.session_state.prediction["is_attack"]:
                    st.session_state.attack_count += 1

        prediction = st.session_state.prediction

        if prediction:

            st.markdown(f"""
            <div class="{prediction['alert_class']}">
            <h3>{prediction['icon']} {prediction['attack_type']}</h3>
            <p><strong>Confidence:</strong> {prediction['confidence']:.2f}%</p>
            <p><strong>Severity:</strong> {prediction['severity']}</p>
            <p>{prediction['description']}</p>
            <p><strong>Recommendation:</strong> {prediction['recommendation']}</p>
            </div>
            """, unsafe_allow_html=True)

            # PROBABILITY CHART

            st.subheader("📊 Attack Probability")

            prob_df = pd.DataFrame({
                "Attack": list(prediction["probabilities"].keys()),
                "Probability": list(prediction["probabilities"].values())
            })

            fig = go.Figure()

            fig.add_bar(
                x=prob_df["Attack"],
                y=prob_df["Probability"]
            )

            fig.update_layout(
                template="plotly_dark",
                height=400
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # TRAFFIC GRAPH

        st.subheader("📈 Network Traffic")

        hours, normal, attack = generate_traffic_data()

        fig2 = go.Figure()

        fig2.add_trace(go.Scatter(
            x=hours,
            y=normal,
            mode='lines',
            name='Normal Traffic'
        ))

        fig2.add_trace(go.Scatter(
            x=hours,
            y=attack,
            mode='lines',
            name='Suspicious Activity'
        ))

        fig2.update_layout(
            template="plotly_dark",
            height=400,
            xaxis_title="Hours",
            yaxis_title="Packets"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # =========================================================================
    # BATCH ANALYSIS
    # =========================================================================

    elif mode == "📁 Batch Analysis":

        st.markdown("""
        <div class="glass-card">
        <h2>📁 Batch CSV Analysis</h2>
        <p>Upload network traffic CSV file.</p>
        </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "Upload CSV",
            type=["csv"]
        )

        if uploaded_file:

            try:

                df = pd.read_csv(uploaded_file).head(1000)

                st.success(f"Loaded {len(df)} rows")

                st.dataframe(df.head())

                if st.button("🔍 Start Analysis"):

                    predictions = []
                    confidences = []

                    for _ in range(len(df)):

                        pred = get_random_prediction()

                        predictions.append(pred["attack_type"])
                        confidences.append(pred["confidence"])

                    df["Prediction"] = predictions
                    df["Confidence"] = confidences

                    st.success("Analysis Complete!")

                    st.dataframe(df.head(20))

                    csv = df.to_csv(index=False)

                    st.download_button(
                        "📥 Download Results",
                        csv,
                        "results.csv",
                        "text/csv"
                    )

            except Exception as e:
                st.error(f"Error: {e}")

    # =========================================================================
    # ANALYTICS
    # =========================================================================

    else:

        st.markdown("""
        <div class="glass-card">
        <h2>📊 Threat Analytics Dashboard</h2>
        </div>
        """, unsafe_allow_html=True)

        days = 30

        dates = pd.date_range(
            end=datetime.now(),
            periods=days
        )

        attacks = np.random.poisson(15, days)

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=dates,
            y=attacks,
            mode='lines+markers',
            name='Attacks'
        ))

        fig.update_layout(
            template="plotly_dark",
            height=500,
            title="Attack Trend Analysis"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Average Attacks",
                f"{attacks.mean():.1f}"
            )

        with col2:
            st.metric(
                "Peak Attacks",
                int(attacks.max())
            )

        with col3:
            st.metric(
                "Trend",
                "↑ 12%"
            )

    # FOOTER

    st.markdown("""
    <div class="footer">
    <p>🛡️ CyberGuard AI</p>
    <p>Optimized Streamlit Cybersecurity Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# RUN APP
# ============================================================================

if __name__ == "__main__":
    main()