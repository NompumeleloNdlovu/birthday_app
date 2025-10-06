import streamlit as st
from PIL import Image
import os

# --- Page config ---
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉", layout="centered")

# --- Custom CSS for background, text, animations, and gold confetti ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
        color: black;
        overflow-x: hidden;
    }

    .gallery-frame {
        text-align: center;
        padding: 10px;
        margin-bottom: 20px;
        transition: transform 0.3s, box-shadow 0.3s;
        border-radius: 15px;
    }

    .gallery-frame:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }

    .gallery-caption {
        margin-top: 10px;
        font-size: 1rem;
        color: #333;
    }

    .main-message {
        text-align: center;
        margin: 40px 20px;
        font-size: 1.2rem;
        line-height: 1.6;
        color: #000;
    }

    /* Gold confetti animation */
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
        width: 10px;
        height: 10px;
        background-color: gold;
        opacity: 0.9;
        transform: rotate(0deg);
        animation: fall 5s linear infinite;
    }
    @keyframes fall {
        0% { transform: translateY(0) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    </style>

    <div class="confetti" id="confetti"></div>

    <script>
    // Generate multiple confetti pieces
    const confettiContainer = document.getElementById('confetti');
    for (let i = 0; i < 100; i++) {
        let confetti = document.createElement('div');
        confetti.className = 'confetti-piece';
        confetti.style.left = Math.random() * 100 + 'vw';
        confetti.style.animationDuration = 3 + Math.random() * 2 + 's';
        confetti.style.width = 5 + Math.random() * 10 + 'px';
        confetti.style.height = 5 + Math.random() * 10 + 'px';
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
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎉 Happy Birthday, Kitso! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Wishing you an amazing day filled with love, laughter, and joy!</h3>", unsafe_allow_html=True)

# --- Gallery Images + Messages Side by Side ---
gallery_items = [
    {"img": "images/IMG-20251006-WA0005.jpg", "message": "They say there’s no day like the present. So, cherish the day."},
    {"img": "images/IMG-20251006-WA0006.jpg", "message": "May God continue to keep you in His graces and bless you abundantly. Wishing you a happy and bountiful birthday!"},
    {"img": "images/IMG-20251006-WA0007.jpg", "message": "Wishing you divine peace and happiness today and throughout your life."}
]

st.markdown("<div style='display: flex; justify-content: center; gap: 20px; flex-wrap: nowrap;'>", unsafe_allow_html=True)
for item in gallery_items:
    img_path = item["img"]
    msg = item["message"]
    if os.path.exists(img_path):
        st.markdown(
            f"""
            <div class="gallery-frame" style="width: 300px;">
                <img src="{img_path}" style="width: 100%; border-radius: 10px;">
                <div class="gallery-caption">{msg}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning(f"Image not found: {img_path}")
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

# --- Videos Side by Side ---
video_files = ["videos/video1.mp4", "videos/video2.mp4"]
st.markdown("<div style='display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;'>", unsafe_allow_html=True)
for vid in video_files:
    if os.path.exists(vid):
        st.video(vid, format="video/mp4", start_time=0)
    else:
        st.warning(f"Video not found: {vid}")
st.markdown("</div>", unsafe_allow_html=True)

# --- Closing line ---
st.markdown("<h3 style='text-align: center;'>🎂 Here's to many more beautiful memories! ❤️</h3>", unsafe_allow_html=True)

