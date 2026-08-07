# Valor total do produto
valor_total = 1200.00

print("====================================")
print(f"TABELA DE PARCELAMENTO - COMPRA R$ {valor_total:.2f}")
print("====================================")

# Laço para calcular de 1 até 10 parcelas
for parcelas in range(1, 11):
    valor_parcela = valor_total / parcelas
    print(f"{parcelas}x de R$ {valor_parcela:.2f}")

print("====================================")