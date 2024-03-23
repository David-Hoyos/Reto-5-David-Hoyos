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

if __name__ =="__main__":
    r1 = float(input("Ingresa el radio del circulo: "))
    r2 = float(input("Ingresa el radio del cono: "))
    h = float(input("Ingresa la altura del cono:"))
    print("El area corresponde a: " + str(area(r1,r2,h)))
    print("El volumen corresponde a: " + str(volumen(r1,r2,h)))