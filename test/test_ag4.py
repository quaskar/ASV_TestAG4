import unittest
import HtmlTestRunner
import os
import argparse
import shutil
from datetime import datetime
from test_gps import TestGps
from test_BandG import TestBandG
from test_weatherbox import TestWeatherbox
from test_ais import TestAis
from test_expedition import TestExpedition
from test_multiplexer import TestMultiplexer


if __name__ == '__main__':

    # configure command line options
    parser = argparse.ArgumentParser()
    parser.add_argument("--testauto", help="Apply all automatic tests", action="store_true")
    parser.add_argument("--testmultiplexer", help="Apply Multiplier tests only", action="store_true")
    parser.add_argument("--testgps", help="Apply GPS tests only", action="store_true")
    parser.add_argument("--testbandg", help="Apply B&G tests only", action="store_true")
    parser.add_argument("--testweatherbox", help="Apply Weatherbox tests only", action="store_true")
    parser.add_argument("--testais", help="Apply AIS tests only", action="store_true")
    parser.add_argument("--testexpedition", help="Apply Expedition tests only", action="store_true")

    args = parser.parse_args()

    # configure test suite
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    #if args.testauto:
    #    pass
    if args.testmultiplexer or args.testauto:
        suite.addTest(unittest.makeSuite(TestMultiplexer))
    if args.testgps or args.testauto:
        suite.addTest(unittest.makeSuite(TestGps))
    if args.testbandg or args.testauto:
        suite.addTest(unittest.makeSuite(TestBandG))
    if args.testweatherbox or args.testauto:
        suite.addTest(unittest.makeSuite(TestWeatherbox))
    if args.testais or args.testauto:
        suite.addTest(unittest.makeSuite(TestAis))
    if args.testexpedition:
        suite.addTest(unittest.makeSuite(TestExpedition))

    # run test suite
    os.system(r'del /S /Q ..\run\* > nul')
    runner = HtmlTestRunner.HTMLTestRunner(output='../run', combine_reports=True, report_name="TestReport", add_timestamp=False)
    print(runner.run(suite))
    shutil.make_archive('..\logs\ASV_TestAG4_Testrun_' + datetime.now().strftime("%Y%m%d_%H%M%S"), 'zip', r'..\run')
    #os.system(r'del /S /Q ..\run\*')

    os.system(r'"C:\Program Files\Mozilla Firefox\firefox.exe" file:///C:/Users/Bordcomputer/OneDrive/ASV_TestAG4/run/TestReport.html')