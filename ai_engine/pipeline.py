from detection.yolo_model import detect_objects
from narration.generate_caption import generate_caption
from narration.speak import speak

def run_pipeline(frame):
    objects = detect_objects(frame)
    caption = generate_caption(objects)
    speak(caption)