from trig import fatorial

def expoenete_simples(b, e):
    if e > 0: return b * expoenete_simples(b, e - 1)
    elif e < 0: return 1/b * expoenete_simples(b, e + 1)
    else: return 1

# Exemplo:
# cientific_notation(4) -> (0, 4)
# cientific_notation(0.006) -> (-2, 6.0)
# cientific_notation(902) -> (2, 9.02)
# Defenição geral:
# cientific_notation(x) -> (a, b) <==> b * 10^a == x
def cientific_notation(number):
    elevado = 0
    while number >= 10:
        elevado += 1
        number = number / 10
    while number < 1:
        elevado -= 1
        number = number * 10
    return (elevado, number)

# Return the ln(x)/2:
# x -> ln of the number you want calculate
# q -> degree of precision
# Quanto maior for o q (degree of precision), mais preciso é o resultado. O valor máximo é de 79, apatir desse
# valor de precição não faz qualquer diferença no resultado
def LN(x, q):
    if q == 1: return (x-1)/(x+1)
    else: return (expoenete_simples( ((x-1)/(x+1)) , 2*q - 1))/(2*q - 1) + LN(x, q - 1)

# Return the ln(x):
# Arredonda o valor na 9 casa decimal:
def ln(x):
    elevado, x = cientific_notation(x)
    return 2 * LN(x, 50) + elevado * 2 * LN(10, 50)

# Arredonda o valor na 7 casa decimal:
def log(base, number): return round(ln(number)/ln(base), 7)

def e(x, q):
    if q >= 0: return expoenete_simples(2.718281828459045, int(x)) * (expoenete_simples(int(x) - x, q)/fatorial(q) + e(int(x) - x, q - 1))
    else: return 0