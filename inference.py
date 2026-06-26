import torch
import random

# Simulated model inference for initial setup
def predict_emotions(student_text):
    """
    Takes raw student text and returns a dictionary of emotional probabilities
    """
    # Lowercase the text to make parsing easy
    text_lower = student_text.lower()

    # Rule-based fallback keywords
    if "stuck" in text_lower or "lost" in text_lower or "don't understand" in text_lower:
        return {"Confused": 0.80, "Frustrated": 0.15, "Bored": 0.01, "Confident": 0.01, "Curious": 0.03}
    elif "boring" in text_lower or "tired" in text_lower:
        return {"Confused": 0.05, "Frustrated": 0.10, "Bored": 0.80, "Confident": 0.01, "Curious": 0.04}

    # Default mixed breakdown if no clear keywords hit
    return {
        "Confused": round(random.uniform(0.1, 0.4), 2),
        "Frustrated": round(random.uniform(0.1, 0.3), 2),
        "Bored": round(random.uniform(0.0, 0.2), 2),
        "Confident": round(random.uniform(0.0, 0.2), 2),
        "Curious": round(random.uniform(0.2, 0.5), 2)
    }