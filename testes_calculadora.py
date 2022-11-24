import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
  # def test_dominio_divisao_igual_zero(self):
  #   calculadora = Calculadora(0, 0)
  #   self.assertRaises(Exception, calculadora._get_times(True))
    
  def test_subtraction_result(self):
    calculadora = Calculadora(1, 2)
    self.assertEqual(-1, calculadora._get_sum(False))

  def test_sum_result(self):
    calculadora = Calculadora(1, 2)
    self.assertEqual(3, calculadora._get_sum(True))

  def test_mod_btw_2_values(self):
    calculadora = Calculadora(5, 2)
    self.assertEqual(1, calculadora._get_mod())

  def test_pot_btw_2_values(self):
    calculadora = Calculadora(5, 2)
    self.assertEqual(25, calculadora._get_pot())

  def test_times_result(self):
    calculadora = Calculadora(6, 2)
    self.assertEqual(3, calculadora._get_times(True))

  def test_times_result(self):
    calculadora = Calculadora(6, 2)
    self.assertEqual(12, calculadora._get_times(False))




if __name__ == '__main__':
    unittest.main()
