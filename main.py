import serial
import graph

# bloque ARDUINO para tomar los valores directamente de arduino
try:
    # ponemos primero el número del puerto, dependiendo de la compu
    arduino = serial.Serial()
    arduino.port = 'COM7'
    arduino.open()
    arduino.baudrate = 9600
    arduino.timeout = 0
except:
    print("Check the port")

rawData = []
count = 0

while count < 3:
    rawData.append(str(arduino.readline()))
    count += 1

print(rawData)
arduino.close()

# bloque PYTHON para graficar
delimiter = "|"
oxig = []
temp = []

# itera en los datos, extrae los valores y los pasa a sus arreglos correspondientes
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