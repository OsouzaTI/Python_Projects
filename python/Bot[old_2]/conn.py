import sqlite3
#Fazendo conexão no arquivo
connection = sqlite3.connect('bd_cerebro.db')
c = connection.cursor()
#Criando Tabela no arquivo de banco de dados
c.execute("CREATE TABLE IF NOT EXISTS 'tb_processo'("+
          "'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"+
          "'tag' text NOT NULL,"+
          "'pergunta' text NOT NULL,"+
          "'resposta' text NOT NULL)")
def conn():
    return c
def connection_():
    return connection
