#iFridge
#API course summer 2024
#(c) Daniel Smigala, Yasmine Hildebrand, Constantin Denden, Julius Schieck, David Nagel

#Dieses Unterprogramm ermöglicht das Einlesen und Abspeichern von Kalenderdateien sowie das Hinzufügen von Terminen.

#Die Terminklasse beinhaltet Datum (YYYY_MM_DD), Uhrzeit (HH_MM), Titel des Termins und eine Beschreibung.
#Eine Kalenderobjekt beinhaltet den Namen des Users sowie eine Liste aus Terminen, Sortiert nach Datum und Uhrzeit.

#Importierte Module
from operator import itemgetter

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
    

    #Unterfunktion zum Einlesen des Kalenderobjektes
    def einlesen(user):
        reader = open("Kalender/" + user + ".xml", "r")
        readstop = 0                            #Hilfsvariable zum Beenden des Loops bei Erreichen des Dateiendes
        entrynr = 0                             #Hilfsvariable zum Starten der Terminliste
        active_line = "default" 	            #Hilfsvariable zum einlesen einer Zeile der Kalenderdatei
        readdate = "default"                    #Hilfsvariable zum einlesen des Datums
        readtime = "default"                    #Hilfsvariable zum einlesen der Uhrzeit
        readtitle = "default"                   #Hilfsvariable zum einlesen des Titels
        readevent = "default"                   #Hilfsvariable zum einlesen des Events

        #Loop zum Verarbeiten der Kalenderdatei, läuft durch bis zum Ende der Kalenderdatei
        while readstop == 0:
            active_line = reader.readline()
            kalender.terminliste = ["default"]              #Setzt die aktuell vorhandene Terminliste des Kalenders zurück
            if active_line[:6] == "<user>":                 #Ändert den Usernamen des Kalenderobjekts zum jeweiligen in der Kalenderdatei angegebenen User
                kalender.user = active_line[6:-7]
            if active_line == "<termin>":                   #Liest bei Erkennen des Anfangs eines Terminblocks in der Datei die Daten des Termins ein 
                                                            #und fügt diesen als neuen Termin zur Terminliste des Kalenderobjekts hinzu
                readdate = reader.readline().strip()[6:-7]
                readtime = reader.readline().strip()[6:-7]
                readtitle = reader.readline().strip()[7:-8]
                readevent = reader.readline().strip()[7:-8]

                termin_neu = termin(readdate, readtime, readtitle, readevent)
                if entrynr == 0:
                    kalender.terminliste[0] = termin_neu
                else:
                    kalender.terminliste.append = termin_neu
                entrynr +=1

            if active_line == "</kalender>":
                readstop = 1
        
        reader.close()                                      #Schließt nach Beendigung des Einlesevorgangs die Datei wieder

    #Unterfunktion zum Abspeichern des Kalenderobjektes
    def ausgeben(user):
        writer = open("Kalender/" + user + ".xml", "w")
        writer.write("<kalender>\n<user>" + user + "</user>\n")
        for x in kalender.terminliste:
            writer.write("    <date>" + kalender.terminliste(x.datum) + "</date>\n" +
                         "    <time>" + kalender.terminliste(x.zeit) + "</time>\n" +
                         "    <title>" + kalender.terminliste(x.titel) + "</title>\n" + 
                         "    <event>" + kalender.terminliste(x.event) + "</event>\n" +
                         "</termin>\n")
        writer.write("</kalender>")
        writer.close()
    
    #Unterfunktion zum hinzufügen eines Termins, benötigt Datum, Zeit, Titel und Beschreibung
    def hinzufg(adddate, addtime, addtitle, addevent):
        termin_neu = termin(adddate, addtime, addtitle, addevent)
        kalender.terminliste.append(termin_neu)
        termine_sortiert = sorted(kalender.terminliste(), key=itemgetter(0))
        kalender.terminliste(termine_sortiert)
    
        
        


