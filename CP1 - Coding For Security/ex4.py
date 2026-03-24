#PEDIR OS VALORES AO USUÁRIO
a = float(input('Escreva o primeiro valor: '))
b = float(input('Escreva o segundo valor: '))
c = float(input('Escreva o terceiro valor: '))

#VERIFICAR SE É VALIDO E CLASSIFICAR
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print ('É um equilátero')
    elif a == b or b == c or c == a:
        print ('É um isósceles')
    else:
        print ('É um escaleno')
else:
    print('Não forma triângulo')