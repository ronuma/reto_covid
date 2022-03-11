import numpy as np
import matplotlib.pyplot as plt

def create(array, label):
    yt = np.array(array) # se transforma a vector

    y = np.reshape(yt, (-1, 1)) # tranformar el vector a vector columna

    u = np.ones(len(array))

    d = [ 1, 2, 3 ]

    xt = np.vstack((u,d))

    x = np.transpose(xt)

    B = np.dot(np.linalg.inv(np.dot(xt,x)), np.dot(xt,y))

    yest = np.dot(x,B)

    plt.scatter(d,yt)
    plt.plot(d,yest)
    plt.xlabel("Frecuencia")
    plt.ylabel(label)
    plt.show()