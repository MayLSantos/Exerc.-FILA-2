import time
import random

class Fila:
   def __init__(self):
       self._itens = list()

   def isVazio(self):
       return len(self._itens)==0

   def peek(self):
       tamanho = len(self._itens)
       return self._itens[0]

   def enqueue(self, item):
       self._itens.append(item)

   def dequeue(self):
       if self.isVazio():
           return False
       return self._itens.pop(0)

   def length(self):
       return len(self._itens)


filaImpressao = Fila()

def adicionarFilaImpressao(documento):
    print("Adicionando na fila...")
    filaImpressao.enqueue(documento)

def imprimir():
    inicio= time. time()
    time.sleep(randint(1,5))
    print("Imprimindo!")
    documento = filaImpressao.dequeue()
    print(documento)
    fim= time.time()
    print("O tempo total da impressão foi de {}." .format (fim-inicio))
    
opcao = 0
def main():
    opcao = 0
    print(""" 1- Adicionar o documento
2- Imprimir
3- Sair""")
    while (opcao !=3):
        opcao= int(input("Qual opção você deseja? "))
        if opcao == 1:
            print("Criando o documento...")
            documento = str(input("Digite o texto que deseja imprimir: "))
            adicionarFilaImpressao(documento)
        elif opcao == 2:
            imprimir()
        else:
            break

if (__name__ == "__main__"):
    main()
