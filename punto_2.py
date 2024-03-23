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