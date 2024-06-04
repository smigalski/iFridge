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
testTag = if_Kalender.kalendertag(False, 0, 0, 10)
print("Testtag erforlgreich initialisiert")
print(str(testTag.istImJahr) + ", " + str(testTag.anzahlTermine))
print("Aendern der Parameter...")
testTag.istImJahr = True
testTag.anzahlTermine = 2
print(str(testTag.istImJahr) + ", " + str(testTag.anzahlTermine))

#'''
kwCount = 0
for kalenderwoche in testJahr.kw:
    printOutput = ""
    tagCount = 0
    for day in woche:
        terminzahl = testJahr.kw[kwCount][tagCount].anzahlTermine
        istImJahr = testJahr.kw[kwCount][tagCount].istImJahr
        imMonat = testJahr.kw[kwCount][tagCount].imMonat
        tagNr = testJahr.kw[kwCount][tagCount].tagNr
        printOutput += woche[tagCount] + " [" + str(istImJahr) + "; " + str(terminzahl) + "; " + str(imMonat) + "; " + str(tagNr) + "]"
        if tagCount < 6:
            printOutput += "; "
        tagCount += 1
    print("KW " + str(kwCount) + ": " + printOutput)
    kwCount += 1


#Anzeige eines beliebigen Monats des Jahres im Kalenderwochenformat
# !!! MUSS NOCH IN EIGENE FUNKTION IM MODUL if_Kalender.py UMGEWANDELT WERDEN !!!
ausgewMonat = int(input("Bitte geben sie den Monat an (als Zahl von 1-12): "))-1
print("Ausgew. Monat ist " + str(ausgewMonat))
kwGefunden = False
kwCount = -1
tagCount = 6
while kwGefunden == False:
    tagCount += 1
    if tagCount == 7:
        tagCount = 0
        kwCount += 1
    print(str(tagCount) + "; " + str(kwCount))
    print(testJahr.kw[kwCount][tagCount].imMonat)
    if testJahr.kw[kwCount][tagCount].imMonat == ausgewMonat:
        kwGefunden = True
print(kwCount)

ausgewKW = [[], [], [], [], [], []] 
counter = 0
while counter < 6:
    ausgewKW[counter] = testJahr.kw[kwCount]
    ausgewKW[counter].append(kwCount+1)
    kwCount += 1
    counter += 1


input("Programmende...")
#'''