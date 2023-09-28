#################################################################################################
# Einkaufsliste 2.0 (Bonusaufgabe)
# Sprache: Python
#
# Funktionsumfang: 
# - Anzeige der Aktuellen Einkaufsliste
# - Artikel der Einkaufliste hinzufügen
# - Artikel aus der Einkaufsliste entfernen
# - Komplette Einkaufsliste leeren
# - Script schliessen
#
# Das Script wurde im Rahmen einer Umschulung zum FIAE als Bonusaufgabe angefertigt.
# Geschrieben von Danny M. (Wab00se)
#################################################################################################

## Die Definition / Variablenvergabe der Liste

Liste = ["Milch","Brot","Bier","Käse","Wurst"] 
menu = "0"
if menu == "0":
    while menu !="5":

## Beginn der Auswahloberfläche

        print("                                    ")
        print("           (-(-(-(-(-(-(-(-(-(-(-() ")
        print("           /¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ /||       .::[Einkaufsliste 2.0]::.") 
        print("          /                    /_|| ")
        print("         /                    /__||  Bitte wählen sie Ihre gewünschte Funktion")
        print("        //|  /               /___|| ")
        print("       // | / ___/_ _  _    /____||  1. Aktuelle Einkaufsliste Anzeigen")
        print("      //  |/(_) (__(/_/_)_ /_____|| ")
        print("     /( _ _ _ _ _ _ _ _ _ /______||  2. Artikel der Einkaufsliste hinzufügen")
        print("    /  ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ ¯ /_______|| ")
        print("   /                    /________||  3. Artikel aus der Einkaufsliste entfernen")
        print("  /                    /_________|| ")
        print(" (____________________(__________||  4. Einkaufsliste komplett leeren")
        print("            |____________________|| ")
        print("            |____________________||  5. Einkaufsliste schliessen")
        print("            |____________________|/ ")
        print("                                    ")

## Ende der Auswahloberfläche

        menu = input ()

## Wenn Menüpunkt 1 gewählt wird Gibt er die Gesamte Einkaufsliste aus

        while menu == "1": 
            print (".:: Ihre aktuelle Einkaufsliste ::.\n")
            for index,Artikel in enumerate(Liste):
                print (f"{index+1}: {Artikel}")
                menu = "0" # In Arbeit, Ohne Listen Inhalt, Unendlich loop, ggf counter.

## Wenn Menüpunkt 2 gewählt wird fordert dich das Programm auf, einen neuen Artikel hinzufügen

        while menu == "2": 
            Artikel = input(".:: Bitte geben sie den neuen Artikel ein ::. \n")
            Liste.append(Artikel)
            print (".:: Neuer Artikel hinzugefügt! ::.\n.:: Ihre aktuelle Einkaufsliste ::.\n")
            for index,Artikel in enumerate(Liste):
                print (f"{index+1}: {Artikel}")
            wahl = input (".:: Wollen sie einen weiteren Artikel hinzufügen (J / N) ::.")
            if wahl == "J" or wahl == "j":
                menu = "2"
            else:
                menu ="0"
                    
## Wenn Menüpunkt 3 gewählt wird fordert dich das Programm auf, einen Artikel zu entfernen

        while menu == "3": 
            for index,Artikel in enumerate(Liste):
                print (f"{index+1}: {Artikel}")
            Artikel = input (".:: Bitte geben sie die Nummer des zu löschenden Artikels ein ::.")
            Artikel = int(Artikel)
            del Liste [Artikel-1]
            print(f".:: Ihre aktuelle Einkaufsliste ::.\n{Liste}")
            wahl = input (".:: Wollen sie einen weiteren Artikel entfernen (J / N) ::.")
            if wahl == "J" or wahl == "j":
                menu = "3"
            else:
                menu ="0"

## Wenn Menüpunkt 4 gewählt wird, wird die Gesamte Einlaufsliste gelöscht
        
        while menu == "4":
            del Liste[:]
            print (".:: Ihre Einkaufsliste wurde geleert! ::.")
            print (Liste)
            menu = "0"

## Benachrichtung beim Beenden des Programms

    print (".:: Vielen Dank für das nutzen dieser APP ::.")
    while menu =="5":
        exit() 