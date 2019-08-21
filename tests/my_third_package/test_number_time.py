import pytest
# import os
# import sys

# src_dir = os.path.join(os.getcwd(), '..', '..', 'src')
# sys.path.append(src_dir)

from my_third_package.number_time import add_twenty_to_anything


class TestAddTwentyToAnything(object):

    def test_on_add_twenty_to_anything(self):

        actual = add_twenty_to_anything(5)
        expected = 25
        assert actual == expected
