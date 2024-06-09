import unittest

import main

class TestStudentRace(unittest.TestCase):


    def test_first(self):
        self.pasha = main.Student(name='Паша')
        self.pasha.distance = 0
        for i in range(1, 11):
            self.pasha.walk()
        self.assertEqual( 500, self.pasha.distance,f'Дистанции не равны! {self.pasha} ПРОШЁЛ:')

    def test_second(self):
        self.pasha = main.Student(name='Паша')
        self.pasha.distance = 0
        for i in range(1, 11):
            self.pasha.run()
        self.assertEqual(1000, self.pasha.distance, f'Дистанции не равны! {self.pasha} ПРОБЕЖАЛ:')


    def test_third(self):
        self.pasha = main.Student(name='Паша')
        self.pasha.distance = 0
        self.vitaly = main.Student(name='Виталик')
        self.vitaly.distance = 100
        for i in range(1, 11):
            self.pasha.run()
            self.vitaly.walk()
        self.assertGreater( self.pasha.distance, self.vitaly.distance, f' {self.pasha} должен преодолеть дистанцию'
                                                                    f' больше, чем {self.vitaly}')


if __name__ == '__main__':
    unittest.main()