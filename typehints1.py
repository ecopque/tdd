# FILE: /TDD/typehints1.py

# pip install mypy
from typing import List, Union, Tuple, Dict, Any, NewType, Callable, Sequence, Iterable
#A: List | #B: Union | #C: Tuple | #D: Dict | E: Any | #F: NewType | #G: Callable | #H: Sequence | #I:

# primitive
number: int = 10
number: int = '10' #wrong

float_number: float = 10.5
bool_number: bool = True
string_var: str = 'Hi'

# sequences
list_var: list = [1, 2, 3]

list_var: List = [1, 2, 3] #A: ##
list_var: List[int] = [1, 2, 3] #A: ##
list_var: List[int] = [1, 2, 3, 'z'] #A: ## #wrong

list_str_int: List[Union[int, str]] = [1, 2, 3, 'z'] #A: #B: ##

tuple_var: tuple = [1, 2, 3] #wrong
tuple_var: tuple = (1, 2, 3)

tuple_var: Tuple = (1, 2, 3) #C:
tuple_var: Tuple[int] = (1, 2, 3) #C: #1: ## #wrong
tuple_var: Tuple[int, int, int] = (1, 2, 3) #C: #2:
tuple_var: Tuple[int, int, int, str] = (1, 2, 3, 'z') #C:

# dictionaries and sets
person: Dict[str, str] = {'name': 'Edson', 'lastname': 'Copque'} #D: #3: ##
person: Dict[str, str] = {'name': 'Edson', 'lastname': 'Copque', 'age': 90} #D: #wrong ##
person: Dict[str, Union[str, int]] = {'name': 'Edson', 'lastname': 'Copque', 'age': 90} #D: #4:
person: Dict[str, Union[str, int, List[int]]] = {'name': 'Edson', 'lastname': 'Copque', 'age': 90, 'list': [1, 2, 3]} #B: #A: ##
person: Dict[str, Any] = {'name': 'Edson', 'lastname': 'Copque', 'age': 90} #E: #5: ##

# my type
my_dict = Dict[str, Union[str, int, List[int]]] #alias
person: my_dict = {'name': 'Edson', 'lastname': 'Copque', 'age': 90, 'list': [1, 2, 3]} #6:

# My new type
userid_ = NewType('userid_', int) ##
userid_var = userid_(123456789) ##

def returns_function(function: Callable[[int, int], int]) -> Callable: #G: ##
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

def iterate(sequence: Sequence[int]): #H: ##
    return [x * 2 for x in sequence]
print(iterate([1, 2, 3]))

def iterate2(sequence: Iterable[int]): #I: ##
    return [x for x in sequence]
print(iterate2([1, 2, 3]))


#1: No caso das tuplas, tenho que informar que cada um é 'int'. Ver outro exemplo.
#2: Observando o #1, agora neste exemplo está correto.
#3: Com '[str, str]' estou informando que a chave e dicionário são strings.
#4: Agora temos as chaves como string, e os valores podem ser string ou int.
#5: Também podemos informar 'Any', mas parece não ser uma boa prática.
#6: Agora fica mais fácil ao usar 'my_dict'.

# https://linktr.ee/edsoncopque