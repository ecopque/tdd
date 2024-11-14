# FILE: /TDD/test_person.py

import unittest
from person import Person
from unittest.mock import patch #1: #2:

class TestPerson(unittest.TestCase):
    def setUp(self): #3:
        self.p1 = Person('Edson', 'Copque')

    def test_person_attr_name_has_the_correct_value(self):
        self.assertEqual(self.p1.name, 'Edson') #4:

    def test_person_attr_name_is_str(self):
        self.assertIsInstance(self.p1.name, str) #5:

    def test_person_attr_lastname_has_the_correct_value(self):
        self.assertEqual(self.p1.last_name, 'Copque')

    def test_person_attr_lastname_is_str(self):
        self.assertIsInstance(self.p1.last_name, str)

    def test_person_attr_data_obtained_starts_false(self):
        self.assertFalse(self.p1.data_obtained) #6:

    def test_get_all_data_success_OK(self):
        with patch('requests.get') as fake_request: #7:
            fake_request.return_value.ok = True #8:
            self.assertEqual(self.p1.get_all_data(), 'Connected') #9:

if __name__ == '__main__':
    unittest.main(verbosity=2)


#1: Com este módulo terei possibilidade de criar dados fakes;
#2: A linha importa o módulo patch da biblioteca unittest.mock, que é usado para substituir partes do código por objetos falsos (mock) durante os testes. Isso permite simular comportamentos de componentes externos sem realmente executar o código de rede ou outros sistemas dependentes.
#3: Este método é executado antes de cada teste na classe TestPerson. Ele serve para preparar o ambiente de teste, criando uma instância da classe Person com os parâmetros 'Edson' e 'Copque'. Esse método é útil para evitar repetição de código, garantindo que cada teste tenha o mesmo ponto de partida. Aqui, ele cria o objeto p1 que será utilizado nos testes subsequentes.
#4: Este teste verifica se o atributo name do objeto p1 (instância da classe Person) contém o valor 'Edson'. O método assertEqual compara o valor atual do atributo com o valor esperado ('Edson'). O teste será bem-sucedido se os valores forem iguais.
#5: Este teste verifica se o atributo name de p1 é do tipo str (string). O método assertIsInstance é usado para garantir que o valor de p1.name seja uma string, o que é esperado para o nome de uma pessoa.
#6: Este teste verifica se o atributo data_obtained de p1 tem o valor False no início. O valor inicial de data_obtained é definido no método __init__ da classe Person como False, e o teste garante que este valor inicial é mantido corretamente.
#7: Aqui, o método patch do unittest.mock é usado para substituir o comportamento da função requests.get (que faria uma solicitação HTTP real). Dentro do bloco with, a variável fake_request é usada como um objeto mock para simular o comportamento da função requests.get. Esse patch é necessário para testar o método get_all_data sem fazer uma solicitação real à Internet.
#8: A linha configura o comportamento do mock fake_request. Ao definir fake_request.return_value.ok = True, estamos simulando que a resposta de uma requisição HTTP feita pelo requests.get seria bem-sucedida (indicando que a propriedade ok da resposta seria True). Isso simula uma resposta positiva de uma API ou de um servidor.
#9: Este teste verifica se o método get_all_data da classe Person retorna 'Connected' quando a resposta da requisição HTTP é bem-sucedida. Como a requisição foi mockada para retornar True em fake_request.return_value.ok, o teste espera que a função get_all_data retorne 'Connected'. Essa linha testa a interação entre o método get_all_data e a simulação do comportamento da rede.

# https://linktr.ee/edsoncopque