"""
iFridge
API course summer 2024
(c) Daniel Smigala, Yasmine Hildebrand, Constantin Denden, Julius Schieck, David Nagel

Dies ist ein Testprogramm für das Modul if_Kalender und nicht relevant für das Hauptprogramm iFridge.
"""

#Importierte Module
import if_Kalender


#Usereingabe und hereinladen des Kalenders
user = input("Bitte Usernamen Eingeben: ")
user = user.replace(" ", "_")
aktivKalender = if_Kalender.kalender(user, [["default"], ["default"], ["default"], ["default"]])
aktivKalender.einlesen(user)
print(aktivKalender)

#Abfrage ob Termin hinzugefügt werden soll oder nicht
addDateQuery = input("Soll ein neuer Termin hinzugefügt werden? [y/n]: ")

if addDateQuery == "y":
    newDate = input("Neues Datum eingeben [dd.mm.yyyy]: ")              #Eingabe der Daten des neuen Termins
    newtime = input("Uhrzeit des Termins eingeben [hh:mm]: ")
    newtitle = input("Titel des Termins eingeben: ")
    newevent = input("Kurze Beschreibung des Event eingeben: ")

    newDate = newDate[6:10] + "_" + newDate[3:5] + "_" + newDate[0:2]   #Umformatieren des Datums von "dd.mm.yyyy" nach "yyyy_mm_dd" zum besseren Sortieren im Kalender
    newtime = newtime.replace(".", "_")                                 #Umformatieren der Zeit von "hh.mm" nach "hh_mm"
    aktivKalender.hinzufg(newDate, newtime, newtitle, newevent)
    print(aktivKalender)

#Abspeichern des Kalenders
saveQuery = input("Soll der Kalender gespeichert werden? [y/n]: ")
if saveQuery == "y":
    aktivKalender.ausgeben
    print("Kalender gespeichert!")

input("Programmende...")
    