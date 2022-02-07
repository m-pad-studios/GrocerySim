import unittest

from colors import ColorChanger

class TestColors(unittest.TestCase):

    def test_color_changer(self):
        color = ColorChanger()

        self.assertIsInstance(color, object)

    def test_color_list(self):
        color = ColorChanger()

        my_list = color.COLORS

        test_list = {}

        self.assertTrue(my_list, test_list)

if __name__ == '__main__':

    unittest.main()
