# Solicita a quantidade de itens
quantidade = int(input("Quantidade de itens: "))

total = 0

# Lê o preço de cada item
for i in range(1, quantidade + 1):
    preco = float(input(f"Preço do item {i}: R$ "))
    total += preco

# Calcula a média
media = total / quantidade

# Exibe os resultados
print(f"\nTotal da compra: R$ {total:.2f}")
print(f"Média por item: R$ {media:.2f}")