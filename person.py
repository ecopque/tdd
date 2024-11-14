# FILE: /TDD/person.py

import requests

class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.data_obtained = False

    def get_all_data(self):
        response = requests.get('https://www.google.com')
        if response.ok:
            return 'Connected'



# https://linktr.ee/edsoncopque