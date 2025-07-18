# test_digitalprovenance.py
"""
Tests for DigitalProvenance module.
"""

import unittest
from digitalprovenance import DigitalProvenance

class TestDigitalProvenance(unittest.TestCase):
    """Test cases for DigitalProvenance class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DigitalProvenance()
        self.assertIsInstance(instance, DigitalProvenance)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DigitalProvenance()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
