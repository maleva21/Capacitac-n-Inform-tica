#coding=utf-8
#Programa para tomar orden 

costo=0
pedido=1
print("Hola cliente, qué  llevará hoy?")
print("""1. Famous star $90 
2.Papas grandes $40
3. Santa fe $100
4. Soda grande $30 """)

while (pedido<5): 
	pedido = int(input("Dame tu pedido:"))


	if(pedido==1):
		costo=costo+ 90 
	elif(pedido==2):
		costo=costo+40
	elif(pedido==3):
		costo=costo+100
	elif(pedido==4):
		costo=costo+30

	print("Su orden es de un total de $%s," %(costo)) 
	
else: 
		print("Gracias por su visita, buen día.")
