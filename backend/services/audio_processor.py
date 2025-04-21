import os
from elevenlabs import generate, set_api_key

def generate_audio(elevenlabs_key, script):
    """
    Generates audio from a script using ElevenLabs.

    Args:
        elevenlabs_key: ElevenLabs API key.
        script: The script to convert to audio.

    Returns:
        The path to the generated audio file, or None on error.
    """
    set_api_key(elevenlabs_key)
    try:
        audio = generate(
            text=script,
            voice="nova",  # Choose a voice
            model="eleven_monolingual_v1" # Choose a model
        )

        # Save the audio to a file
        audio_file_path = "audio.mp3"  #  Make sure the file path is writeable
        with open(audio_file_path, "wb") as f:
            f.write(audio)
        return audio_file_path
    except Exception as e:
        print(f"Error generating audio: {e}")
        return None
