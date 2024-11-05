# FILE: /TDD/test_person.py

import unittest
from person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('Edson', 'Copque')

    def test_person_attr_name_has_the_correct_value(self):
        ...

if __name__ == '__main__':
    unittest.main(verbosity=2)


# https://linktr.ee/edsoncopque