def soma_ate(n):
    if n == 1:
        return 1
    else:
        return n + soma_ate(n - 1)


resultado = soma_ate(5)
print(f"A soma acumulada é: {resultado}")
