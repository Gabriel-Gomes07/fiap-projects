#PEÇA A DATA, MÊS E ANO
dia = int(input('Digite a data: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

#VERIFICAR SE O MÊS É VÁLIDO
if mes >= 1 and mes <= 12:

#VERIFICAR SE O DIA É VÁLIDO
    if mes == 1:
        max_dias = 31
    elif mes == 2:
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            max_dias = 29
        else:
            max_dias = 28
    elif mes == 3:
        max_dias = 31
    elif mes == 4:
        max_dias = 30
    elif mes == 5:
        max_dias = 31
    elif mes == 6:
        max_dias = 30
    elif mes == 7:
        max_dias = 31
    elif mes == 8:
        max_dias = 31
    elif mes == 9:
        max_dias = 30
    elif mes == 10:
        max_dias = 31
    elif mes == 11:
        max_dias = 30
    elif mes == 12:
        max_dias = 31

#VERIFICAR SE O ANO É BISSEXTO
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        bissexto = "Sim"
    else:
        bissexto = "Não"

    if dia >= 1 and dia <= max_dias:
        print (f'''Data: {dia}/{mes}/{ano}
Ano bissexto: {bissexto}
Data válida!''')
    else:
        print (f'''Data: {dia}/{mes}/{ano}
Ano bissexto: {bissexto}
Data inválida: {mes} de {ano} tem apenas {max_dias}''')

#VALOR DO MÊS INVÁLIDO
else:
    print ('O mês é inválido, pois não está entre 1 e 12')