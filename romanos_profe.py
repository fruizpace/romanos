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

def romano_a_entero(romano):
    if not isinstance(romano, str):
        raise ValueError(f"parámetro {romano} debe ser un string")
    suma = 0
    c_repes = 0
    valor_anterior = ""
    for letra in romano:
        if romano.count(letra) >= 4:
            raise OverflowError(f"Demasiados simbolos de tipo {letra}")
        if letra == valor_anterior and letra in tipo_5:
            raise OverflowError(f"Demasiados simbolos de tipo {letra}")
        if letra == valor_anterior:
            c_repes += 1
            if c_repes > 2:
                raise OverflowError(f"Demasiados simbolos de tipo {letra}")
        elif valor_anterior and simbolo_a_entero(letra) > simbolo_a_entero(valor_anterior): # SI NO ESTAMOS EN UNA REPETICIÓN...
            if valor_anterior + letra not in restas:
                raise ValueError
            elif c_repes >= 1:
                raise OverflowError
            suma -= simbolos[valor_anterior] * 2
            c_repes = 0
        else:
            c_repes = 0

        suma = suma + simbolo_a_entero(letra)
        valor_anterior = letra    
    return suma