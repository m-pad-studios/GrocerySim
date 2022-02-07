import unittest

from colors import ColorChanger

class TestColors(unittest.TestCase):

    def test_color_changer(self):
        color = ColorChanger()

        self.assertIsInstance(color, object)

    def test_color_list(self):
        color = ColorChanger()

        my_list = color.COLORS

        test_list = {\
    "black":"\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green":"\u001b[32m",
    "yellow":"\u001b[33;1m",
    "blue":"\u001b[34;1m",
    "magenta":"\u001b[35m",
    "cyan": "\u001b[36m",
    "white":"\u001b[37m",
    "yellow-background":"\u001b[43m",
    "black-background":"\u001b[40m",
    "cyan-background":"\u001b[46;1m",
        }

        self.assertEqual(my_list , test_list)

    def test_colors_in_list(self):
        color = ColorChanger()

        my_list = color.COLORS
        test_color = "black"

        for c in my_list:
            if c == test_color:
                print(c)
                self.assertEqual(c, test_color)
            elif c != test_color:
                print(c)
              
                self.assertTrue(c != test_color) 

if __name__ == '__main__':

    unittest.main()
