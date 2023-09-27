#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install qrcode[pil]


# In[2]:


import qrcode


# In[3]:


from PIL import Image


# In[11]:


qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,border=8,)


# In[16]:


qr.add_data("www.example.com")


# In[17]:


qr.make(fit=True)


# In[18]:


img=qr.make_image(fill_color="blue",back_color="white")


# In[19]:


img.save("example.png")


# In[ ]:




