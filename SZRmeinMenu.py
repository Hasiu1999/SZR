# ============================================
# Aplikacja terminalowa – SZR Menu Główne
# Autor: [Bartłomiej Hasik]
# Wersja: 1.0
# ============================================

import csv
import os

#Ogólony szkielet strony :

def menu_glowne():
    while True:
        print("\n=== STRONA GŁÓWNA SZR ===")
        print("1. Tryby pracy SZR")
        print("2. Zdarzenia")
        print("3. Ustawienia")
        print("4. Aktualny status pracy urządznia")
        print("0. Zakończ program")
        
        wybor = input("Wybierz opcję: ")
        
        if wybor == "1":
            tryby_pracy()
        elif wybor == "2":
            zdarzenia()
        elif wybor == "3":
            ustawienia()
        elif wybor == "4":
            status()
        elif wybor == "0":
            print("\nZamykanie programu... Do zobaczenia!")
            break
        else:
            print("\n[UWAGA] Nieprawidłowy wybór, spróbuj ponownie.")
#Tryby Pracy:
def tryby_pracy():
    while True:
        print("\n--- TRYBY PRACY SZR ---")
        print("1. Automatyczny")
        print("2. Ręczny")
        print("3. Informacje")
        print("0. Powrót do menu głównego")
        
        wybor = input("Wybierz opcję: ")
        
        if wybor == "1":
            tryb_automatyczny()
        elif wybor == "2":
            tryb_reczny()
        elif wybor == "3":
            print("\n[INFO] Tryby pracy SZR: automatyczny, ręczny – w przygotowaniu.")
        elif wybor == "0":
            break
        else:
            print("\n[UWAGA] Nieprawidłowy wybór, spróbuj ponownie.")

#menu_glowne ()-->tryby_pracy-->automatyczny-->
def tryb_automatyczny():
    while True:
        print("\n--- TRYB AUTOMATYCZNY ---")
        print("1. Alternatywna linia zasilająca")
        print("2. Obsługa agregatu")
        print("3. Obsługa banku energii")
        print("0. Powrót do TRYBÓW PRACY")
        
        wybor = input("Wybierz opcję: ")
        
        if wybor == "1":
            obsluga_CSV("1","1")
            obsluga_CSV("4","1")
            obsluga_CSV("5","1")

        elif wybor == "2":
            obsluga_CSV("1","2")
            obsluga_CSV("4","2")
            obsluga_CSV("5","1")
        elif wybor == "3":
            obsluga_CSV("1","3")
            obsluga_CSV("4","3")
            obsluga_CSV("5","1")

        elif wybor == "0":
            break
        else:
            print("\n[UWAGA] Nieprawidłowy wybór, spróbuj ponownie.")
#menu_glowne ()-->tryby_pracy-->ręczny-->
def tryb_reczny():
    while True:
        obsluga_CSV("1","0")
        print("\n--- TRYB RĘCZNY ---")
        print("1. Alternatywna linia zasilająca")
        print("2. Obsługa agregatu")
        print("3. Bank energii")
        print("0. Powrót do TRYBÓW PRACY")

        wybor = input("Wybierz opcję: ")
        
        if wybor == "1":
            obsluga_CSV("4","1")
            sterowanie_reczne("1")
        elif wybor == "2":
            obsluga_CSV("4","2")
            sterowanie_reczne("2")
        elif wybor == "3":
            obsluga_CSV("4","3")
            sterowanie_reczne("3")
        elif wybor == "0":
            break
        else:
            print("\n[UWAGA] Nieprawidłowy wybór, spróbuj ponownie.")

