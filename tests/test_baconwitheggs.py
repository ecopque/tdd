# FILE: /TDD/tests/test_baconwitheggs.py
"""
TDD

Red cicle
. Parte 1: Criar teste e ver falhar;

Green cicle
. Parte 2: Criar o código e ver o teste passar;

Refactor cicle
. Parte 3: Melhorar meu código.
"""

try:
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))) #6:
except:
    raise

import unittest
from baconwitheggs import bacon_with_eggs

# Etapa 1:
class TestBaconWithEggs(unittest.TestCase): #1:
    def test_bacon_with_eggs_throw_assertionerror_if_not_receiving_int(self): #1:
        with self.assertRaises(AssertionError): #1:
            bacon_with_eggs('') #1:

    # Etapa 2:
    def test_bacon_with_eggs_should_return_bacon_with_eggs_if_input_is_a_multiple_of_3_and_5(self): #2:
        entries = (15, 30, 45, 60)
        outputs = 'Bacon with eggs'

        for i in entries: #3:
            with self.subTest(i=i, outputs=outputs): #4:
                self.assertEqual(bacon_with_eggs(i), (outputs)) #5:

    # Etapa 3:
    def test_bacon_with_eggs_should_return_starvation_if_input_is_not_a_multiple_of_3_and_5(self):
        entries = (1, 2, 4, 7, 8)
        ouputs = 'To starve'

        for i in entries:
            with self.subTest(i=i, ouputs=ouputs):
                self.assertEqual(bacon_with_eggs(i), (ouputs))

    # Etapa 4:
    def test_bacon_with_eggs_should_return_bacon_if_input_is_a_multiple_of_3(self):
        entries = (3, 6, 9, 12, 18, 21)
        outputs = 'Bacon'

        for i in entries:
            with self.subTest(i=i, outputs=outputs):
                self.assertEqual(bacon_with_eggs(i), (outputs))

    # Etapa 5:
    def test_bacon_with_eggs_should_return_eggs_if_input_is_a_multiple_of_5(self):
        entries = (5, 10, 20, 25)
        outputs = 'Eggs'

        for i in entries:
            with self.subTest(i=i, outputs=outputs):
                self.assertEqual(bacon_with_eggs(i), (outputs))

if __name__ == '__main__':
    unittest.main(verbosity=2)


# ------------------------------------------------------------------
#6: sys.path.append(...): sys.path é uma lista de diretórios que o Python verifica para procurar módulos e pacotes ao fazer importações. A função append() adiciona um novo diretório ao final de sys.path, tornando-o disponível para importações no código. Este diretório é o resultado da expressão dentro de append(...). os.path.abspath(...): os.path.abspath() converte um caminho em um caminho absoluto. Isso significa que ele transforma o caminho fornecido em um caminho completo que começa na raiz do sistema de arquivos (por exemplo, /home/usuario/... no Linux ou C:\Users\usuario\... no Windows). Nesse caso, o caminho absoluto é gerado para o diretório ../ (o diretório pai) do diretório onde o arquivo atual está localizado. os.path.join(os.path.dirname(__file__), '../'): __file__ é uma variável especial que contém o caminho do arquivo atual. os.path.dirname(__file__) obtém o diretório onde o arquivo atual está localizado. os.path.join(...) combina o diretório do arquivo atual com ../, que representa o diretório pai. Então, os.path.join(os.path.dirname(__file__), '../') gera o caminho do diretório pai do arquivo atual.
# ------------------------------------------------------------------
#1:Primeira etapa, pelo que entendi, precisamos criar uma classe em 'test_baconwitheggs' onde vamos enviar para 'baconwitheggs' uma string, quando só é permitido enviar números inteiros. Quando o erro se apresentar, alcançamos o nosso objetivo;
#2: Esse é um método de teste no módulo de testes /TDD/test_baconwitheggs.py, criado para validar o comportamento de bacon_with_eggs quando a entrada é múltipla de 3 e 5. Seguindo o ciclo TDD, este teste é executado para garantir que a função bacon_with_eggs no outro módulo está retornando o valor esperado ("Bacon with eggs") para múltiplos de 3 e 5.
#3: Esse for itera pela tupla entries, que contém números que devem todos ser múltiplos de 3 e 5 (15, 30, 45, 60). Cada valor em entries é atribuído a i em cada iteração, sendo usado como entrada para a função bacon_with_eggs.
#4: Esse bloco cria subtestes, cada um representando um caso específico do valor i de entries. O uso de self.subTest permite que cada entrada em entries seja testada separadamente, facilitando a identificação de falhas específicas para valores individuais de i. Se um subteste falhar, o relatório mostrará qual valor de i causou a falha.
#5: Esta linha é a asserção que compara o resultado de bacon_with_eggs(i) com o valor esperado, outputs, que é "Bacon with eggs". Se bacon_with_eggs(i) retornar qualquer coisa diferente de "Bacon with eggs" para valores em entries, o teste falhará, indicando um erro na implementação da função.

# https://linktr.ee/edsoncopque