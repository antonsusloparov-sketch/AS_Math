import unittest
from my_math import line_eq, quad_eq

class TestMyMath(unittest.TestCase):

    def test_line_eq(self):
        self.assertEqual(line_eq(1, 5), -5)
        self.assertIsNone(line_eq(0, 5))   # Уравнение x=0 не имеет решений

    def test_quad_eq_positive_discriminant(self):
        expected_roots = [-3, 1]
        actual_roots = quad_eq(1, 2, -3)
        self.assertListEqual(sorted(actual_roots), sorted(expected_roots))
    
    def test_quad_eq_zero_discriminant(self):
        expected_roots = [2]
        actual_roots = quad_eq(1, -4, 4)
        self.assertListEqual(actual_roots, expected_roots)
    
    def test_quad_eq_negative_discriminant(self):
        actual_roots = quad_eq(1, 2, 5)
        self.assertEqual(len(actual_roots), 0)

if __name__ == '__main__':
    unittest.main()