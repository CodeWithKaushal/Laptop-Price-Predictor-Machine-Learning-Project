import streamlit as st
import pickle
import numpy as np





# Import the model.....
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Page Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Laptop Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #808080;'>Predict the price of your desired laptop configuration</p>", unsafe_allow_html=True)

# Divide the UI into two columns with a header
st.markdown("### Select Laptop Specifications")
col1, col2 = st.columns(2)

# Column 1 - Laptop Features
with col1:
    st.subheader("Basic Specifications")
    # Brand
    company = st.selectbox('Brand', df['Company'].unique())
    # Type of laptop
    type = st.selectbox('Type', df['TypeName'].unique())
    # RAM
    ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
    # Weight
    weight = st.number_input('Weight of the Laptop (in kg)', min_value=0.5, max_value=5.0, step=0.1)
    # Touchscreen
    touchscreen = st.radio('Touchscreen', ['No', 'Yes'])

# Column 2 - Display & Performance Features
with col2:
    st.subheader("Display & Performance")
    # Screen size
    screen_size = st.slider('Screen Size (in inches)', 10.0, 18.0, 15.6)
    # Resolution
    resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])
    # IPS
    ips = st.radio('IPS Panel', ['No', 'Yes'])
    # CPU
    cpu = st.selectbox('CPU', df['Cpu brand'].unique())

# Add an additional column for storage and GPU
st.markdown("### Storage & GPU")
col3, col4 = st.columns(2)

# Column 3 - Storage
with col3:
    # HDD
    hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
    # SSD
    ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])

# Column 4 - GPU and OS
with col4:
    # GPU
    gpu = st.selectbox('GPU', df['Gpu Brand'].unique())
    # OS
    os = st.selectbox('Operating System', df['os'].unique())

# Predict button in the center
if st.button('Predict Price'):
    # Query processing
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])
    query = query.reshape(1, 12)

    # Prediction
    predicted_price = int(np.exp(pipe.predict(query)[0]))

    # Display the prediction result
    st.markdown(f"<h2 style='text-align: center; color: #FFFFF;'>The predicted price of this configuration is {predicted_price} ₹</h2>", unsafe_allow_html=True)

# Footer with Developer Name
st.markdown("<p style='text-align: center; color: #808080;'>Developed by <strong>Kaushal Divekar</strong></p>", unsafe_allow_html=True)
