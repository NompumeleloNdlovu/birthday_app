import streamlit as st
from PIL import Image
import os

# Page config
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉", layout="centered")

# --- Custom CSS for beige background ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f5dc;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎵 Background Music
music_file = "music/song.mp3"
if os.path.exists(music_file):
    with open(music_file, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3", start_time=0)
else:
    st.warning("🎵 Music file not found!")

# 🎉 Confetti (balloons)
st.balloons()

# 🎈 Title
st.markdown(
    "<h1 style='text-align: center; color: #ff4b4b;'>🎉 Happy Birthday, Sarah! 🎉</h1>",
    unsafe_allow_html=True
)

# 🎂 Subtext
st.write("## Wishing you an amazing day filled with love, laughter, and joy!")

# 🖼 Main Image
main_image_path = "images/IMG-20251006-WA0005.jpg"
if os.path.exists(main_image_path):
    main_image = Image.open(main_image_path)
    st.image(main_image, caption="Birthday Star", use_container_width=True)
else:
    st.warning(f"Main image not found: {main_image_path}")

st.write("---")

# 📸 Gallery Section
st.write("### Some of our favorite moments:")
col1, col2, col3 = st.columns(3)

gallery_images = [
    "images/IMG-20251006-WA0006.jpg",
    "images/IMG-20251006-WA0007.jpg",
    "images/IMG-20251006-WA0005.jpg",  # reuse main image
]

for col, img_path in zip([col1, col2, col3], gallery_images):
    if os.path.exists(img_path):
        img = Image.open(img_path)
        col.image(img, use_container_width=True)
    else:
        col.warning(f"Image not found: {img_path}")

st.write("---")

# ❤️ Closing Message
st.write("### 🎂 Here's to many more beautiful memories! ❤️")
