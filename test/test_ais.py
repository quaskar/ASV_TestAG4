import unittest
import test_utils


class TestAis(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        Setup UDP socket and record 10 seconds of NMEA data
        """
        super(TestAis, self).setUpClass()


if __name__ == '__main__':
    unittest.main()
