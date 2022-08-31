from trig import *
from string_math import *

class BinaryTreeNode:
    def __init__(self, data):
        self.left = None
        self.rigth = None
        self.data = data
    
    #Print the Node
    def PrintNode(selft):
        print(selft.data)
    
    #Print all tree
    def PrintTree(selft):
        if selft.left != None:
            selft.left.PrintTree()
        print(selft.data)
        if selft.rigth != None:
            selft.rigth.PrintTree()
    
    #Add number on binary tree
    def add_number(selft, data):
        if selft.data != None:
            if data > selft.data:
                if selft.rigth != None:
                    selft.rigth.add_number(data)
                else:
                    selft.rigth = BinaryTreeNode(data)
            else:
                if selft.left != None:
                    selft.left.add_number(data)
                else:
                    selft.left = BinaryTreeNode(data)
        else:
            selft.data = data
        
    def replace_x(selft, number):
        if selft != None:
            if selft.data == "x": selft.data = str(number)
            else:
                if selft.rigth != None: selft.rigth.replace_x(number)
                if selft.left != None: selft.left.replace_x(number)

#Return a tree clone:
def clone(node):
    if node != None:
        tree = BinaryTreeNode(node.data)
        tree.rigth = clone(node.rigth)
        tree.left = clone(node.left)
        return tree
    else: return None

#Return a list with all element this tree line:
def list_line(node, line):
    if line != -1 and node != None:
        if line == 0: return [node.data]
        else: return [] + list_line(node.rigth, line - 1) + list_line(node.left, line - 1)
    else: return []

#Return the height tree:
def height(node):
    if node == None: return -1
    else : return max(height(node.left), height(node.rigth)) + 1

def tree_to_string(node):
    if node != None:
        if node.data == "()":
            return "(" + tree_to_string(node.left) + tree_to_string(node.rigth) + ")"
        elif node.data == "||":
            return "|" + tree_to_string(node.left) + tree_to_string(node.rigth) + "|"
        elif node.data == "sen()":
            return "sen(" + tree_to_string(node.left) + tree_to_string(node.rigth) + ")"
        elif node.data == "cos()":
            return "cos(" + tree_to_string(node.left) + tree_to_string(node.rigth) + ")"
        elif node.data == "tan()":
            return "tan(" + tree_to_string(node.left) + tree_to_string(node.rigth) + ")"
        elif node.data == "ln()":
            return "ln(" + tree_to_string(node.left) + tree_to_string(node.rigth) + ")"
        elif node.data == "log()":
            return "log(" + tree_to_string(node.left) + tree_to_string(node.rigth) + ")"
        return tree_to_string(node.left) + node.data + tree_to_string(node.rigth)
    else: return ""

#Return the total number of elements in tree:
def tree_element_number(node):
    if node == None: return 0
    else: return 1 + tree_element_number(node.left) + tree_element_number(node.rigth)

#Retorna o número de folhas da árvore binária:
def leaves(node):
    if node == None: return 0
    elif node.rigth == None and node.left == None: return 1
    else: return 0 + leaves(node.rigth) + leaves(node.left)

#Retorna uma lista com todas as folhas da árvore binária:
def leaves_list(node):
    if node == None: return []
    elif node.rigth == None and node.left == None: return [node.data]
    else: return [] + leaves_list(node.rigth) + leaves_list(node.left)

#Print the tree by level
def print_tree_by_line(node):
    for i in range(0, height(node) + 1):
        list = (list_line(node, i))
        list.reverse()
        value = ""
        for j in range(0, len(list)):
            value = value + str(list[j]) + " "
        print(value)

#Retorna o número de nodes complexos presentes na árvore binária:
def complex_nodes(node):
    if node == None: return 0
    elif str_type(node.data) == ("complex", sys.getsizeof(node.data) - 49):
        return 1 + complex_nodes(node.rigth) + complex_nodes(node.left)
    else: return 0 + complex_nodes(node.rigth) + complex_nodes(node.left)

#Returns the number of elements x in the tree:
def x_number(node):
    if node != None:
        if node.data == "x": return 1 + x_number(node.rigth) + x_number(node.left)
        else: return x_number(node.rigth) + x_number(node.left)
    else: return 0

