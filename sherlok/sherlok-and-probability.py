
# coding: utf-8

# In[406]:


import os
import sys
import random
from fractions import Fraction


# In[448]:


def load_data():
    file_p = open(os.path.join(os.getcwd(), "input", "input21.txt"), 'r')

    lines = file_p.readlines()

    T = lines[0].strip()
    
    c = 0
    cases = []
    for i in range(0,int(T)):
        N, K = lines[i+1+c].strip().split()
        S = lines[i+2+c].strip()
        c = c + int(1)
        #print(N,K)
        #print(S)
        cases.append({'N': N, 'K': K, 'S':S})
        #print("--")
    
    return cases


# In[449]:


#Brute force
def calc_prob(case):
    N = int(case['N'])
    
    p = 0
    combs = []
    for i in range(1,N+1):
        for j in range(1,N+1):
            if (case['S'][i-1] == '1' and case['S'][j-1] == '1') and abs(i - j) <= int(case['K']):
                if not str(i)+str(j) in combs:
                    combs.append(str(i)+str(j))
                    p = p + 1
    combs.sort()
    return str(p)+"/"+str(N*N)


# In[450]:


# Selecao randomica - Nem sempre será o mesmo resultado
def calc_probR(case):
    N = int(case['N'])
    
    p = 0
    combs = []
    for k in range(N*N):
        i_r = random.randrange(1,N+1)
        j_r = random.randrange(1,N+1)
        if (case['S'][i_r-1] == '1' and case['S'][j_r-1] == '1') and abs((i_r) - (j_r)) <= int(case['K']):
            if not str(i_r)+str(j_r) in combs:
                combs.append(str(i_r)+str(j_r))
                p = p + 1
    combs.sort()
    print(combs)
    return str(p)+"/"+str(N*N)


# In[451]:


def write_results(p):

    fptr = open(os.path.join(os.getcwd(), "output", "output21.txt"), 'w')

    for t_itr in range(len(p)):
        fptr.write(p[t_itr] + '\n')

    fptr.close()


# In[452]:


def solve():
    cases = load_data()
    p = []
    for c in cases:
        p.append(calc_prob(c))
        print(p[-1])
    write_results(p)


# In[453]:


if __name__ == '__main__':
    solve()

