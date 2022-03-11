import numpy as np
import matplotlib.pyplot as plt

def create(array, label):
    yt = np.array(array) # se transforma a vector
    print("-----yt-----")
    print(yt)

    y = np.reshape(yt, (-1, 1)) # tranformar el vector a vector columna
    print("-----y-----")
    print(y)

    u = np.ones(len(array))
    print("-----u-----")
    print(u)

    d = [ 1, 2, 3 ]
    print("-----d-----")
    print(d)

    xt = np.vstack((u,d))
    print("-----xt-----")
    print(xt)

    x = np.transpose(xt)
    print("-----x-----")
    print(x)

    B = np.dot(np.linalg.inv(np.dot(xt,x)), np.dot(xt,y))
    print("-----B-----")
    print(B)

    yest = np.dot(x,B)
    print("-----yest-----")
    print(yest)

    plt.scatter(d,yt)
    plt.plot(d,yest)
    plt.xlabel("Frecuencia")
    plt.ylabel(label)
    plt.show()