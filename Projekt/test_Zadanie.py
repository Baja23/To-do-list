import unittest
import Zadanie
import datetime
import Funkcje
from unittest.mock import patch

class TestZadanie(unittest.TestCase):

    #test sprawdza czy jeśli użytkownik nie poda daty rozpoczęcia, ta ustawi się automatycznie na datę dzisiejszą
    def test_nowe_zadanie(self):
        zadanie1 = Zadanie.Zadanie('projekt1', '07/02/24')
        t = datetime.datetime.today()
        zadanie2 = Zadanie.Zadanie('projekt2', termin='20/02/24', data_rozpoczęcia='19/02/24')
        self.assertEqual(zadanie1.data_rozpoczęcia, t.strftime("%d/%m/%y"))
        self.assertEqual(zadanie2.data_rozpoczęcia, '19/02/24')

    #test sprawdza czy po ustawieniu daty rozpoczęcia na datę późniejszą niż dzisiejsza status zmieni się na 'nierozpoczęte'
    def test_nowe_zadanie2(self):
        zadanie1 = Zadanie.Zadanie(temat='projekt1', termin= '20/02/24', data_rozpoczęcia= '19/02/24')
        self.assertEqual(zadanie1.status, 'nierozpoczęte')

if __name__ == '__main__':
    unittest.main()

