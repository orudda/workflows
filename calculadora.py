
class Calculadora():
  def __init__(self, value1, value2):
    self.value1 = value1
    self.value2 = value2
  
  def _get_sum(self, sub):
    if (sub):
      return self.value1 + self.value2
    else:
      return self.value1 - self.value2
  
  def _get_mod(self):
    return self.value1 % self.value2
  
  def _get_pot(self):
    return self.value1 ** self.value2
  
  def _get_times(self, invert):
    if (invert):
      if (self.value2 == 0):
        raise Exception("deve ser respeitado o dominio na divisao")
      else:
        return self.value1 / self.value2
    else:
      return self.value1 * self.value2
