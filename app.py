import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

st.title("Laptop Price Predictor")

# select the brand
company = st.selectbox("Brand", df["Company"].unique())

# select type of laptop
type = st.selectbox("Type", df["TypeName"].unique())

# RAM
RAM = st.selectbox("RAM (in GB)", [2, 4, 6, 8, 12, 16, 24, 32, 64])

# weight
weight = st.number_input("Weight")

# Touchscreen
touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])

# IPS Panel
IPS = st.selectbox("IPS Panel", ["No", "Yes"])

# Screen size (inches)
screen_size = st.number_input("Screen Size (in inches)")

# resolution
screen_resolution = st.selectbox("Screen Resolution", ["1920x1080", "1366x768", "1600x900", "3840x2160", "3200x1800", "2880x1800", "2560x1600", "2560x1440", "2304x1440"])

# CPU
CPU = st.selectbox("CPU", df["CPU Brand"].unique())

# HDD
hdd = st.selectbox("HDD (in GB)", [0, 128, 256, 512, 1024, 2048])

# SSD
ssd = st.selectbox("SSD (in GB)", [0, 8, 128, 256, 512, 1024])

# GPU
GPU = st.selectbox("GPU Brand", df["GPU Brand"].unique())

# OS
OS = st.selectbox("OS", df["OS"].unique())

if st.button("Predict Laptop Price"):
    pass

    # query
    if touchscreen == "Yes":
        touchscreen = 1
    else:
        touchscreen = 0
    
    if IPS == "Yes":
        IPS = 1
    else:
        IPS = 0

    PPI = None
    X_res = int(screen_resolution.split('x')[0])
    Y_res = int(screen_resolution.split('x')[1])
    PPI = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size

    query = np.array([company, type, RAM, weight, touchscreen, IPS, PPI, CPU, hdd, ssd, GPU, OS])

    query = query.reshape(1, 12)

    st.title("The predicted price for this configuration is: ")
    
    st.title("INR " + str(int(np.exp(pipe.predict(query)[0]))))