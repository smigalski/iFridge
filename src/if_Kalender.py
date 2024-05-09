"""
iFridge
API course summer 2024
(c) Daniel Smigala, Yasmine Hildebrand, Constantin Denden, Julius Schieck, David Nagel

Dieses Unterprogramm ermöglicht das Einlesen und Abspeichern von Kalenderdateien sowie das Hinzufügen von Terminen.

Die Terminklasse beinhaltet Datum (YYYY_MM_DD), Uhrzeit (HH_MM), Titel des Termins und eine Beschreibung.
Eine Kalenderobjekt beinhaltet den Namen des Users sowie eine Liste aus Terminen, Sortiert nach Datum und Uhrzeit.

ACHTUNG: FUNKTIONEN NOCH NICHT GETESTET, TESTPROGRAMM WIRD NOCH ERSTELLT
"""

#Importierte Module
from operator import itemgetter

#Terminklasse erstellen
class termin:
    def __init__(self, datum, zeit, titel, event):
        self.datum = datum                      #Datum eingeben als String in folgendem Format: YYYY_MM_DD
        self.zeit = zeit                        #Zeit eingeben als String in folgendem Format als 24h Uhrzeit: HH_MM
        self.titel = titel                      #Titel als String eingeben
        self.event = event                      #Event als String eingeben

#Kalenderobjekt erstellen mitsamt Unterfunktionen "einlesen" zum einlesen einer Kalenderdatei, "ausgeben" zum abspeichern einer Kalenderdatei, "hinzufg" zum Hinzufügen eines Termins
class kalender:
    def __init__(self, user, terminliste):
        self.user = user                        #Name des zum Kalender gehörigen Users
        self.terminliste = [terminliste]        #Liste aus Terminen, Sortiert nach Datum und Uhrzeit in aufsteigender Reihenfolge
    

    #Unterfunktion zum Einlesen des Kalenderobjektes
    def einlesen(user):
        reader = open("Kalender/" + user + ".xml", "r")
        readStop = 0                            #Hilfsvariable zum Beenden des Loops bei Erreichen des Dateiendes
        entrynr = 0                             #Hilfsvariable zum Starten der Terminliste
        activeLine = "default" 	            #Hilfsvariable zum einlesen einer Zeile der Kalenderdatei
        readDate = "default"                    #Hilfsvariable zum einlesen des Datums
        readTime = "default"                    #Hilfsvariable zum einlesen der Uhrzeit
        readTitle = "default"                   #Hilfsvariable zum einlesen des Titels
        readEvent = "default"                   #Hilfsvariable zum einlesen des Events

        #Loop zum Verarbeiten der Kalenderdatei, läuft durch bis zum Ende der Kalenderdatei
        while readStop == 0:
            activeLine = reader.readline()
            kalender.terminliste = ["default"]              #Setzt die aktuell vorhandene Terminliste des Kalenders zurück
            if activeLine[:6] == "<user>":                 #Ändert den Usernamen des Kalenderobjekts zum jeweiligen in der Kalenderdatei angegebenen User
                kalender.user = activeLine[6:-7]
            if activeLine == "<termin>":                   #Liest bei Erkennen des Anfangs eines Terminblocks in der Datei die Daten des Termins ein 
                                                            #und fügt diesen als neuen Termin zur Terminliste des Kalenderobjekts hinzu
                readDate = reader.readline().strip()[6:-7]
                readTime = reader.readline().strip()[6:-7]
                readTitle = reader.readline().strip()[7:-8]
                readEvent = reader.readline().strip()[7:-8]

                terminNeu = termin(readDate, readTime, readTitle, readEvent)
                if entrynr == 0:
                    kalender.terminliste[0] = terminNeu
                else:
                    kalender.terminliste.append = terminNeu
                entrynr +=1

            if activeLine == "</kalender>":
                readStop = 1
        
        reader.close()                                      #Schließt nach Beendigung des Einlesevorgangs die Datei wieder

    #Unterfunktion zum Abspeichern des Kalenderobjektes
    def ausgeben(user):
        writer = open("Kalender/" + user + ".xml", "w")             #Öffnet die jeweilige Datei aus dem Kalenderordner
        writer.write("<kalender>\n<user>" + user + "</user>\n")
        
        #Schleife zum schreiben jedes Termins in der aktuell geladenen Terminliste des Kalenders in die Datei
        for x in kalender.terminliste:
            writer.write("    <date>" + kalender.terminliste(x.datum) + "</date>\n" +
                         "    <time>" + kalender.terminliste(x.zeit) + "</time>\n" +
                         "    <title>" + kalender.terminliste(x.titel) + "</title>\n" + 
                         "    <event>" + kalender.terminliste(x.event) + "</event>\n" +
                         "</termin>\n")
        writer.write("</kalender>")
        
        writer.close()                                              #Schließt die Datei
    
    #Unterfunktion zum hinzufügen eines Termins, benötigt Datum, Zeit, Titel und Beschreibung
    def hinzufg(self, adddate, addtime, addtitle, addevent):
        terminNeu = termin(adddate, addtime, addtitle, addevent)
        kalender.terminliste.append(terminNeu)
        termine_sortiert = sorted(kalender.terminliste(), key=itemgetter(0))
        kalender.terminliste(termine_sortiert)
    
        
        