def sterowanie_reczne(arg1):
    while True:
        if arg1 == '1':
            print("\n--- Alternatywana Linia zasilająca ---")
        elif arg1 == '2':
            print("\n--- Obsługa Agregatu ---")
        elif arg1 == '3':
            print("\n--- Obsługa Banku energii ---") 
        print("1. Podstawoa ")
        print("2. Rezerwowa ")
        print("3.Wyłącz zasilanie")
        print("0. Powrót do TRYB RĘCZNY")
        wybor1 = input("Wybierz opcję: ")
        if wybor1 == "1":
                obsluga_CSV("5","1")
        elif wybor1 == "2":
                obsluga_CSV("5","2")
        elif wybor1== "3":
            obsluga_CSV("5","3")
        elif wybor1 == "0":
            break
        else:
            print("\n[UWAGA] Nieprawidłowy wybór, spróbuj ponownie.")
#Zdarzenia:

def zdarzenia():
    while True:
        print("\n--- ZDARZENIA ---")
        print("1. Lista zdarzeń")
        print("2. Usuń zdarzenia")
        print("0. Powrót do menu głównego")
        
        wybor = input("Wybierz opcję: ")
        
        if wybor == "1":
            obsluga_CSV("2","1")
        elif wybor == "2":
            print("\n [Uwaga! czy napewno chcesz usnać zdarzenia wpisz kod fabryczny.]")

            wybor2 = input("Wpisz kod: ")

            if wybor2 == "1999":
                obsluga_CSV("3","0")

            else:
                print("zły kod!")
                zdarzenia()

        elif wybor == "0":
            break
        else:
            print("\n[UWAGA] Nieprawidłowy wybór, spróbuj ponownie.")

#Ustawienia :
def ustawienia():
    while True:
        print("\n--- USTAWIENIA ---")
        print("1. Konfiguracja systemu")
        print("2. Informacje o wersji")
        print("0. Powrót do menu głównego")
        
        wybor = input("Wybierz opcję: ")
        
        if wybor == "1":
            print("\n[INFO] Ustawienia systemu – w przygotowaniu.")
        elif wybor == "2":
            print("\n[INFO] Wersja aplikacji: 1.0 – SZR Terminal Demo.")
        elif wybor == "0":
            break
        else:
            print("\n[UWAGA] Nieprawidłowy wybór, spróbuj ponownie.")

def status():
    while True:
        print("\n--- Status urządzenia ---")
        obsluga_CSV("2","2")

        wybor = input("0. Menu główne ")
        if wybor == "0":
            break

