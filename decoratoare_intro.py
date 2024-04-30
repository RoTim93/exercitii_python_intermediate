# Decoratorul este o functie care imbraca o alta functie si ii extinde functionalitatea. Intotdeaduna este precedat de '@'.
# O functie ia ca argument alta functie.
# Intr-o functie se poate crea alta functie: functii imbricate.

from datetime import datetime


def disabled_at_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 21:
            func()
    return wrapper

@disabled_at_night
def ceva():
    print("Hhhhh")

ceva()

########### built-in decorator ##########
from functools import lru_cache

@lru_cache(maxsize=100) # lru - least recently used; ex.1
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(499))

@lru_cache(maxsize=100) #ex.2
def print_fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):   # _ pt a nu aloca memorie
        print(a)
        tmp = a
        a = b
        b = tmp+b

print_fibonacci(100000)