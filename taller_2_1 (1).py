# -*- coding: utf-8 -*-
"""Taller_2_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15s29rdhDEJzH3HOF-4jVhKqej451HrDJ
"""

digitos = [] #LISTA VACIA QUE USAREMOS PARA ANEXAR CADA DIGITO
def separar_digitos_num(numero_n : int)-> int:
  while numero_n > 0: # Para que no lleguemos a negativos
    digitos.append(numero_n % 10) # Agregamos a la lista el residuo al dividirlo entre 10, osea el ultimo digito del número
    numero_n = numero_n // 10 # El numero ahora sera la división entera de el entre 10, osea todos los números excepto el ultimo
  return numero_n

if __name__ == "__main__":
  numero_n = int(input("Ingresa el entero que quieras ")) # El usuario tiene libertad de elegir su numero
  separar_digitos_num(numero_n) # Para ingresarlo a la función
  rev = list(reversed(digitos )) # Revertimos el orden de la lista solo por cuestiones esteticas, ya que orignalmente el número se imprime al revez
  print("Los digitos separados de tu número son :" +str(rev)) # Imprimimos