import csv
import datetime
import re
class Zadanie:
    def __init__(self, temat, termin, opis = '-', data_rozpoczęcia = datetime.date.today().strftime('%d/%m/%y'), status = 'rozpoczęte'):
        self.temat = temat
        self.termin = termin
        self.opis = opis
        self.data_rozpoczęcia = data_rozpoczęcia
        self.status = status

#funkcja tworząca nowe zadanie, zwraca obiekt klasy Zadanie
    @classmethod
    def nowe_zadanie(cls):

        #sprawdza czy podana data przez użytkownika jest w formacie DD/MM/RR, jeśli nie jest to pozwala wpisać datę ponownie
        while True:
            termin = input('Podaj termin w formacie DD/MM/RR: ')
            if not re.match(r'^\d{2}/\d{2}/\d{2}$', termin):
                print('Niepoprawna data.')
            else:
                break
        nowe = Zadanie(input('Podaj temat zadania: ').lower(),termin)
        opis = input('Podaj opis (opcjonalne): ')       #pozwala zmienić opis zadania jeśli użytkownik coś wpisze
        if opis != None:
            Zadanie.opis = opis
            y = input('Wpisz "tak" lub "t" jeśli chcesz podać datę rozpoczęcia. Jeśli nie to wciśnij enter.')    #daje możliwość wpisania daty rozpoczęcia
            if y.lower() == 'tak' or y.lower() == 't':

                # sprawdza czy podana data przez użytkownika jest w formacie DD/MM/RR, jeśli nie jest to pozwala wpisać datę ponownie

                x = input('Podaj datę rozpoczęcia w formacie DD/MM/RR: ')
                while True:
                        if not re.match(r'^\d{2}/\d{2}/\d{2}$', x):
                            print('Niepoprawna data.')
                        else:
                            Zadanie.data_rozpoczęcia = x
                            break
                t = datetime.datetime.today()
                t.strftime("%d/%m/%y")
                data_r = datetime.datetime.strptime(x, "%d/%m/%y")

            # jeśli data rozpoczęcia jest późniejsza niż dzisiejsza, status zmieni się na 'nierozpoczęty
                if data_r > t:
                    Zadanie.status = 'nierozpoczęte'
        return nowe

    #funkcja przyjmuje obiekt i zapisuje go do pliku Lista zadań.csv
    def zapisz_zadanie(object):
        atrybuty = (object.temat, object.termin, object.opis, object.data_rozpoczęcia, object.status)
        with open('Lista zadań.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(atrybuty)
            file.close()
        return print('Zadanie zapisane \n')
