#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import random

#s = np.array([1,1,0,0,1,1,0,1,1,0,1,1,0,0,1,1]) 
#p = np.array([1,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1]) 

s = np.array(['C','C','C','C','A','C','G','A','T','C','T','T','T','A','A','A','G','C','C','G','T','C','G','G','C','C','A','T','T','T']) 
p = np.array(['t','c','a','a','g','t','t','t','a','a','t','g','t','t','a','g','t','c','t','t','g','t','t','t','t','t','a','g','c','t'])


# generating the random number to perform crossover
k1 = random.randint(0, s.size-1)
print("Crossover point :", k1)
    
k2 = random.randint(0, p.size)
print("Crossover point :", k2)
    
t1 = min(k1,k2)
t2 = max(k1,k2)

s1 = s[0:t1+1] #concept of numpy slicing
s2 = s[t1+1:t2+1]
s3 = s[t2+1:s.size]
p1 = p[0:t1+1]
p2 = p[t1+1:t2+1]
p3 = p[t2+1:p.size]

temp = s2 #exhanging chromosomes using a temporary variable
s2   = p2
p2   = temp


#print(s1)
#print(s2)
#print(s3)
#print(p1)
#print(p2)
#print(p3)

finalSarray1 = np.concatenate((s1, s2, s3))

finalParray2 = np.concatenate((p1, p2, p3))

print(np.array2string(finalSarray1, separator='', formatter={'str_kind': lambda x: x}))
print(np.array2string(finalParray2, separator='', formatter={'str_kind': lambda x: x}))


# In[ ]:





# In[ ]:





# In[ ]:




