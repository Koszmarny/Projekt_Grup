from flask import Flask, render_template, session
from datetime import date
import locale
import Cython
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
locale.setlocale(locale.LC_TIME, 'pl_PL.UTF-8')

"""
    Funkcja zwraca tuplę tupli zawierających dane pobrane z pliku csv
    do zapisania w tabeli.
    """


# def pobierz_dane(pliczek):
#
#     dane = []  # deklarujemy pustą listę
#     if os.path.isfile(pliczek):  # sprawdzamy czy plik istnieje na dysku
#         with open(pliczek, "dane.txt") as zawartosc:  # otwieramy plik do odczytu
#             for linia in zawartosc:
#                 linia = linia.replace("\n", "")  # usuwamy znaki końca linii
#                 linia = linia.replace("\r", "")  # usuwamy znaki końca linii
#                 linia = linia.decode("utf-8")  # odczytujemy znaki jako utf-8
#                 # dodajemy elementy do tupli a tuplę do listy
#                 dane.append(tuple(linia.split(",")))
#     else:
#         print "Plik z danymi", pliczek, "nie istnieje!"
#
#     return tuple(dane)


@app.route('/', methods=['GET, POST'])
def home():

    plik = open('dane.txt')
    try:
        dane = plik.read()
    finally:
        plik.close()
    data = "Dzisiaj jest: " + date.today().strftime("%A %d %B %Y")
    plt.plot([])
    plt.ylabel('Poziom promieniowania')
    plt.xlabel('Czas')

    return render_template('Logowanie.html', dzisiaj=data, powitanie="Witaj " + session.get("login", "nieznajomy"))


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
app.run(debug=True, host='0.0.0.0', port=10111)
