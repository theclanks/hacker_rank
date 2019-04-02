
# coding: utf-8

# In[350]:


import os
import sys


# In[352]:


def load_data():
    file_p = open(os.path.join(os.getcwd(), "input", "input00.txt"), 'r')

    lines = file_p.readlines()

    g = lines[0].strip()

    c = 1
    stacks = []
    for i in range(0,int(g)):
        x = int(lines[c].strip().split()[2])
        la = int(lines[c].strip().split()[0])
        lb = int(lines[c].strip().split()[1])
        A = list(map(int, lines[c+1].strip().split()))
        B = list(map(int, lines[c+2].strip().split()))
        c = c + 3
        #print(A,B)
        #print(x)
        stacks.append({'A': A, 'B': B, 'x':x, 'la': la, 'lb': lb})
    
    return stacks


# In[409]:


# stack replace
def play_replace_stacks(stacks):
    fs = 0
    si = 0
    
    x = stacks['x']
    primeira_pilha = []
    
    while True and stacks['A']:
        if si + stacks['A'][0] <= x:
            a = stacks['A'].pop(0)
            si = si + a
            primeira_pilha.append(a)
            print("A",a)
        else:
            break
        
    replace_stack = []
    fs = len(primeira_pilha)
    
    while True and stacks['B']:
        fs = max(fs, len(primeira_pilha) + len(replace_stack))

        if si + stacks['B'][0] <= x:
            b = stacks['B'].pop(0)
            print("B",b)
            si = si + b
            replace_stack.append(b)
            if si > x:
                break
        elif primeira_pilha: # tenta tirar até conseguir um proximo B
            a = primeira_pilha.pop()
            print("-A",a)
            si = si - a
        else:
            break

    return fs     
    


# In[353]:


# greedy
def play_min_num(stacks):
    fs = 0
    si = 0
    na = 0
    nb = 0
    
    ## Menor valor
    x = stacks['x']
    la = stacks['la']
    lb = stacks['lb']
    at = sum(stacks['A'])
    bt = sum(stacks['B'])
    
    a = stacks['A'][na]
    b = stacks['B'][nb]
    
    # melhor inicio
    if at < bt: # Se a soma de A
        si = si + a
        if si <= x:
            na = na + 1
            fs = fs + 1
            print("A:",a)
    else:
        si = si + b
        if si <= x:
            nb = nb + 1
            fs = fs + 1
            print("B:",b)
    
    while si <= x:

        if na < la and nb < lb: # se a pilha ainda nao terminou
            a = stacks['A'][na]
            b = stacks['B'][nb]
            
            if a < b: # por enquanto o A
                si = si + a
                if si <= x:
                    na = na + 1
                    fs = fs + 1
                    print("A:",a)
            elif a == b:
                # melhor decisao
                if at < bt: # Se a soma de A
                    si = si + a
                    if si <= x:
                        na = na + 1
                        fs = fs + 1
                        print("A.:",a)
                else:
                    si = si + b
                    if si <= x:
                        nb = nb + 1
                        fs = fs + 1
                        print("B.:",b)
            else:
                si = si + b
                if si <= x:
                    nb = nb + 1
                    fs = fs + 1
                    print("B:",b)
        else: # uma das pilhas terminou
            if na < la: #pilha a
                a = stacks['A'][na]
                si = si + a
                if si <= x:
                    na = na + 1
                    fs = fs + 1
                    print("A:",a)
            elif nb < lb: #pilha b
                b = stacks['B'][nb]
                si = si + b
                if si <= x:
                    nb = nb + 1
                    fs = fs + 1
                    print("B:",b)
            else: # fim
                break
    return fs


# In[354]:


def write_results(fs):

    fptr = open(os.path.join(os.getcwd(), "output", "output00.txt"), 'w')

    for t_itr in range(len(fs)):
        fptr.write(fs[t_itr] + '\n')

    fptr.close()


# In[419]:


def solve():
    stacks = load_data()
    fs = []
    for s in stacks:
        print("Greedy stacks:")
        pm = play_min_num(s)
        print("Replaced stacks:")
        ps = play_replace_stacks(s)
            
        if ps > pm:
            s = ps
        else:
            s = pm
        
        fs.append(str(s))
        print("Result:",fs[-1])
    write_results(fs)


# In[420]:


if __name__ == '__main__':
    solve()

