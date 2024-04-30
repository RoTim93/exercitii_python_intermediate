'''
Lambda expressions:

def numele_functiei(a, b, b):
    #
    :return

lambda expression: functie anonima, care nu are nume, este definita acolo un este utilizata

lambda...


'''

continut = lambda x: x.lower()

print(continut('xaXAAXaxXaA'))

'''
echivalent cu:
def continut(x):
    return x.lower()
'''

lista_numere = [1, 2, 3, 4, 5]

# map: accepta o functie si o aplica pe fiecare element al unui obiect iterabil (lista, tuplu...)

lista_squared = list(map(lambda x: x ** 2, lista_numere))
print(lista_squared)

# filter: sterge elementele pentru care rezultatul functiei aplicate returneaza False

lista_impare = list(filter(lambda x: x % 2, lista_squared))
print(lista_impare)

# reduce: proceseaza toate elementele dintr-un obiect iterabil de la stanga la dreapta(!) si produce o singura
# valoare in functie de functia aplicata

from functools import reduce

item_sumati = reduce(lambda x, y: x + y, lista_impare)
print(item_sumati)

# [1, 9, 25] -> reduce -> ((1,9), 25) -> (1+9), 25 -> (10+25) -> 35

# MapReduce -> parcurge o lista imensa/ baze de date: sa aplice o functie pentru fiecare element apoi sa reduce intregul
# tabel la o singura valoare

# sorted, max, min

# sorted -> va aranjeaza/ sorteaza in ordine elementele

perechi = [(1, 9), (4, 6), (5, 3)]
print(sorted(perechi, key=lambda x: x[1]))
# print(sorted(perechi, reverse=True))

print(max(perechi))


# Enunt exercitiu: creati o functie care verifica daca un nr este prim
# apoi dintr-o lista filtrati numerele prime folosind filter()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

lista_numere2 = [5, 6, 7, 8, 9, 10, 11, 23, 27, 73, 56, 81]
lista_numere_prime = list(filter(is_prime, lista_numere2))
print(lista_numere_prime)
