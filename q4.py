import time
from Fila import Fila
filaBanco= Fila()

def entrarNaFila(nome):
    filaBanco.enqueue(nome)

def atender():
    filaBanco.dequeue()

def main():
    opcao= 0
    print(""" MENU
1- Entrar na fila de espera
2- Atender
3- Sair""")
    while opcao != 3:
        chegada = time.time()
        n=str(input("Como se chama? "))
        opcao= int(input("Qual opção você deseja {}? ".format(n)))
        if opcao == 1:
            entrarNaFila(n)
        elif opcao == 2:
            atendido= time.time()
            print("Chamando Sr(a) {}...Tempo de espera: {}".format(n,(atendido - chegada)))
            atender()
        else:
            break

if (__name__ == "__main__"):
    main()
