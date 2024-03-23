def num_contagiados(c:int, d:int) -> int:
    x = 2**d
    contagiados = c*x
    return contagiados

if __name__ == "__main__":
    c=int(input("Ingresa el numero de contagiados actuales: "))
    d= int(input("Ingresa el numero de dias: "))
    print(f"El numero de contagiados es de {num_contagiados(c,d)}")