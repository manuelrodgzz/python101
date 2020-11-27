# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

'''
Este es un comentario multilinea
al empezar un string con f antes de la primer comilla me permite poner variables dentro del string entre {}
'''

# El Set no permite valores duplicados y lo ordenan al gusto del set
def sets():
    set = {"a", "b", "c", "c"}
    for s in set:
        print(s)

def diccionarios():
    ejemplo_diccionario = {
        "str": "esto es un string",
        "float" : 1.54,
        "int": 1
    }

    for key, val in ejemplo_diccionario.items():
        print(f'{key}={val}')


def iterate():

    x = range(0,6,1)

    for y in x:
        print(y)

    fruits = ['apple', 'banana', 'cherry']

    for x in fruits:
        print(x)

    for x in range(10, 20):
        print(x)

def printNumber():
    x = 1
    f = 1.1002

def printStr():
    m = 'Manuel'

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sets()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
