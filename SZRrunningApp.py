import time
from datetime import datetime

import RPi.GPIO as GPIO
import time
import csv
import os
#settings
standard_PIN = 2
reserve_PIN = 3
#signalStandard_PIN = 4
#signalReserve_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(standard_PIN, GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(reserve_PIN, GPIO.OUT)
GPIO.output(standard_PIN, GPIO.LOW)
time.sleep(0.2)
GPIO.output(reserve_PIN, GPIO.LOW)
time.sleep(0.2)

def loggsCSV(arg, zdarzenia = "zdarzenia.csv" ):
    
    # Otwieramy plik w trybie dopisywania ('a')
    now = datetime.now()
    dateandtime = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(zdarzenia, mode='a', newline='', encoding='utf-8') as plik:
        writer = csv.writer(plik)
        # Zapisujemy argument jako jeden wiersz
        writer.writerow([dateandtime,arg])

def monitoringCSV():
    opcje = "opcje.csv"
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
                        #print("Tryb ręczny status:")
                        workmood = ['0','10','10']
                    else:
                        #print("Tryb Automatyczny")
                        workmood = ['1','10','10']
                elif idx == 2:
                    if opcje == '1':
                        #print("Alternatywna linia zasilająca")
                        workmood[1] = '1'

                    elif opcje == '2':
                        #print("Obsługa Agregatu")
                        workmood[1] = '2'
                    elif opcje == '3':
                        #print("Obsługa Banku energii")
                        workmood[1] = '3'
                elif idx == 3:
                    if opcje == '1':
                        #print("Linia Podstawowa")
                        workmood[2] = '1'
                    elif opcje == '2':
                        #print("Linia Rezerwowa")
                        workmood[2] = '2'
                    elif opcje == '3':
                        #print("Wyłączone zasilanie")
                        workmood[2] = '3'
                    else:
                        print("Proszę o kontakt z działem technicznym")
    time.sleep(0.1)
    return workmood

def relayservice(atr):
    relay_state = GPIO.input(standard_PIN)
    relay_state1 = GPIO.input(reserve_PIN)

    if atr == 1 and relay_state == GPIO.LOW :
        GPIO.output(standard_PIN, GPIO.HIGH)
        time.sleep(0.2)
    elif atr == 2 and relay_state1 == GPIO.LOW :
        GPIO.output(reserve_PIN, GPIO.HIGH)
        time.sleep(0.2)
    if atr == 1 and relay_state1 == GPIO.HIGH :
        GPIO.output(standard_PIN, GPIO.LOW)
        time.sleep(0.2)
    elif atr == 2 and relay_state1 == GPIO.HIGH:
        GPIO.output(reserve_PIN, GPIO.LOW)
        time.sleep(0.2)    
    else:
        print("Skątaktuj sie z servisem")

