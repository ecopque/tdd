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
    assert isinstance(n, int), '"n" must be int.' #1: #6:

    if n % 3 == 0 and n % 5 == 0: #2: #7:
        return 'Bacon with eggs' #2:
    
    if n % 3 == 0: #4:
        return 'Bacon' #4:
    
    if n % 5 == 0: #5:
        return 'Eggs' #5:
    
    return 'To starve' #3:


#1: Etapa 1;
#2: Etapa 2;
#3: Etapa 3;
#4: Etapa 4;
#5: Etapa 5;
#6: Essa linha usa a declaração assert para garantir que o argumento n passado para a função bacon_with_eggs seja um número inteiro (int). Caso n não seja do tipo int, o programa levanta um AssertionError com a mensagem "n" must be int.'. Isso serve como uma verificação inicial de tipo, garantindo que a função opere apenas com valores inteiros. Essa linha se conecta com o módulo de teste /TDD/test_baconwitheggs.py, onde é testado se um erro ocorre quando bacon_with_eggs recebe um valor que não é inteiro.
#7: Esta linha verifica se n é múltiplo de 3 e de 5 ao mesmo tempo. Isso é feito usando o operador %, que calcula o resto da divisão. Se n for múltiplo de ambos, o restante das divisões (n % 3 e n % 5) será 0, indicando que n é divisível por 3 e 5.

# https://linktr.ee/edsoncopque