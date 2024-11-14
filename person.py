# FILE: /TDD/person.py

import requests

class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.data_obtained = False

    def get_all_data(self):
        response = requests.get('https://www.google.com') #1:
        if response.ok: #2:
            return 'Connected'


#1: A função get_all_data faz uma requisição HTTP para o Google usando requests.get. No código real (não testado diretamente no teste), isso tentaria se conectar à Internet. No entanto, durante os testes, essa chamada será substituída por um mock com o uso de patch para evitar uma requisição real.
#2: Após a requisição, o código verifica se a resposta foi bem-sucedida, usando o atributo ok do objeto response. Se a requisição foi bem-sucedida (status 200 OK), o método retorna a string 'Connected'. Caso contrário, o comportamento padrão não está explicitado neste código, mas poderia envolver um tratamento de erro ou outra resposta. Durante os testes, esse comportamento é simulado com response.ok configurado como True.

# https://linktr.ee/edsoncopque