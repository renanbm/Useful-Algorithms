import random
import time

def Ajuste(numero):
    dobro = numero * 2
    if dobro >= 10:
        dobroSTR = str(dobro)
        ValorAjustado = int(dobroSTR[0]) + int(dobroSTR[1])
        return ValorAjustado
    else:
        return dobro

def ConvertListToString(List):
    ListSTR = ""
    for i in range(len(List)):
        ListSTR += str(List[i])
    return ListSTR

def GeradorSantander():
    Agencia = []
    for _ in range (4):
        Agencia.append(str(random.randrange(0, 10)))

    TiposCC = ['01', '02', '03', '05', '07', '09', '13', '27', '35', '37', '43', '45', '46', '48', '50', '53', '60', '92']  # Tipos de CC do Santander
    CC = []
    CC.append(TiposCC[random.randrange(len(TiposCC))]) # Sorteia um tipo de CC (Dois primeiros dígitos da C.C)

    for _ in range(6):
        CC.append(str(random.randrange(0,10)))

    ContaCompleta = ConvertListToString(Agencia) + ConvertListToString(CC)

    Pesos = [9, 7, 3, 1, 9, 7, 1, 3, 1, 9, 7, 3]
    Soma = 0
    for i in range(len(Pesos)):
        Soma += Pesos[i]*int(ContaCompleta[i])

    Resto = Soma%10
    if Resto == 0:
        DV = 0
    else:
        DV = 10-Resto

    print("Banco Santander")
    print("Agência: ", ConvertListToString(Agencia))
    print("Conta: ", ConvertListToString(CC) + "-" + str(DV))

def GeradorItau():
    # Gerando 4 Números Aleatórios para a Agência
    Agencia = ""
    for _ in range(4):
        Agencia += str(random.randrange(0,10))

    # Gerando 5 Números Aleatórios para a Conta
    Conta = ""
    for _ in range(5):
        Conta += str(random.randrange(0,10))

    ContaCompleta = Agencia + Conta
    S1 = 0
    S2 = 0

    for i in range(0, 9, 2):
        S1 += Ajuste(int(ContaCompleta[i]))
    for j in range(1, 8, 2):
        S2 += int(ContaCompleta[j])

    Resto = (S1+S2)%10
    if Resto == 0:
        DV = 0
    else:
        DV = 10-Resto

    print("Banco Itaú")
    print("Agência: ", Agencia)
    print("Conta: ", Conta + "-" + str(DV))

def GeradorGenerico():
    dict = {1: GeradorSantander, 2: GeradorItau, 3: GeradorItau, 4: GeradorItau, 5: GeradorSantander}

    print("\n")
    print("Menu:")
    print("-----")
    print("1. Gerar conta do Banco Santander")
    print("2. Gerar conta do Banco Itaú")
    print("3. Gerar conta do Banco Bradesco")
    print("4. Gerar conta do Banco do Brasil")
    print("5. Gerar conta da Caixa Econômica Federal\n")

    try:
        op = int(input("Entre com a opção desejada: "))
        dict[op]()
    except KeyError:
        print("Valor Inválido")
        time.sleep(3)
        GeradorGenerico()
GeradorGenerico()