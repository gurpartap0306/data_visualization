
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


# In[2]:


data=pd.read_csv('./master.csv')
print(data.shape)
print(data.dtypes)


# In[3]:


data.head(10)


# How many countries data we have?

# In[4]:


countries=data['country'].unique().tolist()
len(countries)


# how many years of data we have?

# In[5]:


years=data['year'].unique().tolist()
len(years)


# range of years

# In[6]:


print(min(years)," to ",max(years))


# printing data of particular country.

# In[7]:


hist_country = 'United States'
mask = data['country'].str.contains(hist_country)

stage = data[mask]


# In[8]:


stage.head()


# In[9]:


stage2={}
for i in range(1985,2016):
   # hist_year = i
    mask = stage['year']==i
    stage2[i]=stage[mask]


# In[10]:


suicides={}
for i in range(1985,2016):
    suicides[i]=stage2[i]['suicides_no'].sum()
    
suicides


# In[11]:


len(suicides)


# bar chart representing suicides in united states

# In[12]:


years = stage['year'].values
su = list(suicides.keys())
ci = list(suicides.values())

plt.bar(su,ci)

plt.xlabel('year')
plt.ylabel('no. of suicides')
plt.title('number of suicides in united states from 1985 to 2016')
plt.show()


# using graph to represent data

# In[13]:


plt.plot(su,ci)
plt.axis([1985, 2016,0,45000])
plt.xlabel('year')
plt.ylabel('no of suicides')
plt.title('curve showing no of suicides from 1985 to 2016')
plt.show()


# using scatter plot to represent data

# In[14]:


fig, axis = plt.subplots()
#axis.scatter(su,ci)
plt.axis([1985, 2016,0,45000])
axis.set_xlabel('year')
axis.set_ylabel('no of suicides')
axis.scatter(su,ci)
plt.show()


# In[15]:


stage3={}
hist_sexm = 'male'
hist_sexf = 'female'

mask1 = stage['sex'].str.contains(hist_sexm)
mask2 = stage['sex'].str.contains(hist_sexf)

stage3['male'] = stage[mask1]
stage3['female']=stage[mask2]

stage3['male'].head()


# In[16]:


nums={}
nums['male'] = stage3['male']['suicides_no'].sum()
nums['female'] = stage3['female']['suicides_no'].sum()
nums


# In[17]:


labels = 'male','female'
sizes = [1034013,213797]
colors = ['skyblue', 'yellowgreen']
explode = (0.1, 0) 
 
plt.pie(sizes, labels=labels, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('pie char represents suicides by male and female')
 
plt.axis('equal')
plt.show()

