# test_builderquiz.py
"""
Tests for BuilderQuiz module.
"""

import unittest
from builderquiz import BuilderQuiz

class TestBuilderQuiz(unittest.TestCase):
    """Test cases for BuilderQuiz class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BuilderQuiz()
        self.assertIsInstance(instance, BuilderQuiz)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BuilderQuiz()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
