import unittest
from funkcijos import sudetis, atimtis, daugyba, dalyba, ar_lyginis, suapvalinta_dalyba, prideti_i_zodyna

class TestFunkcijos(unittest.TestCase):

    def setUp(self):
        self.x = 10
        self.y = 5

    def tearDown(self):
        self.x = None
        self.y = None

    def test_sudetis(self):
        rezultatas = sudetis(5, 3)
        self.assertEqual(rezultatas, 8)

    def test_atimtis(self):
        rezultatas = atimtis(10, 5)
        self.assertEqual(rezultatas, 5)

    def test_daugyba(self):
        rezultatas = daugyba(5, 10)
        self.assertNotEqual(rezultatas, 40)

    def test_ar_lyginis(self):
        rezultatas = ar_lyginis(8)
        self.assertTrue(rezultatas)
        # self.assertEqual(True, rezultatas)  #tas pats 

    def test_ar_nelyginis(self):
        rezultatas = ar_lyginis(3)
        self.assertFalse(rezultatas)

    def test_suapvalinta_dalyba(self):
        rezultatas = suapvalinta_dalyba(16, 3)
        self.assertAlmostEqual(rezultatas, 5.3, places=1)

    def test_dalyba(self):
        rezultatas = dalyba(self.x, self.y)
        self.assertEqual(rezultatas, 2)

    def test_dalyba_is_nulio(self):
        with self.assertRaises(ZeroDivisionError):
            dalyba(10, 0)

    def test_dalyba_be_argumentu(self):
        with self.assertRaises(Exception):
            dalyba(None, None)

    def test_zodynas(self):
        self.assertDictEqual({'key': 'value'}, {'key': 'value'})

    def test_prideti_i_zodyna(self):
        rezultatas = prideti_i_zodyna('siandien yra pirmadienis')
        zodynas = {'raktas': 'siandien yra pirmadienis'}
        self.assertDictEqual(rezultatas, zodynas)


if __name__ == '__main__':
    unittest.main()
