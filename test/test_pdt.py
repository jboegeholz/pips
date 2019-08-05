import sys
import unittest
import pipdeptree
from unittest.mock import patch

from pip._internal.utils.misc import get_installed_distributions


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_something(self):
        test_args = ["pipdeptree", "--package", "flask"]
        with patch.object(sys, 'argv', test_args):
            args = pipdeptree._get_args()
            pkgs = get_installed_distributions(local_only=args.local_only,
                                               user_only=args.user_only)

            dist_index = pipdeptree.build_dist_index(pkgs)
            tree = pipdeptree.construct_tree(dist_index)
            for entry in tree:
                if entry.key == "flask":
                    print(entry)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
