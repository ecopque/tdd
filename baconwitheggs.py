# FILE: /TDD/baconwitheggs.py
'''
1. Receber um número inteiro;
2. Saber se o número é múltiplo de 3 e 5:
    Bacon com ovos
3. Saber se o número NÃO É múltiplo de 3 e 5:
    Passar fome
4. Saber se o número é múltiplo somente de 3:
    Bacon
5. Saber se o número é múltiplo somente de 5:
    Ovos
'''

def bacon_with_eggs(n):
    assert isinstance(n, int), '"n" must be int.' #1: ##

    if n % 3 == 0 and n % 5 == 0: #2:
        return 'Bacon with eggs' #2:
    
    if n % 3 == 0: #4:
        return 'Bacon' #4:
    
    if n % 5 == 0:
        return 'Eggs'
    
    return 'To starve' #3:


#1: Etapa 1;
#2: Etapa 2;
#3: Etapa 3;
#4: Etapa 4;
#5: 

# https://linktr.ee/edsoncopque