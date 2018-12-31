#!/usr/bin/env python
# coding: utf-8

# In[26]:


######### Find the longest word
def longestWord(wordlist):    
    result = wordlist[0]
    for x in range(1,len(wordlist)):
        len1 = len(wordlist[x])
        len2 = len(result)
        if len1 > len2:
            result = wordlist[x]
    
    print('The longest word from the list is: '+result)

wordlist = ['sourav','Ramakrishnan','Sagar','lavanya']
longestWord(wordlist)
#########

