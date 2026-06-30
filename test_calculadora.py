import unittest
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_sumar(self):
        self.assertEqual(self.calc.sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(self.calc.restar(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(5, 4), 20)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(20, 5), 4)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)


if __name__ == "__main__":
    unittest.main()