import argparse
import subprocess
import sys
import os


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

            # 1. install requirement
            process = subprocess.Popen("pip install " + args.package, shell=True,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)

            # wait for the process to terminate
            out, err = process.communicate()
            errcode = process.returncode
            print(out)
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
            1# get dependencies from pipdeptree
            args = parser.parse_args(sys.argv[2:])
            print('Running pips install, package=%s' % args.package)


if __name__ == '__main__':
    Pips()
