import subprocess
import sys
import os
import unittest
from pips.main import Pips
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    def test_install(self):
        test_args = ["pips", "install"]
        with patch.object(sys, 'argv', test_args):
            Pips()

    def test_install_package(self):
        package = "flask"
        test_args = ["pips", "install", package]
        with patch.object(sys, 'argv', test_args):
            Pips()

        self.assertTrue(os.path.exists("../venv37/Lib/site-packages/" + package))
        # TODO: check if flask is in the files
        self.assertTrue(os.path.exists("requirements.txt"))
        with open("requirements.txt", "r") as f:
            lines = f.readlines()
            self.assertTrue(package in lines)
        self.assertTrue(os.path.exists("requirements.lock"))
        with open("requirements.lock", "r") as f:
            lines = f.readlines()
            self.assertTrue(package in lines)


    def test_uninstall_package(self):
        test_args = ["pips", "install", "flask"]
        with patch.object(sys, 'argv', test_args):
            Pips()

        test_args = ["pips", "uninstall", "flask"]
        with patch.object(sys, 'argv', test_args):
            Pips()

        self.assertFalse(os.path.exists("../venv37/Lib/site-packages/flask"))


    def tearDown(self) -> None:
        process = subprocess.Popen("pip uninstall --yes flask", shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        # wait for the process to terminate
        out, err = process.communicate()
        errcode = process.returncode
        print(out)
        #os.remove("requirements.txt")
        #os.remove("requirements.lock")


if __name__ == '__main__':
    unittest.main()