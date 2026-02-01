# ----------------- CINEMATIC CUE DETECTION -----------------
def detect_cinematic_cues(text):
    text = text.lower()

    cues = {
        "silence": ["silent", "silence", "pause", "paused", "still", "wait", "waiting"],
        "discomfort": ["avoid", "avoids", "forced", "nervous", "uneasy", "awkward"],
        "tension": ["hesitate", "grip", "tight", "shake", "stare"],
        "emotion_release": ["laugh", "cry", "smile", "scream"]
    }

    detected = []
    matched_words = []

    for cue, keywords in cues.items():
        for word in keywords:
            if word in text:
                detected.append(cue)
                matched_words.append(word)

    return list(set(detected)), list(set(matched_words))


# ----------------- INTENSITY -----------------
def calculate_intensity(cues):
    if len(cues) >= 2:
        return "high"
    if len(cues) == 1:
        return "medium"
    return "low"


# ----------------- CONFIDENCE -----------------
def calculate_confidence(cues, emotion):
    score = 0

    if len(cues) >= 2:
        score += 2
    elif len(cues) == 1:
        score += 1

    if emotion != "neutral":
        score += 1

    if score >= 3:
        return "high"
    elif score == 2:
        return "medium"
    else:
        return "low"


# ----------------- VISUAL MAPPING -----------------
def map_visual_intent(emotion, sentiment, cues):
    intensity = calculate_intensity(cues)
    confidence = calculate_confidence(cues, emotion)

    # Silence + discomfort → tense anticipation
    if "silence" in cues and "discomfort" in cues:
        return {
            "camera_options": ["close-up", "static shot"],
            "lighting_options": ["dim", "low-key"],
            "pacing": "very slow",
            "mood": "tense anticipation",
            "tension_level": intensity,
            "confidence": confidence,
            "reasoning": "Detected silence and discomfort indicating internal tension and anticipation."
        }

    # Strong tension
    if "tension" in cues or "discomfort" in cues:
        return {
            "camera_options": ["close-up"],
            "lighting_options": ["low-key"],
            "pacing": "slow",
            "mood": "tense",
            "tension_level": intensity,
            "confidence": confidence,
            "reasoning": "Detected behavioral cues indicating discomfort or tension."
        }

    # Silence alone
    if "silence" in cues:
        return {
            "camera_options": ["static shot", "wide shot"],
            "lighting_options": ["dim"],
            "pacing": "very slow",
            "mood": "anticipation",
            "tension_level": intensity,
            "confidence": confidence,
            "reasoning": "Silence suggests anticipation and emotional pause."
        }

    # Emotion fallback (serious)
    if emotion in ["fear", "sadness", "anger", "disgust"]:
        return {
            "camera_options": ["close-up"],
            "lighting_options": ["low-key"],
            "pacing": "slow",
            "mood": "serious",
            "tension_level": intensity,
            "confidence": confidence,
            "reasoning": "Emotion analysis suggests a serious or intense scene."
        }

    # Positive emotions
    if emotion in ["joy", "surprise"]:
        return {
            "camera_options": ["wide shot", "medium shot"],
            "lighting_options": ["bright", "natural"],
            "pacing": "fast",
            "mood": "uplifting",
            "tension_level": "low",
            "confidence": confidence,
            "reasoning": "Positive emotion detected."
        }

    # Default fallback
    return {
        "camera_options": ["medium shot"],
        "lighting_options": ["natural"],
        "pacing": "moderate",
        "mood": "neutral",
        "tension_level": "low",
        "confidence": confidence,
        "reasoning": "No strong cinematic signals detected."
    }
# ----------------- CINEMATIC ENHANCEMENTS -----------------
def cinematic_enhancements(emotion, mood, pacing):
    """
    Generate soundtrack, color grading, transitions, and storyboard prompts.
    """

    # 🎵 SOUNDTRACK
    soundtrack_map = {
        "fear": "Low ambient drones, suspense strings",
        "sadness": "Soft piano, slow strings",
        "anger": "Heavy percussion, rising tension beats",
        "joy": "Light acoustic guitar, uplifting melodies",
        "surprise": "Sudden orchestral hits, dynamic cues",
        "neutral": "Minimal ambient background"
    }

    soundtrack = soundtrack_map.get(emotion, "Minimal ambient background")

    # 🎨 COLOR GRADING
    color_grading_map = {
        "fear": "Cool blue tones, low saturation",
        "sadness": "Desaturated colors, soft shadows",
        "anger": "High contrast, warm tones",
        "joy": "Bright vibrant colors, warm highlights",
        "surprise": "Dynamic contrast shifts",
        "neutral": "Natural tones"
    }

    color_grading = color_grading_map.get(emotion, "Natural tones")

    # 🎞️ SHOT TRANSITIONS
    if pacing == "very slow":
        transitions = "Fade-in / Fade-out"
    elif pacing == "slow":
        transitions = "Cross dissolve"
    elif pacing == "fast":
        transitions = "Quick cuts"
    else:
        transitions = "Standard cut"

    # 📽️ STORYBOARD PROMPT
    storyboard_prompt = (
        f"A cinematic scene showing {mood} mood with {emotion} emotion, "
        f"shot with {pacing} pacing, dramatic lighting, expressive character focus."
    )

    return {
        "soundtrack": soundtrack,
        "color_grading": color_grading,
        "transitions": transitions,
        "storyboard_prompt": storyboard_prompt
    }
# ----------------- SHOT LIST GENERATOR -----------------
def generate_shot_list(emotion, tension, pacing):
    """
    Generate a recommended cinematic shot list.
    """

    shots = []

    if tension == "high":
        shots.append("Extreme close-up to capture emotional intensity")
        shots.append("Over-the-shoulder shot to build tension")
    elif tension == "medium":
        shots.append("Medium close-up for character focus")
        shots.append("Static reaction shot for subtle emotion")
    else:
        shots.append("Wide establishing shot")
        shots.append("Natural interaction shot")

    if pacing in ["very slow", "slow"]:
        shots.append("Lingering static shot to emphasize mood")
    else:
        shots.append("Quick cut shot for dynamic flow")

    if emotion in ["fear", "sadness"]:
        shots.append("Close-up on facial expressions")
    elif emotion == "joy":
        shots.append("Wide group shot to show shared emotion")

    return shots
# ----------------- CAMERA MOVEMENT SUGGESTIONS -----------------
def suggest_camera_movement(emotion, tension, pacing):
    """
    Suggest camera movements based on emotional tone.
    """

    if tension == "high":
        return "Handheld camera for instability and tension"

    if emotion in ["fear", "sadness"]:
        return "Slow push-in toward character to build emotional depth"

    if emotion == "joy":
        return "Smooth tracking shot to capture positive energy"

    if pacing in ["very slow", "slow"]:
        return "Static camera to emphasize silence and mood"

    return "Natural camera movement"
