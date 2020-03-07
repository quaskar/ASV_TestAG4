import unittest
import HtmlTestRunner
import os
from test_gps import TestGps
from test_BandG import TestBandG
from test_weatherbox import TestWeatherbox
from test_ais import TestAis
from test_expedition import TestExpedition
from test_multiplexer import TestMultiplexer


class TestAG4(unittest.TestCase):

    def test_selftest(self):
        self.assertTrue(True)

    @staticmethod
    def run_suite():
        suite = unittest.TestSuite()
        result = unittest.TestResult()

        suite.addTest(unittest.makeSuite(TestAG4))
        # suite.addTest(unittest.makeSuite(TestGps))
        suite.addTest(unittest.makeSuite(TestBandG))
        # suite.addTest(unittest.makeSuite(TestWeatherbox))
        # suite.addTest(unittest.makeSuite(TestAis))
        suite.addTest(unittest.makeSuite(TestExpedition))
        suite.addTest(unittest.makeSuite(TestMultiplexer))


        #runner = unittest.TextTestRunner()
        runner = HtmlTestRunner.HTMLTestRunner(output='../run',combine_reports=True)
        print(runner.run(suite))


if __name__ == '__main__':

    os.system('rm ../run/*')

    TestAG4.run_suite()

    os.system('zip ../logs/ASV_TestAG4_Testrun_`date +%Y%m%d-%H%M%S`.zip ../run/*')

    #os.system('rm ../run/*')