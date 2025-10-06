import streamlit as st
from PIL import Image
import os

# --- Page config ---
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉", layout="centered")

# --- Custom CSS for background, text, and image animations ---
st.markdown(
    """
    <style>
    /* Page background and text */
    .stApp {
        background-color: white;
        color: black;
    }

    /* Image hover pop-out effect */
    .gallery-img {
        width: 100%;
        transition: transform 0.3s, box-shadow 0.3s;
        border-radius: 10px;
        margin-bottom: 20px;
    }

    .gallery-img:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
    }

    /* Centered title */
    .title {
        text-align: center;
        color: #ff4b4b;
    }

    /* Subtext */
    .subtitle {
        text-align: center;
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

# --- Confetti (balloons) ---
st.balloons()

# --- Title and Subtext ---
st.markdown("<h1 class='title'>🎉 Happy Birthday, Sarah! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>Wishing you an amazing day filled with love, laughter, and joy!</h3>", unsafe_allow_html=True)

# --- Main Image ---
main_image_path = "images/IMG-20251006-WA0005.jpg"
if os.path.exists(main_image_path):
    main_image = Image.open(main_image_path)
    st.image(main_image, caption="Birthday Star", use_container_width=True, output_format="JPEG")
else:
    st.warning(f"Main image not found: {main_image_path}")

st.write("---")

# --- Gallery Section ---
st.write("### Some of our favorite moments:")

# Use columns for layout
col1, col2, col3 = st.columns(3)

gallery_images = [
    "images/IMG-20251006-WA0006.jpg",
    "images/IMG-20251006-WA0007.jpg",
    "images/IMG-20251006-WA0005.jpg",  # reuse main image
]

for col, img_path in zip([col1, col2, col3], gallery_images):
    if os.path.exists(img_path):
        img = Image.open(img_path)
        col.image(img, use_container_width=True, output_format="JPEG", caption=None)
        # Add class for hover effect
        col.markdown(
            f"<img src='{img_path}' class='gallery-img'>",
            unsafe_allow_html=True
        )
    else:
        col.warning(f"Image not found: {img_path}")

st.write("---")

# --- Closing Message ---
st.markdown("<h3 class='subtitle'>🎂 Here's to many more beautiful memories! ❤️</h3>", unsafe_allow_html=True)
