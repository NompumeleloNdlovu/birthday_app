import streamlit as st
from PIL import Image
import os
import streamlit.components.v1 as components

# --- Page config ---
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉", layout="centered")

# --- Realistic Gold Confetti using components.html ---
confetti_html = """
<style>
    .confetti {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 0;
        pointer-events: none;
        z-index: 9999;
    }
    .confetti-piece {
        position: absolute;
        background-color: gold;
        opacity: 0.9;
        border-radius: 2px;
    }
    @keyframes fall {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
</style>
<div class="confetti" id="confetti"></div>
<script>
const confettiContainer = document.getElementById('confetti');
const confettiCount = 120;
for (let i = 0; i < confettiCount; i++) {
    const confetti = document.createElement('div');
    confetti.className = 'confetti-piece';
    const size = Math.random() * 8 + 4;
    confetti.style.width = size + 'px';
    confetti.style.height = size + 'px';
    confetti.style.left = Math.random() * 100 + 'vw';
    const duration = 3 + Math.random() * 3;
    const delay = Math.random() * 5;
    confetti.style.animation = `fall ${duration}s linear ${delay}s infinite`;
    confettiContainer.appendChild(confetti);
}
</script>
"""

# Inject HTML + JS
components.html(confetti_html, height=0, width=0)

# --- Background Music ---
music_file = "music/song.mp3"
if os.path.exists(music_file):
    with open(music_file, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3", start_time=0)
else:
    st.warning("🎵 Music file not found!")

# --- Title ---
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'> Happy Birthday, Kitso! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Wishing you an amazing day filled with love, laughter, and joy!</h3>", unsafe_allow_html=True)

# --- Gallery Images + Messages Side by Side ---
gallery_items = [
    {"img": "images/IMG-20251006-WA0005.jpg", "message": "They say there’s no day like the present. So, cherish the day."},
    {"img": "images/IMG-20251006-WA0006.jpg", "message": "May God continue to keep you in His graces and bless you abundantly. Wishing you a happy and bountiful birthday!"},
    {"img": "images/IMG-20251006-WA0007.jpg", "message": "Wishing you divine peace and happiness today and throughout your life."}
]

cols = st.columns(len(gallery_items))
for col, item in zip(cols, gallery_items):
    img_path = item["img"]
    msg = item["message"]
    if os.path.exists(img_path):
        image = Image.open(img_path)
        col.image(image, use_container_width=True)
        col.markdown(f"<div style='text-align:center; margin-top:5px;'>{msg}</div>", unsafe_allow_html=True)
    else:
        col.warning(f"Image not found: {img_path}")

# --- Central Main Message ---
main_message = """
<p style='text-align:center; margin:40px 20px; font-size:1.2rem; line-height:1.6; color:#000;'>
May the light of the Lord shine upon you and grant you happiness on this birthday and for many years to come.<br><br>
“Delight yourself in the Lord, and He will give you the desires of your heart.” —Psalm 37:4<br>
“The Lord will guide you always; He will satisfy your needs in a sun-scorched land and will strengthen your frame.” —Isaiah 58:11
</p>
"""
st.markdown(main_message, unsafe_allow_html=True)

# --- Single Video with Custom Message ---
video_file = "videos/video1.mp4"
if os.path.exists(video_file):
    st.video(video_file, format="video/mp4", start_time=0)
    st.markdown(
        "<h3 style='text-align: center; color:#333;'>CAN'T WAIT TO SEE YOU REACH EVEN GREATER HEIGHTS, PROUD OF YOU AND ALL YOUR ACHIEVEMENTS, KEEP THRIVING</h3>",
        unsafe_allow_html=True
    )
else:
    st.warning(f"Video not found: {video_file}")

# --- Closing line ---
st.markdown("<h3 style='text-align: center;'>Here's to many more beautiful memories! </h3>", unsafe_allow_html=True)

