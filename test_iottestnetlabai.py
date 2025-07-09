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
        instance = IoTTestnetLabAI()
        self.assertIsInstance(instance, IoTTestnetLabAI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IoTTestnetLabAI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
