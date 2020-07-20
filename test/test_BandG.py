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
        self.nmea_statistic = test_utils.Nmea.udp_stat(duration=10, log="../run/NMEA-Log-B&G-MultiPlexer.log")

        #self.nmea_statistic = {}
        #self.nmea_statistic = test_utils.Nmea.serial_stat(duration=10, device='COM1', baudrate=38400, log="../run/NMEA-Log-B&G-AIS.log")


    def test_DBT(self):
        self.assertTrue("DBT" in self.nmea_statistic)

        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["DBT"]), 2.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["DBT"]), 1.8)

    def test_MTW_exists(self):
        self.assertTrue("MTW" in self.nmea_statistic)

        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["MTW"]), 2.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["MTW"]), 1.8)

    def test_MWD_exists(self):
        self.assertTrue("MWD" in self.nmea_statistic)

        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["MWD"]), 2.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["MWD"]), 1.8)

    def test_VHW_exists(self):
        self.assertTrue("VHW" in self.nmea_statistic)

        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["VHW"]), 2.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["VHW"]), 1.8)

    def test_VLW_exists(self):
        self.assertTrue("VLW" in self.nmea_statistic)

        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["VLW"]), 2.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["VLW"]), 1.8)

    def test_VWR_exists(self):
        self.assertTrue("VWR" in self.nmea_statistic)

        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["VWR"]), 2.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["VWR"]), 0.8)

    def test_VWT_exists(self):
        self.assertTrue("VWT" in self.nmea_statistic)

        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["VWT"]), 2.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["VWT"]), 0.8)


if __name__ == '__main__':
    unittest.main()
