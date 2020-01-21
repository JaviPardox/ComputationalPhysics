# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 17:28:52 2019

@author: Javier Pardo
         with the help of Dr. Nelson
"""

import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

def atoms_arrangement(atoms,m,k):
    #Build the arrays
    array = (atoms,atoms)
    M = np.zeros(array)
    for i in range(atoms):
        M[i,i] = m[i]
    
    K = np.zeros(array)
    for i in range(atoms):
        K[i,i] = 2*k
    for i in range(atoms-1):
        K[i,i+1] = -1*k
        K[i+1,i] = -1*k   
    #Find the eigenvalue
    W = linalg.eig(M,K)
    W = np.real(W[0])
    
    return W**2




#atoms = int(input("Enter the number of atoms: "))
#m = np.zeros(atoms)
#print("for" ,atoms, "atoms, enter the masses (in incresing order)")
#for i in range(atoms):
#    count = i+1
#    m[i] = int(input("Enter mass%d: "%count))
#k = int(input("Enter the value for k: "))


plt.close('all')
k = 2

atoms = 4
fig, ax = plt.subplots()
m = [2,2,2,2]
f = atoms_arrangement(atoms,m,k)
ax.scatter(m,f)
ax.set_title("angular frequency of 4 atoms of the same mass")
ax.set_xlabel("mass")
ax.set_ylabel("angular frequency")

fig, bx = plt.subplots()
m = [2,4,6,8]
f = atoms_arrangement(atoms,m,k)
bx.scatter(m,f)
bx.set_title("angular frequency of 4 atoms which double in mass")
bx.set_xlabel("mass")
bx.set_ylabel("angular frequency")

fig, cx = plt.subplots()
m = [2,4,8,16]
f = atoms_arrangement(atoms,m,k)
cx.scatter(m,f)
cx.set_title("angular frequency of 4 atoms which mass increases 2^n")
cx.set_xlabel("mass")
cx.set_ylabel("angular frequency")

#Same thing but increasing the values of the mass by one order of magnitude

fig, dx = plt.subplots()
m = [20,20,20,20]
f = atoms_arrangement(atoms,m,k)
dx.scatter(m,f)
dx.set_title("angular frequency of 4 atoms of the same mass")
dx.set_xlabel("mass")
dx.set_ylabel("angular frequency")

fig, ex = plt.subplots()
m = [20,40,60,80]
f = atoms_arrangement(atoms,m,k)
ex.scatter(m,f)
ex.set_title("angular frequency of 4 atoms which double in mass")
ex.set_xlabel("mass")
ex.set_ylabel("angular frequency")

