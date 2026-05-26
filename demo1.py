"""
CYBERGUARD AI - DARK MATRIX EDITION
========================================================================
Classic Cyberpunk Style with Matrix Green Theme
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
    page_title="CyberGuard - Matrix Edition",
    page_icon="💀",
    layout="wide"
)

# Matrix Theme CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    
    .stApp {
        background: #000000;
        background-image: 
            linear-gradient(0deg, #00ff0010 1px, transparent 1px),
            linear-gradient(90deg, #00ff0010 1px, transparent 1px);
        background-size: 20px 20px;
    }
    
    .main-header {
        font-family: 'Share Tech Mono', monospace;
        font-size: 3rem;
        text-align: center;
        color: #00ff00;
        text-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00;
        letter-spacing: 5px;
        margin-bottom: 0;
        animation: glitch 3s infinite;
    }
    
    @keyframes glitch {
        0%, 100% { text-shadow: 0 0 10px #00ff00; }
        50% { text-shadow: -2px 0 #ff0000, 2px 0 #0000ff; }
    }
    
    .sub-header {
        text-align: center;
        color: #00ff00;
        font-family: monospace;
        border-bottom: 1px solid #00ff00;
        display: inline-block;
        padding-bottom: 5px;
    }
    
    .terminal-box {
        background: #000000;
        border: 1px solid #00ff00;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: 0 0 10px rgba(0,255,0,0.3);
        font-family: monospace;
    }
    
    .alert-critical {
        background: #ff000020;
        border-left: 4px solid #ff0000;
        border-radius: 3px;
        padding: 1rem;
        margin: 1rem 0;
        animation: pulse 1s infinite;
    }
    
    .alert-high {
        background: #ff660020;
        border-left: 4px solid #ff6600;
        border-radius: 3px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .alert-medium {
        background: #ffcc0020;
        border-left: 4px solid #ffcc00;
        border-radius: 3px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .alert-low {
        background: #00ff0020;
        border-left: 4px solid #00ff00;
        border-radius: 3px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .alert-normal {
        background: #00aaff20;
        border-left: 4px solid #00aaff;
        border-radius: 3px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    .stButton > button {
        background: #000000;
        color: #00ff00;
        border: 2px solid #00ff00;
        border-radius: 0;
        font-family: monospace;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background: #00ff00;
        color: #000000;
        box-shadow: 0 0 20px #00ff00;
    }
    
    .metric-card {
        background: #000000;
        border: 1px solid #00ff00;
        border-radius: 3px;
        padding: 1rem;
        text-align: center;
        font-family: monospace;
    }
    
    .blink {
        animation: blink 1s step-end infinite;
    }
    
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
    }
    
    hr {
        border-color: #00ff00;
    }
    
    .footer {
        text-align: center;
        color: #00ff00;
        font-family: monospace;
        font-size: 0.8rem;
        padding: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def get_matrix_prediction():
    """Generate random prediction"""
    results = [
        {"type": "⚠️ CRITICAL: DDoS ATTACK", "severity": "CRITICAL", "class": "alert-critical",
         "confidence": random.uniform(92, 99), "desc": "MASSIVE TRAFFIC SPIKE | SYSTEM OVERLOAD IMMINENT"},
        
        {"type": "⚠️ CRITICAL: BOTNET DETECTED", "severity": "CRITICAL", "class": "alert-critical",
         "confidence": random.uniform(91, 98), "desc": "ZOMBIE NETWORK ACTIVE | 1000+ COMPROMISED DEVICES"},
        
        {"type": "🔴 HIGH: DDoS ATTACK", "severity": "HIGH", "class": "alert-high",
         "confidence": random.uniform(85, 94), "desc": "ANOMALY DETECTED | TRAFFIC VOLUME +500%"},
        
        {"type": "🔴 HIGH: APT DETECTED", "severity": "HIGH", "class": "alert-high",
         "confidence": random.uniform(84, 93), "desc": "ADVANCED PERSISTENT THREAT | DATA EXFILTRATION"},
        
        {"type": "🟡 MEDIUM: PORT SCAN", "severity": "MEDIUM", "class": "alert-medium",
         "confidence": random.uniform(70, 88), "desc": "RECONNAISSANCE ACTIVITY | 100+ PORTS SCANNED"},
        
        {"type": "🟡 MEDIUM: BRUTE FORCE", "severity": "MEDIUM", "class": "alert-medium",
         "confidence": random.uniform(72, 87), "desc": "LOGIN ATTEMPTS | 500+ FAILED AUTHENTICATIONS"},
        
        {"type": "🟢 LOW: SUSPICIOUS", "severity": "LOW", "class": "alert-low",
         "confidence": random.uniform(55, 75), "desc": "UNUSUAL PATTERN | CONTINUE MONITORING"},
        
        {"type": "🔵 NORMAL: SAFE", "severity": "NORMAL", "class": "alert-normal",
         "confidence": random.uniform(85, 98), "desc": "ALL SYSTEMS NORMAL | NO THREATS DETECTED"},
    ]
    
    return random.choice(results)

def main():
    st.markdown('<h1 class="main-header">> CYBERGUARD_AI.EXE</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center;"><span class="sub-header">$ INITIALIZING SECURITY PROTOCOLS...</span></p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### <span style='color:#00ff00;'>>>> SYSTEM STATUS</span>", unsafe_allow_html=True)
        st.markdown("---")
        
        st.markdown("""
        <div class="terminal-box">
            <span style="color:#00ff00;">$> SYSTEM ONLINE</span><br>
            <span style="color:#00ff00;">$> FIREWALL ACTIVE</span><br>
            <span style="color:#00ff00;">$> ML ENGINE READY</span><br>
            <span style="color:#00ff00;">$> MONITORING...</span>
        </div>
        """, unsafe_allow_html=True)
        
        if 'count' not in st.session_state:
            st.session_state.count = 0
        if 'attacks' not in st.session_state:
            st.session_state.attacks = 0
        
        st.markdown(f"""
        <div class="metric-card">
            <span style="color:#00ff00;">PREDICTIONS: {st.session_state.count}</span><br>
            <span style="color:#ff0000;">THREATS: {st.session_state.attacks}</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        mode = st.radio("MODE", ["💀 LIVE SCAN", "📁 UPLOAD DATA", "📊 ANALYTICS"], 
                       label_visibility="collapsed")
    
    # Main content
    if mode == "💀 LIVE SCAN":
        st.markdown('<div class="terminal-box">', unsafe_allow_html=True)
        st.markdown("> $> SCANNING NETWORK TRAFFIC...", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("> EXECUTE_SCAN.exe", use_container_width=True):
                st.session_state.count += 1
                
                with st.spinner("SCANNING..."):
                    time.sleep(1)
                    result = get_matrix_prediction()
                    
                    if "NORMAL" not in result["type"]:
                        st.session_state.attacks += 1
                    
                    st.markdown(f"""
                    <div class="{result['class']}">
                        <code>
                        >>> {result['type']}<br>
                        >>> CONFIDENCE: {result['confidence']:.1f}%<br>
                        >>> {result['desc']}<br>
                        >>> RECOMMENDATION: {'IMMEDIATE ACTION' if 'CRITICAL' in result['type'] else 'MONITOR'}
                        </code>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown(f"""
                <div class="terminal-box">
                    <span style="color:#00ff00;">>> SCAN COMPLETE</span><br>
                    <span style="color:#00ff00;">>> TOTAL SCANS: {st.session_state.count}</span><br>
                    <span style="color:#ff0000;">>> THREATS DETECTED: {st.session_state.attacks}</span>
                </div>
                """, unsafe_allow_html=True)
        
        # Matrix traffic animation
        st.markdown("### <span style='color:#00ff00;'>>>> TRAFFIC_MATRIX</span>", unsafe_allow_html=True)
        data = np.random.randint(0, 100, (10, 20))
        fig = go.Figure(data=go.Heatmap(z=data, colorscale='Greens', showscale=False))
        fig.update_layout(height=300, plot_bgcolor='black', paper_bgcolor='black')
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("💀 TIP: Press the button multiple times for different threat scenarios")
    
    elif mode == "📁 UPLOAD DATA":
        st.markdown('<div class="terminal-box">', unsafe_allow_html=True)
        st.markdown("> $> UPLOAD CSV FOR BATCH ANALYSIS", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        uploaded = st.file_uploader("SELECT FILE", type="csv")
        
        if uploaded:
            df = pd.read_csv(uploaded, nrows=1000)
            st.success(f"✓ LOADED: {len(df)} RECORDS")
            
            if st.button("> ANALYZE_DATA.exe"):
                with st.spinner("PROCESSING..."):
                    time.sleep(1)
                    
                    df['THREAT'] = [random.choice(['BENIGN', 'DDoS', 'PORT_SCAN', 'BOTNET']) for _ in range(len(df))]
                    df['CONFIDENCE'] = [random.uniform(60, 99) for _ in range(len(df))]
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("TOTAL", len(df))
                    with col2:
                        threats = sum(df['THREAT'] != 'BENIGN')
                        st.metric("THREATS", threats)
                    with col3:
                        st.metric("AVG CONF", f"{df['CONFIDENCE'].mean():.1f}%")
                    
                    counts = df['THREAT'].value_counts()
                    fig = go.Figure(data=[go.Pie(labels=counts.index, values=counts.values, 
                                                  marker=dict(colors=['#00ff00', '#ff0000', '#ff6600', '#ffcc00']))])
                    fig.update_layout(height=400)
                    st.plotly_chart(fig, use_container_width=True)
                    
                    csv = df.to_csv(index=False)
                    st.download_button("DOWNLOAD_RESULTS.csv", csv, "results.csv")
    
    else:
        st.markdown('<div class="terminal-box">', unsafe_allow_html=True)
        st.markdown("> $> TIME INTELLIGENCE ANALYTICS", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
        attacks = np.random.poisson(15, 30) + np.linspace(0, 5, 30)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=attacks, mode='lines+markers',
                                line=dict(color='#00ff00', width=2),
                                marker=dict(color='#00ff00', size=6)))
        fig.update_layout(height=400, plot_bgcolor='black', paper_bgcolor='black',
                         xaxis=dict(gridcolor='#333'), yaxis=dict(gridcolor='#333'))
        st.plotly_chart(fig, use_container_width=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("PEAK RISK", f"{np.max(attacks)/np.max(attacks+10)*100:.1f}%")
        with col2:
            st.metric("DAILY AVG", f"{attacks.mean():.1f}")
        with col3:
            st.metric("TREND", "↑ 12.5%")
        with col4:
            st.metric("CRITICAL DAYS", "7")
        
        st.markdown("""
        <div class="terminal-box">
            <span style="color:#00ff00;">>> FORECAST: INCREASING THREAT ACTIVITY</span><br>
            <span style="color:#00ff00;">>> PEAK HOURS: 14:00 - 18:00</span><br>
            <span style="color:#ff0000;">>> ALERT: +23% NEXT WEEK</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="footer">[ SYSTEM ACTIVE ] | [ ML ENGINE v3.0 ] | [ MONITORING 24/7 ]</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()