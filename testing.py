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

try: #2:
    print(sum_sum('10', 10))
except AssertionError as error_error: #1: #3:
    print(f'You screwed up, friend: {error_error}')


# ------------------------------------------------------------------
#1: Response: You screwed up, friend: X has to be INT or FLOAT, Edson.
#2: A vantagem é que usando 'assert' estamos nos comunicando com outros desenvolvedores, enquanto 'try'/'except' vai impedir que meu código seja interrompido;
#3: Esta linha captura o AssertionError caso ele seja gerado ao tentar executar sum_sum('10', 10).

# https://linktr.ee/edsoncopque