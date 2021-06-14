import unittest2

def collide_with_self(snake):
    snake[0][0]
    if snake[0] in snake[1:]:
        return 1
    else:
        return 0

class Test_collide_with_self(unittest2.TestCase):
    def Test_collide_with_self_success(self):
        actual = collide_with_self(1)
        expected = {1}
        self.assertEqual(actual,expected)
