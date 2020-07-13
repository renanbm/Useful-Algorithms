import random

def GeraCPF():
    CPF = []

    while True:
        for _ in range(9):
            CPF.append(random.randrange(1, 9))
        if (len(CPF) == 9 and
            CPF != [0,0,0,0,0,0,0,0,0] and
            CPF != [1,1,1,1,1,1,1,1,1] and
            CPF != [2,2,2,2,2,2,2,2,2] and
            CPF != [3,3,3,3,3,3,3,3,3] and
            CPF != [4,4,4,4,4,4,4,4,4] and
            CPF != [5,5,5,5,5,5,5,5,5] and
            CPF != [6,6,6,6,6,6,6,6,6] and
            CPF != [7,7,7,7,7,7,7,7,7] and
            CPF != [8,8,8,8,8,8,8,8,8] and
            CPF != [9,9,9,9,9,9,9,9,9]):
            break
        else:
            CPF = []

    Digito1 = (10*CPF[0]+9*CPF[1]+8*CPF[2]+7*CPF[3]+6*CPF[4]+5*CPF[5]+4*CPF[6]+3*CPF[7]+2*CPF[8])%11

    if Digito1 < 2:
        CPF.append(0)
    else:
        CPF.append(11-Digito1)

    Digito2 = (11*CPF[0]+10*CPF[1]+9*CPF[2]+8*CPF[3]+7*CPF[4]+6*CPF[5]+5*CPF[6]+4*CPF[7]+3*CPF[8]+2*CPF[9])%11

    if Digito2 < 2:
        CPF.append(0)
    else:
        CPF.append(11 - Digito2)

    # Formata o CPF na forma "XXXXXXXXX-XX":
    CPFStr = str(CPF[0]) + str(CPF[1]) + str(CPF[2]) + str(CPF[3]) + str(CPF[4]) + str(CPF[5]) + str(CPF[6]) + str(CPF[7]) + str(CPF[8]) + '-' + str(CPF[9]) + str(CPF[10])

    return (CPFStr)

if __name__ == "__main__":
    print(GeraCPF())