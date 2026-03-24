#PEÇA O PESO E A ALTURA
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = round (peso / altura ** 2, 1)

#EXIBA A CLASSIFICAÇÃO
if imc < 18.5:
    print (f'''Peso: {peso} | Altura: {altura}
Seu IMC é:{imc} - Abaixo do peso''')

elif imc >= 18.5 and imc <= 24.9:
    print (f'''Peso: {peso} | Altura: {altura}
Seu IMC é:{imc} - Peso normal''')

elif imc >= 25.0 and imc <= 29.9:
    print (f'''Peso: {peso} | Altura: {altura}
Seu IMC é:{imc} - Sobrepeso''')

elif imc >= 30.0:
    print (f'''Peso: {peso} | Altura: {altura}
Seu IMC é: {imc} - Obesidade''')
