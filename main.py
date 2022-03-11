import serial

# bloque ARDUINO para tomar los valores directamente de arduino
try:
    arduino = serial.Serial("COM4", 9600) # ponemos primero el número del puerto, dependiendo de la compu
except:
    print("Check the port")

rawData = []
count = 0

while count < 3:
    rawData.append(str(arduino.readline()))
    count += 1

print(rawData)
arduino.close()

# bloque PYTHON para tomar los valores y crear arreglos
delimiter = "|"
count = 0
oxig = [0.00, 0.00, 0.00, 0.00, 0.00] 
oxig2 = [0.00, 0.00, 0.00, 0.00, 0.00]
o = []

for read in rawData:
    read = read.split(delimiter)
    print(read[12])
    if count > 5 : continue
    oxig[count] = read[12]
    print(oxig[count])
    o = float(oxig[count])
    oxig2[count] = o
    count += 1