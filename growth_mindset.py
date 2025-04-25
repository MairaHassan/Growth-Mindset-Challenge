import streamlit as st

# ------------------ Page Config ------------------
st.set_page_config(page_title="🌱 Growth Mindset Project", page_icon="🌟", layout="centered")

# ------------------ Custom CSS ------------------
st.markdown("""
    <style>
        h1, h2, h3 {
            color: #2E8B57;
        }
        .section {
            background-color: #F0FFF0;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            border-left: 6px solid #66BB6A;
        }
        .underline {
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 5px;
            margin-bottom: 15px;
            font-weight: bold;
            color: #388E3C;
        }
        .footer {
            font-style: italic;
            color: #888;
            margin-top: 30px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ App Title ------------------
st.markdown('<h1 class="underline">🌱 Growth Mindset Challenge: WEB App with Streamlit</h1>', unsafe_allow_html=True)

# ------------------ Welcome Section ------------------
with st.container():
    st.markdown("""
    <div class="section">
        <h3>🚀 Welcome to Your Growth Journey!</h3>
        <p>Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset through reflection, challenges, and achievements! 🌟</p>
    </div>
    """, unsafe_allow_html=True)

# ------------------ Quote Section ------------------
st.markdown('<h3 class="underline">💡 Today\'s Growth Mindset Quote</h3>', unsafe_allow_html=True)
st.success("“Great works are performed not by strength but by perseverance.” — *Samuel Johnson*")

# ------------------ Challenge Input ------------------
st.markdown('<h3 class="underline">🔧 What\'s Your Challenge Today?</h3>', unsafe_allow_html=True)
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"💪 You're facing: {user_input}. Keep pushing forward towards your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")

# ------------------ Reflection Section ------------------
st.markdown('<h3 class="underline">🧠 Reflect on Your Learning</h3>', unsafe_allow_html=True)
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"💡 Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow. Share your thoughts!")

# ------------------ Achievements ------------------
st.markdown('<h3 class="underline">🏆 Celebrate Your Wins!</h3>', unsafe_allow_html=True)
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🎉 Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now 🤩")

# ------------------ Footer ------------------
st.markdown("""
<div class="footer">
    🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟<br>
    <strong>© Created by Maira Hassan</strong>
</div>
""", unsafe_allow_html=True)
