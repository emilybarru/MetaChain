# test_metachain.py
"""
Tests for MetaChain module.
"""

import unittest
from metachain import MetaChain

class TestMetaChain(unittest.TestCase):
    """Test cases for MetaChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaChain()
        self.assertIsInstance(instance, MetaChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
