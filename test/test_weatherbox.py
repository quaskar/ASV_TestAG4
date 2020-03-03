import unittest
import test_utils


class TestWeatherbox(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        Setup UDP socket and record 10 seconds of NMEA data
        """
        super(TestWeatherbox, self).setUpClass()


if __name__ == '__main__':
    unittest.main()
