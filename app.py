import streamlit as st
from PIL import Image
import os
import base64
import streamlit.components.v1 as components

# --- Page config ---
st.set_page_config(page_title="Happy Birthday Kitso", layout="centered")

# --- Confetti effect at the start (5 seconds) ---
components.html("""
<div id="confetti-holder"></div>
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
<script>
  function launchConfetti() {
    var duration = 5000; // 5 seconds
    var animationEnd = Date.now() + duration;
    var defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 999 };

    var interval = setInterval(function() {
      var timeLeft = animationEnd - Date.now();
      if (timeLeft <= 0) {
        clearInterval(interval);
        return;
      }
      var particleCount = 50 * (timeLeft / duration);
      confetti(Object.assign({}, defaults, {
        particleCount,
        origin: { x: Math.random(), y: Math.random() - 0.2 }
      }));
    }, 250);
  }

  // Run confetti shortly after component loads
  setTimeout(launchConfetti, 100);
</script>
""", height=50)

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
    background-color: #fff8e7; 
    border-radius: 0px; 
    padding: 25px;
    margin: 40px auto;
    max-width: 700px;
    text-align: center;
    font-size: 1.2rem;
    line-height: 1.6;
    color: black;
    font-family: 'Cinzel', serif;
    box-shadow: none;
}

.gallery-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
}

@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes captionFadeIn {
    from {opacity: 0; transform: translateY(10px);}
    to {opacity: 1; transform: translateY(0);}
}

.gallery-frame {
    background-color: #fff8e7;  /* Cream-white background */
    border-radius: 15px; 
    text-align: center; 
    padding: 10px; 
    transition: transform 0.3s, box-shadow 0.3s;
    border-right: 2px solid #f0e6d2; /* subtle cream border */
    flex: 0 0 auto;
    opacity: 0;  
    animation: fadeIn 0.8s forwards;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1); /* soft shadow */
}

.gallery-frame:hover { 
    transform: scale(1.05); 
    box-shadow: 0 15px 30px rgba(0,0,0,0.2); /* stronger shadow on hover */
}

.gallery-frame img { 
    width: 400px; 
    height: 300px; 
    object-fit: contain; 
    border-radius: 10px; 
    display: block; 
    margin: auto; 
    background-color: #fff8e7; /* match frame color */
}

.gallery-caption { 
    margin-top: 10px; 
    font-weight: bold; 
    color: black;  
    font-family: 'Cinzel', serif; 
    background-color: rgba(255, 248, 231, 0.8); /* semi-transparent cream */
    border-radius: 8px;
    padding: 5px 10px;
    display: inline-block;
    opacity: 0;  /* start hidden */
    animation: captionFadeIn 0.8s forwards;
    animation-delay: 0.5s;  /* appears slightly after the image */
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

# --- Helper: convert image to base64 ---
def image_to_base64(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")

# --- Display gallery horizontally with captions ---
st.markdown("<div class='gallery-container'>", unsafe_allow_html=True)
for item in gallery_items:
    if os.path.exists(item["img"]):
        img_b64 = image_to_base64(item["img"])
        st.markdown(f"""
        <div class='gallery-frame'>
            <img src='data:image/png;base64,{img_b64}'>
            <div class='gallery-caption'>{item['msg']}</div>
        </div>
        """, unsafe_allow_html=True)
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
