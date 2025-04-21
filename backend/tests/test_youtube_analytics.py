import unittest
from unittest.mock import patch
from services import youtube_analytics

class TestYoutubeAnalytics(unittest.TestCase):

    @patch('googleapiclient.discovery.build')
    def test_get_analytics(self, mock_build):
        # Mock the YouTube API response
        mock_youtube = mock_build.return_value
        mock_youtube.videos().list.return_value.execute.return_value = {
            'items': [
                {
                    'statistics': {
                        'viewCount': '12345'
                    }
                }
            ]
        }
        youtube_key = "test_youtube_key"
        video_id = "test_video_id"
        view_count = youtube_analytics.get_analytics(youtube_key, video_id)
        self.assertEqual(view_count, '12345')

    @patch('googleapiclient.discovery.build')
    def test_get_analytics_no_video(self, mock_build):
        # Mock the YouTube API response for a video not found
        mock_youtube = mock_build.return_value
        mock_youtube.videos().list.return_value.execute.return_value = {
            'items': []
        }
        youtube_key = "test_youtube_key"
        video_id = "test_video_id"
        view_count = youtube_analytics.get_analytics(youtube_key, video_id)
        self.assertIsNone(view_count)

    @patch('googleapiclient.discovery.build')
    def test_get_analytics_error(self, mock_build):
        # Mock an error
        mock_youtube = mock_build.return_value
        mock_youtube.videos().list.return_value.execute.side_effect = Exception("API Error")
        youtube_key = "test_youtube_key"
        video_id = "test_video_id"
        view_count = youtube_analytics.get_analytics(youtube_key, video_id)
        self.assertIsNone(view_count)
