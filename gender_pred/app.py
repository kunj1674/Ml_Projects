import streamlit as st
import math

# Configure the page layout and UI
st.set_page_config(page_title="Gender Prediction Dashboard", page_icon="🔮", layout="centered")

# Custom CSS for a sleek, high-contrast Dark UI/UX
st.markdown("""
<style>
    /* Main deep gradient background */
    .stApp {
        background-color: #0f172a;
        background-image: radial-gradient(circle at 50% 0%, #1e293b 0%, #0f172a 80%);
    }
    
    /* Force all text, labels, and markdown to be a visible light color */
    .stMarkdown, p, label, span {
        color: #f8fafc !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }

    /* Gradient Title styling */
    .main-title {
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 800;
        font-size: 3rem !important;
        background: linear-gradient(90deg, #a855f7, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }
    
    .emoji-container {
        text-align: center;
        font-size: 3.5rem;
        margin-bottom: -15px;
    }

    .sub-title {
        color: #94a3b8 !important;
        text-align: center;
        font-size: 18px !important;
        margin-top: 5px;
        margin-bottom: 40px;
        font-weight: 400 !important;
    }

    /* Glowing Prediction Result Cards */
    .prediction-card-m {
        background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
        border: 2px solid #38bdf8;
        padding: 25px;
        border-radius: 12px;
        color: #ffffff !important;
        text-align: center;
        font-size: 28px !important;
        font-weight: bold;
        box-shadow: 0 10px 25px -5px rgba(14, 165, 233, 0.5);
        margin-top: 20px;
    }
    .prediction-card-f {
        background: linear-gradient(135deg, #db2777 0%, #be185d 100%);
        border: 2px solid #f472b6;
        padding: 25px;
        border-radius: 12px;
        color: #ffffff !important;
        text-align: center;
        font-size: 28px !important;
        font-weight: bold;
        box-shadow: 0 10px 25px -5px rgba(236, 72, 153, 0.5);
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Dashboard Headers
st.markdown("<div class='emoji-container'>🔮</div>", unsafe_allow_html=True)
st.markdown("<h1 class='main-title'>Gender Prediction AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Select behavioral preferences to run the prediction model</p>", unsafe_allow_html=True)

# 1. Provide UI selections inside a styled container
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        color = st.selectbox("🎨 Favorite Color", ['Cool', 'Neutral', 'Warm'])
        music = st.selectbox("🎵 Favorite Music Genre", ['Rock', 'Hip hop', 'Folk/Traditional', 'Jazz/Blues', 'Pop', 'Electronic', 'R&B and soul'])
    with col2:
        beverage = st.selectbox("☕ Favorite Beverage", ['Vodka', 'Wine', 'Whiskey', "Doesn't drink", 'Beer', 'Other'])
        soft_drink = st.selectbox("🥤 Favorite Soft Drink", ['7UP/Sprite', 'Coca Cola/Pepsi', 'Fanta', 'Other'])

st.markdown("<br>", unsafe_allow_html=True)

# 2. Prediction Button and Logic
if st.button("Predict Gender", use_container_width=True):
    # Hardcoded model coefficients (derived directly from your dataset to avoid DLL errors)
    weights = {
        'Color_Cool': 0.1749, 'Color_Neutral': 0.1094, 'Color_Warm': -0.2845,
        'Music_Electronic': 0.5891, 'Music_Folk/Traditional': -0.1485, 'Music_Hip hop': 0.9772,
        'Music_Jazz/Blues': -0.5031, 'Music_Pop': -1.1725, 'Music_R&B and soul': 0.3913, 'Music_Rock': -0.1338,
        'Bev_Beer': -0.0884, 'Bev_Doesn\'t drink': 0.3429, 'Bev_Other': -0.1771, 
        'Bev_Vodka': 0.1561, 'Bev_Whiskey': -0.1278, 'Bev_Wine': -0.1060,
        'Soda_7UP/Sprite': -0.2671, 'Soda_Coca Cola/Pepsi': -0.4724, 'Soda_Fanta': 0.2193, 'Soda_Other': 0.5199
    }
    intercept = 0.3179
    
    # Calculate the linear score
    score = intercept
    score += weights.get(f'Color_{color}', 0)
    score += weights.get(f'Music_{music}', 0)
    score += weights.get(f'Bev_{beverage}', 0)
    score += weights.get(f'Soda_{soft_drink}', 0)
    
    # Sigmoid function to output binary prediction (F or M)
    probability_m = 1 / (1 + math.exp(-score))
    prediction = 'M' if probability_m >= 0.5 else 'F'
    
    # Display visually stunning result cards
    st.markdown("<br>", unsafe_allow_html=True)
    if prediction == 'M':
        st.markdown("<div class='prediction-card-m'>👦 Predicted Gender: Male</div>", unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown("<div class='prediction-card-f'>👧 Predicted Gender: Female</div>", unsafe_allow_html=True)
        st.balloons()