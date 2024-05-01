import matplotlib.pyplot as plt
from math import cos, sin, radians as rad

X = [2, 6, 3.5, 8, 8, 9, 9, 6, 6, 2.5]
Y = [7, 7, 9.5, 9, 7, 5, 3.3, 3, 1.3, 2]

D = [0.84, 1, -0.1, -0.5, -1, -1.2, -0.25, -1, -0.5, 0.8]
#D = []

HermX = []
HermY = []

def C1(t):
    return ((t-1)**2)*(2*t+1)

def C2(t):
    return (t**2)*(-2*t+3)

def C3(t):
    return ((t-1)**2)*t

def C4(t):
    return (t**2)*(t-1)

def verifC1():
    result = C1(0)
    return result == 1
def verifC2():
    result = C2(0)
    return result == 0
def verifC3():
    result = C3(1)
    return result == 0

def Hermite(n, x1, x2, y1, y2, d1, d2):    
    XH = []
    YH = []
    
    for i in range(n+1):
        t = i/n
        XH.append(x1+(x2-x1)*t)
        YH.append(y1*C1(t)+y2*C2(t)+d1*C3(t)+d2*C4(t))
        
    #if x2 < x1:
        #XH = XH[::-1]
        #YH = YH[::-1]
    
    return XH, YH

def GetDrawing(n, X, Y, D):
    HX = []
    HY = []
    for i in range(len(X)-1):
        tempX, tempY = Hermite(n, X[i], X[i+1], Y[i], Y[i+1], D[i], D[i+1])
        HX = HX + tempX
        HY = HY + tempY
    
    tempX, tempY = Hermite(n, X[-1], X[0], Y[-1], Y[0], D[-1], D[0])
    HX = HX + tempX
    HY = HY + tempY
        
    return HX, HY

#A vérifier
#for i in range(len(Y)-1):
#    D.append((Y[i+1]-Y[i])/(i+i-1)-i)
#D.append((Y[0]-Y[-1])/(i+i-1)-i)
print(len(D), len(X))
print(D)

n = int(input("Donnez un nombre de points n: "))

pX, pY = GetDrawing(n, X, Y, D)

plt.plot(pX, pY)
plt.show()