def valor_prestamo (dinero:float,interes:float,meses:int) -> float:
    valor_final_prestamo=dinero*(1+(interes/100))**meses
    return valor_final_prestamo

if __name__ == "__main__":
    dinero = float(input("Ingrese la cantidad de dinero que se le fue prestado: ")) 
    interes = float(input("Ingrese la tasa de interés mensual (%): "))
    meses = int(input("Ingrese el tiempo del préstamo en meses: ")) 
    prestamo=valor_prestamo(dinero,interes,meses)
    print(f"El valor del préstamo es de {prestamo}")