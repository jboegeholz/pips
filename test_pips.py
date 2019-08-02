import os
import subprocess
import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_pip_install(self):
        # pips install flask
        # 1. install requirement
        package_name = "flask"
        process = subprocess.Popen("pip install " + package_name, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        # wait for the process to terminate
        out, err = process.communicate()
        errcode = process.returncode
        for line in out:
            print(line)
        # 2. add requirement to requirements.txt
        if not os.path.isfile("requirements.txt"):
            f = open("requirements.txt", "w+")
            f.close()
        with open("requirements.txt", "w") as f:
            f.writelines(package_name)
        process = subprocess.Popen("pip freeze > requirements.lock " + package_name, shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        # wait for the process to terminate
        out, err = process.communicate()
        errcode = process.returncode
        for line in out:
            print(line)
        self.assertTrue(os.path.exists("venv37/Lib/site-packages/flask"))
        self.assertTrue(os.path.exists("requirements.txt"))
        self.assertTrue(os.path.exists("requirements.lock"))

    def tearDown(self) -> None:
        process = subprocess.Popen("pip uninstall --yes flask", shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        # wait for the process to terminate
        out, err = process.communicate()
        errcode = process.returncode
        print(out)


if __name__ == '__main__':
    unittest.main()
