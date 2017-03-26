#RSP_emulator ver a0.2
import random

ia_op= ["piedra", "papel", "tijeras"]#opciones de la IA
ia= (random.choice(ia_op))#tomamos la eleccion randomm de la IA

play = input("¿Deseas Jugar vs IA?\n\ny=(YES)\nn=(NO)\n")

if play == "y":
	opciones= int(input("Elige una opcion:\n\n1.Piedra\n2.Papel.\n3.Tijera\n"))
	
	if opciones == 1:
		piedra = "piedra"

		if ia == "papel":
			print("Ha ganado con la maquina con{} y tu tenias {}".format(ia, piedra))
		elif ia == "piedra":
			print("has empatado con {} y la maquina tenia {}".format(piedra, ia))
		else:
			print("Has ganado con {} y la maquina tenia {}".format(piedra, ia))
	elif opciones == 2:
		papel = "papel"
		if ia == "tijeras":
			print("Ha ganado la maquina con{} y tu tenias {}".format(ia, papel))
		elif ia == "papel":
			print("Has empatado con {} y la maquina tenia {}".format(papel, ia))
		else:
			print("Has ganado con {} y la maquina tenia {}".format(papel, ia))
	elif opciones == 3:
		tijeras = "tijeras"
		if ia == "piedra":
			print("Ha ganado la maquina con {} y tu tenias {}".format(ia, tijeras))
		elif ia == "tijeras":
			print("Has empatado con {} y la maquina tenia {}".format(tijeras, ia))
		else:
			print("Has ganado con {} y la maquina tenia {}".format(tijeras, ia))
	else:
		print("Opcion invalida debes leer")
elif play == "n":
	print("¿Pa que ejecutas el juego si no quieres jugar?")
else:
	print("Opcion invalida, compra lentes.")