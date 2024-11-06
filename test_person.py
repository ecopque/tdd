# FILE: /TDD/test_person.py

import unittest
from person import Person

class TestPerson(unittest.TestCase):
    def setUp(self): ##
        self.p1 = Person('Edson', 'Copque')

    def test_person_attr_name_has_the_correct_value(self):
        self.assertEqual(self.p1.name, 'Edson') ##

    def test_person_attr_name_is_str(self):
        self.assertIsInstance(self.p1.name, str) ##

    def test_person_attr_lastname_has_the_correct_value(self):
        self.assertEqual(self.p1.last_name, 'Copque')

    def test_person_attr_lastname_is_str(self):
        self.assertIsInstance(self.p1.last_name, str)

    def test_person_attr_data_obtained_starts_false(self):
        self.assertFalse(self.p1.data_obtained) ##

    def test_get_all_data_success_ok(self):
        ...

if __name__ == '__main__':
    unittest.main(verbosity=2)


# https://linktr.ee/edsoncopque