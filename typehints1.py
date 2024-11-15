# FILE: /TDD/typehints1.py

# pip install mypy

# primitive
number: int = 10
number: int = '10' # wrong
float_number: float = 10.5
bool_number: bool = True
string_var: str = 'Hi'

# sequences
list_var: list = [1, 2, 3]
tuple_var: tuple = (1, 2, 3)
tuple_var: tuple = [1, 2, 3] # wrong

# https://linktr.ee/edsoncopque