import streamlit as st
from PIL import Image
import os

# --- Page config ---
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉", layout="centered")

# --- Custom CSS for background, text, animations, and realistic gold confetti ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
        color: black;
        overflow-x: hidden;
    }

    .gallery-caption {
        margin-top: 5px;
        font-size: 0.95rem;
        color: #333;
    }

    .main-message {
        text-align: center;
        margin: 40px 20px;
        font-size: 1.2rem;
        line-height: 1.6;
        color: #000;
    }

    /* Realistic gold confetti */
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
        transform: rotate(0deg);
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

        // Random size
        const size = Math.random() * 8 + 4; // 4px to 12px
        confetti.style.width = size + 'px';
        confetti.style.height = size + 'px';

        // Random horizontal position
        confetti.style.left = Math.random() * 100 + 'vw';

        // Random animation duration and delay
        const duration = 3 + Math.random() * 3; // 3s to 6s
        const delay = Math.random() * 5; // delay start
        confetti.style.animation = `fall ${duration}s linear ${delay}s infinite`;

        // Append to container
        confettiContainer.appendChild(confetti);
    }
    </script>
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
        col.image(image, use_column_width=True)
        col.markdown(f"<div class='gallery-caption'>{msg}</div>", unsafe_allow_html=True)
    else:
        col.warning(f"Image not found: {img_path}")

# --- Central Main Message ---
main_message = """
<p class="main-message">
May the light of the Lord shine upon you and grant you happiness on this birthday and for many years to come.<br><br>
“Delight yourself in the Lord, and He will give you the desires of your heart.” —Psalm 37:4<br>
“The Lord will guide you always; He will satisfy your needs in a sun-scorched land and will strengthen your frame.” —Isaiah 58:11
</p>
"""
st.markdown(main_message, unsafe_allow_html=True)

# --- Videos Side by Side ---
video_files = ["videos/video1.mp4", "videos/video2.mp4"]
cols_videos = st.columns(len(video_files))
for col, vid in zip(cols_videos, video_files):
    if os.path.exists(vid):
        col.video(vid, format="video/mp4", start_time=0)
    else:
        col.warning(f"Video not found: {vid}")
# --- Closing line ---
st.markdown("<h3 style='text-align: center;'> Here's to many more beautiful memories! </h3>", unsafe_allow_html=True)

