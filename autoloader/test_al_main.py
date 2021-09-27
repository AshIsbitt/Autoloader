# Testing suite devised for al_main using unittest

import unittest
import unittest.mock
import al_main
import os
import json
import io
import sys

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
#        mockedFunction = al_main.viewJSONDoc()
#        mockedFunction = MagicMock()
#        mockedFunction()

#        mockedFunction.assert_called()

        #https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
        capturedOut = io.StringIO()
        sys.stdout = capturedOut
        al_main.viewJSONDoc()
        sys.stdout = sys.__stdout__

        self.assertEqual(len(capturedOut.getvalue().splitlines()), 3)
        self.assertEqual(str(capturedOut.getvalue())[0:4], 'web:')

    # test adding item to json via mocking
    def test_addItemToJSON(self):
        with patch('builtins.open', new_callable=mock_open(read_data = "{'disabed':True}")) as mockedFile:
            with open('autoloader_config.json') as fh:
                print(fh.read())

    # test removing item from json via mocking
    def test_removeItemFromJson(self):
        pass

    # Test main by testing various function calls within the func
        # Test erasing file by checking function call from main()
    def test_main(self):
        pass

if __name__ == '__main__':
    unittest.main()
