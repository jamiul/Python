import unittest
from mspack import msmath
class MspackUnitTestCase(unittest.TestCase):
    def test_sum(self):
        sum = msmath.sum(8,14)
        self.assertEqual(sum,22)
if __name__ == '__main__':
    unittest.main()
