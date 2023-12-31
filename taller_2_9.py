# -*- coding: utf-8 -*-
"""Taller_2_9

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wf9pnozashV1cFJp2ikytDmF4-7QzuRH
"""

# PROMEDIO

import math

def obtener_numeros():
    numeros = []
    for i in range(5): # Definimos cuantos elementos tiene la lista
        numero = float(input(f"Ingrese el número {i+1}: ")) #Aui es donde se le pedira al usuario que coloque sus 5 números
        numeros.append(numero)
    return numeros


def calcular_promedio(numeros): # Definimos la operacion para calcular promedios
    suma = sum(numeros)
    total_elementos = len(numeros)
    promedio = suma / total_elementos
    return promedio

def main():
    numeros = obtener_numeros()
    promedio = calcular_promedio(numeros)
    print(f"El promedio de los números ingresados es: {promedio}")

if __name__ == "__main__":
    main()

#Mediana
from statistics import *
def mediana_(numeros):
  return median(numeros)

if __name__ == "__main__":
  numeros = []
  for i in range(5): # Definimos cuantos elementos tiene la lista
      Num_usuario = float(input(f"Ingrese el número {i+1}: ")) #Aqui es donde se le pedira al usuario que coloque sus 5 números
      numeros.append(Num_usuario)
  print(numeros)
  medianita = mediana_(numeros)
  print("La mediana de los números es:" + str(medianita))

# Promedio multiplicativo
import math

def promedio_multi(lista):
    if not lista:
        return None #Si no hay lista no imprima nada
    product = math.prod(lista) #Multipliación de la lista
    raiz = len(lista) #Número de datos
    return product ** (1 / raiz) #Operación producto multiplicativo

lista = []
for i in range(5):
    number = float(input(f"Ingrese el número {i+1}: "))
    lista.append(number)
print(promedio_multi(lista))

#Orden ascendente
def lista_numeros(lista):
  lista.sort() # Se ultiiza el sort, que nos ordena los elementos de una lista ascendentemende
  return lista

if __name__ == "__main__":
  lista = []
  for i in range(5):
      numeros = float(input(f"Ingrese el número {i+1}: "))
      lista.append(numeros)
  orden = lista_numeros(lista) # Ingresamos la lista a la función
  print(orden)

#Orden descendente
def lista_numeros(lista):
  lista.sort(reverse = True) # Se ultiiza el sort, que nos ordena los elementos de una lista descendentemende
  return lista

if __name__ == "__main__":
  lista = []
  for i in range(5):
      numeros = float(input(f"Ingrese el número {i+1}: "))
      lista.append(numeros)
  orden = lista_numeros(lista) # Ingresamos la lista a la función
  print(orden)

# Aqui es donde estipularemos la condicion clave para hallar la respectiva potendia entre el mayor y menor numero
def raiz_may(lista):
  max_num = max(lista) #Busca número amyor
  min_num = min(lista) # Busca número menor
  resultado = max_num ** min_num # Operación
  return resultado

if __name__ == "__main__":
  lista = []
  for i in range(5):
      numeros = float(input(f"Ingrese el número {i+1}: "))
      lista.append(numeros)
  resultado = raiz_may(lista)
# Mostrar el resultado
print("La potencia del mayor número elevado al menor número es: ", resultado)

# Aqui se coloca el parametro para calcular la raíz cúbica del menor número
def raiz(lista):
  menor_numero = min(lista) # Busca número menor
  raiz_cubica = menor_numero ** (1/3) # Operación
  return raiz_cubica

if __name__ == "__main__":
  lista = []
  for i in range(5):
      numeros = float(input(f"Ingrese el número {i+1}: "))
      lista.append(numeros)
  raiz_cubica = raiz(lista)
  print("La raíz cúbica del menor número es: ", raiz_cubica)