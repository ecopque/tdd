# FILE: /TDD/test_calculator.py

import unittest #2:
from calculator import sum_sum

class TestCalculator(unittest.TestCase):
    def test_sum_5_and_5_should_return_10(self): #1: #3:
        self.assertEqual(sum_sum(5, 5), 10) #4:

    def test_sum_5_negative_and_5_should_return_0(self):
        self.assertEqual(sum_sum(-5, 5), 0)

    def test_sum_multiple_entries(self):
        x_y_outputs = (
            (10, 10, 20),
            (15, 15, 30),
            (15.5, 15.5, 31.0),
            (10, 10, 25),
            (1, 2, 3),
        )

        for i in x_y_outputs: #5:
            with self.subTest(i=x_y_outputs): #6:
                x, y, outputs = i
                self.assertEqual(sum_sum(x, y), outputs)

    def test_sum_x_is_not_int_or_float_should_return_assertionerror(self):
        with self.assertRaises(AssertionError): #7:
            sum_sum('10', 5)

unittest.main(verbosity=2) #8:


# ------------------------------------------------------------------
#1: Os nomes devem ser enormes? Parece que por convenção, sim!
#2: Esta linha importa o módulo unittest, que faz parte da biblioteca padrão do Python e fornece ferramentas para escrever e rodar testes unitários. Esse módulo é necessário para que o código possa definir e executar testes de maneira estruturada e automática.
#3: Esta é a definição de um método de teste dentro da classe TestCalculator. O nome do método (test_sum_5_and_5_should_return_10) sugere que ele verifica se a função sum_sum retorna o valor correto (10) ao somar 5 + 5. No contexto do módulo, ele é um dos métodos que testam o comportamento esperado da função sum_sum.
#4: Nesta linha, self.assertEqual compara o resultado de sum_sum(5, 5) com 10. Se a função sum_sum retorna 10, o teste passa; caso contrário, falha. Essa linha testa a funcionalidade da função sum_sum, que está definida no módulo calculator.
#5: Esse laço for percorre cada tupla dentro de x_y_outputs, que contém diferentes valores para x, y e o resultado esperado. A cada iteração, ele realiza o teste de sum_sum para um conjunto de valores, garantindo que a função funcione conforme o esperado em várias situações.
#6: Cria um subteste para cada iteração, permitindo que, se uma comparação falhar, o teste continue com os próximos casos em vez de interromper. Isso facilita a identificação de qual conjunto específico de valores falhou durante os testes.
#7: Especifica que um AssertionError deve ser levantado ao executar o código dentro do bloco. Se a exceção for levantada, o teste passa; caso contrário, falha. Isso valida que sum_sum trata adequadamente entradas inválidas, como uma string.
#8: Esta linha executa todos os testes definidos na classe TestCalculator. O parâmetro verbosity=2 faz com que o unittest exiba cada teste e seu resultado em detalhes, mostrando o status de cada um (passou ou falhou) ao final.

# https://linktr.ee/edsoncopque