import numpy as np
import streamlit as st
import joblib
from PIL import Image
import pickle
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import re
import string
import matplotlib.pyplot as plt
import time



@st.cache(allow_output_mutation=True)
def load():

    # Load the vectoriser.
    file = open("models_fraud/minmax_scaler.pickle", 'rb')
    vectoriser = pickle.load(file)
    file.close()
    
    # Load the LR Model.
    file = open("models_fraud/LR_Model.pickle", 'rb')
    LRmodel = pickle.load(file)
    file.close()
    
    return vectoriser, LRmodel


def progressbar():
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)





st.title('Sentiment Analysis App')
st.write('Performing Sentiment Analysis')
image = Image.open('data_fraud/rajasekhar.jpg.jpg')
st.image(image, use_column_width=True)
# st.write('Enter some random tweets in the left sidebar and click on Predict Sentiment!')


# uploaded_file = st.sidebar.file_uploader("Choose a csv file", type="csv")
# st.sidebar.write("or")
minmax,model=load()
st.sidebar.subheader("Hi", height=500, max_chars=None, key=None)
cols = ["tweet"]

    
if (st.sidebar.button('Predict Sentiment')):   
    progressbar()
    minmax,model=load()
    st.text("")
    st.text("")
    st.text("")
    plot(result_df)
    
