# FILE: /TDD/calculator.py

def sum_sum(x, y):
    assert isinstance(x, (int, float)), 'X has to be INT or FLOAT, Edson.' #1: #2:
    return x + y


#1: Essa linha utiliza uma assertiva (assert) para verificar se o valor de x é do tipo int ou float.O objetivo é garantir que x seja um número (inteiro ou ponto flutuante) antes de prosseguir com a operação de soma. Se x não for um int ou float, o código lança um AssertionError com a mensagem 'X has to be INT or FLOAT, Edson.'. A assertiva, neste caso, é uma medida de segurança para evitar a soma de tipos inadequados, como strings ou listas, que poderiam causar erros.
#2: No contexto do módulo, isso é especialmente relevante porque o sum_sum será chamado por outro módulo (testing.py). Essa verificação ajuda a manter o código mais robusto e previne que entradas inválidas causem problemas durante a execução.

# https://linktr.ee/edsoncopque