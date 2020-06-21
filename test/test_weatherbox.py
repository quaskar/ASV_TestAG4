import unittest
import pyautogui
import os
import time


class TestWeatherbox(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        Start Weatherbox application
        """
        super(TestWeatherbox, self).setUpClass()

       # start config tool via autohotkey script
        os.system('start "Test" "../autohotkey/start_WIBE.ahk"')
        time.sleep(3)

        # grab of complete screen
        pyautogui.screenshot('../run/weatherbox-generic.png')


    @classmethod
    def tearDownClass(self):
        """
        Close Weatherbox application
        """
        super(TestWeatherbox, self).tearDownClass()

        os.system('start "Test" "../autohotkey/stop_WIBE.ahk"')
        time.sleep(3)

    def test_idle(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()
