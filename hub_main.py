import streamlit as st
import json
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="TEXO Hub - Central Station", page_icon="🏦", layout="wide")

# --- STYLE PREMIUM (Dark-Gold Hub) ---
st.markdown("""
<style>
    .stApp { background-color: #050C1A !important; color: #ffffff !important; }
    h1, h2, h3, h4, h5, h6, p, span, div, li, label, .stMarkdown { color: #ffffff !important; }
    
    .hub-header { 
        background: linear-gradient(90deg, #152A4A 0%, #050C1A 100%);
        padding: 40px;
        text-align: center;
        border-bottom: 3px solid #FFD700;
        margin-bottom: 40px;
        border-radius: 0 0 50px 50px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    
    .hub-title { color: #FFD700 !important; font-weight: 900; font-size: 48px; letter-spacing: 2px; }
    .hub-subtitle { color: #888 !important; font-size: 18px; margin-top: 10px; }

    .app-card {
        background: #152A4A;
        border: 1px solid rgba(255, 215, 0, 0.2);
        border-radius: 20px;
        padding: 25px;
        height: 280px;
        transition: 0.3s ease-in-out;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        margin-bottom: 20px;
    }
    .app-card:hover {
        border: 1px solid #FFD700;
        box-shadow: 0 0 25px rgba(255, 215, 0, 0.2);
        transform: translateY(-5px);
    }
    
    .app-icon { font-size: 50px; margin-bottom: 15px; }
    .app-name { color: #FFD700 !important; font-weight: 800; font-size: 22px; margin-bottom: 10px; }
    .app-desc { color: #cccccc !important; font-size: 14px; line-height: 1.5; }
    
    .launch-btn {
        background: transparent !important;
        color: #FFD700 !important;
        border: 2px solid #FFD700 !important;
        border-radius: 10px;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-weight: bold;
        margin-top: 20px;
        transition: 0.2s;
    }
    .launch-btn:hover {
        background: #FFD700 !important;
        color: #050C1A !important;
    }
</style>
""", unsafe_allow_html=True)

# --- AUTHENTICATION REMOVED BY USER REQUEST ---
# Initial authentication block removed for GitHub deployment.


# --- HEADER ---
st.markdown("""
<div class="hub-header">
    <div class="hub-title">🏦 TEXO HUB</div>
    <div class="hub-subtitle">Trạm Điều Khiển Trung Tâm | Cổng kết nối Hệ sinh thái Công cụ TEXO</div>
</div>
""", unsafe_allow_html=True)

# --- LOAD CONFIG ---
def load_apps():
    try:
        with open('apps_config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

apps = load_apps()

# --- DASHBOARD GRID ---
st.markdown("### 🛠 PHÂN HỆ TIỆN ÍCH")

# Chia lưới 3 cột
cols = st.columns(3)

for i, app in enumerate(apps):
    with cols[i % 3]:
        # Mỗi card là một container
        st.markdown(f"""
        <div class="app-card">
            <div>
                <div class="app-icon">{app['icon']}</div>
                <div class="app-name">{app['name']}</div>
                <div class="app-desc">{app['description']}</div>
            </div>
            <a href="{app['url']}" target="_blank" class="launch-btn">🚀 CHẠY ONLINE</a>
            <a href="{app['local_url']}" target="_blank" style="font-size: 11px; color: #555; display: block; margin-top: 5px; text-decoration: none;">Chạy Local (Máy chủ)</a>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("<p class='footer' style='text-align: center; color: #444;'>© 2026 TEXO Engineering Department | Trưởng phòng: Hoàng Đức Vũ</p>", unsafe_allow_html=True)
