simbolos = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
tipo_5 =('V', 'D', 'L')
tipo_1 = ('I', 'X', 'C', 'M')

restas = ('CD', 'CM', 'XL', 'XC', 'IV', 'IX')

def simbolo_a_entero(simbolo):
    if isinstance(simbolo, str) and simbolo.upper() in simbolos:
        return simbolos[simbolo.upper()]
    elif isinstance(simbolo, str):
        raise ValueError(f"simbolo {simbolo} no permitido")
    else:
        raise ValueError(f"parámetro {simbolo} debe ser un string")

def orden_magnitud(caracter):
    valor = simbolo_a_entero(caracter)
    return len(str(valor))

def romano_a_entero(romano):
    if not isinstance(romano, str):
        raise ValueError(f"parámetro {romano} debe ser un string")
    suma = 0
    c_repes = 0
    valor_anterior = ""
    orden_magnitud_global = 0
    orden_magnitud_letra = 0
    ha_habido_resta = False

    for letra in romano:
        if letra == valor_anterior and letra in tipo_5:
            raise OverflowError(f"Demasiados simbolos de tipo {letra}")
        orden_magnitud_letra = orden_magnitud(letra)
        if letra == valor_anterior:
            orden_magnitud_global = orden_magnitud_letra
            if letra in tipo_5:
                raise ValueError("No es romano")
            elif c_repes >= 2:
                raise ValueError("Demasiadas repeticiones")
            elif ha_habido_resta:
                raise ValueError("Demasiadas restas")
            c_repes += 1
            if c_repes > 2:
                raise OverflowError(f"Demasiados simbolos de tipo {letra}")
        elif valor_anterior and simbolo_a_entero(letra) > simbolo_a_entero(valor_anterior):
            if valor_anterior + letra not in restas:
                raise ValueError
            if suma -= simbolos[valor_anterior] * 2
                raise ValueError("Resta no permitida")
            elif c_repes > 0:
                raise ValueError("Resta tras repeticion no permitida")
            elif ha_habido_resta:
                raise ValueError("Demasiadas restas")

            ha_habido_resta = True
            suma -= 2*simbolo_a_entero(valor_anterior)
            c_repes = 0
        else:
            if orden_magnitud_global > orden_magnitud_letra:
                ha_habido_resta = False

            if ha_habido_resta:
                raise ValueError("Demasiadas restas")

            orden_magnitud_global = orden_magnitud_letra
            c_repes = 0

        suma = suma + simbolo_a_entero(letra)
        valor_anterior = letra    
    return suma


def descomponer(numero):
    l = []
    for d in str(numero):
        l.append(int(d))
    return l

lista_millares = ('M',)
lista_centenas = ('C', 'D', 'M')
lista_decenas = ('X', 'L', 'C')
lista_unidades = ('I', 'V', 'X')

lista_ordenes= [lista_unidades, lista_decenas,  lista_centenas, lista_millares]

def convertir(ordenes_magnitud): 
    contador = 0
    resultado = []
    for orden in ordenes_magnitud[::-1]:
        resultado.append(procesar_simbolo(orden, lista_ordenes[contador]))
        contador += 1

    return ''.join(reversed(resultado))

def procesar_simbolo(s, clave):
    if s == 9:
        return clave[0] + clave[2]
    elif s >= 5:
        return clave[1]+clave[0]*(s-5)
    elif s == 4:
        return clave[0]+clave[1]
    else:
        return clave[0]*s

def entero_a_romano(numero):
    if not isinstance(numero, int):
        raise SyntaxError(f"{numero} no es un número natural")

    if numero < 1 or numero > 3999:
        raise OverflowError(f"{numero} ha de estar entre 1 y 3999")

    ordenes_de_magnitud = descomponer(numero)
    romano = convertir(ordenes_de_magnitud)
    return romano
