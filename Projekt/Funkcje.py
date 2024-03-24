import csv
import datetime
import sys
from Zadanie import Zadanie

#dekorator zmieniający status zadania jeśli termin jest datą wcześniejszą niż dzisiejsza.
def termin(func):
    def wrapper():
        today = datetime.datetime.today()
        today.strftime("%d/%m/%y")
        with open('Lista zadań.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = list(reader)
            for row in rows:
                if row and datetime.datetime.strptime(row[1], "%d/%m/%y") < today:
                    if row[4] != 'ukończone':
                        row[4] = 'po terminie'
                elif row and datetime.datetime.strptime(row[3], "%d/%m/%y") > today:
                    if row[4] == 'rozpoczęte':
                        row[4] = 'nierozpoczęte'
            with open('Lista zadań.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(rows)
                file.close()
        func()
    return wrapper
#funkcja wyświetlająca wszystkie zadania po uruchomieniu programu
@termin
def pokaż_zadania():
    with open('Lista zadań.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
        file.close()

#funkcja pozwalająca na usunięcie zadania poprzez podanie tematu zadania
def usuń_zadanie():
        x = input('Podaj temat zadania, które chcesz usunąć: ')
        with open('Lista zadań.csv', 'r') as file:
            reader = csv.reader(file)
            rows = [row for row in reader if row and row[0] != x]
            with open('Lista zadań.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
                file.close()
        return print('Zadanie usunięte')

#Funkcja pozwalająca edytować wcześniej utworzone zadanie.
def edytuj_zadanie():
    x = input('Podaj temat zadania, które chcesz zmienić: ')
    while True:
        y = input('Podaj atrybut, który chcesz zmienić: ')
        w = input(f'Podaj nową wartość {y} (jeśli zmieniasz termin lub datę rozpoczęcia, pamiętaj o formacie DD/MM/RR, \na jeśli zmieniasz status to wpisz jeden z dostępnych statusów: \nnierozpoczęte, rozpoczęte, ukończone, po terminie):')
        if y == 'status':
            statusy = ['nierozpoczęte', 'rozpoczęte', 'ukończone', 'po terminie']
            if w.lower() not in statusy:
                raise ValueError('Nie ma takiego statusu.')
        rows = []
        with open('Lista zadań.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row and row['temat'] == x:
                    row[y] = w
                rows.append(row)
        with open('Lista zadań.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['temat', 'termin', 'opis', 'data rozpoczęcia', 'status'])
            writer.writeheader()
            writer.writerows(rows)
            file.close()
            z = input('Jeśli nie chcesz zmienić kolejnego atrybutu wciśnij "nie" lub "n". Jeśli chcesz zmienić kolejny atrybut wciśnij "enter"')  #po zmianie jednego atrybutu funkcja daje możliwość edytowania kolejnego atrybutu
            if z.lower() == 'nie' or z.lower() == 'n':
                break
#funkcja wyświetlająca dostępne opcje (menu) programu
def pokaż_opcje():
    opcje = ['Opcje: ', '1. Dodaj nowe zadanie', '2. Edytuj zadanie', '3. Usuń zadanie', '4. Wyjdź']
    for item in opcje:
       print(item)

#funkcja, która pozwala wybrać opcję z wyświetlonych na ekranie.
def wybierz_opcję():
    while True:
        try:
            x = input('Podaj numer opcji: ')
            if x not in ['1', '2', '3', '4']:   #jeśli użytkownik nie poda numeru opcji, funkcja wyświetli błąd i pozwoli ponownie wybrać opcję
                raise ValueError
            else:
                break
        except ValueError:
            print('Nie ma takiej opcji.')
    if x == '1':
        projekt = Zadanie.nowe_zadanie()
        projekt.zapisz_zadanie()
    elif x == '2':
        edytuj_zadanie()
    elif x == '3':
        usuń_zadanie()
    elif x == '4':
        sys.exit()
