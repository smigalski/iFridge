"""
iFridge
API course summer 2024
(c) Daniel Smigala, Yasmine Hildebrand, Constantin Denden, Julius Schieck, David Nagel

Dies ist ein Testprogramm für die Klasse "Jahr" des Moduls if_Kalender und nicht relevant für das Hauptprogramm iFridge.
"""

#Importierte Module
import if_Kalender

inputJahr = int(input("Bitte Jahreszahl eingeben: "))
testJahr = if_Kalender.jahr(inputJahr)
print("Jahr:        " + str(testJahr.jahreszahl))
print("Anzahl Tage: " + str(testJahr.tage))
print("Starttag:    " + str(testJahr.starttag))
print("Endtag:      " + str(testJahr.endtag))

input("Programmende...")
