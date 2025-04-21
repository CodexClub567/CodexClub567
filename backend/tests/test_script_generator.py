import unittest
from unittest.mock import patch
from services import script_generator

class TestScriptGenerator(unittest.TestCase):

    @patch('openai.Completion.create')
    def test_generate_script_openai(self, mock_openai_create):
        # Mock the OpenAI response
        mock_openai_create.return_value.choices = [
            type('obj', (object,), {'text': 'Test script content'})
        ]
        openai_key = "test_openai_key"
        gemini_key = None
        topic = "Test Topic"
        script = script_generator.generate_script(openai_key, gemini_key, topic)
        self.assertEqual(script, "Test script content")

    def test_generate_script_gemini(self):
        #This test will pass, but the function it tests is a placeholder.
        openai_key = "test_openai_key"
        gemini_key = "test_gemini_key"
        topic = "Test Topic"
        script = script_generator.generate_script(openai_key, gemini_key, topic)
        self.assertEqual(script, "Gemini script generation is a placeholder.")

    def test_generate_script_error(self):
        # Mock an error
        openai_key = "test_openai_key"
        gemini_key = None
        topic = "Test Topic"
        script = script_generator.generate_script(openai_key, gemini_key, topic)
        self.assertIsNone(script)



if __name__ == '__main__':
    unittest.main()
