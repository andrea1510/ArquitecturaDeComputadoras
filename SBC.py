from gpio import *
from time import *

puerta = 0
ventana = 2
garage = 1
switch8 = 3
switch10 = 4
switch9 = 5
webcam1 = 6
webcam2 = 7
siren = 8
sensor = 9

def main():
	pinMode(switch8, IN) #pin de entrada del switch de la puerta
	pinMode(switch9, IN) #pin de entrada del switch del garaje
	pinMode(switch10, IN) #pin de entrada del switch del ventana
	pinMode(sensor, IN) #pin de salida del sensor
	pinMode(puerta, OUT) #pin de salida de la puerta
	pinMode(ventana, OUT) #pin de salida de la ventana
	pinMode(garage, OUT) #pin de salida del garaje
	pinMode(webcam1, OUT) #pin de salida de la webcam1
	pinMode(webcam2, OUT) #pin de salida de la webcam2
	pinMode(siren, OUT) #pin de salida de la sirena
	while True:
		#apertura de puerta según el rocket switch
		if digitalRead(switch8):
			customWrite(puerta, "1")
		else:
			customWrite(puerta, "0")
		#apertura de ventana según el rocket switch
		if digitalRead(switch10):
			customWrite(ventana, "1")
		else:
			customWrite(ventana, "0")
		#apertura de garage según el rocket switch
		if digitalRead(switch9):
			customWrite(garage, "1")
		else:
			customWrite(garage, "0")
		#encendido de camaras según el rocket switch
		if digitalRead(switch8):
			customWrite(webcam1, "0")
			customWrite(webcam2, "0")
		else:
			customWrite(webcam1, "1")
			customWrite(webcam2, "1")
		#encendido de la sirena segun el sensor
		if digitalRead(sensor):
			customWrite(siren, "1")
		else:
			customWrite(siren, "0")

if __name__ == "__main__":
	main()
