# Reto-5-David-Hoyos
## Punto 1
Dado la figura de la imagen, desarrolle:

[![Captura-de-pantalla-2024-03-22-193634.png](https://i.postimg.cc/HxD0CRMP/Captura-de-pantalla-2024-03-22-193634.png)](https://postimg.cc/3y10XLng)

+ Una función matemática para calcular el volumen y el área superficial.

+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.

+ Revise como utilizar el valor de pi usando import math y math.pi
```python
import math
def area(r1:float, r2:float,h:float) -> float: 
    x = 4*math.pi*r1**2
    generatriz= math.sqrt(h**2 + r2**2)
    y = (math.pi*r2*generatriz) + (math.pi*(r2**2))
    return x+y

def volumen(r1:float,r2:float,h:float) -> float:
    v_esfera = ((4/3)*math.pi*(r1**3))
    v_cono = ((math.pi*(r2**2)*h)/3)
    return v_cono + v_esfera 

if __name__ == "__main__":
  r1 = float(input("Ingresa el radio del circulo: "))
  r2 = float(input("Ingresa el radio del cono: "))
  h = float(input("Ingresa la altura del cono:"))
  print("El area corresponde a: " + str(area(r1,r2,h)))
  print("El volumen corresponde a: " + str(volumen(r1,r2,h)))
```
## Punto 2
Dado la figura de la imagen, desarrolle:

[![Captura-de-pantalla-2024-03-22-194257.png](https://i.postimg.cc/6pCnfzgr/Captura-de-pantalla-2024-03-22-194257.png)](https://postimg.cc/w1T1656M)

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
+ Revise como utilizar el valor de pi usando import math y math.pi

```python
import math 
def area(r:float,a:float,b:float) -> float:
    area_circulo = math.pi*(r**2)
    area_rectangulo = a*b
    return area_rectangulo + (2*area_circulo)

def perimetro(r:float,a:float,b:float) -> float:
    p_circulo = math.pi*2*r
    p_rectangulo = 2*a + 2*b
    return p_rectangulo + 2*p_circulo

if __name__ == "__main__":
  r = float(input("Ingresa el radio de los circulos: "))
  a = float(input("Ingresa la base del rectangulo: "))
  b = float(input("ingresa el alto del rectangulo: "))
  print(f"El area de la figura corresponde a {area(r,a,b)}")
  print(f"El perimetro de la figura corresponde a: {perimetro(r,a,b)}")
```
## Punto 3
Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.
```python
def cantidad_carne(n:int,m:int,k:int) -> float:
    carne = 6*n + 7*m + k
    return carne

if __name__ == "__main__":
  gallina = int(input("Ingrese el numero de gallinas: "))
  gallos = int(input("Ingrese el numero de gallos: "))
  pollitos = int(input("Ingrese el numero de pollitos: "))
  print(f"La cantidad de carne corresponde a {cantidad_carne(gallina,gallos,pollitos)}")
```
## Punto 4 
Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.
```python
def vueltas(b:float,p:float,m:float,h:float) -> float:
    costo_p = p*300
    costo_m = m*3300
    costo_h = h*350
    v = b - (costo_p + costo_m + costo_h)
    if v < 0:
        x = "Usted debe"
    else:
        x = "Tus vueltas son"
    return str(x ) + " " + str(abs(v))

if __name__ == "__main__":
  panes = int(input("Ingrese la cantidad de panes: "))
  leche = int(input("Ingrese la cantidad de bolsas de leche: "))
  huevos = int(input("Ingrese la cantidad de huevos: "))
  billete = int(input("Ingrese el valor del billete: "))
  print(vueltas(billete, panes, leche, huevos))
```
## Punto 5
Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

```python
def valor_prestamo (dinero:float,interes:float,meses:int) -> float:
    valor_final_prestamo=dinero*(1+(interes/100))**meses
    return valor_final_prestamo

if __name__ == "__main__":
    dinero = float(input("Ingrese la cantidad de dinero que se le fue prestado: ")) 
    interes = float(input("Ingrese la tasa de interés mensual (%): "))
    meses = int(input("Ingrese el tiempo del préstamo en meses: ")) 
    prestamo=valor_prestamo(dinero,interes,meses)
    print(f"El valor del préstamo es de {prestamo}")
```
## Punto 6
El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```python
def num_contagiados(c:int, d:int) -> int:
    x = 2**d
    contagiados = c*x
    return contagiados

if __name__ == "__main__":
  c=int(input("Ingresa el numero de contagiados actuales: "))
  d= int(input("Ingresa el numero de dias: "))
  print(f"El numero de contagiados es de {num_contagiados(c,d)}")
```
## Punto 7 
Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

+ El promedio
+ La mediana
+ El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
+ Ordenar los números de forma ascendente
+ Ordenar los números de forma descendente
+ La potencia del mayor número elevado al menor número
+ La raíz cúbica del menor número
```python
import operaciones
a=float(input("Por favor ingrese el primer numero:"))
b=float(input("Por favor ingrese el segundo numero:"))
c=float(input("Por favor ingrese el tercer numero:"))
d=float(input("Por favor ingrese el cuarto numero:"))
e=float(input("Por favor ingrese el quinto numero:"))
if __name__ == "__main__":
    print(f"El promedio de los numeros corresponde a: {operaciones.promedio(a,b,c,d,e)}")
    print(f"La mediana de los numeros corresponde a: {operaciones.mediana(a,b,c,d,e)}")
    print(f"Al ordenar los numeros de forma ascendente quedan asi: {operaciones.ordenar_ascendente(a,b,c,d,e)}")
    print(f"Al ordenar los numeros de forma descendente quedan asi: {operaciones.ordenar_descendente(a,b,c,d,e)}")
    print(f"El promedio multiplicativo de los numeros es: {operaciones.promedio_multiplicativo(a,b,c,d,e)}")
    print(f"El resultado de la potencia del mayor numero elevado al menor numero es: {operaciones.potencia(a,b,c,d,e)}")
    print(f"La raiz cubica del numero menor es: {operaciones.raiz(a,b,c,d,e)}")
```
## Punto 8 
Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.
```python
def promedio(a:float,b:float,c:float,d:float,e:float) -> float:
    p=(a+b+c+d+e)/5
    return p 

def ordenar_ascendente(a:float, b:float, c:float, d:float, e:float)->float:
    if a < b:
        num = [a,b]
    elif a > b:
        num =[b,a]
    else:
        num = [a,a]
    if a < b:
        if c < a:
            num = [c,a,b]
        elif a < c < b:
            num = [a,c,b]   
        else:   
            num = [a,b,c]
    elif a > b:
        if c < b:
            num = [c,b,a]
        elif b < c < a:
            num = [b,c,a]
        elif b==c==a:
            num =[a,a,a]
        else:
            num =[b,a,c]
    else: 
        num = [a,a,a]
    max = num[2]
    first = num[1]
    min = num[0]
    if max < d:
        num = [min,first,max,d]
    elif min > d:
        num = [d,min,first,max]
    elif min <= d < first:
        num = [min,d,first,max]
    elif first <= d <= max:
        num = [min,first,d,max]
    else:
        num=[min,min,min,min]
    max = num[3]
    second = num[2]
    first = num[1]
    min = num[0]
    if max < e:
        num = [min,first,second,max,e]
    elif min > e:
        num = [e,min,first,second,max]
    elif min <= e < first:
        num = [min,e,first,second,max]
    elif first <= e < second:
        num = [min,first,e,second,max]
    elif second <= e <= max:
        num = [min,first,second,e,max]
    else:
        num=[min,min,min,min,min]
    max = float(num[4])
    third = float(num[3])
    second = float(num[2])
    first = float(num[1])
    min = float(num[0])
    return min,first,second,third,max

def ordenar_descendente(a:float,b:float,c:float,d:float,e:float) -> float:
    if a < b:
        num = [a,b]
    elif a > b:
        num =[b,a]
    else:
        num = [a,a]
    if a < b:
        if c < a:
            num = [c,a,b]
        elif a < c < b:
            num = [a,c,b]   
        else:   
            num = [a,b,c]
    elif a > b:
        if c < b:
            num = [c,b,a]
        elif b < c < a:
            num = [b,c,a]
        elif b==c==a:
            num =[a,a,a]
        else:
            num =[b,a,c]
    else: 
        num = [a,a,a]
    max = num[2]
    first = num[1]
    min = num[0]
    if max < d:
        num = [min,first,max,d]
    elif min > d:
        num = [d,min,first,max]
    elif min <= d < first:
        num = [min,d,first,max]
    elif first <= d <= max:
        num = [min,first,d,max]
    else:
        num=[min,min,min,min]
    max = num[3]
    second = num[2]
    first = num[1]
    min = num[0]
    if max < e:
        num = [min,first,second,max,e]
    elif min > e:
        num = [e,min,first,second,max]
    elif min <= e < first:
        num = [min,e,first,second,max]
    elif first <= e < second:
        num = [min,first,e,second,max]
    elif second <= e <= max:
        num = [min,first,second,e,max]
    else:
        num=[min,min,min,min,min]
    max = float(num[4])
    third = float(num[3])
    second = float(num[2])
    first = float(num[1])
    min = float(num[0])
    return max,third,second,first,min

def mediana(a:float,b:float,c:float,d:float,e:float)->float:
    if a < b:
        num = [a,b]
    elif a > b:
        num =[b,a]
    else:
        num = [a,a]
    if a < b:
        if c < a:
            num = [c,a,b]
        elif a < c < b:
            num = [a,c,b]   
        else:   
            num = [a,b,c]
    elif a > b:
        if c < b:
            num = [c,b,a]
        elif b < c < a:
            num = [b,c,a]
        elif b==c==a:
            num =[a,a,a]
        else:
            num =[b,a,c]
    else: 
        num = [a,a,a]
    max = num[2]
    first = num[1]
    min = num[0]
    if max < d:
        num = [min,first,max,d]
    elif min > d:
        num = [d,min,first,max]
    elif min <= d < first:
        num = [min,d,first,max]
    elif first <= d <= max:
        num = [min,first,d,max]
    else:
        num=[min,min,min,min]
    max = num[3]
    second = num[2]
    first = num[1]
    min = num[0]
    if max < e:
        num = [min,first,second,max,e]
    elif min > e:
        num = [e,min,first,second,max]
    elif min <= e < first:
        num = [min,e,first,second,max]
    elif first <= e < second:
        num = [min,first,e,second,max]
    elif second <= e <= max:
        num = [min,first,second,e,max]
    else:
        num=[min,min,min,min,min]
    max = float(num[4])
    third = float(num[3])
    second = float(num[2])
    first = float(num[1])
    min = float(num[0])
    return second

def promedio_multiplicativo(a:float,b:float,c:float,d:float,e:float) -> float:
    producto=(a*b*c*d*e)
    if producto <0:
        prom_multiplicativo=(-producto)**0.2*-1
    else:
        prom_multiplicativo=producto**0.2
    return prom_multiplicativo

def potencia(a:float, b:float, c:float, d:float, e:float)->float:
    if a < b:
        num = [a,b]
    elif a > b:
        num =[b,a]
    else:
        num = [a,a]
    if a < b:
        if c < a:
            num = [c,a,b]
        elif a < c < b:
            num = [a,c,b]   
        else:   
            num = [a,b,c]
    elif a > b:
        if c < b:
            num = [c,b,a]
        elif b < c < a:
            num = [b,c,a]
        elif b==c==a:
            num =[a,a,a]
        else:
            num =[b,a,c]
    else: 
        num = [a,a,a]
    max = num[2]
    first = num[1]
    min = num[0]
    if max < d:
        num = [min,first,max,d]
    elif min > d:
        num = [d,min,first,max]
    elif min <= d < first:
        num = [min,d,first,max]
    elif first <= d <= max:
        num = [min,first,d,max]
    else:
        num=[min,min,min,min]
    max = num[3]
    second = num[2]
    first = num[1]
    min = num[0]
    if max < e:
        num = [min,first,second,max,e]
    elif min > e:
        num = [e,min,first,second,max]
    elif min <= e < first:
        num = [min,e,first,second,max]
    elif first <= e < second:
        num = [min,first,e,second,max]
    elif second <= e <= max:
        num = [min,first,second,e,max]
    else:
        num=[min,min,min,min,min]
    max = float(num[4])
    third = float(num[3])
    second = float(num[2])
    first = float(num[1])
    min = float(num[0])
    return max**min

def raiz(a:float,b:float,c:float,d:float,e:float)->float:
    if a < b:
        num = [a,b]
    elif a > b:
        num =[b,a]
    else:
        num = [a,a]
    if a < b:
        if c < a:
            num = [c,a,b]
        elif a < c < b:
            num = [a,c,b]   
        else:   
            num = [a,b,c]
    elif a > b:
        if c < b:
            num = [c,b,a]
        elif b < c < a:
            num = [b,c,a]
        elif b==c==a:
            num =[a,a,a]
        else:
            num =[b,a,c]
    else: 
        num = [a,a,a]
    max = num[2]
    first = num[1]
    min = num[0]
    if max < d:
        num = [min,first,max,d]
    elif min > d:
        num = [d,min,first,max]
    elif min <= d < first:
        num = [min,d,first,max]
    elif first <= d <= max:
        num = [min,first,d,max]
    else:
        num=[min,min,min,min]
    max = num[3]
    second = num[2]
    first = num[1]
    min = num[0]
    if max < e:
        num = [min,first,second,max,e]
    elif min > e:
        num = [e,min,first,second,max]
    elif min <= e < first:
        num = [min,e,first,second,max]
    elif first <= e < second:
        num = [min,first,e,second,max]
    elif second <= e <= max:
        num = [min,first,second,e,max]
    else:
        num=[min,min,min,min,min]
    max = float(num[4])
    third = float(num[3])
    second = float(num[2])
    first = float(num[1])
    min = float(num[0])
    precision = 0.00000001
    x = min / 3.0
    while True:
        x_new = (2 * x + min / (x * x)) / 3.0
        if abs(x - x_new) < precision:
            return x_new
        x = x_new
```
## Punto 9 
Consultar qué es y cómo funciona pip en python.

Pip es un sistema de gestión de paquetes utilizado en Python para instalar y administrar paquetes de software escritos en Python. Su nombre es un acrónimo de "Pip Installs Packages" (Pip Instala Paquetes). Pip facilita la instalación, actualización y eliminación de paquetes Python y sus dependencias.

Desde la versión 3.4 en adelante, pip se encuentra preinstalado junto con Python, y su funcionamiento es sencillo. pip está integrado con el Índice de Paquetes de Python (PyPI), que es un repositorio de software para la comunidad de Python. En PyPI, los desarrolladores pueden publicar sus paquetes de código abierto para que otros puedan utilizarlos. Por lo tanto, mediante pip, puedes instalar, actualizar, desinstalar e incluso listar los paquetes disponibles en PyPI, todo mediante comandos simples en el terminal o símbolo del sistema. 

## Punto 10 
Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

Para instalar cualquier paquete se escribe el siguiente comando en el terminal: 

```python
pip install package-name
```
Algunos de los modulos mas populares son: 
|Nombre           | Funcion           |
|-----------------|-------------------|
|Numpy            |Computacion cientifica|
|Pandas           | Analisis de datos |
|SciPy            | Calculo cientifico y ciencia de datos|
|Flask            |Construir aplicaciones web rapidas y escalables|
|tensorflow       |Construir y entrenar modelos de redes neuronales|
|keras            |Construir y entrenar modelos de aprendizaje profundo en python|
|Sckit-learn      |Machine Learning|
|request          |Realizar peticiones HTTP|
