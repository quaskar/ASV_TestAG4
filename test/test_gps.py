import unittest
import test_utils


class TestGps(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        Setup UDP socket and record 10 seconds of NMEA data
        """
        super(TestGps, self).setUpClass()
        self.nmea_statistic = {}
        self.nmea_statistic = test_utils.Nmea.udp_stat(duration=10, log="../run/NMEA-Log-GPS-MultiPlexer.log")

    @unittest.skip
    def test_APB_exists(self):
        self.assertTrue("APB" in self.nmea_statistic)

        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["APB"]), 1.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["APB"]), 0.8)

    def test_GBS_exists(self):
        self.assertTrue("GBS" in self.nmea_statistic)
        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["GBS"]), 1.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["GBS"]), 0.8)

    def test_DTM_exists(self):
        self.assertTrue("DTM" in self.nmea_statistic)
        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["DTM"]), 1.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["DTM"]), 0.8)

    def test_GLL_exists(self):
        self.assertTrue("GLL" in self.nmea_statistic)
        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["GLL"]), 1.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["GLL"]), 0.8)

    @unittest.skip
    def test_RMB_exists(self):
        self.assertTrue("RMB" in self.nmea_statistic)
        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["RMB"]), 1.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["RMB"]), 0.8)

    def test_VTG_exists(self):
        self.assertTrue("VTG" in self.nmea_statistic)
        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["VTG"]), 1.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["VTG"]), 0.8)

    def test_ZDA_exists(self):
        self.assertTrue("ZDA" in self.nmea_statistic)
        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["ZDA"]), 1.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["ZDA"]), 0.8)


if __name__ == '__main__':
    unittest.main()
