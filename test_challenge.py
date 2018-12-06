import unittest
from challenge import PythonChallengeMPRJ

class TesteUnitario(unittest.TestCase):

  def teste_fibonacci(self):
    self.assertEqual(challenge.fibonacci(8), 21)
    self.assertEqual(challenge.fibonacci(9), 34)
    self.assertEqual(challenge.fibonacci(10), 55)
    self.assertEqual(challenge.fibonacci(11), 89)


  def teste_busca_binaria(self):
    vetor = [0, 12, 29, 31, 43, 54, 61, 73, 84, 95, 101, 110, 122]
    chave = len(vetor)-1
    self.assertEqual(challenge.busca_binaria(vetor, 0, len(vetor)-1, chave), [43, 12, 61, 54, 29, 31])


if __name__ == '__main__':
  challenge = PythonChallengeMPRJ()
  unittest.main()