# 🎬 CineIntent AI

**Multimodal Scene Intent & Visual Planning Engine**

CineIntent AI is an intelligent cinematic analysis tool that translates implicit storytelling signals from movie scripts into structured visual planning outputs. It bridges the gap between written narratives and visual execution by extracting emotional context, mood, and cinematic intent from scene descriptions.

---

## 📋 Table of Contents

- [The Problem](#the-problem)
- [Our Solution](#our-solution)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Use Cases](#use-cases)
- [Technical Architecture](#technical-architecture)
- [Examples](#examples)
- [Team](#team)
- [License](#license)

---

## 🎯 The Problem

Movie scripts primarily describe dialogue and actions, but scene intent (emotion, mood, visual tone) is often **implicit**. This creates challenges:

- **Inconsistent storyboards** - Different interpretations of the same scene
- **Unclear visual planning** - Ambiguity in camera, lighting, and pacing decisions
- **Longer pre-production time** - Directors and AI tools must manually infer creative intent

---

## 💡 Our Solution

**CineIntent AI** is a multimodal cinematic intelligence layer that:

1. **Analyzes script text** to extract emotional state, narrative intent, and visual tone
2. **Detects subtle cues** like silence, hesitation, tension, and discomfort
3. **Translates implicit signals** into structured visual planning outputs
4. **Provides actionable recommendations** for camera framing, lighting, pacing, and mood

CineIntent AI acts as an **intent-translation layer** between written scripts and visual generation tools, enabling consistent creative interpretation.

---

## ✨ Features

### 🧠 Scene Understanding
- **Emotion Detection** - Identifies primary emotion (fear, joy, anger, sadness, etc.)
- **Sentiment Analysis** - Classifies overall sentiment (positive, negative, neutral)
- **Emotion Strength** - Measures intensity (high, medium, low)
- **Tension Level** - Calculates scene tension based on cinematic cues

### 🎭 Cinematic Cue Detection
- Detects implicit cues: silence, discomfort, tension, emotion release
- Identifies trigger words that signal specific moods
- Context-aware analysis beyond simple keyword matching

### 🎥 Visual Planning
- **Camera Options** - Recommends shot types (close-up, wide shot, medium shot)
- **Lighting Suggestions** - Suggests lighting style (low-key, natural, bright)
- **Pacing Recommendations** - Determines scene rhythm (very slow, slow, moderate, fast)
- **Shot List Generation** - Creates detailed shot-by-shot recommendations
- **Camera Movement** - Suggests appropriate camera movements

### 🖼️ Image Analysis
- Upload scene images for automatic caption generation
- Converts visual content into analyzable text
- Multimodal input support (text + image)

### 📊 Confidence Metrics
- Provides confidence levels for scene interpretation
- Transparent reasoning for all recommendations

---

## ⚙️ How It Works

```
Input: Script text or scene image
    ↓
AI Understanding Layer:
  • Context-aware NLU
  • Emotional reasoning
  • Subtle cue detection
    ↓
Output: Structured visual planning data
  • Camera framing
  • Lighting style
  • Pacing
  • Mood & emotion tags
  • Shot list
  • JSON output
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8+
- pip package manager
- CUDA-compatible GPU (optional, for faster inference)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/your-username/cineintent-ai.git
cd cineintent-ai
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run app.py
```

4. **Access the web interface**
```
Open your browser and navigate to: http://localhost:8501
```

---

## 📖 Usage

### Text-Based Analysis

1. Enter a movie scene description in the text area
2. Click **"🔍 Analyze Scene"**
3. View comprehensive analysis including:
   - Emotion and sentiment
   - Visual planning suggestions
   - Recommended shot list
   - Camera movement guidance

**Example Input:**
```
"He pauses before answering, avoiding eye contact. The room falls silent."
```

**Example Output:**
- **Emotion:** Anxiety
- **Sentiment:** Neutral
- **Camera:** Close-up, Static shot
- **Lighting:** Dim, Low-key
- **Pacing:** Very slow
- **Mood:** Tense anticipation

### Image-Based Analysis

1. Upload an image (JPG, JPEG, PNG)
2. System generates automatic scene caption
3. Analyzes the generated caption
4. Provides visual planning recommendations

---

## 📁 Project Structure

```
cineintent-ai/
│
├── app.py                  # Main Streamlit application
├── intent_engine.py        # Emotion & sentiment detection
├── visual_mapper.py        # Visual planning & shot recommendations
├── image_caption.py        # Image-to-text caption generation
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

### Module Descriptions

#### `app.py`
Main Streamlit interface with:
- Text and image input handlers
- Visual rendering of analysis results
- Session state management
- Collapsible sidebar with tool information

#### `intent_engine.py`
Core emotion and sentiment analysis engine:
- Multi-model emotion classification
- Sentiment analysis
- Zero-shot intent detection
- Subtle scene adjustment logic
- Emotion strength mapping

#### `visual_mapper.py`
Visual planning and cinematic recommendations:
- Cinematic cue detection
- Intensity and confidence calculation
- Camera, lighting, and pacing mapping
- Shot list generation
- Camera movement suggestions

#### `image_caption.py`
Image understanding module:
- BLIP model integration
- Scene description generation from images
- Device optimization (CUDA/CPU)

---

## 🎬 Use Cases

### 1. **AI Storyboard Generation**
Convert scene intent into visual frames automatically

### 2. **Pre-Visualization Tools**
Plan camera angles, lighting, and pacing early in production

### 3. **Director & Editor Assistants**
Provide quick creative guidance and reference points

### 4. **Generative Video Pipelines**
Act as an intent layer before AI video generation

### 5. **Script Analysis**
Analyze scripts for emotional arc and visual consistency

### 6. **Film Education**
Teach cinematography principles through automated analysis

---

## 🔧 Technical Architecture

### AI Models Used

| Component | Model | Purpose |
|-----------|-------|---------|
| Emotion Detection | `SamLowe/roberta-base-go_emotions` | Multi-label emotion classification |
| Sentiment Analysis | `cardiffnlp/twitter-roberta-base-sentiment` | 3-class sentiment detection |
| Intent Classification | `facebook/bart-large-mnli` | Zero-shot scene intent detection |
| Image Captioning | `Salesforce/blip-image-captioning-base` | Image-to-text generation |

### Processing Pipeline

1. **Input Processing** - Text normalization and preprocessing
2. **Emotion Analysis** - Multi-model emotion and sentiment extraction
3. **Cue Detection** - Pattern matching for cinematic keywords
4. **Intent Mapping** - Zero-shot classification of scene intent
5. **Visual Translation** - Mapping emotions to visual parameters
6. **Confidence Scoring** - Calculating interpretation confidence
7. **Output Generation** - Structured JSON and visual display

---

## 📊 Examples

### Example 1: Tense Scene

**Input:**
```
"She grips the edge of the table, her knuckles white. 
The silence is deafening."
```

**Output:**
- **Emotion:** Fear
- **Tension Level:** High
- **Camera:** Close-up
- **Lighting:** Low-key
- **Pacing:** Very slow
- **Detected Cues:** silence, tension

### Example 2: Joyful Scene

**Input:**
```
"They burst into laughter, the tension finally breaking."
```

**Output:**
- **Emotion:** Joy
- **Tension Level:** Low
- **Camera:** Wide shot
- **Lighting:** Bright, Natural
- **Pacing:** Fast
- **Detected Cues:** emotion_release

### Example 3: Subtle Discomfort

**Input:**
```
"He shifts in his seat, avoiding her gaze."
```

**Output:**
- **Emotion:** Anxiety
- **Tension Level:** Medium
- **Camera:** Close-up
- **Lighting:** Low-key
- **Pacing:** Slow
- **Detected Cues:** discomfort

---

## 🎓 Team

**Team Name:** Endeavor AI

**Event:** Cine AI Hackfest

**Team Members:**
- Baratam Sahith
- Nukala Shoditha

---

## 🌟 Impact

CineIntent AI provides:

- ✅ **Reduced ambiguity** in narrative interpretation
- ✅ **Accelerated workflows** through automated visual guidance
- ✅ **Consistent storytelling** across scenes and productions
- ✅ **Scalability** for films, OTT, advertisements, and short-form content
- ✅ **Enhanced collaboration** between creative professionals and AI tools

---

## 🔮 Future Enhancements

- [ ] Multi-scene analysis for narrative arc tracking
- [ ] Integration with video generation APIs
- [ ] Custom model fine-tuning for genre-specific analysis
- [ ] Storyboard image generation
- [ ] Timeline-based script analysis
- [ ] Color grading recommendations
- [ ] Soundtrack suggestions
- [ ] Export to industry-standard formats (Final Draft, Celtx)

---

## 📝 License

This project was developed for the Cine AI Hackfest. Please contact the team for licensing information.

---

## 🙏 Acknowledgments

- Hugging Face for transformer models
- Salesforce for BLIP image captioning
- Streamlit for the web framework
- The Cine AI Hackfest organizers

---

## 📧 Contact

For questions, suggestions, or collaboration opportunities, please reach out to Team Endeavor AI.

---

**CineIntent AI** - *Bridging the gap between written scripts and visual storytelling through cinematic intelligence.*
