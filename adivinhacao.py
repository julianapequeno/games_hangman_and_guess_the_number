import random

def jogar():
    name = "Juliana"
    print("*****************************************")
    print("Bem vinda", name, "ao jogo de adivinhação!",sep=" ",end="\n")
    #print("Bem vinda",name,sep=" ",end="!")
    print("*****************************************")

    #numero_secreto = round(random.random() * 100) #gera um número aleatório entre 0.0 e 1.0, multiplica por 100, e arredonda para int
    numero_secreto = random.randrange(1,101) # vai de 1 até o 100
    #total_de_tentativas = 0
    rodada = 1
    pontos = 100


    print("Qual o nível de dificuldade?", numero_secreto)
    print("(1)Fácil (2)Médio (3)Difícil")

    nível = int(input("Defina o nível: "))

    if(nível == 1):
        total_de_tentativas = 20
    elif(nível == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #while(rodada <= total_de_tentativas):
    for rodada in range(1,total_de_tentativas+1):
       # print("Tentativa",rodada,"de",total_de_tentativas)
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite o seu número entre 1 e 100: ")  # função input devolve o número
        chute = int(chute_str)  # a função int converte para int
        print("Você", "digitou", chute_str, sep=" ", end="\n")
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue #ele pulatodo o resto do código e continua com a próxima iteração
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:  # OS DOIS PONTOS DEFINEM A ENTRADA DO BLOCO
            print("Você acertou e fez {} pontos!".format(pontos))  # O python exige que haja um identação. Um tab = 4 espaços, o pycharm faz isso
            break #vai quebrar o LAÇO, ou seja, neste caso o FOR, também pode ser o WHILE
        else:
            if (maior):
                print("Você errou! O seu chute foi MAIOR do que o número secreto!", end="\n")
            elif (menor):
                print("Você errou! O seu chute foi MENOR do que o númeroo secreto!", sep=" ", end="!\n")
            pontos_perdidos = abs(numero_secreto - chute) #40-20 = 20(exemplo) abs() -> transforma em número absoluto, ou seja positivo ou negativo ele é positivo
            pontos = pontos - pontos_perdidos
            if(rodada == total_de_tentativas):
               print("O número secreto era {}. Você fez {} pontos".format(numero_secreto,pontos))
        #total_de_tentativas = total_de_tentativas - 1
        #rodada = rodada + 1
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()