#Calculadora em Python
print("\n ************************* Python Calculator *************************** ")

def adicao(x,y):
    return x + y

def subtracao(x,y):
    return  x - y

def multiplicacao(x,y):
    return  x * y

def divisao(x,y):
    return x / y

print("\n Selecione o Número da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("\n Digite sua opção (1/2/3/4): ")

num1 = int(input("\n Digite o primeiro número: "))
num2 = int(input("\n Digite o segundo número: "))

if escolha == '1':
    print("\n")
    print(num1, "+" , num2, " = ", adicao(num1,num2))
    print("\n")

elif escolha == '2':
    print("\n")
    print(num1, "-", num2, " = ", subtracao(num1 , num2))
    print("\n")

elif escolha == '3':
    print("\n")
    print(num1, "*", num2, " = ", multiplicacao(num1 , num2))
    print("\n")

elif escolha == '4':
    print("\n")
    print(num1, "/", num2, " = ", divisao(num1 , num2))
    print("\n")
else:
    print("\n Opção Inválida")








































