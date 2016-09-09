#coding=utf-8

nombre = input("Dime tu nombre:")
print("Hola %s, contesta la pregunta por favor" % nombre)

edad = int(input("%s dime tu edad: " % (nombre)))

nombre2 = input("Dime tu nombre:")
print("Hola %s, contesta la pregunta por favor" % (nombre2))

edad2 = int(input("%s dime tu edad:" % (nombre2)))

if(edad>edad2):
	print("%s es más grande que %s" % (nombre , nombre2))
elif(edad2>edad):
	print("%s es más grande que %s" % (nombre2 , nombre))
else:
	print("%s tiene la misma edad que %s" % (nombre , nombre2))
