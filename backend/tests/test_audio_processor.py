import unittest
from unittest.mock import patch, mock_open
from services import audio_processor

class TestAudioProcessor(unittest.TestCase):

    @patch('elevenlabs.generate')
    @patch('builtins.open', new_callable=mock_open)
    def test_generate_audio(self, mock_open, mock_eleven_generate):
        # Mock the ElevenLabs response
        mock_eleven_generate.return_value = b"test audio data"
        elevenlabs_key = "test_elevenlabs_key"
        script = "Test audio script"
        audio_file_path = audio_processor.generate_audio(elevenlabs_key, script)
        self.assertEqual(audio_file_path, "audio.mp3")
        mock_open.assert_called_once_with("audio.mp3", "wb")

    def test_generate_audio_error(self):
        elevenlabs_key = "test_elevenlabs_key"
        script = "Test audio script"
        audio_file_path = audio_processor.generate_audio(elevenlabs_key, script)
        self.assertIsNone(audio_file_path)
