import unittest
import pyautogui


class TestExpedition(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        """
        Setup UDP socket and record 10 seconds of NMEA data
        """
        super(TestExpedition, self).setUpClass()

    def test_grabimage(self):
        im2 = pyautogui.screenshot('../run/my_screenshot2.png')



if __name__ == '__main__':
    unittest.main()
