# orice operatie pe fisier -> reprezinta un management de resurse (resursa este chiar fisierul)
# ORICE RESURSA TREBUIE INTIALIZATA SI ELIBERATA cand este folosita

f = open('exemple.txt', 'w')
try:
    f.write('ceva')
except IOError:
    print('error occured')
finally:
    f.close()

# context manager: with

with open("exemple.txt", 'w') as fisier:
    fisier.write('altceva')

class FileManager:
    # def __init__, __enter__, __exit__
    def __init__(self, file_name, mod):
        self.mod = mod
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mod)
        print('Am intrat!')
        #....
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb): # exc_type -> type (tip fisier: .txt etc), exc_value -> valoarea curenta, exc_tb -> traceback
        #....
        self.file.close()

with FileManager('exemple2.txt', 'w') as fisier2:
    fisier2.write('harmalem')

with FileManager('exemple2.txt', 'r') as fisier3:
    content = fisier3.read()
    print(content)