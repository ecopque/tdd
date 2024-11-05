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

unittest.main(verbosity=2)


#1:Primeira etapa, pelo que entendi, precisamos criar uma classe em 'test_baconwitheggs' onde vamos enviar para 'baconwitheggs' uma string, quando só é permitido enviar números inteiros. Quando o erro se apresentar, alcançamos o nosso objetivo;
#2: 

# https://linktr.ee/edsoncopque