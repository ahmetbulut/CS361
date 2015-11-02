__author__ = 'ahmetbulut'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(False, False)
        self.assertEqual(True, False)
        self.assertEqual(True, True)
        self.assertEqual(False, True)

        self.assertGreater(4,5)



if __name__ == '__main__':
    unittest.main()
