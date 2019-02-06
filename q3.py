import time

class Fila:
    
    def __init__(self):
        self.listaNome= []
        self.filaChegada= []

    def lenght (self):
        return len(self.listaNome)

    def isEmpyt(self):
        return len(self.listaNome) == 0

    def enqueue (self, nome, tempo):
        self.listaNome.append(nome)
        self.filaChegada.append(tempo)

    def dequeue (self):
        if (not(self.isEmpyt())):
            self.listaNome.pop(0)
            self.filaChegada.pop(0)

filaCliente= Fila()
n= 0
chegada= 0
    
def adicionarCliente(nome, tempo):
    filaCliente.enqueue(n,chegada)
    
def atendimento():
    nome= filaCliente.dequeue()

class Cliente():
    def __init__(self):
        self.nome= nome
        self.chegada= chegada
       
#programa principal
def main():
    opcao = 0
    print("""MENU
    [1] Fazer chamada
    [2] Atender
    [3] Sair""")
    while opcao != 3:
        chegada= time.time()
        n= str(input("Digite seu nome aqui: "))
        opcao= int(input("Digite sua opcao aqui: "))
        if opcao == 1:
            adicionarCliente(n,chegada)
        elif opcao == 2:
            atendido= time.time()
            print("Tempo de espera: {}".format(chegada - atendido))
            atendimento()
        else:
            break
if (__name__ == "__main__"):
    main()
