#RSP_emulator ver a0.1

opciones = int(input("\nElige una opcion:\n\n1. Piedra \n2. Papel \n3. Tijeras\n"))

if opciones == 1:
	piedra = "piedra"
	print("{} le gana a tijeras pero pierde contra papel".format(piedra))
elif opciones == 2:
	papel = "papel"
	print("{} le gana a piedra pero pierde contra tijeras".format(papel))
elif opciones == 3:
	tijeras = "tijeras"
	print("{} le gana a papel pero pierde contra piedra".format(tijeras))
else:
	print("opcion no valida")