import random      #Importando a biblioteca random para usar o random.choice






def pergunta_aleatoria(perguntas):   #Vai pegar uma pergunta aleátoria da lista e printar
    questao = random.choice(perguntas)
    return questao

def leitor_arquivo():    #Tá lendo o arquivo txt, no qual está todas as perguntas, alternativas e respostas corretas
    pergunta = []
    lista_perguntas = []
    arq = open('perguntas.txt', 'r')
    linhas = arq.readlines()
    arq.close()
  
    for linha in linhas:  #Vai por o que está no arquivo dentro de uma lista, linha por linha
        pergunta.append(linha)
        if len(pergunta) == 5:
            lista_perguntas.append(pergunta)
            pergunta = []
    return lista_perguntas





def pontuacao(pergunta, ponto, jogador):  #Atribuição de pontos ao jogador
    ranking = []
    if "F" in pergunta[0]:    #10 pontos para as perguntas facéis
        ponto += 10
    elif "M" in pergunta[0]:   #20 pontos para as perguntas m´médias
        ponto += 20
    elif "D" in pergunta[0]:  #30 pontos para as perguntas dificéis 
        ponto += 30
    global pontos_jogador
    pontos_jogador += ponto
    ranking.append(jogador)
    ranking.append(pontos_jogador)
    return ranking




def conferir_resposta(pergunta, resposta):  #Vai conferir se a resposta dada está dentro da lista criada pela função lá em cima, e todas as respostas estão no índice 4 relacionado a cada pergunta
    if resposta in pergunta[4]:
        certo = True
    else:
        certo = False
    return certo


pontos_jogador = 0


def cria_lista(jogador, pontos):  #Aqui está criando uma lista e relacionando o jogador à pontuação conquistada por ele ao jogar
    pontos_2 = []
    pontos_2.append(jogador)
    pontos_2.append(pontos)
    return pontos_2
pontos = 0
jogar = 12
rank = []

#Aqui começa o jogo

print("=-"*28)
print('''       Seja Bem-Vindo ao Quiz Cami's\n 
  um jogo, que tem por objetivo saber se você sabe tudo de Sword Art Online\n       ''')
print("=-"*28)
jogador = input("Digite o nome do jogador: ")

#Aqui entrará a parte em que o jogo realmente roda

while jogar != '0': 
    print('''\n    1- Digite 1 caso queira começar a jogar
    2- Digite 2 caso queria adicionar mais perguntas
    0- Digite 0 caso queira sair do jogo''')
    jogar = input()
    lista_questoes = leitor_arquivo()
    y = len(lista_questoes)
    
    if jogar == '1':  #Verifica a escolha do jogador, e caso seja 1, vai mostrar as perguntas 
        for a in range (0, 5):
            questao = pergunta_aleatoria(lista_questoes)
            lista_questoes.remove(questao)
            for palavra in (range(0, len(questao) - 1)):
                    print(f"{questao[palavra]}", end ='')
                
            resposta = input().lower()
            if resposta == '0':
                jogar = 0
                break
            correto = conferir_resposta(questao, resposta)
            if correto == True:
                print("Você acertou!")
                ranking = pontuacao(questao, pontos, jogador)
                pontos_jogador = ranking[1]
                cria_lista(jogador, pontos)
            else:
                print("Você errou!")

    elif jogar == '2':  #Caso seja 2, vai permiti-lo adicionar perguntas ao arquivo
      inserir = str(input(print("Digite aqui a pergunta que deseja inserir ao quiz: ")))
      alternativas = str(input(print("Digite aqui a primeira alternativa da seguinte forma - a) alternativa - ")))
      alternativas1 = str(input(print("Digite aqui a segunda alternativa da seguinte forma - b) alternativa - ")))
      alternativas2 = str(input(print("Digite aqui a primeira alternativa da seguinte forma - c) alternativa - ")))
      alternativas3 = str(input(print("Digite aqui a alternativa correta ")))
      arq = open ('perguntas.txt','a')
      arq.append(inserir,alternativas)
      arq.close()        
              
              
         
              
    if resposta == '0':  #E caso seja 0, vai encerrar o programa e mostrar a pontuação final do jogador
        print("Agradecemos por participar do nosso Quiz!")
        input(print("O que achou?"))
        input(print("Gostou de jogar?"))
        print("Agora, aqui vai a sua pontuação no jogo")
        print(f'  {jogador} = {pontos_jogador}')
        jogar = '0'
        break