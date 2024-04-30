from abc import ABC, abstractmethod


### OOP - object oriented programming: Python (totul este un obiect)
### functionale: Lisp, Haskell > aproape toate operatiile sunt functii
### high-level, strongly typed: C, C++ (a = 5 -> int a=5)

# OOP - mostenirea

class Persoana:  # clasa de baza
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def __str__(self):
        return f"{self.nume} are varsta {self.varsta}"


class Angajat(Persoana):  # clasa mostenita (clasa copil) -> si mosteneste init si str
    def __init__(self, nume, varsta, salariu, ore_lucrate):
        Persoana.__init__(self, nume, varsta)  # super() -> adica superclass:  clasa din care mostenim
        self.salariu = salariu
        self.ore_lucrate = ore_lucrate

    def arata_finante(self):
        return self.salariu * self.ore_lucrate


class Student(Persoana):  # clasa mostenita (clasa copil) -> si mosteneste init si str
    def __init__(self, nume, varsta, bursa):
        Persoana.__init__(self, nume, varsta)
        self.bursa = bursa

    def arata_finante(self):
        return self.bursa

    @classmethod
    def create_from_string(cls, sablon: str):   # cls este instanta clasei curente
        # Student.crate_from_string("Ana 15 700")
        nume, varsta, bursa = sablon.split()
        varsta, bursa = int(varsta), int(bursa)  # type casting
        if cls.is_name_correct(nume):
            return cls(nume, varsta, bursa) # echivalent cu a zice asta: __init__(self, nume, varsta, bursa)

    @staticmethod
    def is_name_correct(nume):
        if nume[0].isupper() and len(nume) > 2:
            return True
        return False


class StudentMuncitor(Student, Angajat):  # ordinea conteaza! Primu mostenit este Student, apoi Angajat.
    def __init__(self, nume, varsta, bursa, salariu, ore_lucrate):
        Student.__init__(self, nume, varsta, bursa)  # Student.__ -> instantiere anonima
        Angajat.__init__(self, nume, varsta, salariu, ore_lucrate)

    def arata_finante(self):
        return self.ore_lucrate * self.salariu + self.bursa

    def __str__(self):
        return f'{self.nume} lucrat {self.ore_lucrate} ore si a castigat salariul de {self.salariu} RON'


o1 = Persoana('George', 25)
o2 = Angajat('Andrei', 26, 1000, 40)
o3 = Student('Ion', 15, 800)
o4 = StudentMuncitor('Codrut', 30, 800, 1200, 20)

print(o1)
print(o2)
print(o3)
print(o4)

o5 = Student.create_from_string('Razvan 30 1000')
print(o5)


# dunder methods : __dunder__
# Persoana.__init__(self, nume varsta) VS super().__init__(nume, varsta)
# super() -> Persoana -> self
# Persoana.__init__(self, nume, varsta) trebuie pus "self" pentru a stii la cine se refera


# @classmethod: functie, dar se apeleaza pentru intreaga instanta a clasei: poate modifica membrii sai (ai clasei).
# @staticmethod: functie, dar care este doar asociata clasei, nu este necesara instantierea unui obiect pentru a o folosi. NU MODIFICA membrii clasei.


###################################
# dataclasses
###################################
from dataclasses import dataclass


# valabil doar de la python 3.7 in sus
@dataclass
class Cineva:
    nume: list
    prenume: str

    # dataclass va creeaza automat dunder methods: __str__, __init__, __add__
    def afisare_nume_complet(self):
        return f"Eu sunt {self.nume} {self.prenume}!"


c1 = Cineva([1, 3], "Gheorghe")
print(c1.afisare_nume_complet())
c2 = Cineva([1], "Gheorghe")
print(c1 == c2)