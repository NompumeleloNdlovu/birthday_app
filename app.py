import streamlit as st
import os

# --- Page config ---
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉", layout="centered")

# --- Remove Streamlit top padding ---
st.markdown("""
    <style>
        .css-18e3th9 {padding-top: 0rem;}
        .css-1d391kg {padding-top: 0rem;}
    </style>
""", unsafe_allow_html=True)

# --- Custom CSS ---
st.markdown("""
<style>
.stApp {
    background-color: #fff8e7;
    color: black;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Horizontal gallery with black frames */
.gallery-container {
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    gap: 20px;
    padding: 10px 0;
    justify-content: flex-start;
}

.gallery-frame {
    background-color: black;
    border-radius: 15px;
    flex: 0 0 auto;
    width: 300px;
    text-align: center;
    display: flex;
    flex-direction: column;
}

.gallery-frame img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    border-radius: 10px;
}

.gallery-caption {
    padding: 10px;
    color: black;
    font-weight: bold;
    font-size: 0.95rem;
}

h1, h3 {
    color: black;
    margin-top: 10px;
    margin-bottom: 10px;
}

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
</style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='text-align:center;'>🎉 Happy Birthday, Kitso! 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Wishing you an amazing day filled with love, laughter, and joy!</h3>", unsafe_allow_html=True)

# --- Gallery images horizontally using HTML ---
gallery_items = [
    {"img":"images/IMG-20251006-WA0005.jpg","msg":"They say there’s no day like the present. So, cherish the day."},
    {"img":"images/IMG-20251006-WA0006.jpg","msg":"May God continue to keep you in His graces and bless you abundantly. Wishing you a happy and bountiful birthday!"},
    {"img":"images/IMG-20251006-WA0007.jpg","msg":"Wishing you divine peace and happiness today and throughout your life."}
]

gallery_html = "<div class='gallery-container'>"
for item in gallery_items:
    if os.path.exists(item["img"]):
        gallery_html += f"""
        <div class='gallery-frame'>
            <img src='{item["img"]}'>
            <div class='gallery-caption'>{item["msg"]}</div>
        </div>
        """
    else:
        gallery_html += f"<div class='gallery-frame'><div class='gallery-caption'>Image not found: {item['img']}</div></div>"
gallery_html += "</div>"

st.markdown(gallery_html, unsafe_allow_html=True)

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
st.markdown("<h3 style='text-align:center;'>🎂 Here's to many more beautiful memories! ❤️</h3>", unsafe_allow_html=True)

