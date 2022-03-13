import serial
import graph

# bloque ARDUINO para tomar los valores directamente de arduino
try:
    arduino = serial.Serial()
    arduino.port = 'COM5'
    arduino.baudrate = 9600
    arduino.open()
except:
    print("Check the port")

rawData = []
count = 0

while count < 3: # especificar la condicion a partir del número de datos a evaluar
    rawData.append(str(arduino.readline()))
    count += 1

arduino.close()

# bloque PYTHON para graficar
delimiter = "|"
oxig = []
temp = []

# itera en los datos, sextrae los valores y los pasa a sus arreglos correspondientes
for read in rawData:
    read = read.split(delimiter)
    oxig.append(read[9])
    temp.append(read[8])

# convierte los valores de los arreglos a float porque vienen como strings
oxig = [float(x) for x in oxig]
temp = [float(x) for x in temp]

# se crean las graficas
graph.create(oxig, "Oxigenacion")
graph.create(temp, "Temperatura")