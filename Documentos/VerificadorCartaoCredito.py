def BandeiraCartao(cartao):
    if (cartao[0] == "3" and (cartao[1] == "4" or cartao[1] == "7")) and len(cartao) == 15:
        return "American Express"
    elif (cartao[0] == "5" and (cartao[1] == "1" or cartao[1] == "2" or cartao[1] == "3" or cartao[1] == "4" or cartao[1] == "5")) and len(cartao) == 16:
        return "Master Card"
    elif cartao[0] == "4" and (len(cartao) == 13 or len(cartao) == 16 or len(cartao) == 19):
        return "Visa"
    elif (cartao[0] == "3" and (cartao[1] == "6" or cartao[1] == "8" or cartao[1] == "9" or (cartao[1] == "0" and (cartao[2] == "0" or cartao[2] == "1" or cartao[2] == "2" or cartao[2] == "3" or cartao[2] == "4" or cartao[2] == "5" or cartao[2] == "9")))) and len(cartao) == 14:
        return "Diners Club Interational"
    else:
        return "Cartao Inválido"

def Ajuste(numero):
    dobro = numero * 2
    if dobro >= 10:
        dobroSTR = str(dobro)
        ValorAjustado = int(dobroSTR[0]) + int(dobroSTR[1])
        return ValorAjustado
    else:
        return dobro

def LuhnAlgorithm(number):
    l = len(number)
    Soma1 = 0
    Soma2 = 0
    for i in range(l - 1, -1, -2):
        Soma1 += int(number[i])
    for j in range(l - 2, -1, -2):
        Soma2 += Ajuste(int(number[j]))
    return (Soma1 + Soma2)

def ValidadorCartao(cardNumberInt):
    cardNumber = str(cardNumberInt)
    bandeira = BandeiraCartao(cardNumber)
    luhn = LuhnAlgorithm(cardNumber)
    if (bandeira == "Master Card" or bandeira == "Visa" or bandeira == "Diners Club International" or bandeira == "American Express") and luhn % 10 == 0:
        print("Número do Cartão: ", cardNumber)
        print("Bandeira: ", bandeira)
        print("Cartão Válido")
    else:
        print("Cartão Inválido")


if __name__ == '__main__':
    ValidadorCartao(input("Digite o Número do Cartão de Crédito: "))
    # 5149450324492592