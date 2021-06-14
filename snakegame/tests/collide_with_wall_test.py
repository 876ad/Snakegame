import unittest2
import curses
def collide_with_wall(snake):
    s = curses.initscr()
    sh, sw = s.getmaxyx()
    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw]:
        return 1
    else:
        return 0

class Test_collide_with_wall(unittest2.TestCase):
    def test_collide_with_wall(self):
        acutal = collide_with_wall(1)
        expected = {1}
        self.assertEqual(actual,expected)
