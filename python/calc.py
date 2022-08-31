from trig import *
from tree import *
from string_math import *
from log import *
math_sign_list = ["+", "-", "*", "/", "^", "!", "sen()", "cos()", "tan()", "()", "||", "ln()", "log()"]

#Return the number module:
def modulo(number):
    if number >= 0: return number
    else: return - number

#Premite calcular as raiz não pares de números negativos:
def exp(b, expoenete):
    if b < 0 and (2 % expoenete != 0): return - ((-b) ** expoenete)
    else: return b ** expoenete

#pass operadores[sign](number1, number2)
#return the math result
#Example:
#operadores["+"](2,5) -> 7
#operadores["-"](0,8) -> -8
operadores = {
    "+": lambda n1, n2: n1 + n2,
    "-": lambda n1, n2: n1 - n2,
    "*": lambda n1, n2: n1 * n2,
    "/": lambda n1, n2: n1 / n2,
    "^": lambda n1, n2: exp(n1, n2),
    "!": lambda n1, n2: fatorial(n2),
    "sen()": lambda n1, n2: sen(n2),
    "cos()": lambda n1, n2: cos(n2),
    "tan()": lambda n1, n2: tan(n2),
    "()": lambda n1, n2: n2,
    "||": lambda n1, n2: modulo(n2),
    "ln()": lambda n1, n2: ln(n2),
    "log()": lambda n1, n2: log(2, n2)
}

#Substituir o valor daquele node pelo valor da equação e apaga os nodes da direita e da esquedra onde estavam
#guardados os valora numéricos:
def simple_operations(node):
    if node.rigth != None and node.left != None:
        node.data = operadores[node.data](float(node.left.data),float(node.rigth.data))
        node.rigth = None
        node.left = None
    elif node.rigth == None and node.left != None:
        node.data = operadores[node.data](0,float(node.left.data))
        node.left = None
    else:
        node.data = operadores[node.data](0,float(node.rigth.data))
        node.rigth = None
    if type(node.data) != complex:
        node.data = str_remove_scientific_notacion(round(node.data, 7))
    else: node.data = str(node.data)
    return node

def calc(tree):
    len_rigth = 0
    len_left = 0
    if tree != None:
        if tree.rigth != None: len_rigth = sys.getsizeof(tree.rigth.data) - 49
        if tree.left != None: len_left = sys.getsizeof(tree.left.data) - 49
        if tree.rigth != None and tree.left != None:
            if list_element_index(math_sign_list, tree.data) >= 0 and str_type(tree.rigth.data) == ("numeric", len_rigth) and str_type(tree.left.data) == ("numeric", len_left):
                tree = simple_operations(tree)
        elif tree.rigth == None and tree.left != None:
            if list_element_index(math_sign_list, tree.data) >= 0 and str_type(tree.left.data) == ("numeric", len_left):
                tree = simple_operations(tree)
        elif tree.rigth != None and tree.left == None:
            if list_element_index(math_sign_list, tree.data) >= 0 and str_type(tree.rigth.data) == ("numeric", len_rigth):
                tree = simple_operations(tree)
        calc(tree.rigth)
        calc(tree.left)
    return tree

string = sys.argv[1]
result = []
if str_validate_parentheses(string):
    t = plant_tree(str_pi(string))
    t = calc_comples_nodes(t)
    if x_number(t) > 0:
        for i in range(-1000, 1001):
            tree = clone(t)
            tree.replace_x(i/100)
            while str_type(tree_to_string(tree)) != ("numeric", sys.getsizeof(tree_to_string(tree)) - 49) and not tree_check(tree):
                tree = calc(tree)
            if str_isnumber(tree_to_string(tree)): result.append((float(tree_to_string(tree))))
            else: result.append("erro")
    else:
        while str_type(tree_to_string(t)) != ("numeric", sys.getsizeof(tree_to_string(t)) - 49) and not tree_check(t):
            result.append(tree_to_string(t))
            t = calc(t)
        if str_isnumber(tree_to_string(t)): result.append(round(float(tree_to_string(t)), 6))
        else: result.append("erro")
    print(result)
else: print("erro")