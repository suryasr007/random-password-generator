"""
Test Cases for random password generator
"""

import unittest
from password_generator import PasswordGenerator

class TestRPG(unittest.TestCase):

    def test_generate(self):
        """Test generate() without specifying any attribute"""
        pg = PasswordGenerator()
        self.assertTrue(6 <= len(pg.generate()) <= 16)

    def test_generate_with_different_length(self):
        """Test generate() for fixed length"""
        pg = PasswordGenerator()
        length = 16
        pg.minlen = length
        pg.maxlen = length
        self.assertEqual(len(pg.generate()), length)
    
    def test_exclude_chars(self):
        """Test generate() for excluding chars"""
        pg = PasswordGenerator()
        pg.excludeuchars="A"
        self.assertNotIn("A",pg.generate())


if __name__ == '__main__':
    unittest.main()
