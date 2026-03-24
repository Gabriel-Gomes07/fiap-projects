cedulas = [200, 100, 50, 20, 10]
testes = [380, 1250, 70, 15, -100, 0]

for valor in testes:
    if valor <= 0 or valor % 10 != 0:
        print(f"Valor R$ {valor} é inválido! Precisa ser positivo e múltiplo de 10.\n")
        continue

    print(f"=== Saque: R$ {valor} ===")
    restante = valor
    total_cedulas = 0

    for cedula in cedulas:
        quantidade = restante // cedula

        if quantidade > 0:
            print(f"  R$ {cedula:>3}: {quantidade} cédula(s)")

        total_cedulas += quantidade
        restante -= quantidade * cedula

    print(f'  Total de cédulas: {total_cedulas}')