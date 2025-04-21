from googleapiclient.discovery import build
import os

def get_analytics(youtube_key, video_id):
    """
    Retrieves view count for a given video ID using the YouTube Data API.

    Args:
        youtube_key: YouTube Data API key.
        video_id: The ID of the video.

    Returns:
        The view count, or None on error.
    """
    try:
        youtube = build('youtube', 'v3', developerKey=youtube_key)
        request = youtube.videos().list(
            part='statistics',
            id=video_id
        )
        response = request.execute()
        if response and 'items' in response and len(response['items']) > 0:
            statistics = response['items'][0]['statistics']
            view_count = statistics.get('viewCount', 0)
            return view_count
        else:
            print(f"Video not found or no statistics available for video ID: {video_id}")
            return None
    except Exception as e:
        print(f"Error retrieving YouTube analytics: {e}")
        return None
