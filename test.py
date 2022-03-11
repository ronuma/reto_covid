import graph

# Esto es lo que devuelve el simulador, pero sigo sin saber en qué forma (tipo de dato)
# 1|0|0|0|0|0|1|0|24.71|99.90|1|1|0|0|0

rawData = [
    "1|0|0|0|0|0|1|0|36.50|99.90|1|1|0|0|0",
    "1|0|0|0|0|0|1|0|37.20|94.20|1|1|0|0|0",
    "1|0|0|0|0|0|1|0|36.22|88.56|1|1|0|0|0",
]

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