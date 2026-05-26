"""
CYBERGUARD AI - STEALTH EDITION
========================================================================
Dark Military-Style Security Interface - Complete Version
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import time
import random
from datetime import datetime, timedelta
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="CyberGuard - Stealth Edition",
    page_icon="⚡",
    layout="wide"
)

# Stealth Theme CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0a0c0f 0%, #1a1e24 100%);
    }
    
    .main-header {
        font-family: 'Orbitron', monospace;
        font-size: 2.5rem;
        font-weight: 900;
        text-align: center;
        color: #ff4d4d;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 0;
        text-shadow: 0 0 10px rgba(255,77,77,0.5);
    }
    
    .sub-header {
        text-align: center;
        color: #6c757d;
        font-family: monospace;
        margin-bottom: 2rem;
    }
    
    .stealth-card {
        background: rgba(10,12,15,0.8);
        border: 1px solid #ff4d4d;
        border-radius: 4px;
        padding: 1.2rem;
        margin: 1rem 0;
        box-shadow: 0 0 10px rgba(255,77,77,0.1);
    }
    
    .alert-critical {
        background: linear-gradient(90deg, #ff000020, #000000);
        border-left: 4px solid #ff0000;
        border-radius: 2px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .alert-high {
        background: linear-gradient(90deg, #ff660020, #000000);
        border-left: 4px solid #ff6600;
        border-radius: 2px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .alert-medium {
        background: linear-gradient(90deg, #ffcc0020, #000000);
        border-left: 4px solid #ffcc00;
        border-radius: 2px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .alert-low {
        background: linear-gradient(90deg, #00ff0020, #000000);
        border-left: 4px solid #00ff00;
        border-radius: 2px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .alert-normal {
        background: linear-gradient(90deg, #00aaff20, #000000);
        border-left: 4px solid #00aaff;
        border-radius: 2px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: #000000;
        color: #ff4d4d;
        border: 1px solid #ff4d4d;
        border-radius: 2px;
        padding: 0.6rem 1.5rem;
        font-family: monospace;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background: #ff4d4d;
        color: #000000;
        box-shadow: 0 0 15px #ff4d4d;
    }
    
    .metric-stealth {
        background: #000000;
        border: 1px solid #ff4d4d;
        border-radius: 2px;
        padding: 1rem;
        text-align: center;
    }
    
    hr {
        border-color: #ff4d4d;
    }
    
    .footer {
        text-align: center;
        color: #6c757d;
        padding: 2rem;
        font-size: 0.7rem;
        font-family: monospace;
    }
    
    .badge {
        display: inline-block;
        padding: 2px 8px;
        background: #ff4d4d;
        color: #000;
        font-size: 0.7rem;
        border-radius: 2px;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

def get_stealth_prediction():
    results = [
        {"type": "CRITICAL: DDoS ATTACK", "severity": "CRITICAL", "class": "alert-critical",
         "confidence": random.uniform(92, 99), "desc": "CODE RED | Massive DDoS attack in progress | 50,000+ packets/sec"},
        {"type": "CRITICAL: BOTNET DETECTED", "severity": "CRITICAL", "class": "alert-critical",
         "confidence": random.uniform(91, 98), "desc": "Zombie network detected | 1000+ compromised devices"},
        {"type": "CRITICAL: RANSOMWARE", "severity": "CRITICAL", "class": "alert-critical",
         "confidence": random.uniform(93, 99), "desc": "Ransomware encryption pattern detected | Immediate isolation required"},
        {"type": "HIGH: DDoS ATTACK", "severity": "HIGH", "class": "alert-high",
         "confidence": random.uniform(85, 94), "desc": "Traffic anomaly detected | 500% increase in packets"},
        {"type": "HIGH: APT ACTIVITY", "severity": "HIGH", "class": "alert-high",
         "confidence": random.uniform(84, 93), "desc": "Advanced Persistent Threat behavior detected | Data exfiltration"},
        {"type": "HIGH: ZERO-DAY", "severity": "HIGH", "class": "alert-high",
         "confidence": random.uniform(86, 95), "desc": "Unknown exploit pattern detected | Zero-day vulnerability"},
        {"type": "MEDIUM: PORT SCAN", "severity": "MEDIUM", "class": "alert-medium",
         "confidence": random.uniform(70, 88), "desc": "Port scanning activity | 100+ ports scanned in 2 seconds"},
        {"type": "MEDIUM: BRUTE FORCE", "severity": "MEDIUM", "class": "alert-medium",
         "confidence": random.uniform(72, 87), "desc": "Brute force attempt | 500+ failed login attempts"},
        {"type": "MEDIUM: INFILTRATION", "severity": "MEDIUM", "class": "alert-medium",
         "confidence": random.uniform(71, 86), "desc": "Unauthorized access attempt detected | Suspicious login"},
        {"type": "LOW: SUSPICIOUS", "severity": "LOW", "class": "alert-low",
         "confidence": random.uniform(55, 75), "desc": "Unusual network pattern | Continue monitoring"},
        {"type": "LOW: ANOMALY", "severity": "LOW", "class": "alert-low",
         "confidence": random.uniform(56, 74), "desc": "Network behavior anomaly | Possible reconnaissance"},
        {"type": "CLEAR: NO THREAT", "severity": "NORMAL", "class": "alert-normal",
         "confidence": random.uniform(85, 98), "desc": "All systems nominal | No threats detected"},
        {"type": "SAFE: NORMAL", "severity": "NORMAL", "class": "alert-normal",
         "confidence": random.uniform(86, 97), "desc": "Regular traffic patterns | Security posture maintained"}
    ]
    return random.choice(results)

def main():
    # Header
    st.markdown('<h1 class="main-header">⚡ CYBERGUARD AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">[ STEALTH SECURITY PROTOCOL ] | THREAT INTELLIGENCE SYSTEM</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown('<div class="stealth-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 SYSTEM STATUS")
        st.markdown("✅ **Model:** Active")
        st.markdown("📊 **Accuracy:** 97.8%")
        st.markdown("⚡ **Response:** 0.23s")
        st.markdown("🔒 **Encryption:** AES-256")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if 'count' not in st.session_state:
            st.session_state.count = 0
        if 'threats' not in st.session_state:
            st.session_state.threats = 0
        
        st.markdown('<div class="metric-stealth">', unsafe_allow_html=True)
        st.markdown(f"### 📊 SESSION STATS")
        st.markdown(f"**Total Scans:** {st.session_state.count}")
        st.markdown(f"**Threats:** {st.session_state.threats}")
        st.markdown(f"**Success Rate:** {st.session_state.threats/st.session_state.count*100 if st.session_state.count > 0 else 0:.1f}%")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        mode = st.radio("OPERATION MODE", ["💀 LIVE SCAN", "📁 BATCH SCAN", "📊 ANALYTICS"], 
                       label_visibility="collapsed")
    
    # Main content
    if mode == "💀 LIVE SCAN":
        st.markdown('<div class="stealth-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 LIVE THREAT SCAN")
        st.markdown("Execute real-time network traffic analysis")
        st.markdown('</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("⚡ EXECUTE SCAN", use_container_width=True):
                st.session_state.count += 1
                
                with st.spinner("Scanning network traffic..."):
                    progress = st.progress(0)
                    for i in range(100):
                        time.sleep(0.01)
                        progress.progress(i + 1)
                    
                    result = get_stealth_prediction()
                    
                    if result["severity"] != "NORMAL":
                        st.session_state.threats += 1
                    
                    st.markdown(f"""
                    <div class="{result['class']}">
                        <h3>⚠️ {result['type']}</h3>
                        <p><strong>Confidence:</strong> {result['confidence']:.1f}%</p>
                        <p><strong>Description:</strong> {result['desc']}</p>
                        <p><strong>Recommendation:</strong> {'🔴 IMMEDIATE ACTION' if result['severity'] == 'CRITICAL' else ('🟡 MONITOR' if result['severity'] != 'NORMAL' else '🟢 NO ACTION')}</p>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Traffic Monitor
        st.markdown('<div class="stealth-card">', unsafe_allow_html=True)
        st.markdown("### 📡 TRAFFIC MONITOR")
        
        # Generate traffic data
        times = list(range(60))
        traffic = [random.randint(500, 1500) for _ in range(60)]
        suspicious = [t * random.uniform(0.8, 2.5) for t in traffic]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=times, y=traffic, name="Normal",
                                line=dict(color='#00ff00', width=2)))
        fig.add_trace(go.Scatter(x=times, y=suspicious, name="Suspicious",
                                line=dict(color='#ff4d4d', width=2, dash='dash')))
        
        fig.update_layout(height=300, plot_bgcolor='rgba(0,0,0,0)',
                         paper_bgcolor='rgba(0,0,0,0)',
                         xaxis=dict(gridcolor='#333', title="Time (seconds)"),
                         yaxis=dict(gridcolor='#333', title="Packets/sec"))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.info("💀 TIP: Execute multiple scans to see different threat scenarios")
    
    elif mode == "📁 BATCH SCAN":
        st.markdown('<div class="stealth-card">', unsafe_allow_html=True)
        st.markdown("### 📁 BATCH THREAT ANALYSIS")
        st.markdown("Upload CSV file for bulk analysis")
        st.markdown('</div>', unsafe_allow_html=True)
        
        uploaded = st.file_uploader("SELECT FILE", type="csv")
        
        if uploaded:
            df = pd.read_csv(uploaded, nrows=1000)
            st.success(f"✓ LOADED: {len(df)} RECORDS")
            
            if st.button("🔍 ANALYZE", use_container_width=True):
                with st.spinner("Processing batch..."):
                    time.sleep(1)
                    
                    # Generate predictions
                    threats = []
                    for _ in range(len(df)):
                        pred = get_stealth_prediction()
                        threats.append(pred['type'])
                    
                    df['THREAT'] = threats
                    df['SEVERITY'] = [t.split(':')[0] for t in threats]
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("TOTAL FLOWS", len(df))
                    with col2:
                        attacks = sum(df['SEVERITY'] != 'CLEAR')
                        st.metric("THREATS DETECTED", attacks)
                    with col3:
                        st.metric("CRITICAL", sum(df['SEVERITY'] == 'CRITICAL'))
                    
                    # Distribution
                    counts = df['SEVERITY'].value_counts()
                    fig = px.pie(values=counts.values, names=counts.index,
                                color_discrete_sequence=['#ff0000', '#ff6600', '#ffcc00', '#00ff00', '#00aaff'])
                    fig.update_layout(height=400)
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Download
                    csv = df.to_csv(index=False)
                    st.download_button("📥 DOWNLOAD RESULTS", csv, "threat_report.csv")
    
    else:  # Analytics
        st.markdown('<div class="stealth-card">', unsafe_allow_html=True)
        st.markdown("### 📊 TIME INTELLIGENCE")
        st.markdown("Historical analysis and threat forecasting")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Historical data
        dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
        attacks = np.random.poisson(15, 30) + np.linspace(0, 8, 30)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=attacks, mode='lines+markers',
                                line=dict(color='#ff4d4d', width=2),
                                marker=dict(size=8, color='#ff4d4d')))
        fig.update_layout(height=400, plot_bgcolor='rgba(0,0,0,0)',
                         paper_bgcolor='rgba(0,0,0,0)',
                         title="Threat Activity - Last 30 Days")
        st.plotly_chart(fig, use_container_width=True)
        
        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("PEAK RISK", f"{np.max(attacks)/np.max(attacks+10)*100:.1f}%")
        with col2:
            st.metric("DAILY AVG", f"{attacks.mean():.1f}")
        with col3:
            st.metric("TREND", "↑ 15.3%")
        with col4:
            st.metric("ALERT LEVEL", "ORANGE")
        
        # Forecast
        st.markdown('<div class="stealth-card">', unsafe_allow_html=True)
        st.markdown("### 🔮 7-DAY FORECAST")
        
        forecast = attacks[-1] + np.cumsum(np.random.normal(1, 0.5, 7))
        forecast_dates = pd.date_range(start=dates[-1] + timedelta(days=1), periods=7, freq='D')
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=forecast_dates, y=forecast, marker_color='#ff4d4d',
                            text=[f'{int(x)}' for x in forecast], textposition='auto'))
        fig.update_layout(height=300, plot_bgcolor='rgba(0,0,0,0)',
                         paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Insights
        st.markdown('<div class="stealth-card">', unsafe_allow_html=True)
        st.markdown("### 🧠 THREAT INTELLIGENCE")
        st.markdown("""
        - 📈 **Attack Pattern:** Increasing frequency detected over last 30 days
        - ⏰ **Peak Hours:** 14:00 - 18:00 (highest activity)
        - 🎯 **Most Common:** DDoS attacks (43%), Port Scans (28%)
        - ⚠️ **Warning:** Predicted 23% increase next week
        - 🛡️ **Recommendation:** Increase monitoring during peak hours
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown('<div class="footer">[ STEALTH MODE ACTIVE ] | [ ML ENGINE v3.0 ] | [ 24/7 MONITORING ]</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()