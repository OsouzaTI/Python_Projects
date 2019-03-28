import sqlite3
import math
import random

#Fazendo conexão no arquivo
connection = sqlite3.connect('bd_cerebro.db')
c = connection.cursor()
#Criando Tabela no arquivo de banco de dados
c.execute("CREATE TABLE IF NOT EXISTS 'tb_processo'("+
          "'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"+
          #"'tag' text NOT NULL,"+
          "'pergunta' text NOT NULL,"+
          "'resposta' text NOT NULL)")

#Select todos os dados e verifica se existe a pergunta
def existe(pergunta):
    existe = False
    for raw in c.execute("SELECT * FROM tb_processo"):
        if(raw[1]==pergunta):
            print('Bot:'+raw[2])
            existe = True

    if(not existe):
        c.execute("INSERT INTO tb_processo ('pergunta','resposta') VALUES('{}','{}')".format(pergunta,''))
        connection.commit()
        respVazia = []
        trigger = False
        for raw in c.execute("SELECT * FROM tb_processo"):
            if(raw[1]!='' and not trigger):
                #print('Bot:'+raw[1])
                trigger = True
                
            if(raw[2]==''):
                respVazia.append(raw[1])
        n = math.floor(random.randint(0,len(respVazia)))
        print('Bot:'+respVazia[n]+'->'+str(n))

    
