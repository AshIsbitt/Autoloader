# Testing suite devised

import unittest
from ..autoloader.autoloader import *

class TestAutoloader(unittest.TestCase):
    def test_createJSONFile(self):
        self.assertTrue(os.path.exists('Autoloader/src/autoloader.json'))

if __name__ == '__main__':
    unittest.main()
