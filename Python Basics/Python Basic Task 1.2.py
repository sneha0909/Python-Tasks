#!/usr/bin/env python
# coding: utf-8

# In[13]:


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1 #checking the count of each word. if it has occured more than one time
        else:
            counts[word] = 1

            #int num;
    newdict = dict()
    for myword in counts:
         if counts[myword] > 1:
                newdict[myword] = counts[myword]
                
            
    return newdict       
           
    #return counts
    
counts = word_count('the quick brown fox jumps over the lazy dog.')
print(counts)


# In[8]:


for word in counts:
    print(word,counts[word]) 


# In[ ]:




