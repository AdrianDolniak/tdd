#!/usr/bin/python
import unittest
import program
import random

class TestTdd(unittest.TestCase):
    def test_1_test(self):
        self.assertTrue(True)
#testy f1
    def test_f01_1(self):
        w=program.f1(0)
        self.assertEqual(0,w)

    def test_f01_2(self):
        w=program.f1(1)
        self.assertEqual(1,w)

    def test_f01_3(self):
        w=program.f1(2)
        self.assertEqual(4,w)

    def test_f01_4(self):
        w=program.f1(2,1)
        self.assertEqual(5,w)

    def test_f01_5(self):
        w=program.f1(2,3)
        self.assertEqual(7,w)
# testy f2
    def test_f02_1(self):
        w=program.f2('ala')
        self.assertEqual('a',w)

    def test_f02_2(self):
        w=program.f2([1,2,3])
        self.assertEqual(1,w)

    def test_f02_3(self):
        w=program.f2([])
        self.assertEqual('BUUUUM',w)
#test f3
    def test_f03_1(self):
        w=program.f3(1)
        self.assertEqual('jeden',w)

    def test_f03_2(self):
        w=program.f3(2)
        self.assertEqual('dwa',w)

    def test_f03_3(self):
        w=program.f3(3)
        self.assertEqual('trzy',w)

    def test_f03_4(self):
        w=program.f3(random.choice(range(4,1000)))
        self.assertEqual('other',w)

#test f4
    def test_f04_1(self):
        w=program.f4('ala')
        self.assertEqual('ala ma kota',w)

    def test_f04_2(self):
        w=program.f4('kot')
        self.assertEqual('kot ma kota',w)

    def test_f04_3(self):
        w=program.f4('kot','psa')
        self.assertEqual('kot ma kota i psa',w)

    def test_f04_4(self):
        w=program.f4('kot','mysz')
        self.assertEqual('kot ma kota i mysz',w)
#test f5
    def test_f05_1(self):
        w=program.f5(0)
        self.assertEqual([],w)

    def test_f05_2(self):
        w=program.f5(1)
        self.assertEqual([0],w)

    def test_f05_3(self):
        w=program.f5(2)
        self.assertEqual([0,1],w)

    def test_f05_4(self):
        w=program.f5(7)
        self.assertEqual([0,1,2,3,4,5,6],w)

    def test_f05_5(self):
        w=program.f5(7,2)
        self.assertEqual([0,2,4,6],w)

    def test_f05_6(self):
        w=program.f5(17,2)
        self.assertEqual([0,2,4,6,8,10,12,14,16],w)

    def test_f05_7(self):
        w=program.f5(17,5)
        self.assertEqual([0,5,10,15],w)
#test f6
    def test_f06_1(self):
        w=program.f6(1,'*')
        self.assertEqual('*',w)

    def test_f06_2(self):
        w=program.f6(7,'*')
        self.assertEqual('*******',w)
#test f7
    def test_f07_1(self):
        w=program.f7('ala')
        self.assertEqual('slowo',w)

    def test_f07_2(self):
        w=program.f7(1)
        self.assertEqual('cyfra',w)

    def test_f07_3(self):
        w=program.f7(11111)
        self.assertEqual('liczba',w)

    def test_f07_4(self):
        w=program.f7(-11111)
        self.assertEqual('liczba_ze_znakiem',w)

    def test_f07_5(self):
        w=program.f7('Ala ma kota.')
        self.assertEqual('zdanie',w)

    def test_f07_6(self):
        w=program.f7('<taaag>')
        self.assertEqual('tag poczatkowy',w)

    def test_f07_7(self):
        w=program.f7('</taaag>')
        self.assertEqual('tag koncowy',w)

#test f8
    def test_f08_1(self):
        w=program.f8('kot','ala ma kota')
        self.assertEqual(True,w)

    def test_f08_2(self):
        w=program.f8('pies','ala ma kota')
        self.assertEqual(False,w)

#test f9
    def test_f09_1(self):
        w=program.f9(1,2)
        self.assertEqual('dodatnie',w)

    def test_f09_2(self):
        w=program.f9(-1,-2)
        self.assertEqual('ujemne',w)

    def test_f09_3(self):
        w=program.f9(-1,1)
        self.assertEqual('roznych znakow',w)

    def test_f09_4(self):
        w=program.f9(-1,0)
        self.assertEqual('jest zero',w)

#test f10
    def test_f10_1(self):
        w=program.f10(1,1)
        self.assertEqual('rowne',w)

    def test_f10_2(self):
        w=program.f10(1,2)
        self.assertEqual('rozne',w)

if __name__ == '__main__':
    unittest.main()
