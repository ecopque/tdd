# FILE: /TDD/typehints1.py

# pip install mypy
from typing import List, Union, Tuple, Dict, Any, NewType, Callable, Sequence, Iterable
#A: List | #B: Union | #C: Tuple | #D: Dict | E: Any | #F: NewType | #G: Callable | #H: Sequence | #I: Iterable

# primitive
number: int = 10
number: int = '10' #wrong

float_number: float = 10.5
bool_number: bool = True
string_var: str = 'Hi'

# sequences
list_var: list = [1, 2, 3]

list_var: List = [1, 2, 3] #A: #7:
list_var: List[int] = [1, 2, 3] #A: #8:
list_var: List[int] = [1, 2, 3, 'z'] #A: #9: #wrong

list_str_int: List[Union[int, str]] = [1, 2, 3, 'z'] #A: #B: #10:

tuple_var: tuple = [1, 2, 3] #wrong
tuple_var: tuple = (1, 2, 3)

tuple_var: Tuple = (1, 2, 3) #C:
tuple_var: Tuple[int] = (1, 2, 3) #C: #1: #11: #wrong
tuple_var: Tuple[int, int, int] = (1, 2, 3) #C: #2:
tuple_var: Tuple[int, int, int, str] = (1, 2, 3, 'z') #C:

# dictionaries and sets
person: Dict[str, str] = {'name': 'Edson', 'lastname': 'Copque'} #D: #3:
person: Dict[str, str] = {'name': 'Edson', 'lastname': 'Copque', 'age': 90} #D: #wrong #12:
person: Dict[str, Union[str, int]] = {'name': 'Edson', 'lastname': 'Copque', 'age': 90} #D: #4:
person: Dict[str, Union[str, int, List[int]]] = {'name': 'Edson', 'lastname': 'Copque', 'age': 90, 'list': [1, 2, 3]} #B: #A: #13:
person: Dict[str, Any] = {'name': 'Edson', 'lastname': 'Copque', 'age': 90} #E: #5: #14:

# my type
my_dict = Dict[str, Union[str, int, List[int]]] #alias
person: my_dict = {'name': 'Edson', 'lastname': 'Copque', 'age': 90, 'list': [1, 2, 3]} #6:

# My new type
userid_ = NewType('userid_', int) #15:
userid_var = userid_(123456789) #16:

def returns_function(function: Callable[[int, int], int]) -> Callable: #G: #17:
    return function
def sum_sum(x: int, y: int) -> int:
    return x + y
print(returns_function(sum_sum)(10, 15))

class Person:
    def __init__(self, name: str, lastname: str, age: int) -> None:
        self.name: str = name
        self.lastname: str = lastname
        self.age: int = age
    def speaking(self) -> None:
        print(f'{self.name} {self.lastname} is speaking... ')

def iterate(sequence: Sequence[int]): #H: #18:
    return [x * 2 for x in sequence]
print(iterate([1, 2, 3]))

def iterate2(sequence: Iterable[int]): #I: #19:
    return [x for x in sequence]
print(iterate2([1, 2, 3]))


#1: No caso das tuplas, tenho que informar que cada um é 'int'. Ver outro exemplo.
#2: Observando o #1, agora neste exemplo está correto.
#3: Com '[str, str]' estou informando que a chave e dicionário são strings.
#4: Agora temos as chaves como string, e os valores podem ser string ou int.
#5: Também podemos informar 'Any', mas parece não ser uma boa prática.
#6: Agora fica mais fácil ao usar 'my_dict'.
#7: Aqui, List é importado do módulo typing e utilizado para tipagem. A anotação List especifica que list_var é uma lista, mas sem restrição de tipo específico para os itens. Ou seja, a lista pode conter valores de qualquer tipo (int, str, etc.). Essa linha define list_var como uma lista de elementos não tipados.
#8: Esta linha é semelhante à anterior, mas agora List[int] indica que list_var é uma lista que deve conter apenas inteiros. List[int] é mais específico que apenas List, garantindo que todos os elementos em list_var sejam do tipo int.
#9: Esta linha tenta atribuir uma lista que contém um item str ('z') em uma lista tipada como List[int], que deveria conter apenas inteiros. Isso é considerado incorreto (#wrong) pois viola a anotação List[int], que só permite valores do tipo int.
#10: A anotação List[Union[int, str]] indica que list_str_int pode conter elementos que sejam do tipo int ou str. Union é usado aqui para combinar os tipos permitidos. Essa linha é válida, pois a lista contém inteiros e uma string, o que está de acordo com a tipagem definida.
#11: Aqui, Tuple[int] indica que tuple_var deveria ser uma tupla contendo um único elemento do tipo int. No entanto, (1, 2, 3) contém três elementos, o que viola a tipagem definida (#wrong). Para essa tupla ser válida, deveria ser algo como (1,).
#12: Nesta linha, Dict[str, str] espera que todos os valores sejam str. No entanto, o valor de age é um int (90), o que causa incompatibilidade com a anotação, marcado como #wrong.
#13: Esta linha define person como um dicionário onde os valores podem ser str, int, ou List[int]. Aqui, Union permite combinar esses tipos. A atribuição é válida, pois name e lastname são str, age é int, e list é uma List[int].
#14: Any permite que os valores sejam de qualquer tipo. Aqui, Dict[str, Any] permite que person contenha valores de tipos variados sem restrições. Atribuir {'name': 'Edson', 'lastname': 'Copque', 'age': 90} é válido, pois Any não impõe limitações de tipo.
#15: NewType cria um novo tipo baseado em um tipo existente, neste caso, int. Isso permite que userid_ seja tratado como um tipo distinto de int, útil para adicionar semântica específica ao tipo. userid_ é agora um tipo personalizado, indicando que representa um "ID de usuário".
#16: Aqui, userid_var é inicializado como um userid_, com o valor 123456789. Isso aplica o tipo personalizado criado na linha anterior, diferenciando userid_var de um int comum, apesar de usar internamente o valor int.
#17: Callable[[int, int], int] especifica que function é uma função que recebe dois int como parâmetros e retorna um int. A função returns_function recebe essa Callable e a retorna. Isso permite que qualquer função com essa assinatura seja passada como argumento para returns_function e seja retornada.
#18: Sequence[int] indica que sequence é uma sequência (como uma lista ou tupla) de inteiros. A função iterate recebe essa sequência e retorna uma nova lista com cada elemento multiplicado por 2. Sequence é uma interface que representa uma coleção ordenada de itens e permite flexibilidade ao aceitar listas, tuplas, etc.
#19: Iterable[int] indica que sequence é qualquer objeto iterável de inteiros. A função iterate2 recebe essa sequência e retorna uma lista com os mesmos elementos. Iterable é mais genérico que Sequence, pois inclui qualquer objeto que possa ser iterado (como listas, tuplas, conjuntos e até geradores).


# https://linktr.ee/edsoncopque