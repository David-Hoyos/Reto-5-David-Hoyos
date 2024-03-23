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