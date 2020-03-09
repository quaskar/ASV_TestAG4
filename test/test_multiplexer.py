import unittest
import pyautogui
import os
import time
from PIL import Image
from PIL import ImageChops


class TestMultiplexer(unittest.TestCase):

    gui_pos = []

    @classmethod
    def setUpClass(self):
        """
        Setup UDP socket and record 10 seconds of NMEA data
        """
        super(TestMultiplexer, self).setUpClass()

        os.system('taskkill /IM MPXConfig3.exe 2> nul')

        os.system('start "Test" "C:\Program Files\Shipmodul Miniplex-3\MPXConfig3.exe"')
        time.sleep(3)

        # grab of complete screen
        pyautogui.screenshot('../run/multiplexer-generic.png')

        # localize appliction position
        self.gui_pos = pyautogui.locateOnScreen('../templates/template_multiplexer_localize.png')

        # grab application window
        pyautogui.screenshot('../run/multiplexer.png', region=(self.gui_pos.left, self.gui_pos.top, 848, 575))

        # connect to multiplexer
        pyautogui.moveTo(self.gui_pos.left + 137, self.gui_pos.top + 291)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(self.gui_pos.left + 100, self.gui_pos.top + 328)
        pyautogui.click()
        time.sleep(1)

        pyautogui.moveTo(self.gui_pos.left + 100, self.gui_pos.top + 313)
        pyautogui.click(clicks=2)
        time.sleep(0.5)
        pyautogui.write('192.168.0.250')
        time.sleep(1)

        pyautogui.moveTo(self.gui_pos.left + 75, self.gui_pos.top + 336)
        pyautogui.click(clicks=2)
        time.sleep(0.5)
        pyautogui.write('10110')
        time.sleep(1)

        pyautogui.moveTo(self.gui_pos.left + 190, self.gui_pos.top + 304)
        pyautogui.click()
        time.sleep(2)



    @classmethod
    def tearDownClass(self):
        """
        Setup UDP socket and record 10 seconds of NMEA data
        """
        super(TestMultiplexer, self).tearDownClass()

        os.system('taskkill /IM MPXConfig3.exe > nul')
        time.sleep(3)

    #@unittest.skip("File name issue")
    def test_save_config(self):
        pyautogui.moveTo(self.gui_pos.left + 18, self.gui_pos.top + 37)
        pyautogui.click()
        time.sleep(1)

        pyautogui.moveTo(self.gui_pos.left + 18, self.gui_pos.top + 150)
        pyautogui.click()
        time.sleep(1)

        pyautogui.write(r'C:\Users\Bordcomputer\Desktop\ASV_TestAG4\run\multiplexer.ini')
        pyautogui.press('enter')
        time.sleep(1)


    def test_check_io_settings(self):
        pyautogui.click(self.gui_pos.left + 300, self.gui_pos.top + 275)
        time.sleep(1)
        im = pyautogui.screenshot('../run/multiplexer-io-settions.png', region=(self.gui_pos.left + 238, self.gui_pos.top + 260, 600, 290))
        diff = ImageChops.difference(im, Image.open('../templates/template_multiplexer-io-settions.png'))
        self.assertFalse(diff.getbbox())


    def test_check_options_settings(self):
        pyautogui.click(self.gui_pos.left + 400, self.gui_pos.top + 275)
        time.sleep(1)
        im = pyautogui.screenshot('../run/multiplexer-options-settions.png', region=(self.gui_pos.left + 238, self.gui_pos.top + 260, 600, 290))
        diff = ImageChops.difference(im, Image.open('../templates/template_multiplexer-options-settions.png'))
        self.assertFalse(diff.getbbox())

    def test_check_routing_settings(self):
        pyautogui.click(self.gui_pos.left + 450, self.gui_pos.top + 275)
        time.sleep(1)
        im = pyautogui.screenshot('../run/multiplexer-routing-settions.png', region=(self.gui_pos.left + 238, self.gui_pos.top + 260, 600, 290))
        diff = ImageChops.difference(im, Image.open('../templates/template_multiplexer-routing-settions.png'))
        self.assertFalse(diff.getbbox())

if __name__ == '__main__':
    unittest.main()
