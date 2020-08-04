import unittest
import HtmlTestRunner
import os
import argparse
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QWizard, QWizardPage, QLabel, QVBoxLayout, QRadioButton, QSpacerItem
from PyQt5.QtGui import QPixmap
from datetime import datetime
from test_gps import TestGps
from test_BandG import TestBandG
from test_weatherbox import TestWeatherbox
from test_ais import TestAis
from test_expedition import TestExpedition
from test_multiplexer import TestMultiplexer


class TestWizard(QWizard):

    args = []

    def __init__(self, args):
        super(TestWizard, self).__init__()
        self.args = args

    def show(self):
        self.setWizardStyle(QWizard.ModernStyle)
        self.addPage(self.createIntroPage())
        self.addPage(self.createSuiteSetectPage())
        self.addPage(self.createTurnOnPage())
        self.setWindowTitle("Aquis Granus IV Test Suite Konfigurator")
        super(TestWizard, self).show()

    def createIntroPage(self):
        page = QWizardPage()
        page.setTitle("Aquis Granus IV Test Suite Konfigurator")
        page.setSubTitle("Konfiguriere den nächsten Testlauf")
        page.setPixmap(QWizard.WatermarkPixmap, QPixmap("../images/ag4.png"))
        layout = QVBoxLayout()

        label = QLabel("Die ist die grafische Oberfläche zur Konfiguration ")
        label.setWordWrap(True)
        layout.addWidget(label)

        page.setLayout(layout)

        return page

    def createSuiteSetectPage(self):
        page = QWizardPage()
        page.setTitle("Auswah der unterschiedlichen Test Suites")
        page.setSubTitle("Test suites defines a certain scope fr the test run")
        page.setPixmap(QWizard.WatermarkPixmap, QPixmap("../images/ag4.png"))
        layout = QVBoxLayout()

        radiobox1 = QRadioButton("Automatische Test Suite")
        layout.addWidget(radiobox1)
        label1 = QLabel("Beinhaltet alle Tests, die ohne manuellen Eingriff des Benutzers ablaufen können. Ausschließlich Vorbedingungen müssen vorab manuell erfüllt werden (Einschalten aller zu testenden Geräte)");
        label1.setWordWrap(True)
        radiobox1.setChecked(True)
        layout.addWidget(label1)
        layout.addSpacing(20)

        radiobox2 = QRadioButton("Volle Test Suite")
        layout.addWidget(radiobox2)
        label2 = QLabel("Diese Test Suite bedarf der Mithilfe der Anwenders. Es wird der volle Testumfang abgefahren, der eine geführte Interaktion des Benutzers bedarf (z.B. Umschalten von Funktionen)");
        label2.setWordWrap(True)
        layout.addWidget(label2)
        layout.addSpacing(20)

        radiobox3 = QRadioButton("Eigene Test Suite")
        layout.addWidget(radiobox3)
        label3 = QLabel("Unter der Rubrik der eigenen Test Suite können in einem folgedialog der gewünschte Testumfang konfiguriert werden. Dies ist vorallem für gezielte Test einzelner Geräte vorgesehen.");
        label3.setWordWrap(True)
        layout.addWidget(label3)

        page.setLayout(layout)

        return page

    def createTurnOnPage(self):
        page = QWizardPage()
        page.setTitle("Test")

        label = QLabel("This wizard will help you register your wo.")
        label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(label)
        page.setLayout(layout)

        self.args.testauto = True

        return page


if __name__ == '__main__':

    # configure command line options
    parser = argparse.ArgumentParser()
    parser.add_argument("--gui", help="Show wiarz to configure testrun", action="store_true")
    parser.add_argument("--testsuiteauto", help="Apply all automatic tests", action="store_true")
    parser.add_argument("--testsuitefull", help="Apply all tests", action="store_true")
    parser.add_argument("--testmultiplexer", help="Apply Multiplier tests only", action="store_true")
    parser.add_argument("--testgps", help="Apply GPS tests only", action="store_true")
    parser.add_argument("--testbandg", help="Apply B&G tests only", action="store_true")
    parser.add_argument("--testweatherbox", help="Apply Weatherbox tests only", action="store_true")
    parser.add_argument("--testais", help="Apply AIS tests only", action="store_true")
    parser.add_argument("--testexpedition", help="Apply Expedition tests only", action="store_true")
    args = parser.parse_args()


    # gui wizard
    if args.gui:
        app = QApplication(sys.argv)
        wizard = TestWizard(args)
        wizard.show()
        app.exec_()


    # configure test suite
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    if args.testsuiteauto:
        pass
    elif args.testsuitefull:
        pass
    else:
        if args.testmultiplexer | args.testsuiteauto:
            suite.addTest(unittest.makeSuite(TestMultiplexer))
        if args.testgps:
            suite.addTest(unittest.makeSuite(TestGps))
        if args.testbandg:
            suite.addTest(unittest.makeSuite(TestBandG))
        if args.testweatherbox:
            suite.addTest(unittest.makeSuite(TestWeatherbox))
        if args.testais:
            suite.addTest(unittest.makeSuite(TestAis))
        if args.testexpedition:
            suite.addTest(unittest.makeSuite(TestExpedition))



    # run test suite
    os.system(r'del /S /Q ..\run\* > nul')
    runner = HtmlTestRunner.HTMLTestRunner(output='../run', combine_reports=True)
    print(runner.run(suite))
    shutil.make_archive('..\logs\ASV_TestAG4_Testrun_' + datetime.now().strftime("%Y%m%d_%H%M%S") + r'.zip', 'zip', r'..\run')
    #os.system(r'del /S /Q ..\run\*')