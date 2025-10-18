# calculadora.py
# Projeto acadêmico: Calculadora simples em Python

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero não permitida."

print("=== Calculadora Simples ===")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")

opcao = input("Escolha uma opção: ")

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if opcao == "1":
    print(f"Resultado: {somar(a, b)}")
elif opcao == "2":
    print(f"Resultado: {subtrair(a, b)}")
elif opcao == "3":
    print(f"Resultado: {multiplicar(a, b)}")
elif opcao == "4":
    print(f"Resultado: {dividir(a, b)}")
else:
    print("Opção inválida.")