#VARIAVEIS
cotacoes = {
    "dolar": 5.15,
    "euro": 5.55,
    "libra": 6.45
}

#EXIBA O MENU
print ('''[1] Real -> Dólar
[2] Real -> Euro
[3] Real -> Libra''')


#OPÇÃO DO USUÁRIO
opcao = (input('Digite o número da opção que você deseja escolher: '))

#OPÇÃO ESCOLHIDA - 1
if opcao == '1':
    real_para_dolar = float(input('Digite o valor em reais: '))
    if real_para_dolar < 0:
        print ('Valor inválido')
    else:
        resultadord = real_para_dolar / cotacoes["dolar"]
        print (f'R$ {real_para_dolar:.2f} = US$ {resultadord:.2f}')

#OPÇÃO ESCOLHIDA - 2
elif opcao == '2':
    real_para_euro = float(input('Digite o valor em reais: '))
    if real_para_euro < 0:
        print ('Valor inválido')
    else:
        resultadore = real_para_euro / cotacoes["euro"]
        print (f'R$ {real_para_euro:.2f} = € {resultadore:.2f}')

#OPÇÃO ESCOLHIDA - 3
elif opcao == '3':
    real_para_libra = float(input('Digite o valor em reais: '))
    if real_para_libra < 0:
        print ('Valor inválido')
    else:
        resultadorl = real_para_libra / cotacoes["libra"]
        print (f'R$ {real_para_libra:.2f} = £ {resultadorl:.2f}')

else:
    print ('Opção inválida')

