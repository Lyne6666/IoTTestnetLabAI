# test_iottestnetlabai.py
"""
Tests for IoTTestnetLabAI module.
"""

import unittest
from iottestnetlabai import IoTTestnetLabAI

class TestIoTTestnetLabAI(unittest.TestCase):
    """Test cases for IoTTestnetLabAI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        # Create an instance of IoTTestnetLabAI and verify it's an instance of the class
        instance = IoTTestnetLabAI()
        self.assertIsInstance(instance, IoTTestnetLabAI)
        
    def test_run_method(self):
        """Test the run method."""
        # Create an instance of IoTTestnetLabAI and verify the run method returns True
        instance = IoTTestnetLabAI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    # Run the unit tests
    unittest.main()