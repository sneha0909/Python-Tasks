#!/usr/bin/env python
# coding: utf-8

# In[68]:


def isPrime(n):
    i = 2
    while i * i <= n:

        # n has a factor, hence not a prime 
        if n % i == 0:
            #print(n,'not prime')
            return False
        i += 1
          
    # we reach here if n has no factors 
    # and hence n is a prime number 
    #print(n,"prime")
    return True
      
def summ(l, r):

# iterate from lower to upper 
    arrayofi = []
    arrayofsum = [] #created an array of sum to collect the sum of prime divisors
 
    for i in range(l, r + 1) :
        
        arrayofdivisors = [] #created an array of divisors to collect the divisors which are prime
         
        # if i is prime, it has no factors 
        if isPrime(i) == True:
            i+=1 #incrementing i by one and checking the next i
            #arrayofsum.append(0)
        else: 
            
            for j in range(2, i):
            # check if j is a prime factor of i 
               if i % j == 0 and isPrime(j):
                arrayofdivisors.append(j)
               
                #print(arrayofdivisors)
                
                
        arrayofsum.append( sum(arrayofdivisors) )
        arrayofi.append(i)      
        maxx = arrayofsum[0];    
              
        
        #Loop through the array    
        for m in range(0, len(arrayofsum)):  
        
        #Compare elements of array with max    
              if(arrayofsum[m] > maxx):    
                maxx = arrayofsum[m]; 
                k = m;
    print(arrayofsum)
    return arrayofi[k]
    
    
    
    
    
    
       
# Driver code
if __name__ == "__main__":
    l = 100
    r = 1000
    print(summ(l, r))


# In[ ]:





# In[ ]:





# In[ ]:




