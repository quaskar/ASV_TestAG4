import unittest
import test_utils


class TestBandG(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        Setup UDP socket and record 10 seconds of NMEA data
        """
        super(TestBandG, self).setUpClass()
        self.nmea_statistic = {}
        self.nmea_statistic = test_utils.Nmea.serial_stat(10)


    def test_APB_exists(self):
        self.assertTrue("APB" in self.nmea_statistic)

    def test_GBS_exists(self):
        self.assertTrue("GBS" in self.nmea_statistic)

    def test_DTM_exists(self):
        self.assertTrue("DTM" in self.nmea_statistic)

    def test_GLL_exists(self):
        self.assertTrue("GLL" in self.nmea_statistic)

    def test_RMB_exists(self):
        self.assertTrue("RMB" in self.nmea_statistic)

    def test_VTG_exists(self):
        self.assertTrue("VTG" in self.nmea_statistic)

    def test_ZDA_exists(self):
        self.assertTrue("ZDA" in self.nmea_statistic)


if __name__ == '__main__':
    unittest.main()
