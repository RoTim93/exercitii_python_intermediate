# se cere un scrip python care traverseaza un director, listeaza toate fisierele de tip text!, printrand numele
#fisierului si prima linie cu continutul acesteia.

import os
import linecache

def traverse_directory(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                print(f'{file}')
                with open(os.path.join(root, file), 'r') as f:
                    print(f'Prima linie este {f.readline()}') #-> in paranteza () se poate specifica cate caractere sa numere de pe o linie

traverse_directory('F:\\Apps\\Fresh Start\\office 2007')

def traverse_directory_non_recursive(path):
    with os.scandir(path) as entries:
        for entry in entries:
            if(entry.is_file() and entry.name.endswith('.txt')):
                print(f'Fisierul: {entry.name}.')

traverse_directory_non_recursive('F:\\Apps\\Fresh Start\\office 2007')

def read_multiple_line(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                print(f'{file}')
                with open(os.path.join(root, file), 'r') as f:
                    #for _ in range(2):
                    #    print(f.readline().strip())
                    a_doua_linie = linecache.getline(f.name, 8).strip()
                    print(a_doua_linie)
                    '''
                    lines = f.readlines()
                    for line in lines:
                        print(line.strip())
                    '''

                    '''
                     while True:
                        line = f.readline()
                        if not line:
                            break
                        print(line.strip())
                    '''


read_multiple_line('F:\\Apps\\Fresh Start\\office 2007')




# dat fiind un fisier, de orice tip, care contine mai multe linii
# se cere crearea unei clase ce introduce fiecare linie intr-o structura de date aleasa de voi lista sau dictionar
# a.i atunci cand accesam o linie, sa o putem facem dupa un index/cheie
# tratati posibilile exceptii

# class VectorFileParser:
#     def __init__(self, file_name):
#         self.file_name = file_name
#
#     def convertFileLinesToVectorElement(self):
#         lista_linii = []
# ceva de genu