import streamlit as st
import json
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="TEXO Hub - Command Center", page_icon="🏦", layout="wide")

# --- STYLE PREMIUM (Dark-Gold Dashboard) ---
st.markdown("""
<style>
    .stApp { background-color: #050C1A !important; color: #ffffff !important; }
    h1, h2, h3, h4, h5, h6, p, span, div, li, label, .stMarkdown { color: #ffffff !important; }
    
    .hub-header { 
        background: linear-gradient(90deg, #152A4A 0%, #050C1A 100%);
        padding: 60px 40px;
        text-align: center;
        border-bottom: 2px solid rgba(255, 215, 0, 0.3);
        margin-bottom: 50px;
        border-radius: 0 0 60px 60px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.6);
    }
    
    .hub-title { color: #FFD700 !important; font-weight: 900; font-size: 56px; letter-spacing: 3px; margin-bottom: 10px; }
    .hub-subtitle { color: #888 !important; font-size: 18px; letter-spacing: 1px; }

    /* Category Headers */
    .cat-header {
        color: #FFD700 !important;
        font-size: 24px;
        font-weight: 800;
        margin: 40px 0 20px 10px;
        border-left: 5px solid #FFD700;
        padding-left: 15px;
    }

    /* Clickable App Card */
    .app-card {
        background: #112240;
        border: 1px solid rgba(255, 215, 0, 0.1);
        border-radius: 25px;
        padding: 30px;
        height: 240px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        display: flex;
        flex-direction: column;
        justify-content: center;
        cursor: pointer;
        text-decoration: none !important;
        position: relative;
        overflow: hidden;
    }
    
    .app-card:hover {
        border: 1px solid #FFD700;
        box-shadow: 0 10px 40px rgba(255, 215, 0, 0.15);
        transform: translateY(-8px);
        background: #152A4A;
    }
    
    .app-card::after {
        content: 'TRUY CẬP 🚀';
        position: absolute;
        bottom: -40px;
        right: 20px;
        font-size: 11px;
        color: #FFD700;
        font-weight: bold;
        transition: 0.3s;
        opacity: 0;
    }
    .app-card:hover::after {
        bottom: 20px;
        opacity: 1;
    }
    
    .app-icon { font-size: 55px; margin-bottom: 20px; }
    .app-name { color: #FFD700 !important; font-weight: 800; font-size: 24px; margin-bottom: 12px; }
    .app-desc { color: #a8b2d1 !important; font-size: 14px; line-height: 1.6; }

    .footer { text-align: center; color: #444; font-size: 13px; margin: 80px 0 40px 0; border-top: 1px solid #112240; padding-top: 30px; }
</style>
""", unsafe_allow_html=True)

# --- AUTHENTICATION REMOVED BY USER REQUEST ---
# Initial authentication block removed for GitHub deployment.

# --- HEADER ---
st.markdown("""
<div class="hub-header">
    <div class="hub-title">🏦 TEXO HUB</div>
    <div class="hub-subtitle">Phân hệ Quản trị & Điều phối Công tác Kỹ thuật | AI Ecosystem</div>
</div>
""", unsafe_allow_html=True)

# --- LOAD CONFIG ---
def load_apps():
    try:
        with open('apps_config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

apps_list = load_apps()

# --- GROUP APPS BY CATEGORY ---
categories = {}
for app in apps_list:
    cat = app.get("category", "Sản phẩm khác")
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(app)

# --- DASHBOARD GRID ---
for cat_name, apps in categories.items():
    st.markdown(f"<div class='cat-header'>{cat_name.upper()}</div>", unsafe_allow_html=True)
    
    # Chia lưới 3 cột cho mỗi category
    cols = st.columns(3)
    for i, app in enumerate(apps):
        with cols[i % 3]:
            # Tạo card clickable bằng thẻ <a> bao quanh
            st.markdown(f"""
            <a href="{app['url']}" target="_blank" style="text-decoration: none;">
                <div class="app-card">
                    <div class="app-icon">{app['icon']}</div>
                    <div class="app-name">{app['name']}</div>
                    <div class="app-desc">{app['description']}</div>
                </div>
            </a>
            """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(f"""
<div class="footer">
    © 2026 TEXO Engineering Department | Trưởng phòng: Hoàng Đức Vũ<br>
    Hệ sinh thái Công cụ AI nâng cao năng suất Tư vấn Kỹ thuật hàng đầu Việt Nam
</div>
""", unsafe_allow_html=True)
