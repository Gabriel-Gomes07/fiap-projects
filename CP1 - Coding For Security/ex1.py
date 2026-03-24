#PEÇA A IDADE DO USUÁRIO
idade = int(input('Digite sua idade: '))

#EXIBA A RESPOSTA
if (idade >= 0 and idade <= 11 ):
    print ('Você é uma criança')

elif (idade >= 12 and idade <= 17):
    print ('Você é um adolescente')

elif (idade >= 18 and idade <= 59):
    print ('Você é um adulto')

elif (idade >= 60 and idade <= 120):
    print ('Você é um idoso')

else:
    print ('Idade inválida')