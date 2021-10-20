#!/usr/bin/env python
# coding: utf-8

# In[31]:


import math
import random
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(33)

X = -5 + (13+5) * np.random.rand(10000)
Y = -5 + (13+5) * np.random.rand(10000)

#plt.scatter(X,Y)

plt.plot([-4,-4,6,-4],[-4,6,-4,-4],  color='red') 
plt.plot([-3,-3,6,-3],[-1.5,9.5,-1.5,-1.5],  color='green')
plt.plot([-5,-5,13,-5],[-5,13,-5,-5], color='yellow')


#rectangle = plt.Rectangle((-7,-15), 24, 32, fill = False,ec="red")
#plt.gca().add_patch(rectangle)




#rectangle = plt.Rectangle((-7,-15), 24, 32, fill = False,ec="red")
#plt.gca().add_patch(rectangle)
plt.xticks([-1, -2, -3, -4,-5,-6,-7,0,1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15])    # changing x scale by own
plt.yticks([-1, -3, -5, -7,-9,-11,0,1,3,5,7,9,11,12,13,14,15])    # changing x scale by own
#plt.show()


def area(x1, y1, x2, y2, x3, y3):
 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2.0)
 
 
# A function to check whether point (x, y)
# lies inside the triangle formed by
#(x1, y1), (x2, y2) and (x3, y3)
def isInside(x1, y1, x2, y2, x3, y3, x, y):
 
   
    A = area (x1, y1, x2, y2, x3, y3)
    
   
    A1 = area (x, y, x2, y2, x3, y3)
     
 
    A2 = area (x1, y1, x, y, x3, y3)
     
   
    A3 = area (x1, y1, x2, y2, x, y)
     
    # Check if sum of A1, A2 and A3
    # is same as A
    if(A == A1 + A2 + A3):
        return 1
    else:
        return 0
 

# Driver program to test above function
countofintersectingPoints = 0         
    
for point in range(10000):
    int1 = isInside(-4, -4, 6, -4, -4, 6, X[point],Y[point])
    
    int2 = isInside(-3, -1.5, -3, 9.5, 6, -1.5, X[point],Y[point])
    
    int3 = isInside(-5, -5, -13, -5, -5, 13, X[point],Y[point])
    


    if(int1 + int2 + int3 ):

        arrX = np.array(X[point])
        arrY = np.array(Y[point])
        countofintersectingPoints = countofintersectingPoints + 1
        plt.scatter(arrX,arrY)

plt.show()

#Areaoftriangle1 = area (-4,-4,6,-4,-4,6)
#print(Areaoftriangle1)


#Areaoftriangle2 = area (-3,-1.5,-3,9.5,6,-1.5)
#print(Areaoftriangle2)

Areaofrectangle = 18 * 18

#Area of intersection part = Area of triangle1 + Area of triangle2 * (Number of points inside the intersection area/ Total number of points in both the triangles)


divisionpart = countofintersectingPoints / 10000

print('Number of Intersecting Points = ', countofintersectingPoints)

FinalAreaofIntersection = Areaofrectangle * divisionpart

print('Area of Intersection:',FinalAreaofIntersection)


# 

# In[ ]:





# In[ ]:




