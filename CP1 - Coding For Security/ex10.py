faixas_inss = [
    (1518.00, 0.075),
    (2793.88, 0.09),
    (4190.83, 0.12),
    (8157.41, 0.14),
]

faixas_ir = [
    (2259.20, 0.00),
    (2826.65, 0.075),
    (3751.05, 0.15),
    (4664.68, 0.225),
    (float("inf"), 0.275),
]

def calcular_faixas(valor, faixas):
    parcelas = []
    anterior = 0
    for teto, aliquota in faixas:
        if valor <= anterior:
            parcelas.append(0.0)
        else:
            trecho = min(valor, teto) - anterior
            parcelas.append(trecho * aliquota)
        anterior = teto
    return parcelas

def r(v):
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

testes = [
    {"salario": 2000.00, "dependentes": 0, "pensao": 0,   "idoso": False},
    {"salario": 5000.00, "dependentes": 2, "pensao": 0,   "idoso": False},
    {"salario": 8000.00, "dependentes": 1, "pensao": 500, "idoso": False},
    {"salario": 3500.00, "dependentes": 0, "pensao": 0,   "idoso": True},
]

for t in testes:
    salario     = t["salario"]
    dependentes = t["dependentes"]
    pensao      = t["pensao"]
    idoso       = t["idoso"]

    pi = calcular_faixas(salario, faixas_inss)
    total_inss = sum(pi)

    deducao_dep   = dependentes * 189.59
    deducao_idoso = 1903.98 if idoso else 0.0
    base_ir       = max(salario - total_inss - deducao_dep - pensao - deducao_idoso, 0)

    pr = calcular_faixas(base_ir, faixas_ir)
    total_ir = sum(pr)

    liquido = salario - total_inss - total_ir

    print("====================================")
    print("CONTRACHEQUE — Cálculo de IR Mensal")
    print("====================================")
    print(f"Salário bruto:       {r(salario)}\n")
    print(f"(-) INSS:            {r(total_inss)}")
    print(f"    Faixa 7.5%:      {r(pi[0])}")
    print(f"    Faixa 9%:        {r(pi[1])}")
    print(f"    Faixa 12%:       {r(pi[2])}")
    print(f"    Faixa 14%:       {r(pi[3])}\n")
    print(f"(-) Dependentes ({dependentes}): {r(deducao_dep)}")
    print(f"(-) Pensão:          {r(pensao)}")
    print(f"(-) Isenção 65+:     {r(deducao_idoso)}\n")
    print(f"Base de cálculo IR:  {r(base_ir)}\n")
    print(f"(-) IR:              {r(total_ir)}")
    print(f"    Faixa isenta:    {r(pr[0])}")
    print(f"    Faixa 7.5%:      {r(pr[1])}")
    print(f"    Faixa 15%:       {r(pr[2])}")
    print(f"    Faixa 22.5%:     {r(pr[3])}")
    print(f"    Faixa 27.5%:     {r(pr[4])}\n")
    print("====================================")
    print(f"Salário líquido:     {r(liquido)}")
    print("====================================\n")