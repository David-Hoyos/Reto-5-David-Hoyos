def cantidad_carne(n:int,m:int,k:int) -> float:
    carne = 6*n + 7*m + k
    return carne

if __name__ == "__main__":
    gallina = int(input("Ingrese el numero de gallinas: "))
    gallos = int(input("Ingrese el numero de gallos: "))
    pollitos = int(input("Ingrese el numero de pollitos: "))
    print(f"La cantidad de carne corresponde a {cantidad_carne(gallina,gallos,pollitos)}")