from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3

bot = ChatBot('Nuke')

trainer = ListTrainer(bot)

trainer.train([
	'oi','olá','como vai?','bem e você?','bem também',
	'que bom','animado hoje?','só um pouco'
])

while True:
	perg = input('You:')
	resp = bot.get_response(perg)
	print('Bot:'+str(resp))

	try:
		engine = pyttsx3.init()
		engine.say(resp)
		engine.runAndWait()
	except:
		print('Não foi possível falar!')
