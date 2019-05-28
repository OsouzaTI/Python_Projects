#importando a biblioteca nativa e a classe
import re
from bot import wppbot

#setando o bot com o nome
bot = wppbot('Robo')
#treinando o bot com o arquivo que esta dentro da pasta que passamos
bot.treina('lists')
#informa a pessoa/grupo que vamos conversar
bot.inicia('Camila S2')
#bot.inicia('Teste')
#bot.inicia('Camila S2')
#Setamos nossa saudação a entrar no grupo com duas frases em uma lista.
bot.saudacao('')
#Setamos a váriável último texto sem nada.
ultimo_texto = ''
#Sempre será true então nunca irá para nosso script.
while True:
#Usamos o método de escuta que irá setar na variável texto.
	try:
		texto = bot.escuta()
	#Agora validamos se o texto enviado no grupo/pessoa é o mesmo que o último já lido.
	#Essa validação serve para que o bot não fique respondendo o mesmo texto sempre.
	#Validamos também se no texto possuí o comando :: no início para que ele responda.
		if texto != ultimo_texto and re.match(r'^!', texto):
	#Passando na validação setamos o texto como último texto.
			ultimo_texto = texto
	#Retiramos nosso comando de ativar do bot da string.
			texto = texto.replace('!', '')
	#Tratamos para deixar o texto em caracteres minúsculos.
			texto = texto.lower()
	#Enviamos para o método responde que irá responder no grupo/pessoa.
			bot.responde(texto)
	except:
		pass