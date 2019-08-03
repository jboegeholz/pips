import argparse
import sys


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


if __name__ == '__main__':
    Pips()
