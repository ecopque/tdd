# FILE: /TDD/calculator.py

def sum_sum(x, y):
    """
    #BELLOW⬇: #4: #5:
    >>> sum_sum(10, 30)
    41
    >>> sum_sum('10', 30)
    # BELLOW⬇: #6:
    Traceback (most recent call last):
    ...
    AssertionError: X has to be INT or FLOAT, Edson.
    """
    assert isinstance(x, (int, float)), 'X has to be INT or FLOAT, Edson.' #1: #2:
    return x + y

if __name__ == '__main__':
    import doctest #7:
    doctest.testmod(verbose=True) #3: #8:


# ------------------------------------------------------------------
#3: Com 'verbose=True' também será apresentado no terminal os testes quando funcionarem normalmente;
#4: Esta linha faz parte do bloco de documentação da função sum_sum(x, y). Ela é um exemplo de doctest, ou seja, um teste embutido nos comentários de docstring da função, que demonstra como a função deve se comportar quando chamada com os argumentos 10 e 30.
#5: Serve como teste para que, ao rodar o módulo com o doctest, seja validado se a função sum_sum retorna o valor esperado com esses inputs.
#6: Esta linha indica o tipo de saída esperado quando o teste anterior falha. Ela sugere que o retorno ao tentar somar uma string e um número deve ser uma mensagem de traceback indicando a ocorrência de um erro. Propósito: Descrever que a função deve gerar um erro e mostrar uma AssertionError com a mensagem especificada caso x não seja numérico.
#7: Esta linha importa o módulo doctest, responsável por ler e executar os testes descritos nas docstrings das funções.
#8: Esta linha chama o método testmod() do doctest, que executa todos os exemplos incluídos nas docstrings deste módulo (calculator.py). A opção verbose=True faz com que o doctest exiba cada teste e seu resultado detalhadamente. Interação com doctest: O método doctest.testmod verifica se o código funciona como esperado ao comparar as saídas reais com os valores esperados documentados na docstring da função.
# ------------------------------------------------------------------
#1: Essa linha utiliza uma assertiva (assert) para verificar se o valor de x é do tipo int ou float.O objetivo é garantir que x seja um número (inteiro ou ponto flutuante) antes de prosseguir com a operação de soma. Se x não for um int ou float, o código lança um AssertionError com a mensagem 'X has to be INT or FLOAT, Edson.'. A assertiva, neste caso, é uma medida de segurança para evitar a soma de tipos inadequados, como strings ou listas, que poderiam causar erros.
#2: No contexto do módulo, isso é especialmente relevante porque o sum_sum será chamado por outro módulo (testing.py). Essa verificação ajuda a manter o código mais robusto e previne que entradas inválidas causem problemas durante a execução.

# https://linktr.ee/edsoncopque