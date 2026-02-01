from transformers import pipeline

# -------------------------
# LOAD MODELS
# -------------------------

# Emotion classifier
emotion_classifier = pipeline(
    "text-classification",
    model="SamLowe/roberta-base-go_emotions",
    top_k=None
)

# Sentiment classifier
sentiment_classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
)

# Zero-shot intent classifier
intent_classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

# -------------------------
# LABEL MAPS
# -------------------------

sentiment_map = {
    "LABEL_0": "negative",
    "LABEL_1": "neutral",
    "LABEL_2": "positive"
}

intent_labels = [
    "romance",
    "celebration",
    "sadness",
    "conflict",
    "suspense",
    "reconciliation",
    "anticipation",
    "neutral"
]

intent_emotion_map = {
    "romance": "joy",
    "celebration": "joy",
    "sadness": "sadness",
    "conflict": "anger",
    "suspense": "fear",
    "reconciliation": "relief",
    "anticipation": "anxiety",
    "neutral": "neutral"
}

# -------------------------
# EMOTION STRENGTH
# -------------------------
def map_emotion_strength(score, emotion):
    if emotion == "neutral":
        return "low"

    if score >= 0.6:
        return "high"
    elif score >= 0.4:
        return "medium"
    else:
        return "low"


# -------------------------
# SUBTLE EMOTION ADJUSTMENT
# -------------------------
def adjust_emotion_for_subtle_scenes(text, emotion):
    text = text.lower()

    nervous_cues = [
        "shift", "stare", "staring",
        "avoid", "wait", "waiting",
        "pause", "hesitate",
        "silent", "silence",
        "look down", "floor"
    ]

    if emotion == "neutral":
        for cue in nervous_cues:
            if cue in text:
                return "anxiety"

    return emotion


# -------------------------
# INTENT DETECTION
# -------------------------
def detect_scene_intent(text):
    result = intent_classifier(text, intent_labels)
    return result["labels"][0]


# -------------------------
# MAIN FUNCTION
# -------------------------
def extract_emotion_and_sentiment(text, threshold=0.35):
    """
    Returns:
    emotion, sentiment, emotion_strength
    """

    # -------------------------
    # Emotion Detection
    # -------------------------
    emotions = emotion_classifier(text)[0]
    emotions = sorted(emotions, key=lambda x: x["score"], reverse=True)

    top_emotion_data = emotions[0]
    emotion = top_emotion_data["label"].lower()
    emotion_score = top_emotion_data["score"]

    # -------------------------
    # Neutral Fallback
    # -------------------------
    if emotion_score < threshold:
        emotion = "neutral"

    # -------------------------
    # Subtle Scene Adjustment
    # -------------------------
    emotion = adjust_emotion_for_subtle_scenes(text, emotion)

    # -------------------------
    # Sentiment Detection
    # -------------------------
    sentiment_label = sentiment_classifier(text)[0]["label"]
    sentiment = sentiment_map.get(sentiment_label, "neutral")

    # -------------------------
    # Intent Detection
    # -------------------------
    intent = detect_scene_intent(text)

    if emotion == "neutral":
        emotion = intent_emotion_map.get(intent, emotion)

    # -------------------------
    # Sentiment Override
    # -------------------------
    if sentiment == "neutral" and emotion in ["disgust", "anger"]:
        emotion = "neutral"

    # -------------------------
    # Emotion Strength
    # -------------------------
    emotion_strength = map_emotion_strength(emotion_score, emotion)

    return emotion, sentiment, emotion_strength
