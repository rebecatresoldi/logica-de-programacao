# Variáveis para armazenar os resultados
consumo_total = 0
dias_acima_20 = 0

# Laço para os 7 dias da semana
for dia in range(1, 8):
    consumo = float(input(f"Informe o consumo do dia {dia} (kWh): "))

    consumo_total += consumo

    if consumo > 20:
        dias_acima_20 += 1

# Exibição dos resultados
print("\n===== RELATÓRIO SEMANAL =====")
print(f"Consumo total da semana: {consumo_total:.2f} kWh")
print(f"Dias com consumo acima de 20 kWh: {dias_acima_20}")