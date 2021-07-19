#!/usr/bin/env python
# coding: utf-8

# In[62]:


from flask import Flask, request, jsonify, url_for, render_template
import uuid
import os
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image,ImageFile
from io import BytesIO
from tensorflow.keras.preprocessing import image


# In[63]:


ALLOWED_EXTENSION= set(['png','jpeg','jpg'])
IMAGE_HEIGHT= 32
IMAGE_WIDTH= 32
IMAGE_CHANNELS= 3
os.chdir(r'C:\Users\LENOVO\Desktop\sample_project_1\Take it Out')


# In[57]:


def allowed_file(filename):
    return '.' in filename and     filename.rsplit('.',1)[1] in ALLOWED_EXTENSION


# In[58]:


model= load_model(os.getcwd()+'/model/model_0.909.h5')


# In[61]:


app= Flask(__name__)

@app.route('/index')
def index():
    return render_template('ImageML.html')

@app.route('/api/image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return render_template('ImageML.html',prediction= "No image posted. Should be attribute named image.")
    file= request.files['image']
    
    if file.filename =='':
        return render_template('ImageML.html',prediction= " No Image Selected.")
    
    if file and allowed_file(file.filename):
        print("***" + file.filename)
        x= []
        ImageFile.LOAD_TRUNCATED_IMAGES= False
        img= Image.open(BytesIO(file.read()))
        img.load()
        img= img.resize((IMAGE_WIDTH,IMAGE_HEIGHT),Image.ANTIALIAS)
        x= image.img_to_array(img)
        x= np.expand_dims(x, axis=0)
        pred= model.predict(x)
        result= np.argmax(pred[0])
        if result==0:
            label="AeroPlane"
        elif result==1:
            label= "Car"
        elif result==2:
            label= "Bird"
        prob=float(pred[0][result])    
        response= {'pred': label}
        return render_template('ImageML.html',prediction = f'{response}')
    else:
        return render_template('ImageML.html',prediction = 'Invalid File Extension.... supported types are jpg , jpeg , png')

if __name__=="__main__":
    app.run(debug= True, use_reloader= False)
    


# In[ ]:




