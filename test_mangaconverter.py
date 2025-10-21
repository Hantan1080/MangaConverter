# test_mangaconverter.py
"""
Tests for MangaConverter module.
"""

import unittest
from mangaconverter import MangaConverter

class TestMangaConverter(unittest.TestCase):
    """Test cases for MangaConverter class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MangaConverter()
        self.assertIsInstance(instance, MangaConverter)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MangaConverter()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
