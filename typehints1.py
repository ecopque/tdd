# FILE: /TDD/typehints1.py

# pip install mypy
from typing import List, Union, Tuple, Dict, Any #A: #B: #C:
#A: List | #B: Union | #C: Tuple | #D: Dict | E: Any

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



#1: No caso das tuplas, tenho que informar que cada um é 'int'. Ver outro exemplo.
#2: Observando o #1, agora neste exemplo está correto.
#3: Com '[str, str]' estou informando que a chave e dicionário são strings.
#4: Agora temos as chaves como string, e os valores podem ser string ou int.
#5: Também podemos informar 'Any', mas parece não ser uma boa prática.

# https://linktr.ee/edsoncopque