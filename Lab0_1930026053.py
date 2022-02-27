#!/usr/bin/env python
# coding: utf-8

# My repository

# https://github.com/LamHuang/Financial-Computing.git

# In[1]:


def myfunc(x):
    y = (1+0.5*x)**5
    return y


# In[3]:


def numerical_grad(func,x,dx = 0.00001):
    dy = func(x+dx)-func(x)
    ngrad = dy/dx
    return ngrad


# In[5]:


def newton_method(func, func_value = 1.1, x=-1, max_iteration = 1000000, max_err= 0.000001 ):
    for trial in range(max_iteration): 
        error = func(x) - func_value
        if abs(error) < max_err: 
            y = func(x)
            print("Iteration {}: f = {}, x = {}".format(trial, y, x))
            return x 
        else:
            # grad = 
            #x=
            y = func(x)
            print("Iteration {}: f = {}, x = {}".format(trial, y, x)) 
    raise ValueError("Max iteration reached")
    print("Max Iteration {}: f = {}, x = {}".format(trial, y, x))


# In[8]:


def func_1d(x):
    return x**2-x*2+3


# In[9]:


def grad_1d(x):
    return x*2-2


# In[10]:


def gradient_descent_1d(grad, cur_x=0.1, learning_rate=0.01, precision=0.0001, max_iters=10000):
    for i in range(max_iters):
        grad_cur = grad(cur_x)
        if abs(grad_cur) < precision:
            break
        cur_x = cur_x - grad_cur * learning_rate
        print("Iteration",i,": x= ",cur_x)
        
    print("Current minimum x is ",cur_x)
    return cur_x


# In[16]:


gradient_descent_1d(grad_1d, cur_x=10, learning_rate=0.01, precision=0.000001, max_iters=10000)


# In[ ]:




