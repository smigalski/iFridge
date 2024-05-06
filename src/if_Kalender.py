#iFridge
#API course summer 2024
#(c) Daniel Smigala, Yasmine Hildebrand, Constantin Denden, Julius Schieck, David Nagel

#Dieses Unterprogramm ermöglicht das Einlesen und Abspeichern von Kalenderdateien sowie das Hinzufügen von Terminen.

#Die Terminklasse beinhaltet Datum (YYYY_MM_DD), Uhrzeit (HH_MM), Titel des Termins und eine Beschreibung.
#Eine Kalenderobjekt beinhaltet den Namen des Users sowie eine Liste aus Terminen, Sortiert nach Datum und Uhrzeit.



#Terminklasse erstellen
class termin:
    def __init__(self, datum, zeit, titel, event):
        self.datum = datum                      #Datum eingeben als String in folgendem Format: YYYY_MM_DD
        self.zeit = zeit                        #Zeit eingeben als String in folgendem Format als 24h Uhrzeit: HH_MM
        self.titel = titel                      #Titel als String eingeben
        self.event = event                      #Event als String eingeben

class kalender:
    def __init__(self, user, terminliste):
        self.user = user                        #Name des zum Kalender gehörigen Users
        self.terminliste = [terminliste]        #Liste aus Terminen, Sortiert nach Datum und Uhrzeit in aufsteigender Reihenfolge
    

