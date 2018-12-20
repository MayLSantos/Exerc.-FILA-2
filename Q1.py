class Fila:
    
    def __init__(self):
        self. lista= []

    def lenght (self):
        return len(self.lista)

    def isEmpyt(self):
        return len(self.lista) == 0

    def enqueue (self, valor):
        self.lista.append(valor)

    def dequeue (self):
        if (not(self.isEmpyt())):
            self.lista.pop(0)

class Pilha():

    def __init__(self):
        self.lista2 = []
        
    def push (self, valor):
        self.lista2.append (valor)
        
    def pop (self):
        if (not(self.isEmpty())):
            return self.lista2.pop()
        
    def isEmpty(self):
        return len(self.lista2) == 0
    
    def length (self):
        return len (self.lista2)
    
    def  peek (self):
        if(not(self.isEmpty())):
            return self.lista2[-1]
        

fila=Fila()
pilha= Pilha()
fila.enqueue(10)
fila.enqueue(5)
fila.enqueue(6)
print(fila.lista)


for i in range(len(fila.lista)-1):
    pilha.push(fila.lista[0])
    fila.dequeue()
    print(fila.lista)
print("Pilha: {}".format(pilha.lista2))
    
for c in range(len(pilha.lista2)+1):
    fila.enqueue(pilha.lista2[c-1])
    pilha.pop()
    print(fila.lista)
    if c == 1:
        break
print("LISTA INVERTIDA")



