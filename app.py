import streamlit as st
from PIL import Image
import os
import time
import streamlit.components.v1 as components

# --- Page config ---
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉", layout="centered")

# --- Black Balloons with CSS/HTML ---
balloons_html = """
<style>
.balloon {
  position: absolute;
  bottom: -100px;
  width: 40px;
  height: 60px;
  background-color: black;
  border-radius: 50% 50% 50% 50%;
  opacity: 0.9;
  animation: floatUp linear infinite;
}

@keyframes floatUp {
  0% { transform: translateY(0) rotate(0deg); }
  100% { transform: translateY(-110vh) rotate(360deg); }
}
</style>

<div id="balloons"></div>
<script>
const balloonsContainer = document.getElementById('balloons');
const balloonCount = 30; // Number of balloons

for (let i = 0; i < balloonCount; i++) {
    const balloon = document.createElement('div');
    balloon.className = 'balloon';
    balloon.style.left = Math.random() * 100 + 'vw';  // random horizontal position
    balloon.style.width = (20 + Math.random() * 30) + 'px';  // random width
    balloon.style.height = (30 + Math.random() * 40) + 'px'; // random height
    balloon.style.animationDuration = (5 + Math.random() * 5) + 's'; // random speed
    balloon.style.animationDelay = Math.random() * 5 + 's';
    balloonsContainer.appendChild(balloon);
}
</script>
"""
components.html(balloons_html, height=0, width=0)

# --- Custom CSS for background and text ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fff8e7;  /* Cream white background */
        color: black;
    }
    .gallery-caption {
        margin-top: 5px;
        font-size: 0.95rem;
        color: #000;
    }
    .main-message {
        text-align: center;
        margin: 40px 20px;
        font-size: 1.2rem;
        line-height: 1.6;
        color: #000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Background Music ---
music_file = "music/song.mp3"
if os.path.exists(music_file):
    with open(music_file, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3", start_time=0)
else:
    st.warning("🎵 Music file not found!")

# --- Title ---
st.markdown("<h1 style='text-align: center; color: black;'>Happy Birthday, Kitso! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color:black;'>Wishing you an amazing day filled with love, laughter, and joy!</h3>", unsafe_allow_html=True)

# --- Gallery Images + Messages Sequentially ---
gallery_items = [
    {"img": "images/IMG-20251006-WA0005.jpg", "message": "They say there’s no day like the present. So, cherish the day."},
    {"img": "images/IMG-20251006-WA0006.jpg", "message": "May God continue to keep you in His graces and bless you abundantly. Wishing you a happy and bountiful birthday!"},
    {"img": "images/IMG-20251006-WA0007.jpg", "message": "Wishing you divine peace and happiness today and throughout your life."}
]

st.markdown("<div style='display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;'>", unsafe_allow_html=True)
placeholders = [st.empty() for _ in gallery_items]

for placeholder, item in zip(placeholders, gallery_items):
    img_path = item["img"]
    msg = item["message"]
    if os.path.exists(img_path):
        image = Image.open(img_path)
        placeholder.image(image, use_container_width=True)
        placeholder.markdown(f"<div class='gallery-caption'>{msg}</div>", unsafe_allow_html=True)
        time.sleep(1)  # 1-second delay between images
    else:
        placeholder.warning(f"Image not found: {img_path}")
st.markdown("</div>", unsafe_allow_html=True)

# --- Central Main Message ---
main_message = """
<p class="main-message">
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
        "<h3 style='text-align: center; color:black;'>CAN'T WAIT TO SEE YOU REACH EVEN GREATER HEIGHTS, PROUD OF YOU AND ALL YOUR ACHIEVEMENTS, KEEP THRIVING</h3>",
        unsafe_allow_html=True
    )
else:
    st.warning(f"Video not found: {video_file}")

# --- Closing line ---
st.markdown("<h3 style='text-align: center; color:black;'> Here's to many more beautiful memories! </h3>", unsafe_allow_html=True)

