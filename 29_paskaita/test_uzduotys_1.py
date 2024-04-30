import unittest
from uzduotys_1 import prideti_elementa, ar_nelyginis, ar_palindromas, palyginti_sarasus

# 1

class TestPridetiElementa(unittest.TestCase):

    def setUp(self):
        self.sarasas = [1, 3, 5]
    
    def tearDown(self):
        self.sarasas = None

    def test_prideti_nauja_elementa(self):
        naujas_sarasas = prideti_elementa(self.sarasas, 2)
        self.assertEqual(naujas_sarasas, [1, 2, 3, 5])

    def test_prideti_egzistuojanti_elementa(self):
        naujas_sarasas = prideti_elementa(self.sarasas, 3)
        self.assertEqual(naujas_sarasas, [1, 3, 5])


# 2

class TestArNelyginis(unittest.TestCase):

    def test_ar_nelyginis(self):
        rezultatas = ar_nelyginis(3)
        self.assertTrue(rezultatas)
    
    def test_ar_lyginis(self):
        rezultatas = ar_nelyginis(2)
        self.assertFalse(rezultatas)

# 3

class TestArPalindromas(unittest.TestCase):

    def test_ar_palindromas(self):
        rezultatas = ar_palindromas('level')
        self.assertTrue(rezultatas)

    def test_ne_palindromas(self):
        rezultatas = ar_palindromas('hello')
        self.assertFalse(rezultatas)
        
# 4

class TestPalygintiSarasus(unittest.TestCase):

    def test_lygus_sarasai(self):
        sarasai = palyginti_sarasus([1, 2, 3], [1, 2, 3])
        self.assertEqual(sarasai, True)

    def test_skirtingi_sarasai(self):
        sarasai = palyginti_sarasus([1, 2, 3], [2, 5, 8])
        self.assertNotEqual(sarasai, True)


if __name__ == '__main__':
    unittest.main()