def VerificaCPF(CPFInt):

    CPF = str(CPFInt).replace(" ", "").replace("-", "")

    if (len(CPF) != 11 or CPF == "00000000000" or CPF == "11111111111" or CPF == CPF == "22222222222" or
        CPF == "33333333333" or CPF == CPF == "44444444444" or CPF == "55555555555" or CPF == "66666666666" or
        CPF == "77777777777" or CPF == "88888888888" or CPF == "99999999999"):
        print("CPF Inválido")

    else:
        Digito1 = (10*int(CPF[0])+9*int(CPF[1])+8*int(CPF[2])+7*int(CPF[3])+6*int(CPF[4])+5*int(CPF[5])+
                   4*int(CPF[6])+3*int(CPF[7])+2*int(CPF[8]))%11

        if Digito1 < 2:
            VerifiedDigit1 = 0
        else:
            VerifiedDigit1 = 11-Digito1

        Digito2 = (11*int(CPF[0])+10*int(CPF[1])+9*int(CPF[2])+8*int(CPF[3])+7*int(CPF[4])+6*int(CPF[5])+
                   5*int(CPF[6])+4*int(CPF[7])+3*int(CPF[8])+2*int(CPF[9]))%11

        if Digito2 < 2:
            VerifiedDigit2 = 0
        else:
            VerifiedDigit2 = 11 - Digito2

        if VerifiedDigit1 == int(CPF[9]) and VerifiedDigit2 == int(CPF[10]):
            print(CPF)
            print("CPF Válido")
        else:
            print("CPF Inválido")


if __name__ == "__main__":
    VerificaCPF(input("Digite o número do CPF: "))