import conn
import math
import random
#conexão
c = conn.conn()
connection = conn.connection_()
#Assimilando
def assimilarPergunta(pergunta):
    first = False
    tags = []
    ## Pegando as tags
    for row in c.execute("SELECT * FROM tb_processo"):
        if(not first):
            tags.append(row[1])
            first = True
            
        if(first):
            n = False
            for i in range(len(tags)):
                if(row[1]==tags[i]):
                    n = True
                    
            if(not n):
                tags.append(row[1])
                #print('nova tag salva!')
    ########################################################        

    # Deduzindo as tags da pergunta
    pergArr = pergunta.split(' ')
    tag = [0,0]
    if(len(pergArr)>0):
        for row in c.execute("SELECT * FROM tb_processo"):
            for i in range(len(pergArr)):
                if(pergArr[i]==row[3]):
                    for n in range(len(tags)):
                        if(row[1]==tags[n]):
                            tag[n] += 1
    for k in range(len(tag)):
        if(tag[k]!=0):
            return False
            #print(tags[k]+':'+str(tag[k])+'->'+str( tag[k]/100 )+'%')
    n_max = max(tag)
    n_pos = tag.index(n_max)
    pergJafeita = False
    for row in c.execute("SELECT * FROM tb_processo"):
        if(row[2]==pergunta):
            pergJafeita = True
    if(not pergJafeita):
        c.execute("INSERT INTO tb_processo ('tag','pergunta','resposta') VALUES ('{}','{}','{}')".format(tags[n_pos],pergunta,''))
        connection.commit()
    else:
        for row in c.execute("SELECT * FROM tb_processo"):
            if(row[2]==pergunta):
                print('Bot:',row[2])

                    
    if(not pergJafeita):
        #Perguntando
        primeiraPergunta = ''
        perguntas = []
        for row in c.execute("SELECT * FROM tb_processo"):
            if(row[0]==1):
                primeiraPergunta = row[2]
            if(row[3]==''):
                perguntas.append(row[2])

        n = math.floor(random.randint(0,len(perguntas)-1))
        pergEscolhida = perguntas[n]
        print('Bot:',pergEscolhida)
        resp = input('You:')
        c.execute("UPDATE tb_processo SET resposta='{}' WHERE pergunta='{}'".format(resp,pergEscolhida))
        connection.commit()
        
        print('Bot:',primeiraPergunta)





































    
