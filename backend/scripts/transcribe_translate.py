import whisper
import os
from deep_translator import GoogleTranslator
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

audio_folder = BASE_DIR / "backend" / "db" / "audio"
output_folder = BASE_DIR / "backend" / "db" / "transcripts"

os.makedirs(output_folder, exist_ok=True)

print("Loading Whisper model...")
model = whisper.load_model("base")

for file in os.listdir(audio_folder):
    if file.endswith(".mp4") or file.endswith(".wav") or file.endswith(".m4a"):
        audio_path = os.path.join(audio_folder, file)
        print(audio_path)
        print("transcribing:", file)
        result = model.transcribe(audio_path)
        spanish_text = result["text"]
        #Save spanish
        es_file = os.path.join(output_folder, file + "_es.txt")
        with open(es_file, "w", encoding="utf-8") as f:
            f.write(spanish_text)
        
        #Translate to English
        print("Translating to English...")
        english_text = GoogleTranslator(source='auto', target='en').translate(spanish_text)
        en_file = os.path.join(output_folder, file + "_en.txt")

        with open(en_file, "w", encoding="utf-8") as f:
            f.write(english_text)
        
        print("Finished:", file)

print("All files processed.")