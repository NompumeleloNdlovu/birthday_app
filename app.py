import streamlit as st
from PIL import Image, ImageOps
import os
import time

# --- Page config ---
st.set_page_config(page_title="Happy Birthday Kitso", page_icon=None, layout="centered")

# --- Custom CSS ---
st.markdown("""
<style>
.stApp { 
    background-color: #fff8e7;  /* Cream-white background */
    color: black; 
    font-family: 'Cinzel', serif; 
}

h1 { 
    color: black; 
    font-family: 'Cinzel Decorative', cursive; 
    text-align: center; 
}

h3 { 
    color: black; 
    font-family: 'Cinzel', serif; 
    text-align: center; 
}

.main-message {
    background-color: #fff8e7; /* Same as background */
    border-radius: 0px; /* No frame */
    padding: 25px;
    margin: 40px auto;
    max-width: 700px;
    text-align: center;
    font-size: 1.2rem;
    line-height: 1.6;
    color: black;  /* Black text */
    font-family: 'Cinzel', serif;
    box-shadow: none;  /* Removed shadow */
}

.gallery-container {
    display: flex;
    justify-content: center;
}

.gallery-frame {
    background-color: black;  /* Frame back to black */
    border-radius: 15px; 
    text-align: center; 
    padding: 10px; 
    transition: transform 0.3s, box-shadow 0.3s;
    border-right: 2px solid black; /* Black line to separate images */
}

.gallery-frame:last-child {
    border-right: none; /* No border on last image */
}

.gallery-frame:hover { 
    transform: scale(1.05); 
    box-shadow: 0 10px 25px rgba(0,0,0,0.2); 
}

.gallery-caption { 
    margin-top: 10px; 
    font-weight: bold; 
    color: black;  /* Black captions */
    font-family: 'Cinzel', serif; 
}
</style>
""", unsafe_allow_html=True)

# --- Background music ---
music_file = "music/song.mp3"
if os.path.exists(music_file):
    with open(music_file, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3", start_time=0)
else:
    st.warning("Music file not found!")

# --- Title ---
st.markdown("<h1>Happy Birthday Kitso</h1>", unsafe_allow_html=True)
st.markdown("<h3>Wishing you an amazing day filled with love, laughter, and joy!</h3>", unsafe_allow_html=True)

# --- Gallery images ---
gallery_items = [
    {"img":"images/IMG-20251006-WA0005.jpg","msg":"They say there’s no day like the present. So, cherish the day."},
    {"img":"images/IMG-20251006-WA0006.jpg","msg":"May God continue to keep you in His graces and bless you abundantly. Wishing you a happy and bountiful birthday!"},
    {"img":"images/IMG-20251006-WA0007.jpg","msg":"Wishing you divine peace and happiness today and throughout your life."}
]

st.markdown("<div class='gallery-container'>", unsafe_allow_html=True)

for i, item in enumerate(gallery_items):
    if os.path.exists(item["img"]):
        img = Image.open(item["img"])
        # Fit full image into 400x300 with padding
        img = ImageOps.contain(img, (400, 300), method=Image.Resampling.LANCZOS)
        framed_img = Image.new("RGB", (400, 300), "black")  # Black frame
        framed_img.paste(img, ((400 - img.width)//2, (300 - img.height)//2))
        
        # Display image
        st.image(framed_img, use_container_width=False)
        st.markdown(f"<div class='gallery-caption'>{item['msg']}</div>", unsafe_allow_html=True)
        time.sleep(0.3)  # Sequential fade-in
    else:
        st.warning(f"Image not found: {item['img']}")

st.markdown("</div>", unsafe_allow_html=True)

# --- Main message ---
st.markdown("""
<div class='main-message'>
May the light of the Lord shine upon you and grant you happiness on this birthday and for many years to come.<br><br>
“Delight yourself in the Lord, and He will give you the desires of your heart.” —Psalm 37:4<br>
“The Lord will guide you always; He will satisfy your needs in a sun-scorched land and will strengthen your frame.” —Isaiah 58:11
</div>
""", unsafe_allow_html=True)

# --- Video with message ---
video_file = "videos/video1.mp4"
if os.path.exists(video_file):
    st.video(video_file, format="video/mp4", start_time=0)
    st.markdown("<h3 style='text-align:center;'>CAN'T WAIT TO SEE YOU REACH EVEN GREATER HEIGHTS, PROUD OF YOU AND ALL YOUR ACHIEVEMENTS, KEEP THRIVING</h3>", unsafe_allow_html=True)
else:
    st.warning(f"Video not found: {video_file}")

# --- Closing line ---
st.markdown("<h3 style='text-align:center;'>Here's to many more beautiful memories!</h3>", unsafe_allow_html=True)
