# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random, os, sys

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.won  = False
		self.over = False
		self.error = 0
		self.letterCorrect = []
	# Método para adivinhar a letra
	def guess(self, letter):
		if list(self.word).count(letter) == 0:
			self.error += 1
		else:
			self.letterCorrect.append(letter)

		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		if(self.error >= 6):
			self.over = True
			
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		j = 0
		for i in list(self.word):
			if self.letterCorrect.count(i) != 0:
				j += 1
		
		if j == len(list(self.word)):
			self.won = True

	# Método para não mostrar a letra no board
	def hide_word(self):
		if(sys.platform == "win32" or sys.platform == "cygwin"):
			os.system("cls")
		else:
			os.system("clear")

		for i in list(self.word):
			if self.letterCorrect.count(i):
				print(i, end='')
			else:	
				print('_', end='')
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		if(not self.over):
			self.hide_word()
			print(board[self.error])
		self.hangman_won()
		self.hangman_over()

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())	
	game.hide_word()
	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while(not game.won and not game.over):
		letter = input()
		game.guess(letter)
		# Verifica o status do jogo
		game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.won:
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
