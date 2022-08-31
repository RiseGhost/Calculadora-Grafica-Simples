import sys
from trig import *

#Return element index in the list. If element don't exist return a negative value:
def list_element_index(list, element):
    if list == []: return -999999
    else:
        if list[0] == element: return 0
        else: return 1 + list_element_index(list[1::], element)

#Retorna uma lista que contém todos os elementos das duas listas ordenados:
def list_add(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    if len1 == 0 and len2 > 0: return list2
    elif len2 == 0 and len1 > 0: return list1
    elif len1 == 0 and len2 == 0: return []
    elif len1 >= len2:
        for i in range(len2):
            if list_element_index(list1, list2[i]) < 0: list1.append(list2[i])
        return sorted(list1)
    else:
        for i in range(len1):
            if list_element_index(list2, list1[i]) < 0: list2.append(list1[i])
        return sorted(list2 )

#Return element number on string:
def str_element_number(string, element):
    if string == "": return 0
    else:
        if string[0] == element: return 1 + str_element_number(string[1::], element)
        else: return 0 + str_element_number(string[1::], element)

#Checks if a string is a number:
def str_isnumber(string):
    if string == "" or str_element_number(string, ".") > 1 or str_element_number(string, "-") > 1 or string.find("-") > 0 or ( (sys.getsizeof(string) - 49) == 1 and (string[0] < '0' or string[0] > '9') and string[0] != "x" ) or (string.find('x') != -1 and (sys.getsizeof(string) - 49) != 1):
        return False
    else:
        for i in range(sys.getsizeof(string) - 49):
            if (string[i] < '0' or string[i] > '9') and string[i] != "." and string[i] != '-' and string[i] != "x":
                return False
        return True

#Replace pi per 3.141592653589793
def str_pi(string):
    if string.find("pi") >= 0:
        return str_pi(string[0:string.find("pi")] + str(pi) + string[string.find("pi")+2:])
    else: return string

#Checks if parentheses are well placed:
def str_validate_parentheses(string):
    if str_element_number(string, "(") == str_element_number(string, ")"):
        aux = 0
        for i in range(sys.getsizeof(string) - 49):
            if string[i] == '(': aux = aux + 1
            if string[i] == ')': aux = aux - 1
            if aux < 0: return False
        return True
    else:
        return False

#Return the func index in the string:
def str_func_index(string, func):
    index = []
    if string.find(func) >= 0:
        aux = string[string.find(func)::]
        aux1 = 0
        if func != "|":
            for i in range(0, sys.getsizeof(aux) - 49):
                if aux[i] == "(": aux1 = aux1 + 1
                if aux1 >= 0: index.append(i + string.find(func))
                if aux[i] == ")" and aux1 == 1: aux1 = -1
                elif aux[i] == ")": aux1 = aux1 - 1
        else:
            if aux[0] == "|":
                index.append(string.find(func))
                i = string.find(func) + 1
                while i < sys.getsizeof(aux) - 49 and aux[i] != "|":
                    index.append(i)
                    i = i + 1
                index.append(i)
        return index
    else: return index

#Return the all func index in the string
def str_all_func_index(string):
    index1 = []
    index2 = []
    index1 = str_func_index(string, "sen(")
    index2 = str_func_index(string, "cos(")
    index1 = list_add(index1, index2)
    index2 = str_func_index(string, "tan(")
    index1 = list_add(index1, index2)
    index2 = str_func_index(string, "(")
    index1 = list_add(index1, index2)
    index2 = str_func_index(string, "|")
    index1 = list_add(index1, index2)
    index2 = str_func_index(string, "ln(")
    index1 = list_add(index1, index2)
    index2 = str_func_index(string, "log(")
    return list_add(index1, index2)

#Retorna uma lista com todas as posições da string que têm sinais de operações de +, -, *, /, !, ^
def str_sinais_index(string):
    index = []
    if string == "": return []
    else:
        for i in range(0, (sys.getsizeof(string) - 49)):
            if string[i] == "-" or string[i] == "+" or string[i] == "*" or string[i] == "/" or string[i] == "!" or string[i] == "^":
                index.append(i)
        return index

#Retorna uma string sem a notação ciêntica:
def str_remove_scientific_notacion(string): return '{:f}'.format(float(string))

#Retorna o index dos sinais.
#Retorna o primeiro index que encontrar de + ou - se não existir + ou - retorna o index de *, / ou ^
#Se não existir *, / nem ^ ela procura por fatorial "!"
#Se mesmo assim não existir retorna -1
def str_sinais(string):
    index = str_all_func_index(string)
    for i in range(sys.getsizeof(string) - 50, -1, -1):
        if list_element_index(index, i) < 0 and (string[i] == "-" or string[i] == "+"): return i
    for i in range(sys.getsizeof(string) - 50, -1, -1):
        if list_element_index(index, i) < 0 and (string[i] == "*" or string[i] == "/" or string[i] == "^"): return i
    for i in range(sys.getsizeof(string) - 50, -1, -1):
        if list_element_index(index, i) < 0 and string[i] == "!": return i
    return -1

#Retorna o tipo da string
def str_type(string):
    if string != "":
        if str_isnumber(string): return ("numeric", sys.getsizeof(string) - 49)
        elif len(str_all_func_index(string)) == (sys.getsizeof(string) - 49):
            if string[0] == "(" and string[sys.getsizeof(string) - 50] == ")":
                return ("parentheses", sys.getsizeof(string) - 51)
            elif len(str_func_index(string, "|")) == sys.getsizeof(string) - 49:
                return ("||", sys.getsizeof(string) - 51)
            elif len(str_func_index(string, "sen(")) > 0:
                return ("sen()", sys.getsizeof(string) - 54)
            elif len(str_func_index(string, "cos(")) > 0:
                return ("cos()", sys.getsizeof(string) - 54)
            elif len(str_func_index(string, "tan(")) > 0:
                return ("tan()", sys.getsizeof(string) - 54)
            elif len(str_func_index(string, "ln(")) > 0:
                return ("ln()", sys.getsizeof(string) - 53)
            elif len(str_func_index(string, "log(")) > 0:
                return ("log()", sys.getsizeof(string) - 54)
        elif (sys.getsizeof(string) - 49) == 1 and (string[0] == "+" or string[0] == "-" or string[0] == "*" or string[0] == "/"):
            return (string[0], 1)
        else: return ("complex", sys.getsizeof(string) - 49)

#Função responsável por dividir a string, ela retorna três valores:
#element -> sinal ou função
#left -> parte que esta a esquedra do element
#rigth -> parte a direita do element
#(element, left, rigth)
#Exemplo
#str_div("5!-3") -> ("-", "5!", "3")
#str_div("5!") -> ("!", "8", "")
#str_div("sen(9/5)") -> ("sen()", "9/5", "")
#str_div("sen(9/5)/2") -> ("/", "sen(9/5)", "2")
def str_div(string):
    index = str_all_func_index(string)
    sinais = str_sinais(string)
    typeSTR, l = str_type(string)
    if typeSTR == "numeric": return (string, "", "")
    elif typeSTR == "parentheses": return ("()", string[1:sys.getsizeof(string) - 50], "")
    elif typeSTR == "||": return ("||", string[1:sys.getsizeof(string) - 50], "")
    elif typeSTR == "sen()": return ("sen()", string[index[0] + 4: index[len(index) - 1]], "")
    elif typeSTR == "cos()": return ("cos()", string[index[0] + 4: index[len(index) - 1]], "")
    elif typeSTR == "tan()": return ("tan()", string[index[0] + 4: index[len(index) - 1]], "")
    elif typeSTR == "ln()": return ("ln()", string[index[0] + 3: index[len(index) - 1]], "")
    elif typeSTR == "log()" : return ("log()", string[index[0] + 4: index[len(index) - 1]], "")
    elif typeSTR == "complex": return(string[sinais], string[0:sinais:1], string[sinais+1: sys.getsizeof(string) - 49:1])
    else: return(typeSTR, "", "")

#Verifica se a string é uma função trignometrica e se o número de elementos que contém dentro dela é igual ao size:
def str_trig(string, size):
    if str_type(string) == ("sen()", size): return True
    elif str_type(string) == ("cos()", size): return True
    elif str_type(string) == ("tan()", size): return True
    else: return False