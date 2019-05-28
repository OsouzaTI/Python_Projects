#bibliotecas nativas
import os
import time
import re

#bibliotecas instalados p/ projeto
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from selenium import webdriver

class wppbot:
#setando o caminho do app
	dir_path = os.getcwd()
#construtor da classe
	def __init__(self, nome_bot):
#Setando o bot 
		self.bot = ChatBot(nome_bot)
		#ListTrainer(self.bot)
#setando a pasta onde ta o chrome driver
		self.chrome = self.dir_path+'\chromedriver.exe'
#configurando um profile pra não logar no whats toda hora
		self.options = webdriver.ChromeOptions()
		self.options.add_argument(r"user-data-dir="+self.dir_path+"\profile\wpp")
#iniciando o driver
		self.driver = webdriver.Chrome(self.chrome,chrome_options=self.options)


	# Method start
	def inicia(self,nome_contato):
	#Selenium vai entrar no whats e esperar 15s pra carregar tudo
		self.driver.get('https://web.whatsapp.com/')
		self.driver.implicitly_wait(15)
	#elemento da barra de pesquisa pela classe
		self.caixa_de_pesquisa = self.driver.find_element_by_class_name('jN-F5')
	#escrevemos o nome do contato na caixa e esperamos 2s
		self.caixa_de_pesquisa.send_keys(nome_contato)
		time.sleep(2)
	#buscar o contato/grupo e clicar no mesmo
		self.contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome_contato))
		self.contato.click()
		time.sleep(2)

	# Method speak start
	def saudacao(self,frase_inicial):
	#setando a caixa de mansagem como elemento _2S1VP
		self.caixa_de_mensagem = self.driver.find_element_by_class_name('_2S1VP')
	#validando se a mensagem inicial é uma lista
		if type(frase_inicial) == list:
	#fazendo um for para mandar cada mensagem	
			for frase in frase_inicial:
	#Escrevemos a frase na caixa de mensagem.
				self.caixa_de_mensagem.send_keys(frase)
				time.sleep(1)
	#Setamos o botão de enviar e clicamos para enviar.
				self.botao_enviar = self.driver.find_element_by_class_name('_35EW6')
				self.botao_enviar.click()
				time.sleep(1)
		else:
			return False			

	# Method hear start
	def escuta(self):
	#setando todas as mensagens no grupo
		post = self.driver.find_elements_by_class_name('_3_7SH')
	#pegando o indice da ultima mensagem
		ultima = len(post) - 1
	#texto da ultima conversa
		texto = post[ultima].find_element_by_css_selector('span.selectable-text').text
		return texto

	# Method Responder
	def responde(self,texto):
	#setando a resposta do bot na variavel response
		response = self.bot.get_response(texto)
	#transforma em string a resposta
		response = str(response)
	#coloca o prefixo bot no inicio
		response = '*bot :* _'+ response +'_'
	#setando a caixa de mensagem e atribuindo a resposta e enviando-a
		self.caixa_de_mensagem = self.driver.find_element_by_class_name('_2S1VP')
		self.caixa_de_mensagem.send_keys(response)
		time.sleep(1)
		self.botao_enviar = self.driver.find_element_by_class_name('_35EW6')
		self.botao_enviar.click()

	# Method trainer
	def treina(self,nome_pasta):
	#Listamos todos os arquivos dentro da pasta e para cada linha treinamos nosso bot.
		for treino in os.listdir(nome_pasta):
			conversas = open(nome_pasta+'/'+treino, 'r').readlines()
			trainer = ListTrainer(self.bot)
			trainer.train(conversas)















































