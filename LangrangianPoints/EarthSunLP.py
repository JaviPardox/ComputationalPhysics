# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 01:47:59 2019

@author: Javier Pardo
         with the help of Dr. Nelson
"""

from scipy import optimize
from numpy import pi,sqrt

#DECLARING PARAMETERS
G = (4*pi**2)
Ms = 1
Me = 3.003e-6
Rs = (Me)/(Ms + Me)
Re = (Ms)/(Ms + Me)
w = 2*pi

#INITIALIZING LAGRANGE POINTS
x_lagrange = 0
y_lagrange = 0

def compute_lagrange_points(x):
    
    #EQUATION FOR X AXIS, DIVIDED IN TWO PARTS
    left1_x = (G*Ms*(x[0] + Rs))/(((x[0] + Rs)**2 + x[1]**2)**1.5)
    left2_x = (G*Me*(x[0] - Re))/(((x[0] - Re)**2 + x[1]**2)**1.5)
    x_lagrange = left1_x + left2_x - ((w**2)*x[0]) 
    
    #EQUATION FOR Y AXIS, DIVIDED IN TWO PARTS
    left1_y = (G*Ms*x[1])/(((x[0] + Rs)**2 + x[1]**2)**1.5)
    left2_y = (G*Me*x[1])/(((x[0] - Re)**2 + x[1]**2)**1.5)
    y_lagrange = left1_y + left2_y - ((w**2)*x[1])
    
    #RETURN AN ARRAY
    return [x_lagrange,y_lagrange]


#DISTANCE BETWEEN EARTH AND SUN IS 1AU
#THE ORIGIN IS AT THE SUN
#IN DISTANCE WE WORK WITH AU, HENCE EARTH IS AT Y=0,X=1 
#L1,L2,L3 ARE ALONG THE X AXIS, Y=0
    
#L1 HAS TO BE VERY CLOSE TO EARTH BECAUSE OF THE MASS RATIO
#GUESS IS X=0.99
l1 = optimize.root(compute_lagrange_points, [0.99,0])

#L2 HAS TO BE VERY CLOSE TO EARTH BUT ON THE OPPOSITE SIDE
#GUESS IS X=1.01
l2 = optimize.root(compute_lagrange_points, [1.01,0])

#L3 IS AT ONE AU OPPOSITE FROM EARTH
#GUESS IS X=-1
l3 = optimize.root(compute_lagrange_points, [-1,0])

#L5 AND L4 FORM AN EQUILATERAL TRIANGLE WITH THE SUN AND EARTH
#FOR L4 AND L5 X AXIS, IT IS IN THE MIDDLE BETWEEN EARTH AND SUN
#GUESS IS X=0.5

#FOR L4 Y AXIS, WE CAN GUESS USING THE SIN OF 60
#GUESS IS Y=SIN(60)
l4 = optimize.root(compute_lagrange_points, [0.5,(sqrt(3)/2)])

#FOR L5 Y AXIS, WE GUESS USING THE SIN OF 60, BUT THIS TIME NEGATIVE
#GUESS IS Y=-SIN(60)
l5 = optimize.root(compute_lagrange_points, [0.5,-(sqrt(3)/2)])

#PRINT LAGRANGE POINTS
print(l1.x)
print(l2.x)
print(l3.x)
print(l4.x)
print(l5.x)
