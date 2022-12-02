# from termcolor import colored
import unittest


class testDummy(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dummy(self):
        """descripcion"""
        self.assertFalse(
            False
        )
    # print(colored("xxx", "green"))

    # print(colored("\nTest main OK\n", "green"))
