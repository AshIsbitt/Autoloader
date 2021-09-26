# Testing suite devised for al_main using unittest

import unittest
from unittest.mock import MagicMock
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

    # Test viewing file
    def test_viewJSONDoc(self):
        mockedFunction = al_main.viewJSONDoc()
        mockedFunction = MagicMock()
        mockedFunction()

        mockedFunction.assert_called()

    # test adding item to json via mocking

    # test removing item from json via mocking

    # Test main by testing various function calls within the func
        # Test erasing file by checking function call from main()

if __name__ == '__main__':
    unittest.main()
