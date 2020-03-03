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
        self.nmea_statistic = test_utils.Nmea.udp_stat(10)


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

    def test_no_extra_exists(self):
        for key in self.nmea_statistic.keys():
            self.assertTrue(str(key) in ["GBS", "DTM", "GLL", "RMB", "VTG", "ZDA", "APB"])

    @unittest.skip("Cycling of DTM sentence non-reliable")
    def test_APB_timing(self):
        print("APB : min=%.2f mean=%.2f max=%.2f" % (test_utils.Nmea.min_stat(self.nmea_statistic["APB"]), test_utils.Nmea.mean_stat(self.nmea_statistic["APB"]), test_utils.Nmea.max_stat(self.nmea_statistic["APB"])))
        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["APB"]), 1.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["APB"]), 0.8)

    @unittest.skip("Cycling of DTM sentence non-reliable")
    def test_GBS_timing(self):
        print("GBS : min=%.2f mean=%.2f max=%.2f" % (test_utils.Nmea.min_stat(self.nmea_statistic["GBS"]), test_utils.Nmea.mean_stat(self.nmea_statistic["GBS"]), test_utils.Nmea.max_stat(self.nmea_statistic["GBS"])))
        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["GBS"]), 1.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["GBS"]), 0.8)

    @unittest.skip("Cycling of DTM sentence non-reliable")
    def test_DTM_timing(self):
        print("DTM : min=%.2f mean=%.2f max=%.2f" % (test_utils.Nmea.min_stat(self.nmea_statistic["DTM"]), test_utils.Nmea.mean_stat(self.nmea_statistic["DTM"]), test_utils.Nmea.max_stat(self.nmea_statistic["DTM"])))
        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["DTM"]), 1.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["DTM"]), 0.8)

    @unittest.skip("Cycling of DTM sentence non-reliable")
    def test_GLL_timing(self):
        print("GLL : min=%.2f mean=%.2f max=%.2f" % (test_utils.Nmea.min_stat(self.nmea_statistic["GLL"]), test_utils.Nmea.mean_stat(self.nmea_statistic["GLL"]), test_utils.Nmea.max_stat(self.nmea_statistic["GLL"])))
        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["GLL"]), 1.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["GLL"]), 0.8)

    @unittest.skip("Cycling of DTM sentence non-reliable")
    def test_RMB_timing(self):
        print("RMB : min=%.2f mean=%.2f max=%.2f" % (test_utils.Nmea.min_stat(self.nmea_statistic["RMB"]), test_utils.Nmea.mean_stat(self.nmea_statistic["RMB"]), test_utils.Nmea.max_stat(self.nmea_statistic["RMB"])))
        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["RMB"]), 1.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["RMB"]), 0.8)

    @unittest.skip("Cycling of DTM sentence non-reliable")
    def test_VTG_timing(self):
        print("VTG : min=%.2f mean=%.2f max=%.2f" % (test_utils.Nmea.min_stat(self.nmea_statistic["VTG"]), test_utils.Nmea.mean_stat(self.nmea_statistic["VTG"]), test_utils.Nmea.max_stat(self.nmea_statistic["VTG"])))
        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["VTG"]), 1.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["VTG"]), 0.8)

    @unittest.skip("Cycling of DTM sentence non-reliable")
    def test_ZDA_timing(self):
        print("ZDA : min=%.2f mean=%.2f max=%.2f" % (test_utils.Nmea.min_stat(self.nmea_statistic["ZDA"]), test_utils.Nmea.mean_stat(self.nmea_statistic["ZDA"]), test_utils.Nmea.max_stat(self.nmea_statistic["ZDA"])))
        self.assertLess(test_utils.Nmea.max_stat(self.nmea_statistic["ZDA"]), 1.2)
        self.assertGreater(test_utils.Nmea.min_stat(self.nmea_statistic["ZDA"]), 0.8)


if __name__ == '__main__':
    unittest.main()
