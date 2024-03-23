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