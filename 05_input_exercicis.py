###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
tecnic = input("Introdueix el nom d'un tecnic: ")
xarxa = input("Introdueix el nom de la xarxa:  ")
print(f"El tecnic {tecnic} esta instal·lant la xarxa {xarxa}.") # No existe el printf en phyton

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud = float(input("Introdueix la longitud de l'enllaç (en km): "))
velocitat = float(input(" Introdueix la velocitat de transmissio (en Ggps): "))

segons = 8 / velocitat  # velocitat es distancia entre velocitat.
print(f"Es triguen {segons} segons per transmetre 1 GB de dades.")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.

hores = float(input("Introdueix el nombre d'hores de feina: "))
preu_hores = float(input("Introdueix el preu per hora (en €): "))
preu_material = float(input("Introdueix el preu del material (en €): "))

cost_total = (hores*preu_hores) + preu_material
print(f"El cost total de la instalacio es {cost_total}€.")

