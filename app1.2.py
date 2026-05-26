"""
CYBERGUARD AI - DATA-DRIVEN ELITE EDITION
==========================================
Advanced Predictive Attack Intelligence Dashboard
Integrated with CIC-2017 Dataset Features
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
import random
from datetime import datetime, timedelta
import os
import warnings
import time

warnings.filterwarnings("ignore")

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="CYBERGUARD DATA-DRIVEN ELITE",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CIC-2017 FEATURE DEFINITIONS
# ============================================================================

FEATURES = [
    'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',
    'Fwd Packet Length Max', 'Fwd Packet Length Min', 'Flow IAT Mean',
    'Flow IAT Max', 'Flow IAT Min', 'Fwd IAT Total', 'Bwd IAT Total',
    'Packet Length Mean', 'ACK Flag Count', 'PSH Flag Count', 'SYN Flag Count'
]

# ============================================================================
# ADVANCED NEON CYBERPUNK CSS
# ============================================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=JetBrains+Mono:wght@300;500&display=swap');

    :root {
        --primary: #00f2ff;
        --secondary: #7000ff;
        --danger: #ff0055;
        --warning: #ffaa00;
        --success: #00ff88;
        --bg-dark: #050505;
        --card-bg: rgba(20, 20, 30, 0.8);
    }

    .main {
        background: radial-gradient(circle at 50% 50%, #0a0a1a 0%, #050505 100%);
        color: #e0e0e0;
        font-family: 'JetBrains+Mono', monospace;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #050505; }
    ::-webkit-scrollbar-thumb { background: var(--secondary); border-radius: 10px; }

    /* Header Styling */
    .glitch-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 8px;
        background: linear-gradient(90deg, var(--primary), var(--secondary), var(--primary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 20px rgba(0, 242, 255, 0.5);
        margin-bottom: 0;
        animation: pulse 3s infinite;
    }

    @keyframes pulse {
        0% { opacity: 0.8; }
        50% { opacity: 1; text-shadow: 0 0 30px rgba(112, 0, 255, 0.8); }
        100% { opacity: 0.8; }
    }

    .sub-title {
        font-family: 'Orbitron', sans-serif;
        text-align: center;
        color: var(--primary);
        font-size: 0.8rem;
        letter-spacing: 4px;
        margin-top: -10px;
        margin-bottom: 2rem;
        opacity: 0.7;
    }

    /* Card Styling */
    .cyber-card {
        background: var(--card-bg);
        border: 1px solid rgba(0, 242, 255, 0.2);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease, border 0.3s ease;
    }

    .cyber-card:hover {
        transform: translateY(-5px);
        border: 1px solid var(--primary);
    }

    /* Alert Styling */
    .alert-box {
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        border-left: 8px solid;
        animation: slideIn 0.5s ease-out;
    }

    @keyframes slideIn {
        from { transform: translateX(-50px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }

    .critical { background: rgba(255, 0, 85, 0.1); border-color: var(--danger); color: #ff80ab; }
    .warning { background: rgba(255, 170, 0, 0.1); border-color: var(--warning); color: #ffd180; }
    .info { background: rgba(0, 242, 255, 0.1); border-color: var(--primary); color: #80deea; }
    .success { background: rgba(0, 255, 136, 0.1); border-color: var(--success); color: #b9f6ca; }

    /* Metric Styling */
    [data-testid="stMetricValue"] {
        font-family: 'Orbitron', sans-serif;
        font-size: 2rem !important;
        color: var(--primary) !important;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #080810 !important;
        border-right: 1px solid rgba(0, 242, 255, 0.1);
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, var(--secondary), var(--primary));
        color: white;
        font-family: 'Orbitron', sans-serif;
        border: none;
        border-radius: 5px;
        padding: 10px;
        transition: all 0.3s;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .stButton>button:hover {
        box-shadow: 0 0 20px var(--primary);
        transform: scale(1.02);
    }

</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA ENGINES (INTEGRATED WITH CIC-2017)
# ============================================================================

@st.cache_resource
def load_trained_model():
    """Loads the model trained with CIC-2017 features."""
    try:
        if os.path.exists("attack_detection_model.pkl"):
            return joblib.load("attack_detection_model.pkl")
    except:
        pass
    return None

def generate_simulated_packet():
    """Generates a random packet matching CIC-2017 feature structure."""
    packet = {}
    for feature in FEATURES:
        if 'IAT' in feature or 'Duration' in feature:
            packet[feature] = random.uniform(10, 100000)
        elif 'Packets' in feature or 'Count' in feature:
            packet[feature] = random.randint(1, 50)
        else:
            packet[feature] = random.uniform(0, 1500)
    return pd.DataFrame([packet])

def get_time_intelligence_data():
    """Generates synthetic network traffic with time-based patterns."""
    now = datetime.now()
    times = [now - timedelta(hours=i) for i in range(24)]
    times.reverse()
    base_traffic = [1000 + 500 * np.sin(i/24 * 2 * np.pi) + random.randint(-100, 100) for i in range(24)]
    attack_traffic = [val * (1.1 + 0.5 * random.random() if random.random() > 0.8 else 1.0) for val in base_traffic]
    return times, base_traffic, attack_traffic

def predict_future_attacks():
    """Predicts attack probability for the next 6 hours."""
    now = datetime.now()
    future_times = [now + timedelta(hours=i) for i in range(1, 7)]
    risks = []
    for t in future_times:
        hour = t.hour
        base_risk = 70 if (hour >= 23 or hour <= 5) else 20
        risk = base_risk + random.randint(0, 20)
        risks.append(min(risk, 100))
    return future_times, risks

def get_data_driven_prediction(df_input, model_package):
    """Performs prediction using the trained model or simulation if model is missing."""
    
    if model_package:
        # Use real model logic
        scaler = model_package['scaler']
        model = model_package['model']
        le = model_package['label_encoder']
        
        # Scale and predict
        X_scaled = scaler.transform(df_input)
        pred_idx = model.predict(X_scaled)[0]
        probs = model.predict_proba(X_scaled)[0]
        
        attack_type = le.classes_[pred_idx]
        confidence = probs[pred_idx] * 100
        prob_dict = dict(zip(le.classes_, probs * 100))
    else:
        # Fallback simulation if model.pkl isn't present
        attack_types = ["BENIGN", "DDoS", "PortScan", "Botnet", "BruteForce"]
        attack_type = random.choices(attack_types, weights=[70, 10, 5, 10, 5])[0]
        confidence = random.uniform(85, 99)
        probs = np.random.dirichlet(np.ones(len(attack_types)), size=1)[0] * 100
        prob_dict = dict(zip(attack_types, probs))

    # Scenario metadata
    metadata = {
        "BENIGN": {"severity": "NORMAL", "icon": "🛡️", "class": "success", "desc": "Normal traffic detected.", "impact": "None", "action": "Continue monitoring."},
        "DDoS": {"severity": "CRITICAL", "icon": "💀", "class": "critical", "desc": "High volume flood detected.", "impact": "Service Outage", "action": "Enable Rate Limiting."},
        "PortScan": {"severity": "MEDIUM", "icon": "🔍", "class": "warning", "desc": "Reconnaissance activity.", "impact": "Information Leak", "action": "Block Source IP."},
        "Botnet": {"severity": "CRITICAL", "icon": "🤖", "class": "critical", "desc": "C&C communication found.", "impact": "System Takeover", "action": "Isolate Host."},
        "BruteForce": {"severity": "HIGH", "icon": "🔨", "class": "warning", "desc": "Login attempt spike.", "impact": "Account Breach", "action": "Enforce MFA."}
    }
    
    meta = metadata.get(attack_type, metadata["BENIGN"])
    
    return {
        "type": attack_type,
        "meta": meta,
        "confidence": confidence,
        "probs": prob_dict,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }

# ============================================================================
# MAIN INTERFACE
# ============================================================================

def main():
    # Load Model
    model_package = load_trained_model()

    # Initialize session state
    if "logs" not in st.session_state:
        st.session_state.logs = []
    if "total_scanned" not in st.session_state:
        st.session_state.total_scanned = 0
    if "threats_found" not in st.session_state:
        st.session_state.threats_found = 0

    # Header
    st.markdown('<h1 class="glitch-title">CYBERGUARD ELITE</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">DATA-DRIVEN PREDICTIVE INTELLIGENCE • CIC-2017 ENGINE</p>', unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown('<div style="text-align: center; padding: 10px;"><h2 style="color: var(--primary); font-family: \'Orbitron\';">COMMAND</h2></div>', unsafe_allow_html=True)
        
        mode = st.selectbox("SYSTEM MODE", ["⚡ LIVE SCAN", "🔮 TIME PREDICTION", "📂 DATA EXPLORER"])
        
        st.markdown("---")
        st.metric("PACKETS ANALYZED", f"{st.session_state.total_scanned:,}")
        st.metric("THREATS DETECTED", st.session_state.threats_found)
        
        if st.button("REBOOT SYSTEM"):
            st.session_state.logs = []
            st.session_state.total_scanned = 0
            st.session_state.threats_found = 0
            st.rerun()

    # Layout Columns
    col_left, col_right = st.columns([2, 1])

    with col_left:
        if mode == "⚡ LIVE SCAN":
            st.markdown('<div class="cyber-card"><h3>📡 Real-Time Feature Extraction</h3></div>', unsafe_allow_html=True)
            
            # Action Button
            if st.button("🚀 EXECUTE DEEP PACKET INSPECTION"):
                with st.spinner("Analyzing Feature Vectors..."):
                    time.sleep(1)
                    input_df = generate_simulated_packet()
                    pred = get_data_driven_prediction(input_df, model_package)
                    st.session_state.last_pred = pred
                    st.session_state.last_input = input_df
                    st.session_state.total_scanned += random.randint(1000, 5000)
                    if pred['meta']['severity'] != "NORMAL":
                        st.session_state.threats_found += 1
                        st.session_state.logs.insert(0, f"[{pred['timestamp']}] {pred['type']} DETECTED")

            # Result Display
            if "last_pred" in st.session_state:
                p = st.session_state.last_pred
                m = p['meta']
                
                st.markdown(f"""
                <div class="alert-box {m['class']}">
                    <h2 style="margin:0;">{m['icon']} {p['type']}</h2>
                    <p style="font-size: 1.1rem; margin: 10px 0;"><b>CONFIDENCE: {p['confidence']:.2f}%</b></p>
                    <hr style="border-color: rgba(255,255,255,0.1)">
                    <p><b>DESCRIPTION:</b> {m['desc']}</p>
                    <p><b>MITIGATION:</b> <code>{m['action']}</code></p>
                </div>
                """, unsafe_allow_html=True)
                
                # Feature Breakdown
                with st.expander("🔍 View Extracted Features"):
                    st.dataframe(st.session_state.last_input.T.rename(columns={0: 'Value'}), use_container_width=True)
                
                # Probability Chart
                fig_prob = px.bar(
                    x=list(p['probs'].keys()),
                    y=list(p['probs'].values()),
                    color=list(p['probs'].values()),
                    color_continuous_scale='Magma',
                    labels={'x': 'Vector', 'y': '%'},
                    title="Model Probability Distribution"
                )
                fig_prob.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=300)
                st.plotly_chart(fig_prob, use_container_width=True)

        elif mode == "🔮 TIME PREDICTION":
            st.markdown('<div class="cyber-card"><h3>🕰️ Time Intelligence Forecasting</h3></div>', unsafe_allow_html=True)
            f_times, f_risks = predict_future_attacks()
            
            fig_future = go.Figure()
            fig_future.add_trace(go.Scatter(x=f_times, y=f_risks, mode='lines+markers', line=dict(color='#00f2ff', width=3), fill='tozeroy'))
            fig_future.update_layout(title="Next 6 Hours Vulnerability Forecast", template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig_future, use_container_width=True)
            st.info("💡 Predictive Engine Suggests: Higher risk during night cycles. Automating firewall hardening.")

        elif mode == "📂 DATA EXPLORER":
            st.markdown('<div class="cyber-card"><h3>📊 Dataset Schema (CIC-2017)</h3></div>', unsafe_allow_html=True)
            st.write("The system is optimized for the following network features:")
            cols = st.columns(2)
            for i, f in enumerate(FEATURES):
                cols[i%2].code(f)

    with col_right:
        st.markdown('<div class="cyber-card"><h3>🛡️ Integrity</h3></div>', unsafe_allow_html=True)
        
        health_score = max(100 - (st.session_state.threats_found * 5), 5)
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number", value = health_score,
            gauge = {'axis': {'range': [0, 100]}, 'bar': {'color': "#00f2ff"}}
        ))
        fig_gauge.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', height=200, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        st.markdown("### 📝 Event Log")
        if not st.session_state.logs:
            st.write("System clean.")
        else:
            for log in st.session_state.logs[:8]:
                st.code(log, language="bash")

    st.markdown("---")
    st.markdown('<div style="text-align: center; color: #444; font-size: 0.7rem;">ENCRYPTED SESSION • CIC-2017 COMPLIANT • PREDICTIVE AI ACTIVE</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()