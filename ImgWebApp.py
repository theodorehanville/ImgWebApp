# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:59:07 2021

@author: Theodore Hanville Anyika
"""

import streamlit as st
from PIL import Image
import cv2
import numpy as np
import tensorflow as tf


def sidebar():
    st.sidebar.header("About")
    st.sidebar.write('''This WebApp can identify ten(10) different types of objects,
             namely; airplane, automobile, bird, cat, deer, dog, 
             frog, horse, ship and truck.''')
    st.sidebar.write("AUTHOR: Anyika Theodore Hanville")

def main():
    
    # label mapping
    labels = '''airplane
    automobile
    bird
    cat
    deer
    dog
    frog
    horse
    ship
    truck'''.split()
    
    sidebar()
    
    st.title("IMAGE CLASSIFIER")

    st.write('''This WebApp can identify ten(10) different types of objects,
             namely; airplane, automobile, bird, cat, deer, dog, 
             frog, horse, ship and truck.''')
    
    uploaded_file = st.file_uploader("Upload a picture below",type=['png',
                                                                    'jpeg',
                                                                    'jpg'])
 
    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name,
                          "FileType":uploaded_file.type,
                          "FileSize":uploaded_file.size}
         
        #Upload and display the image
        img = Image.open(uploaded_file)
        st.image(img,width=700,caption=file_details["FileName"],use_column_width=True)

        #convert image to array
        img_array = np.array(img)
        cv2.imwrite('out.jpg', cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR))
        
    if st.button("classify"):
        if uploaded_file is None:
            st.error("Upload an image")
        else:
            # loadin g the model
            model = tf.keras.models.load_model('CIFR10-model.h5')
            
            # reshaping the picture to fit the model
            resized_image = np.array([cv2.resize(img_array,(32,32))])  
            prediction = model.predict(resized_image).argmax(axis=1)[0]
            
            #print prediction
            st.success(labels[prediction])

if __name__ == "__main__":
    main()
