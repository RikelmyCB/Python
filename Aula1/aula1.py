saldoInicial = 1300
saldo = 1300
extrato = []

def sacar(valor: float):
    global saldo
    if valor > saldo:
        print('Saldo insuficiente!')
    elif valor <= saldo:
        saldo -= valor
        extrato.append(f"Foi sacado R${valor} do seu saldo de {saldoInicial}. Agora você tem R${saldo}.")
    
def depositar(valor: float):
    global saldo
    if valor < 0:
        print('Não é possível depositar valores menores que 0!')
    elif valor > 0:
        saldo += valor
        extrato.append(f"Foi depositado R${valor} em cima seu saldo de {saldoInicial}. Agora você tem R${saldo}.")

sacar(valor=float(input("Insira o valor a ser sacado: ")))
depositar(valor=float(input("Insira o valor a ser depositado: ")))
print(extrato)