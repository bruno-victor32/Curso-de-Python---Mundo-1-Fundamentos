n1 = input('Digite um valor:')
print('O tipo primitivo desse valor é', type(n1))
print('Só tem espaços?' , n1.isspace())
print('O valor digitado', n1, 'e numerico =',n1.isnumeric())
print('O valor digitado', n1, 'e letra (alfabetico) =',n1.isalpha())
print('O valor digitado', n1, 'e alfanumerico, ou seja, numeros e letras =', n1.isalnum())
print('O valor digitado', n1, 'tem todas letras maiusculas =', n1.isupper())
print('O valor digitado', n1, 'tem todas letras minusculas =', n1.islower())
print('O valor digitado', n1, 'esta capitalizado =', n1.istitle())
