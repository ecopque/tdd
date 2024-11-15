# FILE: /TDD/typehints1.py

# pip install mypy
from typing import List, Union, Tuple #A: #B: #C:
#A: List | #B: Union | #C: Tuple

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


#1: No caso das tuplas, se tenho que informar que cada um é 'int'. Ver outro exemplo;

# https://linktr.ee/edsoncopque