# Calculadora em Python

print("\n******************* Python Calculator *******************")

# Funções das operações
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

# Impressão das opções de operações para o usuário escolher
print("\nSelecione o número da operação desejada: \n")
print("\n1 - Soma")
print("\n2 - Subtração")
print("\n3 - Multiplicação")
print("\n4 - Divisão")

# Variável que vai gravar a escolha da operação do usuário
escolha = input("\nDigite sua opção (1/2/3/4): ")

# Variáveis que vão gravar os valores que o usuário digitar para fazer a operação desejada
num1 = int(input("\nDigite o primeiro número: "))
num2 = int(input("\nDigite o segundo número: "))

# Condicionais para realizar a operação
if escolha == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))
    print("\n")

elif escolha == '2':
    print("\n")
    print(num1, "-", num2, "=", subtract(num1, num2))
    print("\n")

elif escolha == '3':
    print("\n")
    print(num1, "*", num2, "=", multiply(num1, num2))
    print("\n")

elif escolha == '4':
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2))
    print("\n")

else:
    print("\nOpção Inválida")