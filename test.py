import graph

# Esto es lo que devuelve el simulador, pero sigo sin saber en qué forma (tipo de dato)
# 1|0|0|0|0|0|1|0|24.71|99.90|1|1|0|0|0

rawData = [
    "1|0|0|0|0|0|1|0|36.50|99.90|1|1|0|0|0",
    "1|0|0|0|0|0|1|0|37.20|94.20|1|1|0|0|0",
    "1|0|0|0|0|0|1|0|36.22|88.56|1|1|0|0|0",
]

# bloque PYTHON para tomar los valores y crear arreglos
delimiter = "|"
oxig = []
temp = []

for read in rawData:
    read = read.split(delimiter)
    oxig.append(read[9])
    temp.append(read[8])

graph.create(oxig, "Oxigenacion")