simbolos = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X' : 10, 'V': 5, 'I': 1}

def simbolo_a_entero(simbolo):
    if isinstance(simbolo, str) and simbolo.upper() in simbolos: # así compruebo si romano es string y mayúscula está en el diccionario símbolos 
        return simbolos[simbolo.upper()]
    elif isinstance(simbolo, str):
        raise ValueError(f"simbolo {simbolo} no permitido") 
    else:
        raise ValueError(f"parámetro {simbolo} debe ser un string") # raise: lanza una excepción

def cuentaSimbolos(romano):
    frecuencias = dict() # diccionario vacio
    for caracter in romano:
        if caracter in frecuencias: # si el caracter está en el diccionario
            frecuencias[caracter] += 1 # suma uno
        else: # si no está
            frecuencias[caracter] = 1
    return frecuencias # diccionario con la frecuencia de los simbolos

def romano_a_entero(romano):
    tipo1 = ['I', 'X', 'C', 'M']
    tipo5 = ['V', 'L', 'D']
    listaTemp = []
    acumulador = 0
    
    if not isinstance(romano, str): # si metemos un número dará error
        raise ValueError(f"parámetro {romano} debe ser un string")
    
    for simbolo in romano:
        entero = simbolo_a_entero(simbolo) # da su valor arábigo
        listaTemp.append(entero) # lista validada de valores arábigos
    
    if len(listaTemp)>1:  # comprobación de tipos de resta
        for i in range(1, len(listaTemp)):
            if listaTemp[i-1] < listaTemp[i] and listaTemp[i-1] in (5, 50, 500): 
                raise OverflowError(f"Hay un valor {listaTemp[i-1]} (tipo 5) a la izquierda de uno mayor")      
            elif listaTemp[i-1] < listaTemp[i] and listaTemp[i-2] == listaTemp[i-1] and listaTemp[i-1] in (1, 10, 100, 1000):
                raise OverflowError(f"Hay un valor {listaTemp[i-1]} (tipo 1) restando y repetido a la izquierda")  
        
        for i in range(1, len(listaTemp)):
            if listaTemp[i-1] < listaTemp[i] and not ((listaTemp[i-1] == 1 and listaTemp[i] in (10, 5)) or (listaTemp[i-1] == 10 and listaTemp[i] in (100, 50)) or  (listaTemp[i-1] == 100 and listaTemp[i] in (1000, 500))):
                raise OverflowError(f"Hay una resta no aceptada") 
            elif  listaTemp[i-1] < listaTemp[i] and  (listaTemp[i-1] == 1 and listaTemp[i] in (10, 5)) or (listaTemp[i-1] == 10 and listaTemp[i] in (100, 50)) or (listaTemp[i-1] == 100 and listaTemp[i] in (1000, 500)):
                listaTemp[i-1] = listaTemp[i-1] * -1

    frecuenciaSimbolos = cuentaSimbolos(romano) # diccionario con frecuencia de símbolos
    
    for i in frecuenciaSimbolos: # comprobamos repeticiones de símbolos
        if i in tipo5 and frecuenciaSimbolos[i] >= 2:
            raise OverflowError(f"Más de dos símbolos tipo 5")
        elif i in tipo1 and frecuenciaSimbolos[i] > 3:
            raise OverflowError(f"Más de tres símbolos tipo 10")
        
    for i in range(len(listaTemp)): # Suma (y resta) los valores validados 
        acumulador += listaTemp[i]

    return acumulador



def descomponer(numero):
    if not isinstance(numero, int):
        raise SyntaxError(f"{numero} no es un número natural")
    l = []
    for d in str(numero):
        l.append(int(d))
    return l

#return [int(d) for d in str(numero)] # es lo mismo que arriba

unidades = ('I','V', 'X')
decenas = ('X','L', 'C')
centenas = ('C','D', 'M')
millares = ('M',) # tupla con esa coma

lista_ordenes = [unidades, decenas, centenas, millares]

def convertir(ordenes_magnitud):
    resultado = []
    contador = 0
    for orden in ordenes_magnitud[::-1]:
        resultado.append(procesar_simbolo(orden, lista_ordenes[contador]))
        contador += 1
    
    #resultado.reverse() # esta función no devuelve nada así que hay que cogerla con join.
    return ''.join(reversed(resultado))



def procesar_simbolo(s, clave):
    if s== 9:
        return clave[0] + clave[2]
    elif s >= 5:
        return clave[1] + clave[0]*(s-5)
    elif s == 4:
        return clave[0] + clave[1]
    else:
        return clave[0]*s

print(descomponer(1983))
print(convertir([1, 9, 8, 3]))