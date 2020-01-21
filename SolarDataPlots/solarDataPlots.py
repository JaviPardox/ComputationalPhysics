# -*- coding: utf-8 -*-
"""
This script demonstrates how to load data from a file into a 40 by 40 by 3 array.
    
Created on Tue Sep 13 07:59:54 2016

@author: Javier Pardo
with help from Dr. Nelson
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
plt.close('all') #Close all open figures

#Auxiliar function to plot a nicer vector field
#Helps with the coloring 
def E(x,y):
    r = np.sqrt(x**6 + y**6)
    return (x/r,y/r)


temp = np.fromfile('velocity_vectors.txt', sep=', ') #Load all of the data into a 1D array
vel = np.reshape(temp,(40,40,3)) #Rearrange the data inot a 40 by 40 by 3 array

#Create a grid for the limits
y,x = np.mgrid[slice(0,90,2.25),slice(0,90,2.25)]

#Final step for a better coloring
Ex,Ey = E(vel[:,:,1],vel[:,:,2])
EE=np.sqrt(Ex**2+Ey**2)

fig, ax = plt.subplots()
fig1, bx = plt.subplots()
fig2, cx = plt.subplots()
fig3, dx = plt.subplots()
fig4, ex = plt.subplots()
fig5, fx = plt.subplots()

#   FIGURE 1
#Density plot of Vx
#Can me done by just selecting the whole array of x values
#In this case it's 0
c = ax.pcolor(x,y,vel[:,:,0]) #x
ax.set_title("Vx (m/s)")
ax.set_xlabel("Position (Mm)")
ax.set_ylabel("Position (Mm)")
fig.colorbar(c, ax=ax)

#   FIGURE 2
#Density plot of Vy
#Can me done by just selecting the whole array of x values
#In this case it's 1
c = bx.pcolor(x,y,vel[:,:,1]) #y
bx.set_title("Vy (m/s)")
bx.set_xlabel("Position (Mm)")
bx.set_ylabel("Position (Mm)")
fig1.colorbar(c, ax=bx)

#   FIGURE 3
#Density plot of Vz
#Can me done by just selecting the whole array of x values
#In this case it's 2
e = cx.pcolor(x,y,vel[:,:,2]) #z
cx.set_title("Vz (m/s)")
cx.set_xlabel("Position (Mm)")
cx.set_ylabel("Position (Mm)")
fig2.colorbar(e, ax=cx)

#   FIGURE 4
#Calculate Horizontal velocity by adding Vy and Vz
#Again, done by selecting the whole array and adding them up
dx.quiver(np.arange(0,90,2.25),np.arange(0,90,2.25),vel[:,:,1],vel[:,:,2],EE,cmap='coolwarm',norm=colors.LogNorm(vmin=EE.min(),vmax=EE.max()))
dx.set_title("Horizontal velocity")
dx.set_xlabel("Position (Mm)")
dx.set_ylabel("Position (Mm)") 

#   FIGURE 5
#The specific Kinetic Energy is computed by adding all velocities
#Squaring them up, and finally dividing it by 2
specific_ke = (1/2)*((vel[:,:,0])**2 + (vel[:,:,1])**2 + (vel[:,:,2])**2)
f = ex.pcolor(x,y,specific_ke) #specific
ex.set_title("Specific Kinetic Energy (J)")
ex.set_xlabel("Position (Mm)")
ex.set_ylabel("Position (Mm)")
fig4.colorbar(f, ax=ex)

#   FIGURE 6
#Average kinetic energy over the y direction
#Done by adding Vy values  of every single column
#And storing them in a single array
avg_ke_y = sum(vel[:,:,1]**2)/(len(vel[:,:,1])*2)
fx.plot(np.arange(0,90,2.25),avg_ke_y)
fx.set_title("Average Specific Kinetic Energy over Y (m/s)")
fx.set_xlabel("Position (Mm)")
fx.set_ylabel("Average Specific Kinetic Energy (m/s)")
fx.grid()



plt.show()

