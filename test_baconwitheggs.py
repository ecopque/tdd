# FILE: /TDD/test_baconwitheggs.py
"""
TDD

Red cicle
. Parte 1: Criar teste e ver falhar;

Green cicle
. Parte 2: Criar o código e ver o teste passar;

Refactor cicle
. Parte 3: Melhorar meu código.
"""

import unittest
from baconwitheggs import bacon_with_eggs

class TestBaconWithEggs(unittest.TestCase): #1:
    def test_bacon_with_eggs_throw_assertionerror_if_not_receiving_int(self): #1:
        with self.assertRaises(AssertionError): #1:
            bacon_with_eggs('') #1:

    def test_bacon_with_eggs_should_return_bacon_with_eggs_if_input_is_a_multiple_of_3_and_5(self):
        entries = (15, 30, 45, 60)
        outputs = 'Bacon with eggs'

        for i in entries:
            with self.subTest(i=i, outputs=outputs):
                self.assertEqual(bacon_with_eggs(i), (outputs))

    def test_bacon_with_eggs_should_return_starvation_if_input_is_not_a_multiple_of_3_and_5(self):
        entries = (1, 2, 4, 7, 8)
        ouputs = 'To starve'

        for i in entries:
            with self.subTest(i=i, ouputs=ouputs):
                self.assertEqual(bacon_with_eggs(i), (ouputs))

unittest.main(verbosity=2)


#1:Primeira etapa, pelo que entendi, precisamos criar uma classe em 'test_baconwitheggs' onde vamos enviar para 'baconwitheggs' uma string, quando só é permitido enviar números inteiros. Quando o erro se apresentar, alcançamos o nosso objetivo;
#2: 




# https://linktr.ee/edsoncopque