import unittest
from test_gps import TestGps
from test_BandG import TestBandG
from test_weatherbox import TestWeatherbox
from test_ais import TestAis
from test_expedition import TestExpedition



def Test_AG4_Suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()

    suite.addTest(unittest.makeSuite(TestGps))
    suite.addTest(unittest.makeSuite(TestBandG))
    suite.addTest(unittest.makeSuite(TestWeatherbox))
    suite.addTest(unittest.makeSuite(TestAis))
    suite.addTest(unittest.makeSuite(TestExpedition))

    runner = unittest.TextTestRunner()
    print(runner.run(suite))


if __name__ == '__main__':
    Test_AG4_Suite()