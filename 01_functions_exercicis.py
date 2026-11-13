###
# EXERCICIS (funcions)
###

# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.

def saludar_a(nom, salutacio="Hola"):
    print(f"{salutacio}, {nom}!")

saludar_a("Juanjo")

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.
def es_parell(numero):
    return numero % 2 == 0

print(es_parell(2))
print(es_parell(3))
    
# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
def mitjana(numeros):
    if not numeros:
        return 0
    suma = 0
    for num in numeros:
        suma += num
    return suma /len(numeros)

print(mitjana([10,20,30,40,50]))

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.

def sumar_tot(*args):
    return sum(args)

print(sumar_tot(5, 10))
print(sumar_tot(1, 2, 3, 4, 5))
print(sumar_tot(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().
def taula_multiplicar(numero, limit=10):
    for i in range(1, limit + 1):
        print(f"{numero} x {i} = {numero * i}")

taula_multiplicar(5)

# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).

def mostrar_perfil(**kwargs):
    for clau, valor in kwargs.items():
        print(f"{clau}: {valor}")

mostrar_perfil(nom="Laura", edat=20, grau="Enginyeria Informàtica")


# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
def factorial(n):
    resultat = 1
    comptador = 1
    while comptador <= n:
        resultat *= comptador
        comptador += 1
    return resultat

def maxim_llista(numeros):
    if not numeros:
        return None
    maxim = numeros[0]
    for num in numeros:
        if num > maxim:
            maxim = num
    return maxim
print(factorial(5))             
print(maxim_llista([3, 12, 8, 23, 5]))

# Exercici 8: Comptar vocals
# Crea una funció comptar_vocals(text) que rebi una cadena de text i retorni quantes vocals
# (a, e, i, o, u) conté. Ha de funcionar tant amb majúscules com amb minúscules.
def comptar_vocals(text):
    vocals = "aeiouAEIOU"
    comptador = 0
    for lletra in text:
        if lletra in vocals:
            comptador += 1
    return comptador


print(comptar_vocals("Programació en Python"))  # 7

# Exercici 9: Retorn múltiple (mínim i màxim)
# Crea una funció minim_i_maxim(numeros) que rebi una llista de números i retorni tant el valor
# mínim com el valor màxim alhora. Desempaqueta el resultat en dues variables.
def minim_i_maxim(numeros):
    return min(numeros), max(numeros)
valor_min, valor_max = minim_i_maxim([14, 2, 89, 5, 43])
print(f"Mínim: {valor_min}, Màxim: {valor_max}")

# Exercici 10: Palíndrom
# Crea una funció es_palindrom(text) que retorni True si una paraula es llegeix igual d'esquerra a dreta
# que de dreta a esquerra (ignorant majúscules i minúscules), i False en cas contrari.

def es_palindrom(text):
    text_net = text.lower()
    return text_net == text_net[::-1]

print(es_palindrom("Radar"))   # True
print(es_palindrom("Python"))  # False
