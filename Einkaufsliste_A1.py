#-------------------------------------
# Einkaufsliste Aufgabe 1
#-------------------------------------

#-------------------------------------
# Aufgabe: Mach eine Liste wo 
# man die items zeigen kann und man 
# ein item auswahählen kann
#--------------------------------------

# Einkaufsliste
Einkaufsliste = ["1. Schokolade", "2. Chips", "3. Kaffee"]

# Einkaufsliste zeigen
print ("--------------------------------------------")
print ("Wählen sie eines der folgenden Produkte aus")
print (*Einkaufsliste, sep="\n")
print ("--------------------------------------------")

# Item auswählen
Auswahl = int(input("Ihre Wahl:"))

if Auswahl == 1:
    print("Sie haben " + Einkaufsliste[Auswahl-1] + " gewählt")

if Auswahl == 2:
    print("Sie haben " + Einkaufsliste[Auswahl-1] + " gewählt")

if Auswahl == 3:
    print("Sie haben " + Einkaufsliste[Auswahl-1] + " gewählt")