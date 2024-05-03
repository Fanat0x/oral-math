import matplotlib.pyplot as plt
from math import cos, sin, radians as rad

import tkinter as tk
from tkinter import ttk

#X = [2, 6, 3.5, 8, 8, 9, 9, 6, 6, 2.5]
#Y = [7, 7, 9.5, 9, 7, 5, 3.3, 3, 1.3, 2]

X = [4.0, 8.6, 8.2, 9.4, 8.0, 6.0, 2.5, 2.0, 6.0]
Y = [9.6, 8.0, 4.6, 5.4, 3.2, 2.0, 2.0, 7.0, 7.0]

#D = [0.84, 1, -0.1, -5.5, -10, -9.2, -0.25, -1, -0.5, 0.8]
DX = [3.0, -3.0, 2.5, 0.4, -5.0, 1.0, -2.0, 2.0, -0.4, 3.0]
DY = [-0.1, -3.5, -0.5, -3.0, 0.0, -3.0, 2.0, 1.5, 1.0, -0.1]
D = []

def Phi1(t):
    return 2 * t**3 - 3 * t**2 + 1
    #return ((t-1)**2)*(2*t+1)

def Phi2(t):
    return t**3 - 2 * t**2 + t
    #return (t**2)*(-2*t+3)

def Phi3(t):
    return -2 * t**3 + 3 * t**2
    #return ((t-1)**2)*t

def Phi4(t):
    return t**3 - t**2
    #return (t**2)*(t-1)

def verifPhi1():
    result = Phi1(0)
    return result == 1
def verifPhi2():
    result = Phi2(0)
    return result == 0
def verifPhi3():
    result = Phi3(1)
    return result == 0

def Hermite(t, aY, bY, aD, bD):    
    XH = []
    YH = []

    P1 = Phi1(t)
    P2 = Phi2(t)
    P3 = Phi3(t)
    P4 = Phi4(t)

    return (P1*aY+P2*aD+P3*bY+P4*bD)
    
    #for i in range(n+1):
    #    t = i/n
    #    XH.append(x1+(x2-x1)*t)
    #    YH.append(y1*Phi1(t)+y2*Phi2(t)+d1*Phi3(t)+d2*Phi4(t))
        
    #if x2 < x1:
        #XH = XH[::-1]
        #YH = YH[::-1]
    
    #return XH, YH

def GetCoord(n, X, Y, D):
    HX = []
    HY = []
    for i in range(len(X)-1):
        if X[i+1] < X[i]:
            tempX = []
            tempY = []
            for j in range(n, 0, -1):
                t = j/(n-1)
                tempX.append(X[i]+(X[i+1]-X[i])*t)
                tempY.append(Hermite(t, Y[i], Y[i+1], D[i], D[i+1]))
            HX = HX + tempX[::-1]
            HY = HY + tempY[::-1]
        else:
            for j in range(n):
                t = j / (n-1)
                HX.append(X[i]+(X[i+1]-X[i])*t)
                HY.append(Hermite(t, Y[i], Y[i+1], D[i], D[i+1]))
    
    HX.append(X[0])
    HY.append(Hermite(1, Y[-1], Y[0], D[-1], D[0]))
    #tempX, tempY = Hermite(n, X[-1], X[0], Y[-1], Y[0], D[-1], D[0])
    #HX = HX + tempX
    #HY = HY + tempY
        
    return HX, HY

# Main function
def main():
    # Retrives data from GUI
    n = int(n_entry.get())
    #Separate the values in a list and convert them to floats
    X = [float(x) for x in X_entry.get().split(",")]
    Y = [float(y) for y in Y_entry.get().split(",")]
    DX = [float(x) for x in DX_entry.get().split(",")]
    DY = [float(y) for y in DY_entry.get().split(",")]
    D = []
    
    #A vérifier
    for i in range(len(DY)-1):
        D.append(abs(DY[i+1])-abs(DY[i])/abs(DX[i+1])-abs(DX[i]))

    pX, pY = GetCoord(n, X, Y, D)

    plt.plot(pX, pY)
    plt.show()
    
############## TKINTER ##############

root = tk.Tk()
root.title("HermGUI")
root.resizable(width=False, height=False)

def check_n(action, value):
    if action == '1':
        if value.isdigit():
            return True
        else:
            return False
    else:
        return True

n_checker = root.register(check_n)
n_label = tk.Label(root, text="Enter number of interpolation points n:")
n_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5)
n_entry = tk.Entry(root, width=4, validate="key", validatecommand=(n_checker, '%d', '%P'))
n_entry.grid(row=0, column=1, columnspan=1, padx=10, pady=5)
n_entry.insert(0, 100)

X_label = tk.Label(root, text="Enter points' X coordinates:")
X_label.grid(row=2, column=0, padx=10, pady=5)
X_entry = tk.Entry(root, width=31)
X_entry.grid(row=3, column=0, padx=10, pady=5)
X_entry.insert(0, "4.0, 8.6, 8.2, 9.4, 8.0, 6.0, 2.5, 2.0, 6.0")

Y_label = tk.Label(root, text="Enter points' Y coordinates:")
Y_label.grid(row=4, column=0, padx=10, pady=5)
Y_entry = tk.Entry(root, width=31)
Y_entry.grid(row=5, column=0, padx=10, pady=5)
Y_entry.insert(0, "9.6, 8.0, 4.6, 5.4, 3.2, 2.0, 2.0, 7.0, 7.0")

DX_label = tk.Label(root, text="Enter derivatives' X coordinates:")
DX_label.grid(row=2, column=1, padx=10, pady=5)
DX_entry = tk.Entry(root, width=31)
DX_entry.grid(row=3, column=1, padx=10, pady=5)
DX_entry.insert(0, "3.0, -3.0, 2.5, 0.4, -5.0, 1.0, -2.0, 2.0, -0.4, 3.0")

DY_label = tk.Label(root, text="Enter derivatives' Y coordinates:")
DY_label.grid(row=4, column=1, padx=10, pady=5)
DY_entry = tk.Entry(root, width=31)
DY_entry.grid(row=5, column=1, padx=10, pady=5)
DY_entry.insert(0, "-0.1, -3.5, -0.5, -3.0, 0.0, -3.0, 2.0, 1.5, 1.0, -0.1")

confirm_button = tk.Button(root, text="Confirm", command=main)
confirm_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
