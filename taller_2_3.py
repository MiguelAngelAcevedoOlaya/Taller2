# -*- coding: utf-8 -*-
"""Taller_2_3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wf9pnozashV1cFJp2ikytDmF4-7QzuRH
"""

# Aqui vamos a dar el parametro general que permita identificar números iguales, ya despues le daremos el criterio de espejo
def num_espejo(num1, num2):
    return str(num1) == str(num2)

def numeros_analizar():
    num1 = int(input("Ingresa un primer número: "))
    num2 = int(input("Ingresa ahora un segundo número: "))
    return num1, num2

# Aqui se da el criterio de espejo
def main():
    num1, num2 = numeros_analizar()
    if num_espejo(num1, num2):
        print("Los números"  + str(num1) +  " y"  + str(num2) + "son números espejo ")
    else:
        print("Los números" + str(num1) + " y " + str(num2) + "no son números espejo")

if __name__ == "__main__":
    main()