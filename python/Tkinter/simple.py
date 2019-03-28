from tkinter import *
import bot
import time
class Myapp:	
	def __init__(self, intTK):
		#variaveis
		bot = '...' # resposta do bot
		eu = '' # pergunta do usuario
	
		#Defininvo título
		intTK.title('BOT - v1')
		
		self.fr1 = Frame(intTK, background='#b03060')
		self.fr1.pack()
		
		self.fr2 = Frame(intTK, background='#b03060')
		self.fr2.pack()
		#Meus campos
		self.lb1 = Label(self.fr1,font=('Rockwell','18'), text='Eu: ', background='#b03060', foreground='white')
		self.lb1.grid(row=0, sticky=W)
		
		#Campo de entrada
		self.ed1 = Entry(self.fr1,font=('Rockwell','18'),width=25, bd=0, textvariable=eu, background='#b03060', foreground='white')
		eu = 'ola mundo'
		self.ed1.bind('<Return>',self.key)
		self.ed1.grid(column=1,row=0)
		self.ed1.focus_set()
		
		#Campos do bot
		self.lb2 = Label(self.fr2,font=('Rockwell','18'),width=25, text='Bot:', background='#b03060', foreground='white', anchor=W)
		self.lb2.pack()
		
		self.lb2 = Message(self.fr2,font=('Rockwell','18'),width=290, text=bot, background='#b03060', foreground='white')
		self.lb2.pack()		


	#função de limpar e de atribuição
	def key(self, event):
		eu = self.ed1.get()
		self.lb2['text'] = bot.bot_(eu)
		self.ed1.delete(0, 'end')
		print(eu)
		
	
	
	
	
	
raiz=Tk()
raiz.configure(background='#b03060')
raiz.resizable(width=False,height=False)
raiz.geometry('360x300')
Myapp(raiz)
raiz.mainloop()