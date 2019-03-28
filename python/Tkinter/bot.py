from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyttsx3

bot = ChatBot('Nuke')

trainer = ListTrainer(bot)

trainer.train([
	'oi','olá','como vai?','bem e você?','bem também',
	'que bom','animado hoje?','só um pouco'
])

def bot_(perg):
	resp = bot.get_response(perg)
	try:
		engine = pyttsx3.init()
		engine.say(resp)
		engine.runAndWait()
		return resp
	except:
		print('Não foi possível falar!')