import sqlite3
import random
import math
connection = sqlite3.connect('bd_cerebro.db')
c = connection.cursor()
if (connection):
    print("Conectado com sucesso!")
else:
    print("Erro ao conectar")

def Inserir_user(nome):
    c.execute("INSERT INTO tb_usuario (nome) VALUES('{}')".format(nome))
    connection.commit()
def Get_user():
    for row in c.execute("SELECT nome FROM tb_usuario WHERE id=1"):
        return row[0]
    
def Get_Bot():
    perguntas = []
    i = 0
    for row in c.execute("SELECT * FROM tb_pergunta"):
        perguntas.insert(i,row[1])
        i+=1
    if(len(perguntas)>1):
        n = math.floor(random.randint(0,len(perguntas)-1))
    else:
        n = 0
    print("Bot:",perguntas[n])

    
def User_exists():
    try:
        for row in c.execute("SELECT nome FROM tb_usuario WHERE id=1"):
            #print(row[0])
            return True
    except:
        #print("Tabela não existe")
        return False
def CreateTable():
    c.execute("CREATE TABLE IF NOT EXISTS 'tb_pergunta' ('id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'pergunta' text NOT NULL,'resposta' text NOT NULL)")
    connection.commit()

def VerificaExistenciaPergunta(pergunta):
    inexistente = True;
    for row in c.execute("SELECT * FROM tb_pergunta"):
        if(row[1]==pergunta):
            print("Bot:",row[2])
            inexistente = False
    if(inexistente):
        arr = []
        i = 0
        for row in c.execute("SELECT * FROM tb_pergunta"):
            if(row[2]==''):
                arr.insert(i,row[1])
                i+=1
        if(len(arr)>0):
            n = 0      
            if(len(arr)>1):
                n = math.floor(random.randint(0,len(arr)-1))
            else:
                n = 0

            print('Bot:',arr[0])
            resp = input('You: ')
            for row in c.execute("SELECT * FROM tb_pergunta"):
                if(row[1]==arr[n]):
                    c.execute("UPDATE tb_pergunta SET resposta='{}' WHERE pergunta='{}'".format(resp,arr[n]))
                    connection.commit()
        else:
            #print("\nSem perguntas vazias\n")
            respAleatorias = []
            i = 0
            for row in c.execute("SELECT * FROM tb_pergunta"):
                respAleatorias.insert(i,row[1])
                i+=1
            n = math.floor(random.randint(0,len(respAleatorias)-1))
            print("Bot:",respAleatorias[n])
            c.execute("INSERT INTO tb_pergunta (pergunta,resposta) VALUES('{}','{}')".format(pergunta,''))
            


    
