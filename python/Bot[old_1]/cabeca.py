#Parte 'Cerebral' onde ha interpretação de textos básicos
import conn
conn.CreateTable()

def intencao(pergunta):
    intencao = 'Nenhuma'

    if(pergunta.find('!')!=-1):
        intencao ='Afirmação'
        conn.VerificaExistenciaPergunta(pergunta)
    elif(pergunta.find('?')!=-1):
        intencao ='Pergunta'
        conn.VerificaExistenciaPergunta(pergunta)
    else:
        intencao ='fala'
        conn.VerificaExistenciaPergunta(pergunta)
        
    #print(intencao)









