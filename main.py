from romanos import * # así ya no es necesario poner romano.funcion. Uso el nombre de la funcion directamente
import unittest

#romano_a_entero("IIII")
print(romano_a_entero('MCMXIX'))

'''
assert romano_a_entero('I') == 1, 'I es incorrecto'
assert romano_a_entero('M') == 1000, 'M es incorrecto'
assert romano_a_entero('D') == 500, 'D es incorrecto'
assert romano_a_entero('C') == 100, 'C es incorrecto'
assert romano_a_entero('L') == 50, 'L es incorrecto'
assert romano_a_entero('X') == 10, 'X es incorrecto'
assert romano_a_entero('V') == 5, 'V es incorrecto'

print(romano_a_entero(23))
print(romano_a_entero('Z'))
'''