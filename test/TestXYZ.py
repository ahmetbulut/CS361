__author__ = 'ahmetbulut'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # adding a single test case.
        self.assertGreaterEqual(14,15)


if __name__ == '__main__':
    unittest.main()
