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
import time

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
        self.terminliste = terminliste          #Liste aus Terminen, Sortiert nach Datum und Uhrzeit in aufsteigender Reihenfolge    

    #Unterfunktion zum Einlesen des Kalenderobjektes
    def einlesen(self, user):
        print("Datei öffnen...")
        reader = open("Kalender/" + user + ".xml", "r")
        readStop = 0                            #Hilfsvariable zum Beenden des Loops bei Erreichen des Dateiendes
        entrynr = 0                             #Hilfsvariable zum Starten der Terminliste
        activeLine = "defaultLine" 	            #Hilfsvariable zum einlesen einer Zeile der Kalenderdatei
        readDate = "defaultDate"                #Hilfsvariable zum einlesen des Datums
        readTime = "defaultTime"                #Hilfsvariable zum einlesen der Uhrzeit
        readTitle = "defaultTitle"              #Hilfsvariable zum einlesen des Titels
        readEvent = "defaultEvent"              #Hilfsvariable zum einlesen des Events
        defaultTermin = termin(readDate, readTime, readTitle, readEvent)
        self.terminliste =  [defaultTermin]     #Setzt die aktuell vorhandene Terminliste des Kalenders zurück

        #Loop zum Verarbeiten der Kalenderdatei, läuft durch bis zum Ende der Kalenderdatei
        print("Datei einlesen...")
        while readStop == 0:
            activeLine = reader.readline()
            if activeLine == "":
                print("Fehler! Datei ist leer!")
                readStop = 1
            if activeLine[:6] == "<user>":                  #Ändert den Usernamen des Kalenderobjekts zum jeweiligen in der Kalenderdatei angegebenen User
                self.user = activeLine[6:-8]
                print("Neuer User: " + self.user.replace("_", " "))

            if activeLine == "<termin>\n":                  #Liest bei Erkennen des Anfangs eines Terminblocks in der Datei die Daten des Termins ein 
                                                            #und fügt diesen als neuen Termin zur Terminliste des Kalenderobjekts hinzu
                print("Neuer Termin erkannt...")
                readDate = reader.readline().strip()[6:-7]
                print(readDate)
                readTime = reader.readline().strip()[6:-7]
                print(readTime)
                readTitle = reader.readline().strip()[7:-8]
                print(readTitle)
                readEvent = reader.readline().strip()[7:-8]
                print(readEvent)

                terminNeu = termin(readDate, readTime, readTitle, readEvent)
                if entrynr == 0:
                    self.terminliste[0] = terminNeu
                else:
                    self.terminliste.append(terminNeu)
                print("Termin " + str(entrynr+1) + " eingelesen...")
                entrynr +=1

            if activeLine == "</kalender>":
                readStop = 1
        
        reader.close()                                      #Schließt nach Beendigung des Einlesevorgangs die Datei wieder
        print("Kalender für " + self.user + " eingelesen!")

    #Unterfunktion zum Abspeichern des Kalenderobjektes
    def ausgeben(self, user):
        writer = open("Kalender/" + user + ".xml", "w")             #Öffnet die jeweilige Datei aus dem Kalenderordner
        writer.write("<kalender>\n<user>" + user + "</user>\n")
        
        #Schleife zum schreiben jedes Termins in der aktuell geladenen Terminliste des Kalenders in die Datei
        writeCounter = 0
        for x in self.terminliste:
            writer.write("<termin>\n")
            writer.write("    <date>" + self.terminliste[writeCounter].datum + "</date>\n")
            writer.write("    <time>" + self.terminliste[writeCounter].zeit + "</time>\n")
            writer.write("    <title>" + self.terminliste[writeCounter].titel + "</title>\n")
            writer.write("    <event>" + self.terminliste[writeCounter].event + "</event>\n")
            writer.write("</termin>\n")
            writeCounter += 1
        writer.write("</kalender>")
        
        writer.close()                                              #Schließt die Datei
    
    #Unterfunktion zum hinzufügen eines Termins, benötigt Datum, Zeit, Titel und Beschreibung
    def hinzufg(self, adddate, addtime, addtitle, addevent):
        terminNeu = termin(adddate, addtime, addtitle, addevent)
        self.terminliste.append(terminNeu)
        self.terminliste.sort(key=lambda termin: termin.datum)

#Objekt "Jahr" zum Laden eines ganzen Jahres in eine Liste, welche die jeweiligen Wochen beinhaltet, welche wiederum Tage beinhalten
class Jahr:
    
    def __init__(self, jahreszahl):
        #Setzt das Jahr des Objekts auf das eingegebene Jahr
        self.jahreszahl = jahreszahl
        #Setzt die anzahl der Tage des Jahres auf 365 oder 366, je nachdem ob es ein Schaltjahr ist oder nicht
        if checkSchalt(self.jahreszahl) == True:
            self.tage = 366
        else:
            self.tage = 365
        #Bestimmt den Starttag des Jahres
        schaltCount = 0
        if self.jahreszahl == 2024:
            jahrDelta = 0
            tagDelta = 0
        elif self.jahreszahl > 0:
            jahrCounter = self.jahreszahl
            while jahrCounter > 2024:
                if checkSchalt(jahrCounter) == True:
                    schaltCount += 1
                jahrCounter -= 1
            tagDelta = jahrDelta*365 + schaltCount
        elif self.jahreszahl < 0:
            jahrCounter = self.jahreszahl
            while jahrCounter < 2024:
                if checkSchalt(jahrCounter) == True:
                    schaltCount += 1
                jahrCounter += 1
            tagDelta = jahrDelta*365 + schaltCount
        self.starttag = tagDelta%7
        self.endtag = (tagDelta + self.tage)%7
        

#Funktion zum Überprüfen, ob das eingegebene Jahr ein Schaltjahr ist
def checkSchalt(self, jahreszahl):
    istSchalt = False
    if jahreszahl%4 == 0:                                       #Prüft, ob die Jahreszahl durch 4 Teilbar ist, falls ja -> Schaltjahr
        istSchalt = True
    if jahreszahl%100 == 0 and jahreszahl%400 != 0:             #Prüft, ob die Jahreszahl durch 100 Teilbar ist und NICHT durch 400, falls ja -> kein Schaltjahr
        istSchalt = False
    return(istSchalt)


'''
#Klasse 'Kalenderwoche' zum besseren Darstellen von Wochen im Kalender
class kalenderwoche:
    def __init__(self):
        self.mo = 0
        self.di = 0

        
#Klasse 'Kalendertag' zum füllen der Woche und markieren von Terminen
class kalendertag:
    def __init__(self, jahr):
        self.istImJahr = 0
        self.hatTermin = 0
'''