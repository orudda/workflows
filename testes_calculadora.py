import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
  def test_dominio_divisao_igual_zero(self):
    calculadora = Calculadora(0, 0)
    self.assertRaises(Exception, calculadora._get_times(true))
    
  def test_get_faixa_textual_nao_isento(self):
      calculadora = Calculadora(1, 2)
      self.assertEqual(3, calculadora._get_sum(false))



if __name__ == '__main__':
    unittest.main()
