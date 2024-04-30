class Oarecare:

    lista_mea = []  # variabila comuna instantei clasei Oarecare # variabila globala a instantei clasei, shared!!!!! de obiecte

    def __init__(self, item: str):
         self.lista_mea.append(item)

    @classmethod
    def get_list(cls):
        return cls.lista_mea

    @classmethod
    def create_with_item(cls, item):
        return cls(item)   # echivalent obiect = Oarecare(5)

    @staticmethod
    def get_list_length():
        return len(Oarecare.lista_mea)

# o1 = Oarecare('123')
# o1.create_with_item('345')
# o2 = Oarecare(5)
# o3 = Oarecare("789")
# # o1.create_with_item obiectul o1 este alocat: crate with item, get list, lista mea;
# print(o1.lista_mea)
# print(Oarecare.get_list_length())

class Oarecare2:

    def __init__(self, item):
        self.lista_mea = []  # membru local obiectului
        self.lista_mea.append(item)

    def get_list(self):
        return self.lista_mea


o1 = Oarecare2(5)
o2 = Oarecare2(11)

print(o1.get_list())
print(o2.get_list())
