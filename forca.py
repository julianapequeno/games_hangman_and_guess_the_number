import random

def jogar():
    imprime_cabecalho_do_jogo()
    ##########DESENVOLVIMENTO DO CÓDIGO NO CURSO 2 ###########
    palavra_secreta = escolhe_palavra_secreta_aleatorio()
    letras_acertadas = inicializa_letras_acertadas_underlines(palavra_secreta)
    print(letras_acertadas)

    enforcou = False #as palavras-valores da linguagem, possuem a first word maiúscula
    acertou = False
    erros = 0

    while(not enforcou and not acertou): #as palavras da linguagem sempre com letra minúscula!!
        #index = 0
        chute = jogador_digita_chute()
        if(chute in palavra_secreta):
            marca_chute(palavra_secreta,chute,letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
            print("Você errou! Ainda faltam {} vidas".format(7-erros))
        enforcou = erros == 7 #quando forem feitos 6 erros, vc já não pode mais tentar. É forca!
        acertou = "_" not in letras_acertadas #quando não estiver mais, vai dar true aqui e false no while, assim acabando as rodadas.
        print(letras_acertadas)
        #letras_faltando = str(letras_acertadas.count("_")) -> Conta a quantidade de vezes que aparece
        #if(letras_faltando == str(0)):
         #   acertou = True
        #else:
         #   print("Ainda faltam acertar {} letras".format(letras_faltando))
       # print("jogando...");
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)
    #print("Fim do jogo. A palavra secreta era: {}".format(palavra_secreta))

    #Testendo um outro programa, esta contido nesta função: programa_funcao_len()

def imprime_cabecalho_do_jogo():
    name = "Juliana"
    print("*****************************************")
    print("Bem vinda", name, "ao jogo de Forca!!!",sep=" ",end="\n")
    print("*****************************************")

def escolhe_palavra_secreta_aleatorio():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip().upper())  # aqui ele tira o \n e bota para maiúsculo de uma vez só, já adianta

    arquivo.close()

    palavra_secreta = random.choice(palavras)
    return palavra_secreta

def inicializa_letras_acertadas_underlines(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def jogador_digita_chute():
    chute = input("Qual a letra?")
    chute = chute.strip().upper()  # faço a limpeza de espaços e logo coloco tudo para maiúsculo
    return chute

def marca_chute(palavra_secreta,chute,letras_acertadas):
    index = 0
    for letra in palavra_secreta:  # vai andar pela 'palavra
        if (chute == letra):  # if(letra.upper() == chute.upper()):
            print("Encontrei a letra {} no index {}".format(letra, index))
            # O COUNT() CONTA QUANTAS VEZES A VARIÁVEL APARECE NA PALAVRA!!
            # cont = palavra_secreta.count(letra)
            # print("Tem {} letras assim nesta palalvra".format(cont))
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def programa_funcao_len():
    #####TESTANDO UMA ATIVIDADE DO CURSO DA ALURA.  O PROGRAMA ABAIXO É POSSUI A MESMA UTILIDADE DA FUNÇÃO LEN()
    print("#############################################\nPROGRAMA DA FUNÇÃO LEN")
    total = 0
    acabou = False
    palavra = "python rocks!"
    while (not acabou):
        total = total + 1
        acabou = (total == len(palavra))
    print("O tamnho da string: \"{}\" é de {} caracteres\n".format(palavra, total))

    # total = 0
    for i in palavra:
        # total = total + 1
        total = i  # neste caso, ele vai pegar o valor da palavra na posição i e não o índice como eu esperava. Interessante!!
    # print(total)
    print(total)
    ######################################################

if(__name__ == "__main__"): #A variável __name__ é setada quando vc chama um programa diretamente por ele para rodar.
    #a variável __main__ corresponde ao arquivo do projeto, que é o __main__
    jogar()