def meinMotor():
        
        workmoodCSV_first = monitoringCSV()
        print(workmoodCSV_first)
        
        while True:
            workmoodCSV_second = monitoringCSV()
            if workmoodCSV_first != workmoodCSV_second:
                print(workmoodCSV_second)
                workmoodCSV_first = workmoodCSV_second
                #Automat:
                if workmoodCSV_second == ["1","1","1"]:
                    #Wyłącz przkaznik rezerwy , załącz przekażnik podstawy
                    print("Linia Alternatywna")
                    print("Załączono przekaźnik lini podstawoej")
                    loggsCSV("Linia Alternatywna")
                    loggsCSV("Załączono przekaźnik lini podstawoej")
                    relayservice(1)
                elif workmoodCSV_second == ["1","1","2"]:
                    #Wyłącz przekaźnik podstawy, załącz przekaźnik rezerwy 
                    print("Linia Alternatywna")
                    print ("Załączono przekaznik lini rezerwowej")
                    loggsCSV("Linia Alternatywna")
                    loggsCSV("Załączono przekaznik lini rezerwowej")
                elif workmoodCSV_second == ["1","1","3"]:
                    #Wyłącz przkaznik podstawy i rezerwy 
                    print("Linia Alternatywna")
                    print("wyłączono zasilanie")
                    loggsCSV("Linia Alternatywna")
                    loggsCSV("wyłączono zasilanie")
                elif workmoodCSV_second == ["1","2","1"]:
                    #Wyłącz przkaznik rezerwy , załącz przekażnik podstawy
                    print("obsługa agregatu")
                    print("Załączono przekaźnik lini podstawowej")
                    loggsCSV("obsługa agregatu")
                    loggsCSV("Załączono przekaźnik lini podstawowej")

                elif workmoodCSV_second == ["1","2","2"]:
                    #Wyłącz przkaznik Podstawy 
                    #Załącz przkaznik ssanie 
                    #załącz przekaznik rozruch 
                    #sprawdz napiecie jesli jest wyłącz ssanie 
                    #załacz przkaznik rezerwy 
                    print("Obsługa agregatu ")
                    print("Załączono agregat")
                    loggsCSV("obsługa agregatu")
                    loggsCSV("Załączono agregat")
                elif workmoodCSV_second == ["1","2","3"]:
                    #Wyłącz przkaznik rezerwy , załącz przekażnik podstawy , wyłącz rozruch agregatu
                    print("Obsługa agregatu")
                    print("wyłączono zasilanie")
                    loggsCSV("obsługa agregatu")
                    loggsCSV("Wyłączono Zasilanie")
                elif workmoodCSV_second == ["1","3","1"]:
                    #Wyłącz przkaznik rezerwy , załącz przekażnik podstawy , wyłącz rozruch agregatu
                    print("Obsługa Banku energii")
                    print("In Progress")
                    loggsCSV("Obsługa Banku energii")
                    loggsCSV("In Progress")
                elif workmoodCSV_second == ["1","3","2"]:
                    #Wyłącz przkaznik rezerwy , załącz przekażnik podstawy , wyłącz rozruch agregatu
                    print("Obsługa Banku energii")
                    print("In Progress") 
                    loggsCSV("Obsługa Banku energii")
                    loggsCSV("In Progress") 
                elif workmoodCSV_second == ["1","3","3"]:
                    #Wyłącz przkaznik rezerwy , załącz przekażnik podstawy , wyłącz rozruch agregatu
                    print("Obsługa Banku energii")
                    print("In Progress")   
                    loggsCSV("Obsługa Banku energii")
                    loggsCSV("In Progress") 
                #Sterowanie ręczne 
                elif workmoodCSV_second == ["0","1","1"]:
                    #załącz przekaźnik podstawy, wyłącz przekaźnik rezerwy 
                    print("Linia Alternatywna sterownie ręczne")
                    print ("Załączono przekaznik lini Podstawowej")
                    loggsCSV("Linia Alternatywna sterowanie ręczne")
                    loggsCSV("Załączono przekaznik lini podstawoej")
                elif workmoodCSV_second == ["0","1","2"]:
                    #Wyłącz przekaźnik podstawy, załącz przekaźnik rezerwy 
                    print("Linia Alternatywna sterownie ręczne")
                    print ("Załączono przekaznik lini rezewowej")
                    loggsCSV("Linia Alternatywna sterowanie ręczne")
                    loggsCSV("Załączono przekaznik lini rezerwowej")
                elif workmoodCSV_second == ["0","1","3"]:
                    #Wyłącz przekaźnik podstawy, wyłącz przekaźnik rezerwy 
                    print("Linia Alternatywna sterownie ręczne")
                    print ("Wyłączono zasilanie")
                    loggsCSV("Linia Alternatywna sterowanie ręczne")
                    loggsCSV("Wyłączono zasilanie")

                elif workmoodCSV_second == ["0","2","1"]:
                    #Wyłącz przkaznik rezerwy , załącz przekażnik podstawy
                    print("obsługa agregatu sterownie ręczne")
                    print("Załączono przekaźnik lini podstawowej")
                    loggsCSV("obsługa agregatu sterownie ręczne")
                    loggsCSV("Załączono przekaźnik lini podstawowej")

                elif workmoodCSV_second == ["0","2","2"]:
                    #Wyłącz przkaznik Podstawy 
                    #Załącz przkaznik ssanie 
                    #załącz przekaznik rozruch 
                    #sprawdz napiecie jesli jest wyłącz ssanie 
                    #załacz przkaznik rezerwy 
                    print("Obsługa agregatu sterownie ręczne ")
                    print("Załączono agregat")
                    loggsCSV("obsługa agregatu sterownie ręczne")
                    loggsCSV("Załączono agregat")

                elif workmoodCSV_second == ["0","2","3"]:
                    #Wyłącz przkaznik rezerwy , załącz przekażnik podstawy , wyłącz rozruch agregatu
                    print("Obsługa agregatu sterownie ręczne")
                    print("wyłączono zasilanie")
                    loggsCSV("obsługa agregatu sterownie ręczne")
                    loggsCSV("Wyłączono Zasilanie")   

                elif workmoodCSV_second == ["0","3","1"]:
                    #Wyłącz przkaznik rezerwy , załącz przekażnik podstawy , wyłącz rozruch agregatu
                    print("Obsługa Banku energii sterownie ręczne")
                    print("In Progress")
                    loggsCSV("Obsługa Banku energii sterownie ręczne")
                    loggsCSV("In Progress")
                elif workmoodCSV_second == ["0","3","2"]:
                    #Wyłącz przkaznik rezerwy , załącz przekażnik podstawy , wyłącz rozruch agregatu
                    print("Obsługa Banku energii sterownie ręczne")
                    print("In Progress") 
                    loggsCSV("Obsługa Banku energii sterownie ręczne")
                    loggsCSV("In Progress") 
                elif workmoodCSV_second == ["0","3","3"]:
                    #Wyłącz przkaznik rezerwy , załącz przekażnik podstawy , wyłącz rozruch agregatu
                    print("Obsługa Banku energii sterownie ręczne ")
                    print("In Progress")   
                    loggsCSV("Obsługa Banku energii sterownie ręczne ")
                    loggsCSV("In Progress")

                else:
                    print("Serwis !")
                    


if __name__ == "__main__":
    meinMotor()