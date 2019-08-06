import argparse
import subprocess
import sys
import os
from pip._internal import main as pipmain
import pipdeptree



class Pips:
    def __init__(self):
        parser = argparse.ArgumentParser(
            usage='''pips <command> [<args>]
        ''')
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def install(self):
        parser = argparse.ArgumentParser()
        # prefixing the argument with -- means it's optional
        parser.add_argument('package')
        if sys.argv[2:]:
            args = parser.parse_args(sys.argv[2:])
            print('Running pips install, package=%s' % args.package)

            pipmain(['install', args.package])
            # 2. add requirement to requirements.txt
            if not os.path.isfile("requirements.txt"):
                f = open("requirements.txt", "w+")
                f.close()
            with open("requirements.txt", "w") as f:
                f.writelines(args.package)
            process = subprocess.Popen("pip freeze > requirements.lock ", shell=True,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            # wait for the process to terminate
            out, err = process.communicate()
            errcode = process.returncode
            print(out)

    def uninstall(self):
        parser = argparse.ArgumentParser()
        # prefixing the argument with -- means it's optional
        parser.add_argument('package')
        if sys.argv[2:]:
            # 1 get dependencies from pipdeptree
            args = parser.parse_args(sys.argv[2:])
            print('Running pips install, package=%s' % args.package)
            # 2 run pip uninstall for every package in req
            pipmain(['uninstall', "--yes", args.package])


if __name__ == '__main__':
    Pips()
