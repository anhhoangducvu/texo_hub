import streamlit as st
import json
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="TEXO Hub - Command Center", page_icon="🏦", layout="wide")

# --- STYLE PREMIUM (Dark-Gold Dashboard) ---
st.markdown("""
<style>
    /* --- TỐI ƯU HÓA CSS CHO CẢ 2 CHẾ ĐỘ (ADAPTIVE THEME) --- */
    
    .hub-header { 
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 50px 30px;
        text-align: center;
        border-bottom: 2px solid #FFD700;
        margin-bottom: 40px;
        border-radius: 0 0 40px 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .hub-title { color: #FFD700 !important; font-weight: 900; font-size: 52px; margin-bottom: 15px; }
    .hub-subtitle { color: #94a3b8 !important; font-size: 16px; font-weight: 500; }

    /* Category Headers: Tự động đổi màu chữ theo theme */
    .cat-header {
        font-size: 22px;
        font-weight: 800;
        margin: 40px 0 20px 10px;
        border-left: 5px solid #FFD700;
        padding-left: 15px;
    }

    /* Thẻ ứng dụng thông minh: Tự thích ứng Light/Dark */
    .app-card {
        background-color: var(--secondary-background-color) !important;
        border: 1px solid rgba(255, 215, 0, 0.1) !important;
        border-radius: 20px !important;
        padding: 30px !important;
        height: 220px !important;
        transition: all 0.3s ease !important;
        display: flex !important;
        flex-direction: column !important;
        justify-content: center !important;
        text-decoration: none !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
        position: relative;
        overflow: hidden;
    }
    
    .app-card:hover {
        border: 1px solid #FFD700 !important;
        box-shadow: 0 12px 25px rgba(255, 215, 0, 0.1) !important;
        transform: translateY(-8px) !important;
    }

    .app-icon { font-size: 45px; margin-bottom: 15px; }
    
    .app-name { 
        color: #FFD700 !important; 
        font-size: 22px !important; 
        font-weight: 800 !important; 
        margin-bottom: 10px !important; 
    }
    
    .app-desc { 
        font-size: 14px !important; 
        opacity: 0.8 !important; 
        line-height: 1.5 !important;
    }
    
    .app-card::after {
        content: 'TRUY CẬP 🚀';
        position: absolute;
        bottom: -30px;
        right: 20px;
        font-size: 10px;
        color: #FFD700;
        font-weight: bold;
        transition: 0.3s;
        opacity: 0;
    }
    .app-card:hover::after {
        bottom: 15px;
        opacity: 1;
    }

    .footer { text-align: center; color: #888; font-size: 12px; margin-top: 50px; border-top: 1px solid rgba(255, 215, 0, 0.2); padding-top: 20px; }
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
