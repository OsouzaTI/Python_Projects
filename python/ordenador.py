import random, time, os
trigger = True
verifica = 0
lista = []

for i in range(10):
	lista.append(random.randint(0, 100))
print(lista)
while(trigger):
	verifica = 0
	os.system('clear')
	for i in range(len(lista)-1):
		if( lista[i] > lista[i+1] ):
			temp = lista[i]
			lista[i] = lista[i+1]
			lista[i+1] = temp
		else:
			verifica += 1
	if(verifica == len(lista)-1 ):
		print("Acabou")
		trigger = False
	print(lista)
	print("Verifica = %d, Tamanho da lista: %d "%(verifica, len(lista)))
	time.sleep(1)
