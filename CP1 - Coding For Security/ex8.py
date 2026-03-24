testes = [
    {"entrada": 14, "saida": 16, "placa_final": 3, "dia": "quarta"},
    {"entrada": 9,  "saida": 9,  "placa_final": 7, "dia": "sexta"},
    {"entrada": 23, "saida": 2,  "placa_final": 5, "dia": "sabado"},
    {"entrada": 8,  "saida": 12, "placa_final": 4, "dia": "segunda"},
    {"entrada": 20, "saida": 3,  "placa_final": 2, "dia": "segunda"},
]

for t in testes:
    entrada = t["entrada"]
    saida = t["saida"]
    placa_final = t["placa_final"]
    dia = t["dia"]

    horas = saida - entrada if saida > entrada else (24 - entrada) + saida
    horas = max(horas, 1)

    tarifa_base = 10 + max(horas - 1, 0) * 5

    noturno = entrada >= 22 or entrada < 6 or saida > 22 or saida <= 6
    adicional_noturno = tarifa_base * 0.5 if noturno else 0

    total = tarifa_base + adicional_noturno

    desconto_segunda = dia == "segunda" and placa_final % 2 == 0
    desconto_valor = total * 0.10 if desconto_segunda else 0

    total -= desconto_valor

    print(f"=== Estacionamento ===")
    print(f"Entrada: {entrada:02d}h | Saída: {saida:02d}h")
    print(f"Permanência: {horas} hora(s)")
    print(f"Tarifa base:              R$ {tarifa_base:.2f}")

    if noturno:
        print(f"Adicional noturno (50%):  R$ {adicional_noturno:.2f}")
    if desconto_segunda:
        print(f"Desconto segunda/par(10%): -R$ {desconto_valor:.2f}")

    print(f"Total:                    R$ {total:.2f}")