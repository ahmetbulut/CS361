__author__ = 'ahmetbulut'

import unittest
import source.dataprocess as DP

class MyTestCase(unittest.TestCase):

    def testDataProcess(self):
        self.assertEqual(DP.getwords("<body></body>"),[])

if __name__ == '__main__':
    unittest.main()
