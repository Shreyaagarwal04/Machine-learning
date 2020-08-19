#!/usr/bin/env python
# coding: utf-8

# In[2]:


# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt


# In[3]:


# normal plot
x= [1,2,3,4,5,6]
y= [1,2,3,4,5,6]

plt.plot(x,y) 
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('My first plot')
plt.show()


# In[4]:


import numpy as np


# In[5]:


#Subplot
x1= np.linspace(0.0,5.0)
x2= np.linspace(0.0,2.0)

y1= np.cos(2*np.pi*x1)*np.exp(-x1)
y2= np.cos(2*np.pi*x2)

plt.subplot(2,1,1)
# 2 rows column -1
plt.plot(x1,y1, 'o-')
# represent as o-
plt.xlabel('x1')
plt.ylabel('y1')
plt.title('First plot')

plt.subplot(2,1,2)
#2nd row column -2
plt.plot(x2,y2,'-')
plt.xlabel('x2')
plt.ylabel('y2')
plt.title("Second plot")
plt.show()


# ## Scatter plot

# In[8]:


x= [1,2,3,4,5,6,7,8,9,10]

y= [4,7,1,8,9,11,12,3,2,6]

plt.scatter(x,y, label="Stars", color='Blue', marker='*', s=30)
# s --> size of the marker

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.title("Scatter Plot")

plt.legend()

plt.show()


# ## Pie chart

# In[13]:


act= ['eat', 'sleep', 'work', 'play']

slices= [3,7,8,6]

color=['red','blue','pink','green']

plt.pie(slices, labels= act, colors=color, startangle=90, shadow=True,
       explode=(0.2,0,0,0))
plt.title=('Pie chart')

plt.legend()
plt.show()


# In[14]:


act= ['eat', 'sleep', 'work', 'play']

slices= [3,7,8,6]

color=['red','blue','pink','green']

plt.pie(slices, labels= act, colors=color, startangle=90, shadow=True)
plt.title=('Pie chart')

plt.legend()
plt.show()


# In[ ]:





# In[ ]:




