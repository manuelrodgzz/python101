import csv

def leer_csv_dict():
    ruta_archivo = 'data/employees.csv'

    with open(ruta_archivo, 'r') as archivo_csv:
        lector_dic = csv.DictReader(archivo_csv)
        for mapa in lector_dic:
            print(mapa)

def leer_csv():
    ruta_archivo = 'data/employees.csv'

    with open(ruta_archivo, 'r') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for linea in lector:
            print(linea)




if __name__ == '__main__':
    leer_csv_dict()