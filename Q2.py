import time 
import random
 
class Fila:
    
    def __init__(self):
        self. lista= []

    def lenght (self):
        return len(self.lista)

    def isEmpyt(self):
        return len(self.lista) == 0

    def enqueue (self, valor):
        self. lista. append(valor)

    def dequeue (self):
        if (not(self.isEmpyt())):
            self.lista.pop(0)

fila= Fila()
inicio = time.time()
#adicionando impressões a lista
for c in range (5):          
    fila. enqueue(random.randint(1,10))
print(fila.lista)
#imprimindo
for i in range(len(fila.lista)):
    fila.dequeue()
    pausa = time.sleep(5)
    fim = time.time()
    print("Tempo da {}ª impressão - {} " .format(i+1, fim-inicio))
    print(fila.lista)
    print("  ")
    if len(fila.lista) == 0:
        print("IMPRESSÕES FINALIZADAS")
            
