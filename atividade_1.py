from graphviz import Digraph
import random

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def parse_expression(tokens):
    token = tokens.pop(0)
    if token == '(':
        left = parse_expression(tokens)
        op = tokens.pop(0)
        right = parse_expression(tokens)
        tokens.pop(0)  # Remove ')'
        return Node(op, left, right)
    else:
        return Node(token)

def visualize_tree(root, filename):
    dot = Digraph()
    def add_nodes_edges(node):
        if node:
            dot.node(str(id(node)), str(node.value))
            if node.left:
                dot.edge(str(id(node)), str(id(node.left)))
                add_nodes_edges(node.left)
            if node.right:
                dot.edge(str(id(node)), str(id(node.right)))
                add_nodes_edges(node.right)
    add_nodes_edges(root)
    dot.render(filename, view=True, format='png')

def generate_random_expression():
    operands = [str(random.randint(1, 20)) for _ in range(3)]
    operators = random.sample(['+', '-', '*', '/'], 2)
    expr = f"( ( {operands[0]} {operators[0]} {operands[1]} ) {operators[1]} {operands[2]} )"
    return expr

# Árvore com valores fixos
expr1 = "( ( ( 7 + 3 ) * ( 5 - 2 ) ) / ( 10 * 20 ) )"
tokens1 = expr1.replace('(', ' ( ').replace(')', ' ) ').split()
tree1 = parse_expression(tokens1)
visualize_tree(tree1, 'arvore_fixa')

# Árvore com valores randômicos
expr2 = generate_random_expression()
print("Expressão aleatória gerada:", expr2)
tokens2 = expr2.replace('(', ' ( ').replace(')', ' ) ').split()
tree2 = parse_expression(tokens2)
visualize_tree(tree2, 'arvore_randomica')