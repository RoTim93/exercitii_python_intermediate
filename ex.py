from abc import ABC, abstractmethod


### OOP - object oriented programming: Python (totul este un obiect)
### functionale: Lisp, Haskell > aproape toate operatiile sunt functii
### high-level, strongly typed: C, C++ (a = 5 -> int a=5)

# OOP - mostenirea

class Persoana: # clasa de baza
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def __str__(self):
        return f"{self.nume} are varsta {self.varsta}"


class Angajat(Persoana): #clasa mostenita (clasa copil) -> si mosteneste init si str
    def __init__(self, nume, varsta, salariu, ore_lucrate):
        super().__init__(nume, varsta)  # super() -> adica superclass:  clasa din care mostenim
        self.salariu = salariu
        self.ore_lucrate = ore_lucrate

    def arata_finante(self):
        return self.salariu * self.ore_lucrate

class Student(Persoana): #clasa mostenita (clasa copil) -> si mosteneste init si str
    def __init__(self, nume, varsta, bursa):
        super().__init__(nume, varsta)
        self.bursa = bursa

    def arata_finante(self):
        return self.bursa

    def __str__(self):
        return f"{self.nume} are {self.varsta} ani si bursa: {self.bursa}$."


o1 = Persoana('George', 25)
o2 = Angajat('Andrei', 26, 1000, 40)
o3 = Student('Ion', 15, 800)

print(o1)
print(o2)
print(o3)


# dunder methods : __dunder__
