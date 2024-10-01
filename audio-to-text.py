import openai
from pydub import AudioSegment
import os 
import uuid 
from dotenv import load_dotenv 

load_dotenv(dotenv_path=".env")
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPEN_API_KEY


def convert_to_mono_16k(audio_file_path, output_dir="assets"):
    """Converts audio to mono and 16kHz, returns the path to the converted audio."""
    sound = AudioSegment.from_file(audio_file_path)
    sound = sound.set_channels(1)  # Mono
    sound = sound.set_frame_rate(16000)  # 16kHz
    
    # Generate a unique filename for the mono version
    converted_file_name = f"{uuid.uuid4()}.wav"
    converted_file_path = os.path.join(output_dir, converted_file_name)

    # Export the converted audio file
    sound.export(converted_file_path, format="wav")
    return converted_file_path

def transcribe_audio(audio_file_path, clean_up=True):
    """Transcribes audio to text using OpenAI's Whisper."""
    # Convert audio to mono and 16kHz
    mono_audio_path = convert_to_mono_16k(audio_file_path)

    # Transcribe audio using OpenAI's Whisper
    with open(mono_audio_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    # Clean up the converted file if needed
    if clean_up:
        os.remove(mono_audio_path)

    return transcript['text']

# Example usage
audio_file = "assets/jackhammer.wav"
transcription = transcribe_audio(audio_file)
print("Transcription:", transcription)