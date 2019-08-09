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
        package = "Jinja2"
        sub_dependency = "MarkupSafe"
        test_args = ["pips", "install", package]
        with patch.object(sys, 'argv', test_args):
            Pips()

        self.assertTrue(os.path.exists("../venv37/Lib/site-packages/" + package.lower()))
        self.assertTrue(os.path.exists("requirements.txt"))
        self.assertTrue(os.path.exists("requirements.lock"))

        with open("requirements.txt", "r") as f:
            lines = f.readlines()
            package_found = False
            for line in lines:
                if package in line:
                    package_found = True
            self.assertTrue(package_found)

        with open("requirements.lock", "r") as f:
            lines = f.readlines()
            package_found = False
            sub_dep_found = False
            for line in lines:
                if package in line:
                    package_found = True
                if sub_dependency in line:
                    sub_dep_found = True
            self.assertTrue(package_found)
            self.assertTrue(sub_dep_found)

    def test_uninstall_package(self):
        package = "Jinja2"
        sub_dependency = "MarkupSafe"
        test_args = ["pips", "install", package]
        with patch.object(sys, 'argv', test_args):
            Pips()

        test_args = ["pips", "uninstall", package]
        with patch.object(sys, 'argv', test_args):
            Pips()

        self.assertFalse(os.path.exists("../venv37/Lib/site-packages/" + package.lower()))
        self.assertFalse(os.path.exists("../venv37/Lib/site-packages/" + sub_dependency.lower()))

    def tearDown(self) -> None:
        process = subprocess.Popen("pip uninstall --yes flask", shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        # wait for the process to terminate
        out, err = process.communicate()
        errcode = process.returncode
        print(out)
        os.remove("requirements.txt")
        os.remove("requirements.lock")


if __name__ == '__main__':
    unittest.main()
