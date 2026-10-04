###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom_encaminador = "Router_Juanjo"
ubicacio = "Sala de servidors"
num_ports = 25
ences = True   # valor booleano para representar si o no si estuviera apagado seria False

print(f"L'encaminador {nom_encaminador} es troba a {ubicacio}, te {num_ports} ports i el seu estat es d'ences es {ences}.")


# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
gb_inclosos = 150
gb_consumits = 25

gb_restants = gb_inclosos - gb_consumits

print(f"Hi queden {gb_restants} GB de Dades restants.")