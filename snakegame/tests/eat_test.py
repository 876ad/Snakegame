import unittest2

def eats_food(score):

    if snake[0] == food:
        score += 1
        return score

class Test_eats_food(unittest2.TestCase):
    def Test_eats_food_success(self):

        actual = eats_food(score=1)
        expected = {1}
        self.assertEqual(actual, expected)
