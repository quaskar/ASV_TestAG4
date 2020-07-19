import unittest
import test_utils
import pyautogui
import os
import time
from PIL import Image
from PIL import ImageChops

class TestAis(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        Setup UDP socket and record 10 seconds of NMEA data
        """
        super(TestAis, self).setUpClass()

        self.nmea_statistic = {}
        self.nmea_statistic = test_utils.Nmea.serial_stat(duration=60, device='COM1', baudrate=38400,
                                                          log="../run/NMEA-Log-AIS.log")

        # start config tool via autohotkey script
        os.system('start "Test" "../autohotkey/start_easyTX2.ahk"')
        time.sleep(3)

        # grab of complete screen
        pyautogui.screenshot('../run/ais-generic.png')

        # grab application window
        pyautogui.screenshot('../run/ais.png', region=(0, 0, 711, 544))

        # click refresh com port button
        pyautogui.moveTo(186, 125)
        pyautogui.click()
        time.sleep(1)

        # select drop down menu for ports and enter COM1
        pyautogui.moveTo(142, 125)
        pyautogui.click()
        time.sleep(1)
        pyautogui.write('COM1')
        time.sleep(1)

        # click on connect button
        pyautogui.moveTo(247, 106)
        pyautogui.click()
        time.sleep(20)

    @classmethod
    def tearDownClass(self):
        """
        Setup UDP socket and record 10 seconds of NMEA data
        """
        super(TestAis, self).tearDownClass()

        os.system('start "Test" "../autohotkey/stop_easyTX2.ahk"')
        time.sleep(3)

    def test_check_SetupTab(self):
        pyautogui.click( 24,  60)
        time.sleep(1)
        im = pyautogui.screenshot('../run/ais-Setup.png', region=(0, 0, 711, 544))
        diff = ImageChops.difference(im, Image.open('../templates/template_ais-Setup.png'))
        self.assertFalse(diff.getbbox())


    def test_check_DiagnosticTab(self):
        pyautogui.click(80, 60)
        time.sleep(1)
        im = pyautogui.screenshot('../run/ais-Diagnostic.png', region=(0, 0, 711, 544))
        diff = ImageChops.difference(im, Image.open('../templates/template_ais-Diagnostic.png'))
        self.assertFalse(diff.getbbox())


    def test_check_SendDataTab(self):
        pyautogui.click( 142,  60)
        time.sleep(1)
        im = pyautogui.screenshot('../run/ais-SendData.png', region=(0, 0, 711, 544))
        diff = ImageChops.difference(im, Image.open('../templates/template_ais-SendData.png'))
        self.assertFalse(diff.getbbox())


    def test_check_ReceiveDataTab(self):
        pyautogui.click( 206,  60)
        time.sleep(1)
        im = pyautogui.screenshot('../run/ais-ReceiveData.png', region=(0, 0, 711, 544))
        diff = ImageChops.difference(im, Image.open('../templates/template_ais-ReceiveData.png'))
        self.assertFalse(diff.getbbox())


    def test_check_SDCardTab(self):
        pyautogui.click( 272,  60)
        time.sleep(1)
        im = pyautogui.screenshot('../run/ais-SDCard.png', region=(0, 0, 711, 544))
        diff = ImageChops.difference(im, Image.open('../templates/template_ais-SDCard.png'))
        self.assertFalse(diff.getbbox())


    def test_check_CPAAlarmTab(self):
        pyautogui.click( 331,  60)
        time.sleep(1)
        im = pyautogui.screenshot('../run/ais-CPAAlarm.png', region=(0, 0, 711, 544))
        diff = ImageChops.difference(im, Image.open('../templates/template_ais-CPAAlarm.png'))
        self.assertFalse(diff.getbbox())


    def test_check_AnchorAlarmTab(self):
        pyautogui.click( 415,  60)
        time.sleep(1)
        im = pyautogui.screenshot('../run/ais-AnchorAlarm.png', region=(0, 0, 711, 544))
        diff = ImageChops.difference(im, Image.open('../templates/template_ais-AnchorAlarm.png'))
        self.assertFalse(diff.getbbox())


if __name__ == '__main__':
    unittest.main()
