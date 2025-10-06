import streamlit as st
from PIL import Image
import os
import time
import streamlit.components.v1 as components

# --- Page config ---
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉", layout="centered")

# --- Black Balloons ---
balloons_html = """
<style>
.balloon {
  position: absolute;
  bottom: -60px;
  width: 30px;
  height: 50px;
  background-color: black;
  border-radius: 50%;
  opacity: 0.9;
  animation: floatUp linear infinite;
}

@keyframes floatUp {
  0% { transform: translateY(0) rotate(0deg); }
  100% { transform: translateY(-100vh) rotate(360deg); }
}
</style>
<div style="position: fixed; top:0; left:0; width:100%; height:100vh; pointer-events:none; z-index:9999;" id="balloons"></div>
<script>
const container = document.getElementById('balloons');
for (let i=0; i<30; i++){
    const b = document.createElement('div');
    b.className='balloon';
    b.style.left = Math.random()*100+'vw';
    b.style.width = (20+Math.random()*20)+'px';
    b.style.height = (30+Math.random()*30)+'px';
    b.style.animationDuration = (5+Math.random()*5)+'s';
    b.style.animationDelay = Math.random()*5+'s';
    container.appendChild(b);
}
</script>
"""
components.html(balloons_html, height=600, width=0)

# --- Custom CSS ---
st.markdown("""
<style>
.stApp {
    background-color: #fff8e7;  /* Cream-white */
    color: black;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Gallery layout */
.gallery-container {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
    margin: 20px 0;
}
.gallery-frame {
    background-color: black;
    border-radius: 15px;
    padding: 10px;
    text-align: center;
    max-width: 300px;
    transition: transform 0.3s, box-shadow 0.3s;
}
.gallery-frame:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
}
.gallery-frame img {
    border-radius: 10px;
    width: 100%;
    height: auto;
}
.gallery-caption {
    margin-top: 8px;
    font-size: 0.95rem;
    color: black;  /* Keep text black */
}

/* Main message card */
.main-message {
    background-color: #fdf3d9;
    border-radius: 20px;
    padding: 25px;
    margin: 40px auto;
    max-width: 700px;
    text-align: center;
    font-size: 1.2rem;
    line-height: 1.6;
    color: black;
    box-shadow: 0 6px 20px rgba(0,0,0,0.2);
}

h1, h3 {
    color: black;
}
</style>
""", unsafe_allow_html=True)

# --- Background Music ---
music_file = "music/song.mp3"
if os.path.exists(music_file):
    with open(music_file,"rb") as f:
        st.audio(f.read(), format="audio/mp3")

# --- Title ---
st.markdown("<h1 style='text-align:center;'>Happy Birthday, Kitso! </h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Wishing you an amazing day filled with love, laughter, and joy!</h3>", unsafe_allow_html=True)

# --- Gallery Images Side by Side ---
gallery_items = [
    {"img":"images/IMG-20251006-WA0005.jpg","msg":"They say there’s no day like the present. So, cherish the day."},
    {"img":"images/IMG-20251006-WA0006.jpg","msg":"May God continue to keep you in His graces and bless you abundantly. Wishing you a happy and bountiful birthday!"},
    {"img":"images/IMG-20251006-WA0007.jpg","msg":"Wishing you divine peace and happiness today and throughout your life."}
]

st.markdown("<div class='gallery-container'>", unsafe_allow_html=True)
for item in gallery_items:
    if os.path.exists(item["img"]):
        img = Image.open(item["img"])
        st.markdown("<div class='gallery-frame'>", unsafe_allow_html=True)
        st.image(img, use_container_width=True)
        st.markdown(f"<div class='gallery-caption'>{item['msg']}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        time.sleep(0.5)
    else:
        st.warning(f"Image not found: {item['img']}")
st.markdown("</div>", unsafe_allow_html=True)

# --- Main Message ---
st.markdown("""
<div class='main-message'>
May the light of the Lord shine upon you and grant you happiness on this birthday and for many years to come.<br><br>
“Delight yourself in the Lord, and He will give you the desires of your heart.” —Psalm 37:4<br>
“The Lord will guide you always; He will satisfy your needs in a sun-scorched land and will strengthen your frame.” —Isaiah 58:11
</div>
""", unsafe_allow_html=True)

# --- Video with Custom Message ---
video_file = "videos/video1.mp4"
if os.path.exists(video_file):
    st.video(video_file, format="video/mp4", start_time=0)
    st.markdown("<h3 style='text-align:center;'>CAN'T WAIT TO SEE YOU REACH EVEN GREATER HEIGHTS, PROUD OF YOU AND ALL YOUR ACHIEVEMENTS, KEEP THRIVING</h3>", unsafe_allow_html=True)
else:
    st.warning(f"Video not found: {video_file}")

# --- Closing Line ---
st.markdown("<h3 style='text-align:center;'> Here's to many more beautiful memories! </h3>", unsafe_allow_html=True)
