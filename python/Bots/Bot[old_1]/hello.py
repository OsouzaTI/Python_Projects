##############################################
#   Projeto: Chat Bot
#   Autor : Osouza
#   Data : 23/03/2019
#   Hora : 10:37
##############################################

#imports
from time import *
import conn
import cabeca
#

##### específicações do indivíduo
Nome, Idade = '',''
##### específicações do momento
Dia, Hora, = strftime("%d"), strftime("%H:%M:%S")

User_exists = conn.User_exists()
if(conn.User_exists()):
    nome = conn.Get_user()
    print("=======================================================================\n")
    print("Olá {}\n".format(nome))
    print("Hoje é dia {} as {}\n".format(Dia,Hora))
    print("=======================================================================")
else:
    print("Olá novo visitante, meu nome é X.")
    nome = input("Qual o seu?\t")
    conn.Inserir_user(nome)
i = False
while True:
    if(i==False):
        conn.Get_Bot()
        i = True
    perg = input("You: ")
    cabeca.intencao(perg)