# Obsługa plików csv
def obsluga_CSV(arg1,arg2):
    opcje = "opcje.csv"
    zdarzenia = "zdarzenia.csv"

    if arg1 == "1":
        dane = []
        # Wczytaj istniejące dane, jeśli plik istnieje
        if os.path.exists(opcje):
            with open(opcje, mode="r", newline="", encoding="utf-8") as plik:
                reader = csv.reader(plik)
                dane = list(reader)

            # Jeśli plik pusty – po prostu dodaj nowy wpis
        if not dane:
            dane.append([arg2])
        else:
            dane[0] = [arg2]  # <-- nadpisuje tylko pierwszy wiersz

        # Zapisz całość z powrotem do pliku
            with open(opcje, mode="w", newline="", encoding="utf-8") as plik:
                writer = csv.writer(plik)
                writer.writerows(dane)

                print(f"\n[OK] Zmieniono pierwszy wpis na: {arg2}")
    
    elif arg1 == "2":

        if arg2 == "1":
            "Wyświetla wszystkie zdarzenia z pliku CSV, każde po przecinku jako osobna linia."""
            if not os.path.exists(zdarzenia):
                print("\n[INFO] Plik CSV nie istnieje. Brak zapisanych zdarzeń.")
                return

            wszystkie = []
            with open(zdarzenia, mode="r", newline="", encoding="utf-8") as plik:
                reader = csv.reader(plik)
                for wiersz in reader:
                    # dla każdego elementu w wierszu (CSV może mieć wiele kolumn)
                    for pole in wiersz:
                        # dziel po przecinku i dodaj do listy
                        elementy = [e.strip() for e in pole.split(",") if e.strip()]
                        wszystkie.extend(elementy)

            if not wszystkie:
                print("\n[INFO] Brak zapisanych zdarzeń.")
            else:
                print("\n--- Zapisane zdarzenia ---")
                for idx, zdarzenie in enumerate(wszystkie, start=1):
                    print(f"{idx}. {zdarzenie}")

        elif arg2 == "2":
            "Wyświetla wszystkie zdarzenia z pliku CSV, każde po przecinku jako osobna linia."""
            if not os.path.exists(opcje):
                print("\n[INFO] Plik CSV nie istnieje. Brak zapisanych zdarzeń.")
                return

            wszystkie = []
            with open(opcje, mode="r", newline="", encoding="utf-8") as plik:
                reader = csv.reader(plik)
                for wiersz in reader:
                    # dla każdego elementu w wierszu (CSV może mieć wiele kolumn)
                    for pole in wiersz:
                        # dziel po przecinku i dodaj do listy
                        elementy = [e.strip() for e in pole.split(",") if e.strip()]
                        wszystkie.extend(elementy)

            if not wszystkie:
                print("\n[INFO] Brak zapisanych zdarzeń.")
            else:

                for idx, opcje in enumerate(wszystkie, start=1):
                    if idx == 1:
                        if opcje == '0':
                            print("Tryb ręczny status:")
                        else:
                            print("Tryb Automatyczny")
                    elif idx == 2:
                        if opcje == '1':
                            print("Alternatywna linia zasilająca")
                        elif opcje == '2':
                            print("Obsługa Agregatu")
                        elif opcje == '3':
                            print("Obsługa Banku energii")
                    elif idx == 3:
                        if opcje == '1':
                            print("Linia Podstawowa")
                        elif opcje == '2':
                            print("Linia Rezerwowa")
                        elif opcje == '3':
                            print("Wyłączone zasilanie")
                    else:
                        print("Proszę o kontakt z działem technicznym")

    elif arg1 == "3":

        """Kasuje wszystkie zdarzenia z pliku CSV."""
        if not os.path.exists(zdarzenia):
            print("\n[INFO] Plik CSV nie istnieje. Brak zdarzeń do usunięcia.")
            return

        # Otwórz plik w trybie "w", co nadpisuje jego zawartość pustą
        with open(zdarzenia, mode="w", newline="", encoding="utf-8") as plik:
            pass  # po prostu nadpisujemy pustym plikiem

        print("\n[OK] Wszystkie zdarzenia zostały usunięte.")

    elif arg1 == "4":
        dane = []
        # Wczytaj istniejące dane, jeśli plik istnieje
        if os.path.exists(opcje):
            with open(opcje, mode="r", newline="", encoding="utf-8") as plik:
                reader = csv.reader(plik)
                dane = list(reader)

            # Jeśli plik pusty – po prostu dodaj nowy wpis
        if not dane:
            dane.append([arg2])
        else:
            dane[1] = [arg2]  # <-- nadpisuje tylko pierwszy wiersz

        # Zapisz całość z powrotem do pliku
            with open(opcje, mode="w", newline="", encoding="utf-8") as plik:
                writer = csv.writer(plik)
                writer.writerows(dane)

                print(f"\n[OK] Zmieniono pierwszy wpis na: {arg2}")
    elif arg1 == "5":
        dane = []
        # Wczytaj istniejące dane, jeśli plik istnieje
        if os.path.exists(opcje):
            with open(opcje, mode="r", newline="", encoding="utf-8") as plik:
                reader = csv.reader(plik)
                dane = list(reader)

            # Jeśli plik pusty – po prostu dodaj nowy wpis
        if not dane:
            dane.append([arg2])
        else:
            dane[2] = [arg2]  # <-- nadpisuje tylko pierwszy wiersz

        # Zapisz całość z powrotem do pliku
            with open(opcje, mode="w", newline="", encoding="utf-8") as plik:
                writer = csv.writer(plik)
                writer.writerows(dane)

                print(f"\n[OK] Zmieniono pierwszy wpis na: {arg2}")

if __name__ == "__main__":
    menu_glowne()
