global pi
pi = 3.141592653589793

# Calculo do fatorial de um número:
def fatorial(number):
    if number == 0:
        return 1
    else:
        return round(number) * fatorial(round(number) - 1)

# Calcula uma base elevada a um expoenete:
def expoente(b, e):
    return b**e

#Aproximação da função sen(x) pelo polinómio de Taylor:
def sen(rad):
    i = 0
    if rad > 0:
        while rad > pi:
            rad = rad - pi
            i = i + 1
    else:
        while rad < - pi:
            rad = rad + pi
            i = i + 1
    if i % 2 == 0:
        return round((rad - expoente(rad, 3) / fatorial(3) + expoente(rad, 5) / fatorial(5) - expoente(rad, 7) / fatorial(7) + expoente(rad, 9) / fatorial(9) - expoente(rad,11) / fatorial(11) + expoente(rad,13) / fatorial(13) - expoente(rad,15) / fatorial(15)) + expoente(rad,17) / fatorial(17) - expoente(rad,19) / fatorial(19) + expoente(rad,21) / fatorial(21),7)
    else:
        return round((-(rad - expoente(rad, 3) / fatorial(3) + expoente(rad, 5) / fatorial(5) - expoente(rad,7) / fatorial(7) + expoente(rad, 9) / fatorial(9) - expoente(rad,11) / fatorial(11) + expoente(rad,13) / fatorial(13) - expoente(rad,15) / fatorial(15)) + expoente(rad,17) / fatorial(17) - expoente(rad,19) / fatorial(19) + expoente(rad,21) / fatorial(21)),7)


#Aproximação da função cos(x) pelo polinómio de Taylor:
def cos(rad):
    i = 0
    if rad > 0:
        while rad > pi:
            rad = rad - pi
            i = i + 1
    else:
        while rad < - pi:
            rad = rad + pi
            i = i + 1
    if i % 2 == 0:
        return round((1 - expoente(rad,2) / 2 + expoente(rad,4) / fatorial(4) - expoente(rad,6) / fatorial(6) + expoente(rad,8) / fatorial(8) - expoente(rad,10) / fatorial(10) + expoente(rad,12) / fatorial(12) - expoente(rad,14) / fatorial(14) + expoente(rad,16) / fatorial(16) - expoente(rad,18) / fatorial(18) + expoente(rad, 20) / fatorial(20) - expoente(rad,22) / fatorial(22)),7)
    else:
        return round((-(1 - expoente(rad, 2) / 2 + expoente(rad, 4) / fatorial(4) - expoente(rad, 6) / fatorial(6) + expoente(rad, 8) / fatorial(8) - expoente(rad,10) / fatorial(10) + expoente(rad,12) / fatorial(12) - expoente(rad,14) / fatorial(14) + expoente(rad,16) / fatorial(16)) - expoente(rad,18) / fatorial(18) + expoente(rad, 20) / fatorial(20) - expoente(rad,22) / fatorial(22)), 7)


def tan(rad):
    return round((sen(rad)/cos(rad)),4)