import unittest
import pyautogui
import os
import time
from PIL import Image
from PIL import ImageChops


class TestMultiplexer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        Setup UDP socket and record 10 seconds of NMEA data
        """
        super(TestMultiplexer, self).setUpClass()

        # start config tool via autohotkey script
        os.system('start "Test" "../autohotkey/start_MPXConfig3.ahk"')
        time.sleep(3)

        # grab of complete screen
        pyautogui.screenshot('../run/multiplexer-generic.png')

        # grab application window
        pyautogui.screenshot('../run/multiplexer.png', region=(0, 0, 848, 575))

        # connect to multiplexer
        pyautogui.moveTo( 137,  291)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo( 100,  328)
        pyautogui.click()
        time.sleep(1)

        pyautogui.moveTo( 100,  313)
        pyautogui.click(clicks=2)
        time.sleep(0.5)
        pyautogui.write('192.168.0.250')
        time.sleep(1)

        pyautogui.moveTo( 75,  336)
        pyautogui.click(clicks=2)
        time.sleep(0.5)
        pyautogui.write('10110')
        time.sleep(1)

        pyautogui.moveTo( 190,  304)
        pyautogui.click()
        time.sleep(2)



    @classmethod
    def tearDownClass(self):
        """
        Setup UDP socket and record 10 seconds of NMEA data
        """
        super(TestMultiplexer, self).tearDownClass()

        os.system('start "Test" "../autohotkey/stop_MPXConfig3.ahk"')
        time.sleep(3)

    #@unittest.skip("File name issue")
    def test_save_config(self):
        pyautogui.moveTo( 18,  37)
        pyautogui.click()
        time.sleep(1)

        pyautogui.moveTo( 18,  150)
        pyautogui.click()
        time.sleep(1)

        pyautogui.write(r'C:\Users\Bordcomputer\Desktop\ASV_TestAG4\run\multiplexer.ini')
        pyautogui.press('enter')
        time.sleep(1)


    def test_check_io_settings(self):
        pyautogui.click( 300,  275)
        time.sleep(1)
        im = pyautogui.screenshot('../run/multiplexer-io-settions.png', region=( 238,  260, 600, 290))
        diff = ImageChops.difference(im, Image.open('../templates/template_multiplexer-io-settions.png'))
        self.assertFalse(diff.getbbox())


    def test_check_options_settings(self):
        pyautogui.click( 400,  275)
        time.sleep(1)
        im = pyautogui.screenshot('../run/multiplexer-options-settions.png', region=( 238,  260, 600, 290))
        diff = ImageChops.difference(im, Image.open('../templates/template_multiplexer-options-settions.png'))
        self.assertFalse(diff.getbbox())

    def test_check_routing_settings(self):
        pyautogui.click( 450,  275)
        time.sleep(1)
        im = pyautogui.screenshot('../run/multiplexer-routing-settions.png', region=( 238,  260, 600, 290))
        diff = ImageChops.difference(im, Image.open('../templates/template_multiplexer-routing-settions.png'))
        self.assertFalse(diff.getbbox())

if __name__ == '__main__':
    unittest.main()
