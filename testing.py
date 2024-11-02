# FILE: /TDD/testing.py

from calculator import sum_sum

# print(sum_sum(10, 50))
# print(sum_sum(-10, 50))
# print(sum_sum(10.5, 11))

try:
    print(sum_sum('100', 50))
except TypeError as error_error:
    print('Error, man!')
    print(error_error)
    

# https://linktr.ee/edsoncopque