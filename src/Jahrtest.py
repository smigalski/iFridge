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
woche = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
print("Starttag:    " + woche[testJahr.starttag])
print("Endtag:      " + woche[testJahr.endtag])

#Test der Kalendertag Klasse
print("\nKalendertag Test:")
testTag = if_Kalender.kalendertag(False, 0)
print("Testtag erforlgreich initialisiert")
print(str(testTag.istImJahr) + ", " + str(testTag.anzahlTermine))
print("Aendern der Parameter...")
testTag.istImJahr = True
testTag.anzahlTermine = 2
print(str(testTag.istImJahr) + ", " + str(testTag.anzahlTermine))

#'''
for kalenderwoche in woche:
    printOutput = ""
    for tag in testJahr.kw:
        printOutput += woche(tag) + " [" + str(testJahr.kw[kalenderwoche][tag].istImJahr) + "; " + str(testJahr.kw[kalenderwoche][tag].anzahlTermine) + "]"
        if tag < 6:
            printOutput += "; "
        tag += 1
    print("KW " + str(kalenderwoche) + ": " + printOutput)

#input("Programmende...")
#'''