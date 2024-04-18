def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return 0
    else:
        return 0

# Exemplo de uso:
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
op = int(input("Digite o número da operação (1-Soma, 2-Subtração, 3-Multiplicação, 4-Divisão): "))

resultado = calculadora(numero1, numero2, op)
print("Resultado:", resultado)
