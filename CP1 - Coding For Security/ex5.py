#CAPTURAR OS DOIS VALORES DO USUÁRIO
valor_compra = float(input('Digite o valor da compra: '))
vip = input('Você é VIP? (Sim ou Não): ').lower()

#CONDIÇÕES
if valor_compra <= 100:
    desconto = 0
    percentual = "0%"

elif valor_compra > 100 and valor_compra <= 300:
    desconto = valor_compra * 0.10
    percentual = "10%"

elif valor_compra > 300 and valor_compra <= 500:
    desconto = valor_compra * 0.15
    percentual = "15%"

else:
    desconto = valor_compra * 0.20
    percentual = "20%"

#VERIFICAR SE É VIP
if vip == "sim":
    desconto_vip = (valor_compra * 0.05)

else:
    desconto_vip = 0

#EXIBIR O VALOR FINAL
valor_final = valor_compra - desconto - desconto_vip

if vip == "sim":
    print (f'''=== Resumo da Compra ===
Valor original:  R$ {valor_compra:.2f}
Desconto ({percentual}):  R$ {desconto:.2f}
Desconto VIP (5%): R$ {desconto_vip:.2f}
Valor final:     R$ {valor_final:.2f}''')
else:
    print (f'''=== Resumo da Compra ===
Valor original:  R$ {valor_compra:.2f}
Desconto ({percentual}):  R$ {desconto:.2f}
Valor final:     R$ {valor_final:.2f}''')
