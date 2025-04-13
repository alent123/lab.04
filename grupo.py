
# Exercise 1: Reverse a String

def invertirCadena(pila,s):
    for char in s:
        pila.append(char)
    invertida = ''
    while pila:
        invertida += pila.pop()
    return invertida
if __name__ == "__main__":
    pila = [] 
    entrada = "EL TEST DE INVERCION "
    invertida = invertirCadena(pila,entrada)
    print(f"Original: {entrada}")
    print(f"Invertida: {invertida}")

# Exercise 2: Evaluate Infix Expressions
def prioridad(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    return 0
def esOperador(c):
    return c in '+-*/'
def convertirAPostfijo(expresion):
    salida = []
    pila = []
    tokens = expresion.split()  
    for token in tokens:
        if token.isdigit():
            salida.append(token)
        elif token == '(':
            pila.append(token)
        elif token == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()  
        elif esOperador(token):
            while pila and prioridad(pila[-1]) >= prioridad(token):
                salida.append(pila.pop())
            pila.append(token)
    while pila:
        salida.append(pila.pop())
    return salida
def evaluarPostfijo(expresionPostfijo):
    pila = []
    for token in expresionPostfijo:
        if token.isdigit():
            pila.append(int(token))
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                pila.append(a / b)
    return pila[0]
def evaluarExpresion(expresion):
    postfijo = convertirAPostfijo(expresion)
    resultado = evaluarPostfijo(postfijo)
    return resultado

# Ejemplo de uso
expresion = "( 3 + 4 ) * 2"
print("Resultado:", evaluarExpresion(expresion))

#3
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.minStack[-1]:
                self.minStack.pop()
            self.stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.minStack[-1] if self.minStack else None

#4
class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def type(self, new_text):
        self.history.append(self.text)
        self.text += new_text

    def delete(self):
        if self.text:
            self.history.append(self.text)
            self.text = self.text[:-1]

    def undo(self):
        if self.history:
            self.text = self.history.pop()

    def show(self):
        return self.text


#Exercise 5: Check for Balanced HTML Tags
import re
def balanceadas(html):
    pila = []
    patron = r'</?([a-zA-Z0-9]+)>'
    etiquetas = re.findall(patron, html)
    for etiqueta in etiquetas:
        if etiqueta[0] != "/":  
            pila.append(etiqueta)
        else: 
            nombre_etiqueta = etiqueta[1:] 
            if pila and pila[-1] == nombre_etiqueta:
                pila.pop() 
            else:
                return False
    return len(pila) == 0
html = "<html><body><h1>Título</h1><p> test de funcionamiento</p></body></html>"
if balanceadas(html):
    print("Las etiquetas están balanceadas.")
else:
    print("Las etiquetas NO están balanceadas.")

#6
class FixedArrayStack:
    def __init__(self, capacity):
        self.stack = [None] * capacity
        self.top = -1
        self.capacity = capacity

    def push(self, item):
        if self.top + 1 >= self.capacity:
            raise OverflowError("Pila llena (overflow)")
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.top == -1:
            raise IndexError("Pila vacía (underflow)")
        item = self.stack[self.top]
        self.top -= 1
        return item
#6.2
class DynamicArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item) 

    def pop(self):
        if not self.stack:
            raise IndexError("Pila vacía")
        return self.stack.pop()

#6.3
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            raise IndexError("Pila vacía")
        item = self.top.value
        self.top = self.top.next
        return item
#7
def next_greater_element(arr):
    stack = []  
    result = [-1] * len(arr)  

    for i in range(len(arr) - 1, -1, -1):  
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

 
        stack.append(arr[i])

    return result



arr = [4, 5, 2, 10, 8]
print("Entrada:", arr)
print("Next Greater Elements:", next_greater_element(arr))



