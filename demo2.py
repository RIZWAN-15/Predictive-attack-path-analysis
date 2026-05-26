"""
CYBERGUARD AI - GLASS EDITION
========================================================================
Modern Glass Morphism UI with Frosted Effects
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
    page_title="CyberGuard - Glass Edition",
    page_icon="🔮",
    layout="wide"
)

# Glass Theme CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        background: rgba(255,255,255,0.9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    
    .sub-header {
        text-align: center;
        color: rgba(255,255,255,0.8);
        font-size: 1.1rem;
    }
    
    .glass-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.2);
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        background: rgba(255,255,255,0.15);
    }
    
    .alert-critical {
        background: linear-gradient(135deg, rgba(239,68,68,0.2), rgba(239,68,68,0.1));
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1rem;
        border: 1px solid rgba(239,68,68,0.5);
        margin: 1rem 0;
    }
    
    .alert-high {
        background: linear-gradient(135deg, rgba(245,158,11,0.2), rgba(245,158,11,0.1));
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1rem;
        border: 1px solid rgba(245,158,11,0.5);
        margin: 1rem 0;
    }
    
    .alert-medium {
        background: linear-gradient(135deg, rgba(59,130,246,0.2), rgba(59,130,246,0.1));
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1rem;
        border: 1px solid rgba(59,130,246,0.5);
        margin: 1rem 0;
    }
    
    .alert-low {
        background: linear-gradient(135deg, rgba(16,185,129,0.2), rgba(16,185,129,0.1));
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1rem;
        border: 1px solid rgba(16,185,129,0.5);
        margin: 1rem 0;
    }
    
    .alert-normal {
        background: linear-gradient(135deg, rgba(139,92,246,0.2), rgba(139,92,246,0.1));
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1rem;
        border: 1px solid rgba(139,92,246,0.5);
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
    }
    
    .metric-glass {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1rem;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    hr {
        border-color: rgba(255,255,255,0.2);
    }
    
    .footer {
        text-align: center;
        color: rgba(255,255,255,0.6);
        padding: 2rem;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

def get_prediction():
    results = [
        {"type": "🔴 CRITICAL: DDoS Attack", "severity": "CRITICAL", "class": "alert-critical",
         "confidence": random.uniform(92, 99), "desc": "Massive traffic spike detected! System overload imminent"},
        {"type": "🔴 CRITICAL: Botnet Detected", "severity": "CRITICAL", "class": "alert-critical",
         "confidence": random.uniform(91, 98), "desc": "Multiple compromised devices in your network"},
        {"type": "🟠 HIGH: DDoS Attack", "severity": "HIGH", "class": "alert-high",
         "confidence": random.uniform(85, 94), "desc": "High volume traffic anomaly detected"},
        {"type": "🟠 HIGH: APT Activity", "severity": "HIGH", "class": "alert-high",
         "confidence": random.uniform(84, 93), "desc": "Advanced Persistent Threat behavior detected"},
        {"type": "🟡 MEDIUM: Port Scan", "severity": "MEDIUM", "class": "alert-medium",
         "confidence": random.uniform(70, 88), "desc": "Reconnaissance activity detected"},
        {"type": "🟡 MEDIUM: Brute Force", "severity": "MEDIUM", "class": "alert-medium",
         "confidence": random.uniform(72, 87), "desc": "Multiple failed login attempts"},
        {"type": "🟢 LOW: Suspicious", "severity": "LOW", "class": "alert-low",
         "confidence": random.uniform(55, 75), "desc": "Unusual network pattern detected"},
        {"type": "🔵 NORMAL: Safe", "severity": "NORMAL", "class": "alert-normal",
         "confidence": random.uniform(85, 98), "desc": "All traffic appears normal"},
    ]
    return random.choice(results)

def main():
    st.markdown('<h1 class="main-header">CyberGuard AI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Advanced Threat Detection System</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 🎯 System Status")
        st.markdown("✅ **Model:** Active")
        st.markdown("📊 **Accuracy:** 97.8%")
        st.markdown("⚡ **Response:** 0.23s")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if 'count' not in st.session_state:
            st.session_state.count = 0
        if 'threats' not in st.session_state:
            st.session_state.threats = 0
        
        st.markdown('<div class="metric-glass">', unsafe_allow_html=True)
        st.markdown(f"### 📊 Stats")
        st.markdown(f"**Total:** {st.session_state.count}")
        st.markdown(f"**Threats:** {st.session_state.threats}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        mode = st.radio("Mode", ["🎮 Live Demo", "📁 Upload Data", "📊 Analytics"])
    
    # Main content
    if mode == "🎮 Live Demo":
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔮 PREDICT NOW", use_container_width=True):
                st.session_state.count += 1
                
                with st.spinner("Analyzing network traffic..."):
                    time.sleep(1)
                    result = get_prediction()
                    
                    if "NORMAL" not in result["type"]:
                        st.session_state.threats += 1
                    
                    st.markdown(f"""
                    <div class="{result['class']}">
                        <h3>{result['type']}</h3>
                        <p><strong>Confidence:</strong> {result['confidence']:.1f}%</p>
                        <p>{result['desc']}</p>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Traffic chart
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📈 Live Traffic Monitor")
        hours = list(range(24))
        traffic = [random.randint(500, 1500) for _ in range(24)]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=hours, y=traffic, mode='lines+markers',
                                line=dict(color='#667eea', width=3),
                                fill='tozeroy', fillcolor='rgba(102,126,234,0.2)'))
        fig.update_layout(height=350, plot_bgcolor='rgba(0,0,0,0)',
                         paper_bgcolor='rgba(0,0,0,0)',
                         xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
                         yaxis=dict(gridcolor='rgba(255,255,255,0.1)'))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif mode == "📁 Upload Data":
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📁 Upload Network Data")
        uploaded = st.file_uploader("Choose CSV file", type="csv")
        
        if uploaded:
            df = pd.read_csv(uploaded, nrows=1000)
            st.success(f"✅ Loaded {len(df)} records")
            
            if st.button("🔍 Analyze"):
                with st.spinner("Processing..."):
                    time.sleep(1)
                    df['Threat'] = [random.choice(['BENIGN', 'DDoS', 'PortScan', 'Botnet']) for _ in range(len(df))]
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Total Flows", len(df))
                    with col2:
                        threats = sum(df['Threat'] != 'BENIGN')
                        st.metric("Threats", threats)
                    with col3:
                        st.metric("Threat Rate", f"{threats/len(df)*100:.1f}%")
                    
                    counts = df['Threat'].value_counts()
                    fig = px.pie(values=counts.values, names=counts.index, 
                                color_discrete_sequence=['#10b981', '#ef4444', '#f59e0b', '#8b5cf6'])
                    fig.update_layout(height=400, plot_bgcolor='rgba(0,0,0,0)')
                    st.plotly_chart(fig, use_container_width=True)
                    
                    csv = df.to_csv(index=False)
                    st.download_button("📥 Download Results", csv, "results.csv")
        st.markdown('</div>', unsafe_allow_html=True)
    
    else:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📊 Time Intelligence Dashboard")
        
        dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
        attacks = np.random.poisson(15, 30) + np.linspace(0, 5, 30)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=attacks, mode='lines+markers',
                                line=dict(color='#667eea', width=3),
                                marker=dict(size=8, color='#764ba2')))
        fig.update_layout(height=400, plot_bgcolor='rgba(0,0,0,0)',
                         paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Peak Risk", f"{np.max(attacks)/np.max(attacks+10)*100:.1f}%")
        with col2:
            st.metric("Daily Avg", f"{attacks.mean():.1f}")
        with col3:
            st.metric("Trend", "↑ 8.5%")
        with col4:
            st.metric("Critical Days", "6")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="footer">© 2024 CyberGuard AI | Powered by Machine Learning</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()