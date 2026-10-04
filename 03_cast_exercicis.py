###
# Exercicis - conversió de tipus (casting)
# Completa els exercicis següents convertint dades entre tipus.


# Exercici 1
# Demana a l'usuari quants paquets ha rebut un encaminador. Converteix el valor
# introduït a un nombre enter, suma-hi 1200 paquets i mostra el total.
paquets_rebuts = int(input("Introdueix el nombre de paquets rebuts:"))
total_paquets = paquets_rebuts + 1200  # Hem sumat 1200 paquets a la quantitat introduïda per l'usuari.
print(f"El total de paquets es {total_paquets}.")
# Exercici 2
# Demana a l'usuari la velocitat d'una connexió en Mbps. Converteix el valor
# introduït a un nombre decimal i calcula la velocitat equivalent en MB/s
# dividint-la per 8. Mostra el resultat.
velocitat_connexioMbps = float(input("Introdueix la teva velocitat de connexio (En Mbps): "))  # el nombre decimal = float
velocitat_connexioMbs = velocitat_connexioMbps/8 # Conversio de Mbps a Mb/s dividint per 8.
print(f"La teva velocitat de connexio en Mbs es: {velocitat_connexioMbs}")


# Dato curioso: Mbps mide la capacidad maxima de transferencia de datos en tu conexion a Internet.
# Dato curioso: Mb/s mide la velocidad de descarga de archivos.