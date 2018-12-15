
# coding: utf-8

# In[1]:

# Data Prep
import pandas as pd

# Plotting 
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic(u'matplotlib inline')


# # FUEL MAK RAME

# In[2]:

f_mak_rame = pd.read_csv("data/fuel_mak_rame.csv")
print("Fuel MAK Rame")
f_mak_rame.head()


# In[3]:

f_mak_rame["day"] = 1
f_mak_rame["date"] = pd.to_datetime(f_mak_rame[['year', 'month', 'day']])


# In[4]:

f_mak_rame.count()


# In[5]:

f_mak_rame.head()


# ### Monthly Fuel

# In[6]:

plt.plot(f_mak_rame.month[:12], f_mak_rame.quant[:12])
plt.plot(f_mak_rame.month[12:24], f_mak_rame.quant[12:24])
plt.plot(f_mak_rame.month[24:], f_mak_rame.quant[24:])
plt.title("Monthly Fuel: MAK Rame")
plt.xlabel("Month")
plt.ylabel("Quantitity (KG)")
plt.legend(['2016', '2017', '2018'], loc='upper right')
plt.show()


# ### Monthly Fuel

# In[12]:

plt.plot(f_mak_rame.date, f_mak_rame.quant)
plt.xlabel("Date")
plt.ylabel("Quantitity (KG)")
plt.title("Total Fuel: MAK Rame")
plt.show()


# In[14]:

plt.scatter(f_mak_rame.month[:12], f_mak_rame.quant[:12])
plt.show()


# # FUEL MAK CUT

# In[15]:

f_mak_cut = pd.read_csv("data/fuel_mak_cut.csv")
f_mak_cut.head()


# In[16]:

f_mak_cut["day"] = 1
f_mak_cut["date"] = pd.to_datetime(f_mak_cut[['year', 'month', 'day']])


# In[63]:

f_mak_cut.count()


# ### Monthly Fuel

# In[17]:

plt.plot(f_mak_cut.month[:5], f_mak_cut.quant[:5])
plt.plot(f_mak_cut.month[5:17], f_mak_cut.quant[5:17])
plt.plot(f_mak_cut.month[17:], f_mak_cut.quant[17:])
plt.xlabel("Month")
plt.ylabel("Quantitity (KG)")
plt.title("Monthly Fuel: MAK Cut")
plt.legend(['2016', '2017', '2018'], loc='upper right')
plt.show()


# ### Total Fuel

# In[18]:

plt.plot(f_mak_cut.date, f_mak_cut.quant)
plt.xlabel("Date")
plt.ylabel("Quantitity (KG)")
plt.title("Total Fuel: MAK Cut")
plt.show()


# In[19]:

plt.scatter(f_mak_cut.month[:5], f_mak_cut.quant[:5])
plt.show()


# # FUEL SALSAPRINT
# 

# In[20]:

f_sp = pd.read_csv("data/fuel_salsaprint.csv")
f_sp.head()


# In[21]:

f_sp["day"] = 1
f_sp["date"] = pd.to_datetime(f_sp[['year', 'month', 'day']])


# In[22]:

f_sp.count()


# ### Monthly Fuel

# In[23]:

plt.plot(f_sp.month[:12], f_sp.quant[:12])
plt.plot(f_sp.month[12:24], f_sp.quant[12:24])
plt.plot(f_sp.month[24:], f_sp.quant[24:])
plt.xlabel("Month")
plt.ylabel("Quantitity (L)")
plt.title("Monthly Fuel: SalsaPrint")
plt.legend(['2016', '2017', '2018'], loc='upper right')
plt.show()


# ### Total Fuel

# In[25]:

plt.plot(f_sp.date, f_sp.quant)
plt.xlabel("Date")
plt.ylabel("Quantitity (L)")
plt.title("Total Fuel: SalsaPrint")
plt.show()


# In[ ]:




# # FUEL TINTCOLOR

# In[27]:

f_tc_fork = pd.read_csv("data/fuel_tintcolor_fork.csv")
f_tc_fork.head()


# In[28]:

f_tc_fork["day"] = 1
f_tc_fork["date"] = pd.to_datetime(f_tc_fork[['year', 'month', 'day']])


# In[29]:

f_tc_fork.count()


# ### Monthly Fuel

# In[30]:

plt.plot(f_tc_fork.month[:12], f_tc_fork.quant[:12])
plt.plot(f_tc_fork.month[12:24], f_tc_fork.quant[12:24])
plt.plot(f_tc_fork.month[24:], f_tc_fork.quant[24:])
plt.xlabel("Month")
plt.ylabel("Quantitity (L)")
plt.title("Monthly Fuel: TintColor Forklift")
plt.legend(['2016', '2017', '2018'], loc='upper right')
plt.show()


# ### Total Fuel

# In[31]:

plt.plot(f_tc_fork.date, f_tc_fork.quant)
plt.xlabel("Date")
plt.ylabel("Quantitity (L)")
plt.title("Total Fuel: TintColor Forklift")
plt.show()

