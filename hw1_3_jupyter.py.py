#!/usr/bin/env python
# coding: utf-8

# In[7]:


import matplotlib.pyplot as plt
import random
lines=[]
with open("C:/Users/USER/Downloads/cdata.csv","r") as file:
    r=file.readline()
    for line in file:
        lines.append(line.split(","))
size=10
color=['peru','burlywood','bisque','sandybrown']
name=['A','B','C','D']
x,y=[],[]
plt.figure()
for i in range(len(lines)):
    x+=[float(lines[i][0])]
    y+=[float(lines[i][1])]


# In[8]:


import pandas as pd
df = pd.read_csv('C:/Users/USER/Downloads/cdata.csv')


# In[9]:


def distance(x,y,xc,yc):
    dis=((x-xc)**2+(y-yc)**2)**(1/2)
    return round(dis,6)


# In[10]:


def k_means(k):
    center=[]
    for i in range(k):
        xc=random.choice(x)
        yc=y[x.index(xc)]
        center.append((xc,yc))
    while True:
        center1=[]
        for i in range(len(x)):
            d=[]
            for ii in range(k):
                r=distance(x[i],y[i],center[ii][0],center[ii][1])
                d+=[r]
            col=int(d.index(min(d)))
            df.iloc[i]={'x':x[i],'y':y[i],'cluster':col}
        for i in range(k):
            mask=df['cluster']==i
            xc=round(df[mask]['x'].mean(),4)
            yc=round(df[mask]['y'].mean(),4)
            center1+=[(xc,yc)]
        if center==center1:
            break
        else:
            center=center1
            continue
    return center,df


# ## 1

# In[11]:


k=4
center=[]
for i in range(k):
    xc=random.choice(x)
    yc=y[x.index(xc)]
    center.append((xc,yc))
while True:
    plt.figure()
    center1=[]
    for i in range(len(x)):
        d=[]
        for ii in range(k):
            r=distance(x[i],y[i],center[ii][0],center[ii][1])
            d+=[r]
        col=int(d.index(min(d)))
        df.iloc[i]={'x':x[i],'y':y[i],'cluster':col}
    for i in range(k):
        mask=df['cluster']==i
        plt.scatter(df[mask]['x'],df[mask]['y'],s=size,c=color[i],label=name[i])
        plt.legend()
        xc=round(df[mask]['x'].mean(),4)
        yc=round(df[mask]['y'].mean(),4)
        center1+=[(xc,yc)]
        plt.scatter(center1[i][0],center1[i][1],marker='x',c='black',s=100)
    if center==center1:
        break
    else:
        center=center1
        continue


# # 2

# In[12]:


def ssee(a,b):
    sse=[]
    for k in range(a,b+1):
        result=k_means(k)
        center,df=result[0],result[1]
        one=[]
        for i in range(k):
            mask=df['cluster']==i
            df['square']=(df[mask]['x']-center[i][0])**2+(df[mask]['y']-center[i][1])**2
            one+=[df['square'].sum()]
        sse+=[sum(one)]
    return sse


# In[15]:


y_=ssee(2,10)
print(y_)
x_=range(2,len(y_)+2)
plt.xlabel('Number of k')
plt.ylabel('Sum of square error')
plt.plot(x_,y_,'')


# # 3

# In[18]:


xx,yy=[],[]
for ind in range(10):
    yy+=ssee(10,10)
    xx+=[ind]
plt.xlabel('Fixed k=10')
plt.ylabel('Sum of square error')
plt.title('Result of ten times randomly pick the initial points')
plt.ylim(100,200)
plt.bar(xx,yy)


# In[ ]:


xx,yy

