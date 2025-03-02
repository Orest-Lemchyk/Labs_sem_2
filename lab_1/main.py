import unittest
from monoton import is_monoton

class TestIsMonoton(unittest.TestCase):
    '''Перевірка роботи функції is_monoton'''
    def test_increasing(self):
        self.assertTrue(is_monoton([1, 2, 3, 4, 5]))

    def test_decreasing(self):
        self.assertTrue(is_monoton([5, 4, 3, 2, 1]))

    def test_not_monoton(self):
        self.assertFalse(is_monoton([1, 3, 2, 4, 5]))

    def test_single_element(self):
        self.assertTrue(is_monoton([42]))

    def test_two_elements_increasing(self):
        self.assertTrue(is_monoton([1, 2]))

    def test_two_elements_decreasing(self):
        self.assertTrue(is_monoton([2, 1]))

if __name__ == '__main__':
    unittest.main()
