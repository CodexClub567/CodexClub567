import unittest
from services import seo_optimizer

class TestSeoOptimizer(unittest.TestCase):

    def test_generate_metadata(self):
        script = "This is a test script for SEO optimization."
        metadata = seo_optimizer.generate_metadata(script)
        self.assertEqual(metadata["title"], "This is a test script for SEO optimization.")
        self.assertEqual(metadata["description"], "This is a test script for SEO optimization.")
        self.assertEqual(metadata["tags"], ["old money", "luxury", "lifestyle"])

    def test_generate_metadata_long_script(self):
        long_script = "This is a very long test script for SEO optimization.  It should be longer than 50 characters for the title and 150 for the description."
        metadata = seo_optimizer.generate_metadata(long_script)
        self.assertEqual(metadata["title"], "This is a very long test script for SEO optim...")
        self.assertEqual(metadata["description"], "This is a very long test script for SEO optimization.  It should be longer than 50 characters for the title and 150 for the description...")
        self.assertEqual(metadata["tags"], ["old money", "luxury", "lifestyle"])
