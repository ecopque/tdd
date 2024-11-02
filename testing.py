# FILE: /TDD/testing.py

from calculator import sum_sum

# print(sum_sum(10, 50))
# print(sum_sum(-10, 50))
# print(sum_sum(10.5, 11))

# try:
#     print(sum_sum('100', 50))
# except TypeError as error_error:
#     print('Error, man!')
#     print(error_error)

try:
    print(sum_sum('10', 10))
except AssertionError as error_error:
    print(f'You screwed up, friend: {error_error}')



#1: Response: 

# https://linktr.ee/edsoncopque