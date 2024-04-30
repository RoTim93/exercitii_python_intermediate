# Deep copy vs shallow copy ( copiere adanca vs copiere superficiala )


# shallow copy retine referintele la elementele originale ( dar nu si pe cele adaugate dupa)
# deep copy copiaza recursiv toate elementele originale, dar fara referinte ( pastreaza o copie a obiectului original )

import copy

class Ceva:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'{self.a!r}, {self.b!r}'

