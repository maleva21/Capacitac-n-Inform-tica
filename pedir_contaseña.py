#Programa que pida nombre de 
#usuario y contraseÑa de empleado

import time


password="cangrejo"
correcto=0
intentos=1

print("Bienvenido a Carl's Jr., intoduzca la contraseña") 

while(correcto==0) & (intentos<=4):
	intento=input("Intoduce tu contraseña:")
	if intento==password:
		correcto=1
		print("Tu contaseña es correcta!")
	else:
		time.sleep(5)
		print("La contraseña que has introducido es incorrecta")
		intentos=intentos +1 
		if intentos>4:
			print("Has introducido demasiadas contraseñas incorrectas")
