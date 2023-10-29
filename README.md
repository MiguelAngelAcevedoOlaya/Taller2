# Segundo Hackeo de este bello duo

## Como integrantes estan:
Juan Andres Valderrama Parra, Alias: AnonymusconH 

Miguel Angel Acevedo Olaya, Alias: Mickey

## LOGO:

[![Hanonimus-con-H.png](https://i.postimg.cc/zvK2hP3Y/Hanonimus-con-H.png)](https://postimg.cc/T52cM0rt)

## PUNTO 1 - LAS MATEMATICAS COMO LA BASE DE TODO

### Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).

Para este punto se desarrollo una función en la que se divide entero el número entre 10, el residuo de esa division sera el ultimo digito, este lo agregaremos a la lista, y el resultado de la división, reppetira el ciclo hasta que el numero deje de ser mayor de 0.

Al final en el resulado invertiremos el orden de la lista, por cuestiones de estetica y para que se entiendan los digitos con el que se ingreso al inicio.

```
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
```

## PUNTO 2 - Sorpresita no fue mate

### Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.

Creamos las listas necesarias para el codigo.

```
digitos = [] #LISTA VACIA QUE USAREMOS PARA ANEXAR CADA DIGITO
entero = [] # Lista para los enteros
decimal = [] # Lista para los flotantes
```

Ahora definimos la función, se decidió hacerla convirtiendo el flotante en string y utilizar el remove en las lsitas para separarlos, se penso hacerlo con el punto 1, pero este tiene un porblema para la aproximacion de flotantes debido a su codigo. Por lo que se opto por este.

```
def separar_digitos_num(numero_n : float)-> int: # Función
  str_numero_n = str(numero_n) # Convertimos el flotante en un string
  for i in str_numero_n:
    decimal.append(i) # Agregamos todos elementos del string a la lista
  decimal_aux = decimal [:] # Creamos una variable auxiliar que será necesaria
  for i in decimal_aux: #Esto se usa para separar la lista en los elementos antes del punto y los de despues, la variable auxiliar era para que el remove no fallara
    if i == "." :
      decimal.remove(i)
      break #No incluir el punto y que funcione hasta que aparezca el
    else:
      decimal.remove(i) #Eliminar de la lista
      entero.append(i)  #Agregar a la lista
  print("La parte entera es: " +str(entero)) #Tenemos la parte entera
  print("La parte decimal es: " +str(decimal)) # Tenemos la parte decimal
  for i in str_numero_n:  # Este para repetir lo del escenario anterior pero dejarlo en una lista aparte, sin el punto
    if i == ".":
      continue
    digitos.append(i)
  print("Todos los digitos son: " +str(digitos))
```

Ahora le pedimos al usuario ingresar al número que desee, que sea flotante

```
if __name__ ==  "__main__":
  numero_n = float(input("Ingresa el flotante que quieras ")) # El usuario tiene libertad de elegir su numero
  separar_digitos_num(numero_n) # Para ingresarlo a la función
```

## Punto 3 - espejito, espejito ¿Quien es el más bonito?

### Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.

```
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
```
## Punto 4 - SUMATORIAS DE ******

### Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.

Para este punto importamos expoencial y factorial de la libreria math, establecimos la función con la variable numero como flotante y n como entero. Una variable dentro de la función llamada suma = 0, que usaremos para el ciclo for, minetras la variable i este entre 0 y (n +1) usamos la serie de Maclaurin que se ira sumando porgresivamente a la variable suma hasta que deje de cumplirse el ciclo.

Luego le damos valor a las variables necesarias, y sacamos el valor real al elevar el número a cierto exponente, y establecimos un ciclo while que determine cuando el margen de error es inferior al 0.1%, ese sera el nuevo valor de n que utliziremos, corriendo nuevamente la función, dandonos el valor aproximado y el real.

En esta primera es la función en la que no buscamos que el margen de error sea menor a 0.1%, el usuaario tiene la libertad de elegir el número n, considerando que el margen de error

```
import math

def cos_approx_TaylorSwift(x, n):
    # Variable para almacenar el resultado
    resultado = 0

    # Sumamos los términos de la serie de Taylor
    for i in range(n):
        resultado += ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)

    # Devolvemos el resultado
    return resultado


x = float(input("Ingrese el valor de x: "))
n = int(input("Ingrese el número de términos de la serie: "))

# Calculamos la aproximación y mostramos la diferencia entre el valor real y la aproximación
cos_x = math.cos(x)
cos_approx = cos_approx_TaylorSwift(x, n)
print(f"El valor real de cos({x}) es: {cos_x}")
print(f"La aproximación de cos({x}) usando {n} términos de la serie es: {cos_approx}")
print(f"La diferencia entre el valor real y la aproximación es: {abs(cos_x - cos_approx)}")
```
En esta si buscamos encontrar el valor en el que el margen de error sea 0.001%

```
import math

def aprox_exp(numero: float, n: int)-> float:
  suma: float = 0
  for i in range(0, n+1):
    n_ter = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    suma += n_ter
  return suma

if __name__ == "__main__":
  numero = float(input("Ingresa un número real "))
  n: int = 1
  aprx: float = aprox_exp(numero, n)
  v_real : float = math.cos(x)

while((abs(v_real - aprx)/v_real * 100)>0.001):
  aprx: float = aprox_exp(numero, n)
  n += 1
print("Para que el margen de error sea 0.001  el valor debe ser:" +str(n))
print("La aproximación es " +str(aprx))
print("El valor real es " +str(v_real))
```
En esta si buscamos encontrar el valor en el que el margen de error sea 0.1%

```
import math

def aprox_exp(numero: float, n: int)-> float:
  suma: float = 0
  for i in range(0, n+1):
    n_ter = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    suma += n_ter
  return suma

if __name__ == "__main__":
  numero = float(input("Ingresa un número real "))
  n: int = 1
  aprx: float = aprox_exp(numero, n)
  v_real : float = math.cos(x)

while((abs(v_real - aprx)/v_real * 100)>0.1):
  aprx: float = aprox_exp(numero, n)
  n += 1
print("Para que el margen de error sea 0.1  el valor debe ser:" +str(n))
print("La aproximación es " +str(aprx))
print("El valor real es " +str(v_real))
```
En esta si buscamos encontrar el valor en el que el margen de error sea 1%

```
import math

def aprox_exp(numero: float, n: int)-> float:
  suma: float = 0
  for i in range(0, n+1):
    n_ter = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    suma += n_ter
  return suma

if __name__ == "__main__":
  numero = float(input("Ingresa un número real "))
  n: int = 1
  aprx: float = aprox_exp(numero, n)
  v_real : float = math.cos(x)

while((abs(v_real - aprx)/v_real * 100)>1):
  aprx: float = aprox_exp(numero, n)
  n += 1
print("Para que el margen de error sea 1  el valor debe ser:" +str(n))
print("La aproximación es " +str(aprx))
print("El valor real es " +str(v_real))
```

En esta si buscamos encontrar el valor en el que el margen de error sea 10%

```
import math

def aprox_exp(numero: float, n: int)-> float:
  suma: float = 0
  for i in range(0, n+1):
    n_ter = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    suma += n_ter
  return suma

if __name__ == "__main__":
  numero = float(input("Ingresa un número real "))
  n: int = 1
  aprx: float = aprox_exp(numero, n)
  v_real : float = math.cos(x)

while((abs(v_real - aprx)/v_real * 100)>10):
  aprx: float = aprox_exp(numero, n)
  n += 1
print("Para que el margen de error sea 10%  el valor debe ser:" +str(n))
print("La aproximación es " +str(aprx))
print("El valor real es " +str(v_real))
```

## Punto 5 - ¿Cúall es tu addición con la matemática?

###  Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. Pista: Puede ser de utilidad chequear el Algoritmo de Euclides para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.

El algortimo de euclides para encontrar un Mínimo Común Multiplo es un algoritmo que permite sistematizar mediante la busquedad de un Máximo Común Divisior la solución a esta.

Hay que tener presente antes de, el máximo común divisor (MCD) de dos enteros A y B es el entero más grande que divide tanto a A como a B. y con esto e l algoritmo de Euclides es una técnica para encontrar rápidamente el MCD de dos enteros.

El algortitmo:

El algoritmo de Euclides para encontrar MCD(A,B) es como sigue:
Si A = 0 entonces MCD(A,B)=B, ya que el MCD(0,B)=B, y podemos detenernos.  
Si B = 0 entonces MCD(A,B)=A, ya que el MCD(A,0)=A, y podemos detenernos.  
Escribe A en la forma cociente y residuo (A = B ⋅Q + R).
Encuentra MCD(B,R) al usar el algoritmo de Euclides, ya que MCD(A,B) = MCD(B,R).

Trasladado a codigo quedaria asi:

```
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa ahora otro número: "))
def MCD(a, b):
    if b == 0:
        return a
    else:
        return MCD(b, a % b)

def MCM(a, b):
    return a * b // MCD(a, b)


print(f"El mínimo común multiplo de {a} y {b} es: {MCM(a, b)}")
```

## Punto 6 - Unico, bonito y bello, como nosotros

### Desarrollar un programa que determine si en una lista existen o no elementos repetidos. Pista: Maneje valores booleanos y utilice el operador in

Para este punto se le pide al usuario que ingrese valores separados por coma para crear la lista, ahora se crea un ciclo en el que busva si por cada elemento de la lista esta en algun otro punto de ella, en caso de que halla tan solo 1 repetido hace break ya que cumple la condición, en caso de que no continuara en el ciclo hasta que se acabe el ciclo

```
numeros = (input("Coloca una lista de número y separalos con una coma: "))

# Variable booleana para indicar si hay elementos repetidos
tiene_repetidos = False

# Bucle for para recorrer cada elemento de la lista
for i in range(len(numeros)):
    # Estructura condicional if para verificar si el elemento actual de la lista está presente en la lista entera
    if numeros[i] in numeros[i] + numeros[i+1]:
        tiene_repetidos = True
        break

# Verificar el valor de la variable booleana "tiene_repetidos"
if tiene_repetidos:
    print("Existen elementos repetidos en la lista.")
else:
    print("No existen elementos repetidos en la lista.") 
```

## PUNTO 7 - aeiou ¿Te los sabes?

### Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'

Para este punto se desarrollo un ciclo for en el que para cada palabra que ingrese el usuario, busque las vocales aeiou en minuscula o mayuscula si si sume al contador que determina cunatas palabras tendra, en caso de ser menor a dos la agrega a una lista de nombre. no existe y retorna "No existe", en cambio si es mayor a 2 el número de vocales, lo agregar a la lista, si existe, y retorna la palabra.

Al final se imprime la lista, si la palabra existe o no, y la lista de las que existen y las que no

```
existe = [] # Lista para agregar las que existen
no_existe = [] # Lista para agregar las que no  existen
def contar_vocales(palabra):
  for i in palabra:
    contador = 0
    for letra in palabra:
      if letra.lower() in "aeiou": # Busca si la pañanra tiene una de las 5 vocales en mayuscula o miniscula
        contador += 1 # Cuente el contador
    if contador >= 2: # Si el contador es mayor o igual a 2 retorne la palabra y la agregue a la lista que existe
      existe.append(palabra)
      return palabra
    else:
      no_existe.append(palabra) # Si el contador es menor a 2 retorne no existe y la agregue a la lista que no existe
      return "No existe"

if __name__ == "__main__":
  palabras_ = []
  num = int(input("Ingresa el número de palabras que desees ")) # Determine cuantas palabras quiere
  for i in range(num):
    palabra_ = input("Ingrese la palabra que desee ") # Ingrese la palabra
    palabras = palabra_  # Variable auxiliar
    palabras_.append(palabras) # Agregar palabras con la lista auxilair a a lista
    existe_o_no = contar_vocales(palabra_) #Ejecutar la función
    print(existe_o_no)
  print("Todas las palanras que pusiste son " +str(palabras_))
  print("Las que existen " +str(existe))
  print("Las que no existen " +str(no_existe))
```

## Punto 8 - A sin B puede vivir, pero tu sin tu ex no

### Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista

Utilizaremos codigos for que ayuden a buscar si los elementos coineciden en cada lista siendo la lista A la que buscara si tiene elementos en la lista b, los que no coincidan los agregaremos en una tercera lista

```
def lista_a_in_b(lista_A,lista_B):
  lista_A_sin_b = []
  for i in lista_A: #Primero i en los elementos en a
    contador = 0
    for i_2 in lista_B: #Ahora i2 en los elemenos en b
      if i == i_2: #Si i y i2 son iguales le sumara uno e el contador
        contador = contador + 1
      else: continue
    if contador == 0 and i not in lista_A_sin_b: # Si el contador es 0 lo agregara a la otra lista
      lista_A_sin_b.append(i)
  return lista_A_sin_b

```

Ahora le pedimos al usuario que ingrese los valores que desee a la lista a y a la lista b

```
if __name__ == "__main__":
  num_a = int(input("Ingresa cuantas cosas quieres en la lista A: ")) #numero elementos lista A
  lista_A = []
  for i in range(num_a):  # Ingresar palabra y que lo ingrese a la lista
    a = input( "Ingresa lo que desees ingresar: ")
    lista_A.append(a)
  num_b = int(input("Ingresa cuantas cosas quieres en la lista B: ")) #numero elementos lista B
  lista_B = []
  for i in range(num_b): # Ingresar palabra y que lo ingrese a la lista
    b = input( "Ingresa lo que desees ingresar: ")
    lista_B.append(b)
  resultado = lista_a_in_b(lista_A,lista_B) # Ejecutar en la función
  print("Lista A: " +str(lista_A)) # Lista A
  print("Lista B: " +str(lista_B)) # Lista B
  print("Lista de A sin elementos en B " +str(resultado)) # Lista A sin elementos en B
```

## Punto 9 - Reviviendo el pasado

### Resolver el punto 7 del taller 1 usando operaciones con vectores.

Para el promedio creamos los 5 números, se agregan a la lista, utilizamos math para calcular la suma de estos 5 valores, y esto lo dividiremos entre la cantidad de elementos que tenga la lista, en este caso 5

```
# PROMEDIO

import math

def obtener_numeros():
    numeros = []
    for i in range(5): # Definimos cuantos elementos tiene la lista
        numero = float(input(f"Ingrese el número {i+1}: ")) #Aui es donde se le pedira al usuario que coloque sus 5 números #Se define la lista
        numeros.append(numero)
    return numeros


def calcular_promedio(numeros): # Definimos la operacion para calcular promedios
    suma = sum(numeros) # Parte de math que permite calcular la suma de elementos de la lista
    total_elementos = len(numeros) # Canidad de elementos
    promedio = suma / total_elementos # Calcula el promedio
    return promedio

def main():
    numeros = obtener_numeros() # LLamamos a la función
    promedio = calcular_promedio(numeros) # LLamamos a la función
    print(f"El promedio de los números ingresados es: {promedio}")

if __name__ == "__main__":
    main()

```

Para la mediana importamos una libreria, en la cual permite encontrar la mediana de la lista, en caso de tener cantidad par de elementos, imprimira el promedio de los valores de la mitad, como no es el caso, imprimira el 3 valor.

```
#Mediana
from statistics import * # Libreria
def mediana_(numeros):
  return median(numeros) # Halla la mediana

if __name__ == "__main__":
  numeros = []
  for i in range(5): # Definimos cuantos elementos tiene la lista
      Num_usuario = float(input(f"Ingrese el número {i+1}: ")) #Aqui es donde se le pedira al usuario que coloque sus 5 números
      numeros.append(Num_usuario) # Codigo para crear lista
  print(numeros)
  medianita = mediana_(numeros)
  print("La mediana de los números es:" + str(medianita)) # Respuesta
``` 

Para el promedio multiplicativo establecemos una función en la que gracias a math determinamos el producto de los valores de la lista, a este valor le sacaremos la raiz del número de elementos de la lista, este caso 5-

```
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
```

Para ordenar la lista ascedentemente utilizamos la variable sort, que la organiza de esta manera

```
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
```

Utilizamos el sor inverso para que organice de manera descendente

```
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
```

Utilizamos una función que busque el mayor número y el menor, y luego elelve el mayor al segundo

```
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
```

Buscamos el menor número de los 5 le sacamos la raiz cubica

```
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
```

## Punto 10 - el bono estaba mas sencillo

### Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas. Desafío: Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). Pista: Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad?

Para este punto estabelecemos la lista que ingresaremos, una funcíón con ciclo for que para cada elemento de la lista determine si su residuo al divirlo entre 3 es igual a 0, los que si los agregue a la lista nueva y los que no, se mantengan igual, al final de la función esta retornara la lista.

```
def multiplos_3(lista_numeros):
  lista_multiplos = []
  for i in lista_numeros: # Ciclo en el que si el residuo de dividir el número entre 3 lo agregue a lista que se usara para eso, sino continue
    if i % 3 == 0:
      lista_multiplos.append(i)
    else: continue
  #lista_multiplos = lista_multiplos.sort() #Si la quieres ordenada quita el numeral del inicio
  return lista_multiplos

```

Para el bono lo que se hizo fue cambiar la parte del residuo por una resta en la que si la division flotante (/) menos la division entera (//) al dividir entre tres es igual a 0, entonces sera multiplo de 3.

```
def bono(lista_numeros):
  lista_multiplos = []
  for i in lista_numeros: # Ciclo en el que si la resta de la division flotante y su division real, al divir entre 3, lo agregue a lista que se usara para eso, sino continue
    if (i/3)-(i//3)  == 0:
      lista_multiplos.append(i)
    else: continue
  #lista_multiplos = lista_multiplos.sort() #Si la quieres ordenada quita el numeral del inicio
  return lista_multiplos
```

Ahora le pedimos al usuario que ingrese los números que desee a la lista y la respuesta

```
if __name__ == "__main__":
  lista_numeros = []
  num = int(input("Ingresa cuantas cosas quieres en la lista A: ")) # numero elementos lista
  for i in range(num):  # Ingresar los números y que lo ingrese a la lista
    numero = int(input( "Ingresa lo que desees ingresar: "))
    lista_numeros.append(numero)
  print("La lista esta compuesta por: " +str(lista_numeros))
  resultado = multiplos_3(lista_numeros)
  resultado_bono = bono(lista_numeros)
  print("De la lista los que son multiplos de 3 son: " +str(resultado))
  print("De la lista los que son multiplos de 3 con la parte del bono, son: " +str(resultado_bono))****
```
