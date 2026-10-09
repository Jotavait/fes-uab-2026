###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

rssi = float(input("Introdueix el nivell de la senyal (RSSI) en (dBm): "))

if rssi >= -50:
    print("Exel·lent")
elif rssi >= -67:
    print("Bona")
elif rssi >= -75:
    print("Feble")
else: 
    print("Molt be")
# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

potencia = float(input("Introdueix la potencia optica en (dBm): "))

if potencia < -27:
    print("Molt baix")
elif potencia <= -8:
    print("Acceptable")
else:
    print("Massa alt")  


# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

consum = float(input("Introdueix el consum de dades (GB): "))
limit = 20

if consum <= limit:
    print("El consum esta dins del limit")

else:
    exces = consum - limit
    print(f"S'ha consumit d'exces {exces} GB adicionals")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

los = input("l'indicador LOS del terminal òptic està encès? (Si/No) :")
internet = input("L'indicador d'Internet està encès? (sí/no): ")
if los == "Si" or los == "si":
    print("Cal revisar el cable de fibra.")
elif internet == "No" or internet == "no":
    print("Consulta el servei de priveïdor.")
else:
    print("Tot sembla funcionar correctament.")

# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
bateria = float(input("Introdueix el percentatge de bateria del SAI (%): "))

if bateria < 0 or bateria > 100:
    print("Valor fora de rang (ha de ser entre 0 i 100%).")
elif bateria < 20:
    print("Nivell crític")
elif bateria <= 49:
    print("Nivell baix")
else:
    print("Nivell suficient")