#Retorna True se existir divisão por zero e False se não existir divisão por zero
def tree_check_div_zero(node):
    if node != None:
        if node.data == "/" and str_isnumber(node.rigth.data) and float(node.rigth.data) == 0: return True
        if node.data == "^" and str_isnumber(node.rigth.data) and str_isnumber(node.left.data) and float(node.left.data) == 0 and float(node.rigth.data) < 0: return True
        else: return tree_check_div_zero(node.rigth) or tree_check_div_zero(node.left)
    else: return False

#Retorna True se existir na árvore uma raiz quadrada de um número negativo:
def tree_check_negative_square_root(node):
    if node != None:
        if node.data == "^" and str_isnumber(node.rigth.data) and str_isnumber(node.left.data):
            if float(node.left.data) < 0 and 0.5 % float(node.rigth.data) == 0: return True
        return tree_check_negative_square_root(node.left) or tree_check_negative_square_root(node.rigth)
    else: return False

#verefica se não existe logaritmos inválidos:
def tree_check_log(node):
    if node != None:
        if node.rigth != None:
            if (node.data == "ln()" or node.data == "log()") and str_isnumber(node.rigth.data):
                if float(node.rigth.data) <= 0: return True 
            return tree_check_log(node.rigth) or tree_check_log(node.left)
        if node.left != None:
            if (node.data == "ln()" or node.data == "log()") and str_isnumber(node.left.data):
                if float(node.left.data) <= 0: return True 
            return tree_check_log(node.rigth) or tree_check_log(node.left)
    else: return False

#Retorna True se existir alguma folha que não seja um número e False caso contrário:
def tree_check_leaves(list):
    if list != []:
        if str_isnumber(list[0]): return tree_check_leaves(list[1::])
        else: return True
    else: return False

# Retorna True caso existe algum erro no árvore binária e False caso não exista nenhum erro na árvore binária:
def tree_check(node):
    return tree_check_leaves(leaves_list(node)) or tree_check_div_zero(node) or tree_check_log(node) or tree_check_negative_square_root(node)

#Responsável por construir a árvore em si,
#Coloca as string nos ramos certos da árvore:
def plant_tree(data):
    element, left, rigth = str_div(data)
    left_size = sys.getsizeof(left) - 49
    rigth_size = sys.getsizeof(rigth) - 49
    if left_size == rigth_size == 0: return BinaryTreeNode(element)
    elif left_size != 0 and rigth_size == 0 and str_type(left) == ("numeric", left_size):
        tree = BinaryTreeNode(element)
        tree.left = BinaryTreeNode(left)
        return tree
    elif left_size != 0 and rigth_size == 0 and str_type(left) != ("numeric", left_size):
        tree = BinaryTreeNode(element)
        tree.rigth = BinaryTreeNode(left)
        return tree
    elif left_size != 0 and rigth_size != 0 and str_type(rigth) == ("numeric", rigth_size) and (str_type(left) != ("numeric", left_size) and str_trig(left, left_size) and str_type(left) != ("()", left_size)):
        tree = BinaryTreeNode(element)
        tree.left = BinaryTreeNode(rigth)
        tree.rigth = BinaryTreeNode(left)
        return tree
    elif left_size == 0 and rigth_size != 0 and ((str_type(rigth) == ("numeric", left_size) or str_trig(rigth, rigth_size) or str_type(rigth) != ("()", left_size))):
        tree = BinaryTreeNode(element)
        tree.left = BinaryTreeNode(rigth)
        return tree
    else:
        tree = BinaryTreeNode(element)
        tree.left = BinaryTreeNode(left)
        tree.rigth = BinaryTreeNode(rigth)
        return tree

#Vai indo precorendo árvore até ter todas as strings simplificadas/resolvidas:
def calc_comples_nodes(node):
    if node != None and (node.rigth != None or node.left != None):
        if node.rigth != None and str_type(node.rigth.data) != ("numeric", sys.getsizeof(node.rigth.data) - 49):
            node.rigth = plant_tree(node.rigth.data)
        if node.left != None and str_type(node.left.data) != ("numeric", sys.getsizeof(node.left.data) - 49):
            node.left = plant_tree(node.left.data)
        calc_comples_nodes(node.rigth)
        calc_comples_nodes(node.left)
    return node