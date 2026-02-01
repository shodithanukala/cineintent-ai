import streamlit as st
from intent_engine import extract_emotion_and_sentiment
from visual_mapper import (
    detect_cinematic_cues,
    map_visual_intent,
    generate_shot_list,
    suggest_camera_movement
)
from image_caption import generate_caption
from PIL import Image

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="CineIntent AI",
    page_icon="🎬",
    layout="centered"
)

# -------------------------
# SESSION STATE
# -------------------------
if "scene" not in st.session_state:
    st.session_state.scene = ""

if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

# -------------------------
# CSS (OLD UI + SIDEBAR ONLY)
# -------------------------
st.markdown("""
<style>

/* Main App */
.stApp {
    background-color: #0f0f14;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #141826;
    border-right: 1px solid #2a2f45;
}

section[data-testid="stSidebar"] * {
    color: #e6e6e6 !important;
}

/* Generic Card */
.card {
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    text-align: center;
    font-weight: bold;
    color: #1f1f1f;
}

/* Emotion Colors */
.fear { background-color: #ffe0e0; }
.joy { background-color: #fff9c4; }
.anger { background-color: #ffcdd2; }
.sadness { background-color: #bbdefb; }
.neutral { background-color: #e0e0e0; }
.surprise { background-color: #e1bee7; }
.disgust { background-color: #c8e6c9; }
.anxiety {
    background-color: #ffe6cc;  /* soft peach */
    color: #2b2b2b;
}


/* Sentiment Colors */
.positive { background-color: #c8e6c9; }
.negative { background-color: #ffcdd2; }

/* Strength Colors */
.high { background-color: #c8e6c9; }
.medium { background-color: #fff9c4; }
.low { background-color: #ffcdd2; }

/* Visual Planning Colors */
.camera { background-color: #e1bee7; }
.lighting { background-color: #bbdefb; }
.pacing { background-color: #fff9c4; }

h1, h2, h3 {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# SIDEBAR (COLLAPSIBLE)
# -------------------------
st.sidebar.markdown("## 🎬 CineIntent AI")
st.sidebar.markdown("---")

with st.sidebar.expander("🎯 What This Tool Does"):
    st.markdown("""
    - Understands scene emotion  
    - Detects cinematic intent  
    - Extracts implicit cues  
    - Suggests visuals & shots  
    - Assists directors & creators  
    """)

with st.sidebar.expander("⚙️ How It Works"):
    st.markdown("""
    1. Text / image input  
    2. Emotion inference  
    3. Cue detection  
    4. Visual intent mapping  
    5. Shot & movement planning  
    """)

with st.sidebar.expander("🎬 Use Cases"):
    st.markdown("""
    - Film pre-visualization  
    - Script breakdown  
    - Storyboarding  
    - Creative direction  
    - AI-assisted filmmaking  
    """)

# -------------------------
# HEADER
# -------------------------
st.title("🎬 CineIntent AI")
st.markdown("### Multimodal Scene Intent & Visual Planning Engine")
st.divider()

# -------------------------
# TEXT INPUT
# -------------------------
scene = st.text_area(
    "🎭 Enter a movie scene",
    height=120,
    placeholder="The room falls silent. He avoids eye contact before answering.",
    value=st.session_state.scene
)

st.session_state.scene = scene

analyze_text = st.button("🔍 Analyze Scene", key="analyze_text")


# -------------------------
# IMAGE INPUT
# -------------------------
st.divider()
st.markdown("### 🖼️ Image Scene Analyzer")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"],
    key="image_uploader"
)

if uploaded_file:
    st.session_state.uploaded_file = uploaded_file
    image = Image.open(uploaded_file)
    st.image(image, use_container_width=True)

    caption = generate_caption(image)
    st.info(f"📝 Generated Scene: {caption}")
    st.session_state.scene = caption
    scene = caption

col1, col2 = st.columns(2)

with col1:
    analyze_image = st.button("🔍 Analyze Scene", key="analyze_image")

# PROCESS
# -------------------------
if analyze_text or analyze_image or st.session_state.uploaded_file:
    if st.session_state.scene.strip() == "":
        st.warning("Please enter a scene.")
    else:
        emotion, sentiment, emotion_strength = extract_emotion_and_sentiment(st.session_state.scene)
        cues, matched_words = detect_cinematic_cues(st.session_state.scene)
        visuals = map_visual_intent(emotion, sentiment, cues)

        # SCENE UNDERSTANDING
        st.markdown("## 🧠 Scene Understanding")
        c1, c2, c3, c4 = st.columns(4)

        c1.markdown(f"<div class='card {emotion}'>Emotion<br>{emotion.capitalize()}</div>", unsafe_allow_html=True)
        c2.markdown(f"<div class='card {emotion_strength}'>Emotion Strength<br>{emotion_strength.capitalize()}</div>", unsafe_allow_html=True)
        c3.markdown(f"<div class='card {sentiment}'>Sentiment<br>{sentiment.capitalize()}</div>", unsafe_allow_html=True)
        c4.markdown(f"<div class='card {visuals['tension_level']}'>Tension Level<br>{visuals['tension_level'].capitalize()}</div>", unsafe_allow_html=True)

        # CONFIDENCE
        st.markdown("## 📊 Emotion Confidence")
        confidence = visuals["confidence"]

        if confidence == "high":
            st.success("High Confidence – Strong cinematic signals detected")
        elif confidence == "medium":
            st.warning("Medium Confidence – Scene interpretation is plausible")
        else:
            st.error("Low Confidence – Scene may be ambiguous")

        # VISUAL PLANNING
        st.markdown("## 🎥 Visual Planning Suggestions")
        v1, v2, v3 = st.columns(3)

        v1.markdown(f"<div class='card camera'>📷 Camera Options<br>{', '.join(visuals['camera_options'])}</div>", unsafe_allow_html=True)
        v2.markdown(f"<div class='card lighting'>💡 Lighting Options<br>{', '.join(visuals['lighting_options'])}</div>", unsafe_allow_html=True)
        v3.markdown(f"<div class='card pacing'>⏱ Pacing<br>{visuals['pacing']}</div>", unsafe_allow_html=True)

        # SHOT LIST
        st.markdown("## 🎞️ Recommended Shot List")
        shot_list = generate_shot_list(
            emotion,
            visuals["tension_level"],
            visuals["pacing"]
        )

        for i, shot in enumerate(shot_list, 1):
            st.write(f"{i}. {shot}")

        # CAMERA MOVEMENT
        st.markdown("## 🎥 Camera Movement Suggestion")
        st.info(
            suggest_camera_movement(
                emotion,
                visuals["tension_level"],
                visuals["pacing"]
            )
        )

        # CUES
        st.markdown("## 🎭 Cinematic Cues")
        if cues:
            st.write("Detected Intent Cues:", ", ".join(cues))
            st.write("Trigger Words:", ", ".join(matched_words))
        else:
            st.write("No strong cinematic cues detected.")

        # MOOD
        st.markdown("### 🎬 Scene Mood")
        st.info(visuals["mood"].capitalize())

        # REASONING
        st.markdown("### 🧩 Why this recommendation?")
        st.write(visuals["reasoning"])

        # JSON OUTPUT
        with st.expander("🔎 View Structured Output"):
            st.json({
                "scene": st.session_state.scene,
                "emotion": emotion,
                "emotion_strength": emotion_strength,
                "sentiment": sentiment,
                "cues": cues,
                **visuals,
                "shot_list": shot_list
            })
