"""
CYBERGUARD AI - ADVANCED ATTACK PREDICTION & TIME INTELLIGENCE SYSTEM
========================================================================
Professional UI for Network Attack Detection using Machine Learning
Version: 2.4 - Fixed Random Demo
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import time
import random
from datetime import datetime, timedelta
import os
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="CyberGuard AI - Attack Prediction & Time Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS FOR PROFESSIONAL UI
# ============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
        animation: gradientBG 3s ease infinite;
    }
    
    .sub-header {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        border-color: rgba(102, 126, 234, 0.5);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }
    
    .metric-card {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        border-radius: 15px;
        padding: 1.2rem;
        text-align: center;
        border: 1px solid rgba(102, 126, 234, 0.3);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .alert-critical {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.2), rgba(239, 68, 68, 0.05));
        border-left: 4px solid #ef4444;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        animation: pulse 2s infinite;
    }
    
    .alert-warning {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.2), rgba(245, 158, 11, 0.05));
        border-left: 4px solid #f59e0b;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .alert-medium {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(59, 130, 246, 0.05));
        border-left: 4px solid #3b82f6;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .alert-success {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(16, 185, 129, 0.05));
        border-left: 4px solid #10b981;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.8; }
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
    }
    
    .status-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        margin-right: 8px;
        animation: blink 1s infinite;
    }
    
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.3; }
    }
    
    .timeline-item {
        padding: 0.8rem;
        border-left: 2px solid #667eea;
        margin-left: 1rem;
        margin-bottom: 1rem;
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        color: #64748b;
        font-size: 0.8rem;
        border-top: 1px solid #334155;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# LOAD MODEL
# ============================================================================
@st.cache_resource
def load_trained_model():
    """Load the trained model"""
    try:
        model_path = "attack_detection_model.pkl"
        
        if os.path.exists(model_path):
            model_data = joblib.load(model_path)
            return model_data
        else:
            return None
    except Exception as e:
        return None

# ============================================================================
# RANDOM PREDICTION GENERATOR - FIXED VERSION
# ============================================================================
def get_random_prediction():
    """Generate truly random prediction - changes every call"""
    
    # List of all possible results with their probabilities
    results = [
        # CRITICAL (15%)
        {"type": "🔥 CRITICAL: DDoS Attack", "severity": "CRITICAL", "icon": "🔴", "class": "alert-critical", 
         "confidence": random.uniform(92, 99), "desc": "Massive traffic spike detected! DDoS attack in progress!"},
        
        {"type": "🔥 CRITICAL: Botnet Attack", "severity": "CRITICAL", "icon": "🔴", "class": "alert-critical",
         "confidence": random.uniform(91, 98), "desc": "Multiple compromised devices detected! Botnet activity confirmed!"},
        
        {"type": "🔥 CRITICAL: Ransomware", "severity": "CRITICAL", "icon": "🔴", "class": "alert-critical",
         "confidence": random.uniform(93, 99), "desc": "Ransomware encryption pattern detected! Immediate isolation required!"},
        
        # HIGH (20%)
        {"type": "⚠️ HIGH: DDoS Attack", "severity": "HIGH", "icon": "🟠", "class": "alert-critical",
         "confidence": random.uniform(85, 94), "desc": "High volume traffic anomaly detected!"},
        
        {"type": "⚠️ HIGH: Botnet C&C", "severity": "HIGH", "icon": "🟠", "class": "alert-critical",
         "confidence": random.uniform(84, 93), "desc": "Command & control communication detected!"},
        
        {"type": "⚠️ HIGH: Advanced Persistent Threat", "severity": "HIGH", "icon": "🟠", "class": "alert-critical",
         "confidence": random.uniform(86, 95), "desc": "APT behavior patterns detected!"},
        
        # MEDIUM (25%)
        {"type": "⚡ MEDIUM: Port Scan", "severity": "MEDIUM", "icon": "🟡", "class": "alert-warning",
         "confidence": random.uniform(70, 88), "desc": "Multiple port scanning attempts detected!"},
        
        {"type": "⚡ MEDIUM: Infiltration Attempt", "severity": "MEDIUM", "icon": "🟡", "class": "alert-warning",
         "confidence": random.uniform(72, 87), "desc": "Unauthorized access attempt detected!"},
        
        {"type": "⚡ MEDIUM: Web Attack", "severity": "MEDIUM", "icon": "🟡", "class": "alert-warning",
         "confidence": random.uniform(71, 86), "desc": "Web application attack pattern detected!"},
        
        {"type": "⚡ MEDIUM: Brute Force", "severity": "MEDIUM", "icon": "🟡", "class": "alert-warning",
         "confidence": random.uniform(73, 89), "desc": "Multiple failed login attempts!"},
        
        # LOW (20%)
        {"type": "🔵 LOW: Suspicious Pattern", "severity": "LOW", "icon": "🔵", "class": "alert-medium",
         "confidence": random.uniform(55, 75), "desc": "Unusual traffic pattern detected"},
        
        {"type": "🔵 LOW: Anomaly Detected", "severity": "LOW", "icon": "🔵", "class": "alert-medium",
         "confidence": random.uniform(56, 74), "desc": "Network behavior anomaly detected"},
        
        {"type": "🔵 LOW: Unusual Behavior", "severity": "LOW", "icon": "🔵", "class": "alert-medium",
         "confidence": random.uniform(57, 76), "desc": "Unusual protocol usage detected"},
        
        # NORMAL (20%)
        {"type": "✅ NORMAL: BENIGN Traffic", "severity": "NORMAL", "icon": "🟢", "class": "alert-success",
         "confidence": random.uniform(85, 98), "desc": "Normal network traffic - No threats detected"},
        
        {"type": "✅ NORMAL: Safe Activity", "severity": "NORMAL", "icon": "🟢", "class": "alert-success",
         "confidence": random.uniform(86, 97), "desc": "All network flows appear legitimate"},
    ]
    
    # Randomly select a result (equal probability for variety)
    result = random.choice(results)
    
    # Generate random probabilities for chart
    attacks = ['BENIGN', 'DDoS', 'PortScan', 'Botnet', 'Infiltration', 'Web Attack', 'Brute Force', 'Ransomware']
    
    # Make the top prediction match the result
    if "DDoS" in result["type"]:
        probs = [random.uniform(5, 15), random.uniform(70, 95), random.uniform(2, 10), random.uniform(1, 8), 
                 random.uniform(1, 5), random.uniform(1, 5), random.uniform(1, 5), random.uniform(1, 5)]
    elif "Botnet" in result["type"]:
        probs = [random.uniform(5, 15), random.uniform(2, 10), random.uniform(2, 10), random.uniform(70, 95),
                 random.uniform(1, 5), random.uniform(1, 5), random.uniform(1, 5), random.uniform(1, 5)]
    elif "Port Scan" in result["type"]:
        probs = [random.uniform(10, 20), random.uniform(2, 10), random.uniform(65, 90), random.uniform(1, 8),
                 random.uniform(1, 5), random.uniform(1, 5), random.uniform(1, 5), random.uniform(1, 5)]
    elif "Infiltration" in result["type"] or "Web Attack" in result["type"]:
        probs = [random.uniform(10, 25), random.uniform(2, 10), random.uniform(2, 10), random.uniform(1, 8),
                 random.uniform(55, 85), random.uniform(1, 10), random.uniform(1, 5), random.uniform(1, 5)]
    elif "Brute Force" in result["type"]:
        probs = [random.uniform(15, 30), random.uniform(1, 8), random.uniform(1, 8), random.uniform(1, 8),
                 random.uniform(1, 5), random.uniform(1, 8), random.uniform(55, 85), random.uniform(1, 5)]
    elif "Ransomware" in result["type"]:
        probs = [random.uniform(5, 15), random.uniform(1, 8), random.uniform(1, 8), random.uniform(1, 8),
                 random.uniform(1, 5), random.uniform(1, 8), random.uniform(1, 5), random.uniform(70, 90)]
    else:  # BENIGN
        probs = [random.uniform(70, 95), random.uniform(1, 10), random.uniform(1, 8), random.uniform(1, 8),
                 random.uniform(1, 5), random.uniform(1, 5), random.uniform(1, 5), random.uniform(1, 5)]
    
    # Normalize probabilities to 100%
    probs = np.array(probs)
    probs = probs / probs.sum() * 100
    
    prob_dict = {attacks[i]: probs[i] for i in range(len(attacks))}
    
    # Recommendation based on severity
    recommendations = {
        "CRITICAL": "🔴 IMMEDIATE: Isolate systems, activate incident response, block suspicious IPs, notify security team",
        "HIGH": "🟠 URGENT: Block traffic from suspicious sources, increase monitoring, alert security team immediately",
        "MEDIUM": "🟡 Monitor: Log analysis, pattern tracking, prepare countermeasures, increase vigilance",
        "LOW": "🔵 Observe: Document behavior, update rules if pattern repeats, continue monitoring",
        "NORMAL": "🟢 All good: Continue normal operations, maintain security posture"
    }
    
    return {
        'attack_type': result["type"],
        'confidence': result["confidence"],
        'probabilities': prob_dict,
        'is_attack': result["severity"] != "NORMAL",
        'severity': result["severity"],
        'icon': result["icon"],
        'alert_class': result["class"],
        'description': result["desc"],
        'recommendation': recommendations[result["severity"]]
    }

# ============================================================================
# PREDICTION ENGINE
# ============================================================================
class PredictionEngine:
    def __init__(self, model_data):
        self.model_data = model_data
        self.use_demo = model_data is None
        
        if not self.use_demo:
            self.model = model_data['model']
            self.scaler = model_data['scaler']
            self.label_encoder = model_data['label_encoder']
            self.feature_names = model_data['feature_names']
            self.accuracy = model_data.get('accuracy', 0.95)
    
    def predict_single(self, features_dict):
        """Predict single network flow"""
        # ALWAYS use random predictions for demo mode
        return get_random_prediction()
    
    def predict_batch(self, df):
        """Predict multiple network flows"""
        if self.use_demo:
            num_samples = len(df)
            predictions = []
            confidences = []
            
            for _ in range(num_samples):
                pred = get_random_prediction()
                predictions.append(pred['attack_type'])
                confidences.append(pred['confidence'])
            
            return np.array(predictions), np.array(confidences)
        else:
            try:
                X = df[self.feature_names].copy()
                X_scaled = self.scaler.transform(X)
                
                predictions = self.model.predict(X_scaled)
                probabilities = self.model.predict_proba(X_scaled)
                
                attack_types = self.label_encoder.inverse_transform(predictions)
                confidences = np.max(probabilities, axis=1) * 100
                
                return attack_types, confidences
            except:
                return None, None

# ============================================================================
# MAIN APPLICATION
# ============================================================================
def main():
    model_data = load_trained_model()
    predictor = PredictionEngine(model_data)
    
    # Header
    st.markdown('<h1 class="main-header">🛡️ CYBERGUARD AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Advanced Attack Prediction & Time Intelligence System</p>', unsafe_allow_html=True)
    
    with st.expander("ℹ️ **What is CyberGuard AI?**", expanded=False):
        st.markdown("""
        **CyberGuard AI** detects network attacks using Machine Learning:
        
        🎯 **Real-time Detection** - Identifies DDoS, Botnet, PortScan, and more
        ⏰ **Time Intelligence** - Analyzes patterns to predict future threats
        🎲 **Random Demo** - Each click shows different scenarios!
        """)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 🎮 **System Dashboard**")
        st.markdown("---")
        
        st.markdown("#### 🤖 Model Status")
        st.info("🎲 **DEMO MODE ACTIVE**")
        st.success("✨ Each click gives random results!")
        
        st.markdown("---")
        
        st.markdown("#### 🎯 **Operation Mode**")
        mode = st.radio(
            "Select Mode",
            ["🚀 Live Demo", "📁 Batch Analysis", "📊 Analytics Dashboard"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        st.markdown("#### ⚙️ **Alert Settings**")
        alert_threshold = st.slider("Alert Threshold", 0, 100, 70)
        
        st.markdown("---")
        st.markdown("#### 📊 **Session Stats**")
        if 'click_count' not in st.session_state:
            st.session_state.click_count = 0
        if 'attack_count' not in st.session_state:
            st.session_state.attack_count = 0
        
        st.metric("Total Clicks", st.session_state.click_count)
        st.metric("Attacks Detected", st.session_state.attack_count)
        
        st.markdown("---")
        st.caption("🔒 Powered by Random Forest ML")
    
    # Main content
    if mode == "🚀 Live Demo":
        st.markdown("""
        <div class="glass-card">
            <h2>🎮 Interactive Live Demo</h2>
            <p><strong>Click the button below - EACH CLICK gives a DIFFERENT result!</strong></p>
            <p>🎲 Results include: Critical 🔴 | High 🟠 | Medium 🟡 | Low 🔵 | Normal 🟢</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎲 **GET RANDOM PREDICTION**", use_container_width=False):
                # Update counters
                st.session_state.click_count += 1
                
                with st.spinner("🔍 Analyzing network traffic..."):
                    # Progress bar
                    progress_bar = st.progress(0)
                    for i in range(100):
                        time.sleep(0.005)
                        progress_bar.progress(i + 1)
                    
                    # Get prediction
                    prediction = get_random_prediction()
                    
                    if prediction['is_attack']:
                        st.session_state.attack_count += 1
                    
                    st.success("✅ Analysis Complete!")
                    
                    # Display result
                    st.markdown(f"""
                    <div class="{prediction['alert_class']}">
                        <h3>{prediction['icon']} {prediction['attack_type']}</h3>
                        <p><strong>Confidence:</strong> {prediction['confidence']:.1f}%</p>
                        <p><strong>Severity:</strong> {prediction['severity']}</p>
                        <p>{prediction['description']}</p>
                        <p><strong>📋 Recommendation:</strong> {prediction['recommendation']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Probability Chart
                    st.markdown("#### 📊 Attack Probability Distribution")
                    prob_df = pd.DataFrame({
                        'Attack Type': list(prediction['probabilities'].keys()),
                        'Probability (%)': list(prediction['probabilities'].values())
                    }).sort_values('Probability (%)', ascending=False)
                    
                    fig = px.bar(prob_df.head(8), x='Attack Type', y='Probability (%)',
                               color='Probability (%)', color_continuous_scale='Reds',
                               title='Prediction Confidence by Attack Type')
                    fig.update_layout(
                        plot_bgcolor='rgba(0,0,0,0)',
                        paper_bgcolor='rgba(0,0,0,0)',
                        font_color='white',
                        height=400
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Show stats
                    st.info(f"📊 **Session Stats:** {st.session_state.click_count} total predictions | {st.session_state.attack_count} attacks detected")
        
        # Traffic Pattern
        st.markdown("#### 📈 Live Traffic Pattern")
        
        # Generate random traffic data
        hours = list(range(24))
        normal = [random.randint(500, 1500) for _ in range(24)]
        attack = [n * random.uniform(0.5, 3.0) for n in normal]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=hours, y=normal, name="Normal Traffic",
                                line=dict(color='#10b981', width=2), fill='tozeroy'))
        fig.add_trace(go.Scatter(x=hours, y=attack, name="Suspicious Activity",
                                line=dict(color='#ef4444', width=2, dash='dash')))
        
        fig.update_layout(title="Network Traffic Pattern (Last 24 Hours)",
                         xaxis_title="Hour", yaxis_title="Packets per Second",
                         plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
                         height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        with st.expander("💡 **How to Use**"):
            st.markdown("""
            ### 🎮 Instructions
            1. **Click the button REPEATEDLY** - Each click gives a DIFFERENT random result!
            2. **Watch the stats** - See how many attacks were detected
            3. **Check the probability chart** - See confidence levels for each attack type
            4. **Try 10 times** - You'll see Critical, High, Medium, Low, and Normal results!
            
            🎲 **Results you'll see:**
            - 🔴 CRITICAL: DDoS, Botnet, Ransomware
            - 🟠 HIGH: DDoS, Botnet C&C, APT
            - 🟡 MEDIUM: Port Scan, Infiltration, Web Attack, Brute Force
            - 🔵 LOW: Suspicious patterns, anomalies
            - 🟢 NORMAL: BENIGN traffic
            """)
    
    elif mode == "📁 Batch Analysis":
        st.markdown("""
        <div class="glass-card">
            <h2>📁 Batch Network Analysis</h2>
            <p>Upload CSV file for bulk attack prediction</p>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader("Choose CSV file", type="csv")
        
        if uploaded_file:
            try:
                df = pd.read_csv(uploaded_file, nrows=5000)
                st.success(f"✅ Loaded {len(df)} network flows")
                
                with st.expander("📊 Data Preview"):
                    st.dataframe(df.head(10))
                
                if st.button("🔍 **Start Analysis**", use_container_width=False):
                    with st.spinner(f"Analyzing {len(df)} network flows..."):
                        attack_types, confidences = predictor.predict_batch(df)
                        
                        if attack_types is not None:
                            df['Predicted_Attack'] = attack_types
                            df['Confidence_%'] = confidences
                            df['Alert'] = df['Confidence_%'] > alert_threshold
                            
                            col1, col2, col3, col4 = st.columns(4)
                            with col1:
                                st.metric("Total Flows", len(df))
                            with col2:
                                attacks = sum(df['Predicted_Attack'].str.contains('BENIGN') == False)
                                st.metric("Attacks Detected", attacks)
                            with col3:
                                high_conf = sum(df['Confidence_%'] > 90)
                                st.metric("High Confidence", high_conf)
                            with col4:
                                st.metric("Avg Confidence", f"{df['Confidence_%'].mean():.1f}%")
                            
                            attack_counts = df['Predicted_Attack'].value_counts().head(10)
                            fig = px.pie(values=attack_counts.values, names=attack_counts.index,
                                       title="Attack Distribution")
                            fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', height=400)
                            st.plotly_chart(fig, use_container_width=True)
                            
                            csv = df.to_csv(index=False)
                            st.download_button("📥 Download Results", csv, "analysis_results.csv", "text/csv")
            except Exception as e:
                st.error(f"Error: {e}")
    
    else:
        st.markdown("""
        <div class="glass-card">
            <h2>📊 Time Intelligence Dashboard</h2>
            <p>Historical analysis and predictive insights</p>
        </div>
        """, unsafe_allow_html=True)
        
        days = 30
        dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
        attacks = np.random.poisson(15, days) + np.linspace(0, 5, days)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=attacks, mode='lines+markers',
                                name='Attacks', line=dict(color='#ef4444', width=2)))
        fig.update_layout(title="Attack Pattern Analysis - Last 30 Days",
                         plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', height=500)
        st.plotly_chart(fig, use_container_width=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Peak Risk", f"{np.max(attacks)/np.max(attacks+10)*100:.1f}%")
        with col2:
            st.metric("Daily Avg", f"{attacks.mean():.1f}")
        with col3:
            st.metric("Trend", "↑ 12%")
        with col4:
            st.metric("Critical Days", "8")
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>🛡️ CyberGuard AI | Random Forest ML | Real-time Detection</p>
        <p>🎲 Click the button multiple times - EACH CLICK gives DIFFERENT results!</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()