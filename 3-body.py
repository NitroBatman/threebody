# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 20:58:29 2017

@author: User
"""
import numpy as np
import matplotlib.pyplot as plt

m1 = 5.9724 #6
x1 = -1.747 #4
y1 =  0 #0

m2 = 10.07346 #2
x2 = 35 #-6
y2 =  0 #0

w = 0.05

G = 1 #1 #m^3 kg^-1 s^-2

x = np.arange(-50, 50, 0.08)
y = np.arange(-50, 50, 0.08)

def V(x,y):
    return - G*m1/(np.sqrt((x - x1)**2 + (y - y1)**2)) - G*m2/(np.sqrt((x - x2)**2 + (y - y2)**2)) + ((w**2) * (m1 + m2) * (x**2 + y**2)) / 2

def Vcen(x,y,w):
    return -(w**2*(m1+m2)*np.sqrt((x - x1)**2 + (y - y1)**2))/2

X, Y = np.meshgrid(x, y)
Z = V(X, Y)

for i in range(len(x)):
    for j in range(len(y)):
        if(Z[i][j] < -1.5):
            Z[i][j] = -1.5

Z2 = Vcen(X, Y, w)

def grad(x, y):
    return G*m1/((x - x1)**2 + (y - y1)**2) + G*m2/((x - x2)**2 + (y - y2)**2) + w**2*(m1+m2)*np.sqrt(x**2 + y**2)

L = grad(X, Y)
t = 0
minix = []
miniy = []
for i in range(len(x)-1):
    for j in range(len(y)-1):
        if(L[i][j] < L[i+1][j] and L[i][j] < L[i][j-1] and L[i][j] < L[i-1][j] and L[i][j] < L[i][j+1]):
            minix.append(x[i])
            miniy.append(y[i])
            t += 1
            print(L[i][j])
            print(t)

print(minix , miniy)
plt.scatter(minix,miniy, s = 1)
CS = plt.contour(X, Y, Z, 20)
plt.clabel(CS, inline = 1, fontsize = 10)
#plt.show()
plt.savefig("3body.png")

#plt.xlim(33,37) < v
#plt.ylim(-2,2) <Drugo telo

#CS2 = plt.contour(X, Y, Z2, 10)
#plt.clabel(CS2, inline = 1, fontsize = 8)

# function = lambda argument: function( as in, the thing that does the thing )
