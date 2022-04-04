from turtle import width
import streamlit as st
from PIL import Image


from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from skimage.filters import frangi, hessian
import cv2
import numpy as np
from matplotlib import pyplot as pl

st.set_page_config(layout="wide")    
###########################
import streamlit as st
import base64

LOGO_IMAGE = "./logo.png"

st.markdown(
    """
    <style>
    .container {
        text-align: center;
    }
   
    .logo-img {
      
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
        
    </div>
    """,
    unsafe_allow_html=True
)







###########################
def clicker2():
        img0=cv2.imread('./stef.jpeg')
        dim = (450, 450)
  
        img0 = cv2.resize(img0, dim, interpolation = cv2.INTER_AREA)
        img0=filter1(img0)
        return img0

def filter1(img):     
        return hessian(img)
# st.title('Image Processing using Streamlit')
# st.image('./logo.png',width=700)

col1, col2,col3 = st.columns(3)

col1.header("Original")
col2.header("Processed")
heart1=col3.button("Heart 3D segmented")
heart2=col3.button("Heart 2D segmented")
hassan = col3.button("Hassan filter")
if hassan :
    original = Image.open('./stef.jpeg')

    col1.image(original, width=800)
    original=clicker2()

    # col2.header("hassan filter")

    col2.image(original, width=800)
if heart1 :
    file_ = open("./Heart.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    col1.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="800" height="800" alt="cat gif">',
        unsafe_allow_html=True,
    )

    file_ = open("./Heart_segmented_small.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    col2.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="800" height="800" alt="cat gif">',
        unsafe_allow_html=True,
    )
if heart2 :
    file_ = open("./Heart_2D.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    col1.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="800" height="800" alt="cat gif">',
        unsafe_allow_html=True,
    )

    file_ = open("./Heart_2D_segmented.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    col2.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="800" height="800" alt="cat gif">',
        unsafe_allow_html=True,
    )

