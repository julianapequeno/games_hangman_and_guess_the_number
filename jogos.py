import forca #chamamos de módulo, pode ser uma biblioteca, e neste caso, um arquivo tbm
import adivinhacao #ao importar dessa forma, sem as funções nos arquivos, ele já começa a executar os arquivos

def escolhe_jogo():
    print("*****************************************")
    print("Escolha o seu jogo!!!",sep=" ",end="\n")
    print("*****************************************")

    print("(1) Forca")
    print("(2) Adivinhação")

    op = int(input("Qual o jogo? "))

    if(op == 1):
        print("Jogando forca")
        forca.jogar() #usar as funções para o código funcionar apenas quando a func for chamada
    elif(op == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()  #usar as funções para serem chamadas apenas quando for chamada

if(__name__=="__main__"):
    escolhe_jogo()