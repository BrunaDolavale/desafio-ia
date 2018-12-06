import re
import numpy as np

class PythonChallengeMPRJ():

  def fibonacci(self, n):
    # Questão 1

    f1, f2 = 0, 1
    for i in range(0, n):
      f1, f2 = f2, f1 + f2

    return f1

  def fibonacci_complexidade(self, n):
    # Questão 2

    '''
    Como F(n) cresce exponencialmente,
    o número de dígitos é igual a O(n).
    Portanto, a complexidade resultante de
    fibonacci é O (n^2).
    Logo, se n=10000, O(10000^2)
    '''
    n = 10000
    resultado = self.fibonacci(n)

    return resultado


  def busca_binaria(self, vetor, pos_inicial, pos_final, resultado, todos_nos=[]):
    # Questão 3

    if pos_inicial <= pos_final:
      meio = (pos_inicial + pos_final) // 2
      aux_no = vetor[meio]
      todos_nos.append(aux_no)
      if resultado > vetor[meio]:
        return self.busca_binaria(vetor, pos_inicial+1, pos_final, resultado)
      elif resultado < vetor[meio]:
        return self.busca_binaria(vetor, pos_inicial-1, pos_final, resultado)
      else:
        return list(set(todos_nos))
    return -1


  def acesso_servidor(self, tamanho=200):
    # Questão 4
    # O usuário é capaz de determinar quantos endereços deseja exibir na lista

    log = open("mock_data/log.txt", "r") # Mock do log de dados de um servidor
    uniques = []
    ip = log.read()
    ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,9}", ip)

    return np.unique(ips)[:tamanho]


  def normaliza_com_regex(self):
    # Questão 5

    arquivo = open("mock_data/nomes_procurados.txt", "r").read()
    primeira_parte = re.sub(r'(?<![a-z])nome(?![a-z])', '\nnome', arquivo)
    resultado = re.sub(r'([a-z])nome(?![a-z])', '\\1\nnome', primeira_parte)

    return resultado


if __name__ == '__main__':
  challenge = PythonChallengeMPRJ()
