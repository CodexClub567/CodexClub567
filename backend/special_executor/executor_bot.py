import os
from dotenv import load_dotenv
from services import script_generator, fact_checker, audio_processor, seo_optimizer, youtube_analytics

load_dotenv()  # Load environment variables from .env

def main():
    """
    Main function to orchestrate the video creation process.
    """
    openai_key = os.getenv("OPENAI_API_KEY")
    gemini_key = os.getenv("GEMINI_API_KEY") # Optional
    elevenlabs_key = os.getenv("ELEVENLABS_API_KEY")
    youtube_key = os.getenv("YOUTUBE_API_KEY")

    # 1. Generate Script
    script_content = script_generator.generate_script(openai_key, gemini_key, topic="Old Money Luxury Lifestyle")  # Pass Gemini key

    if not script_content:
        print("Failed to generate script.")
        return

    print("Script generated successfully:\n", script_content)

    # 2. Fact Check
    facts_checked_script = fact_checker.check_facts(script_content)
    if not facts_checked_script:
        print("Failed to fact-check script.")
        return
    print("Script fact-checked:\n", facts_checked_script)

    # 3. Generate Audio
    audio_file_path = audio_processor.generate_audio(elevenlabs_key, facts_checked_script)
    if not audio_file_path:
        print("Failed to generate audio.")
        return
    print(f"Audio file generated: {audio_file_path}")

    # 4. Generate SEO Metadata
    metadata = seo_optimizer.generate_metadata(script_content)
    if not metadata:
        print("Failed to generate SEO metadata.")
        return
    print("SEO Metadata generated:\n", metadata)

    # 5. Get YouTube Analytics (Simplified - requires a video ID)
    # This is a placeholder.  You'd need a way to get the video ID.
    video_id = "YOUR_VIDEO_ID"  # Replace with a real video ID
    if video_id: # only runs if a video ID is provided.
      analytics = youtube_analytics.get_analytics(youtube_key, video_id)
      if analytics:
          print("YouTube Analytics:\n", analytics)
      else:
          print("Failed to retrieve YouTube analytics.")

if __name__ == "__main__":
    main()
