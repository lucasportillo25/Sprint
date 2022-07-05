#Defino librerias a utilixar
import csv
from distutils.file_util import write_file

#defino constantes y variables
amigos = []

#defino funciones
def readFile():
    file = open("phonebook.csv", "r")
    csvfile = csv.reader(file)
    for row in csvfile:
        if row in csvfile:
            if row != []:
                data = {"nombre":row[0], "Apellido":row[1], "Teléfono": row[2], "Cumpleaños": row[3]}
                #amigos.append(data)
    file.close()


def grabarAmigos():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    telefono = input("Ingrese telefono: ")
    cumpleaños = input("Ingrese cumpleaños: ")
    data = {"Nombre":nombre, "Apellido":apellido, "Telefono": telefono, "Cumpleaños": cumpleaños}
    amigos.append(data)
    writeFile(amigos)


def printAmigos(amigos):
    for amigo in amigos:
        csvfile.writerow(amigo['Nombre'], amigo ['Apellido'],amigo['Telefono'], amigo['Cumpleaños'] )
    file.close()
#defino el método principal
if __name__=="__main__":
    print("Bienvenido a la agenda telefonica")
    print("-----Elija la opcion-----")
    print("1. Imprimir amigos")
    print("2. Agregar amigo")
    op = input("Ingrese opcion: ")
    if op == "1":
        readFile()
        printAmigos(amigo)
    elif op == "2":
        grabarAmigos()
    else:
        print("Gracias por utilizar la agenda")

    