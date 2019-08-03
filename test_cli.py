import sys
import unittest
from pips.main import Pips
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    def test_install(self):
        test_args = ["pips", "install"]
        with patch.object(sys, 'argv', test_args):
            Pips()

    def test_install_package(self):
        test_args = ["pips", "install", "flask"]
        with patch.object(sys, 'argv', test_args):
            Pips()



if __name__ == '__main__':
    unittest.main()
