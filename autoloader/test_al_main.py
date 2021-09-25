# Testing suite devised for al_main using unittest

import unittest
import al_main
import os
import json

class TestAutoloader(unittest.TestCase):

    # Test JSON file creation
    def test_createJSONFile(self):
        self.assertTrue(os.path.exists('autoloader_config.json'))

        # Open file to test if dictionary exists in file
        with open('autoloader_config.json', 'r') as f:
            self.assertEqual(f.read(1), '{')
            self.assertEqual(str(f.read())[-1], '}')

    # test each type of file being opened

if __name__ == '__main__':
    unittest.main()
