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
print(user)
termine = if_Kalender.termin("default", "default", "default", "default")
aktivKalender = if_Kalender.kalender(user, [termine])
print("User: " + aktivKalender.user)
print(aktivKalender.terminliste[0])
aktivKalender.einlesen(user)

#Ausgabe des aktiven Terminkalenders in der Konsole
print("\n\nUser: " + aktivKalender.user.replace("_", " "))
printCounter = 0
for x in aktivKalender.terminliste:
    printAusgabe = "Termin " + str(printCounter) + ":\n"
    aktivTermin = aktivKalender.terminliste[printCounter]
    printAusgabe += "Datum: " + aktivTermin.datum
    printAusgabe += " Zeit: " + aktivTermin.zeit
    printAusgabe += " Titel: " + aktivTermin.titel
    printAusgabe += " Event: " + aktivTermin.event
    print(printAusgabe)
    printCounter +=1

#Abfrage ob Termin hinzugefügt werden soll oder nicht
addDateQuery = input("Soll ein neuer Termin hinzugefügt werden? [y/n]: ")

if addDateQuery == "y":
    newDate = input("Neues Datum eingeben [dd.mm.yyyy]: ")              #Eingabe der Daten des neuen Termins
    newTime = input("Uhrzeit des Termins eingeben [hh:mm]: ")
    newTitle = input("Titel des Termins eingeben: ")
    newEvent = input("Kurze Beschreibung des Event eingeben: ")

    newDate = newDate[6:10] + "_" + newDate[3:5] + "_" + newDate[0:2]   #Umformatieren des Datums von "dd.mm.yyyy" nach "yyyy_mm_dd" zum besseren Sortieren im Kalender
    newTime = newTime.replace(".", "_")                                 #Umformatieren der Zeit von "hh.mm" nach "hh_mm"
    aktivKalender.hinzufg(newDate, newTime, newTitle, newEvent)
    
    #Ausgabe des Kalenders mit neuem Termin über die Konsole
    print("\n\nNeuer Termin hinzugefügt: ")
    printCounter = 0
    for x in aktivKalender.terminliste:
        printAusgabe = "Termin " + str(printCounter) + ":\n"
        aktivTermin = aktivKalender.terminliste[printCounter]
        printAusgabe += "Datum: " + aktivTermin.datum
        printAusgabe += " Zeit: " + aktivTermin.zeit
        printAusgabe += " Titel: " + aktivTermin.titel
        printAusgabe += " Event: " + aktivTermin.event
        print(printAusgabe)
        printCounter +=1

#Abspeichern des Kalenders
saveQuery = input("Soll der Kalender gespeichert werden? [y/n]: ")
if saveQuery == "y":
    aktivKalender.ausgeben
    print("Kalender gespeichert!")

input("Programmende...")
    