import unittest
from my_math import line_eq


class TestLineEq(unittest.TestCase):

    def test_positive_solution(self):
        result = line_eq(1, -5)
        self.assertEqual(result, 5, 'Корень уравнения должен быть равен 5')

    def test_zero_coefficient(self):
        result = line_eq(0, 7)
        self.assertIsNone(result, 'Для уравнения вида 0x + c корень отсутствует')

    def test_zero_and_zero_coefficients(self):
        result = line_eq(0, 0)
        self.assertIsNone(result, 'При a=0 и b=0 уравнение становится тождеством и решений нет')


if __name__ == '__main__':
    unittest.main()