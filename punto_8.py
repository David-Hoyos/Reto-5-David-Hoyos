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


