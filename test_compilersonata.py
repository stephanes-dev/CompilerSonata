# test_compilersonata.py
"""
Tests for CompilerSonata module.
"""

import unittest
from compilersonata import CompilerSonata

class TestCompilerSonata(unittest.TestCase):
    """Test cases for CompilerSonata class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CompilerSonata()
        self.assertIsInstance(instance, CompilerSonata)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CompilerSonata()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
