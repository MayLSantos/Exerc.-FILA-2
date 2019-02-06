from Fila import Fila
filaCliente= Fila()
filaTempo= Fila()
    
def adicionarCliente(nome):
    filaCliente.enqueue(nome))
        
def atendimento():
    nome= filaCliente.dequeue()

class Cliente():
    def __init__(self):
        self.nome= nome
        self.chegada= chegada
        
#programa principal
class main():
    opcao = 0
    print("""MENU
    [1] Fazer chamada
    [2] Atender
    [3] Sair""")
    while opcao != 3:
        chegada= time.time()
        n= str(input("Digite seu nome aqui "))
        opcao= int(input("Digite sua opcao aqui: "))
    if opcao == 1:
        adicionarCliente(n)
    elif opcao == 2:
        atendido= time.time()
        print("Tempo de espera: {}".format(chegada - atendido))
        atendimento()
        
if (__name__ == "__main__"):
    main()
