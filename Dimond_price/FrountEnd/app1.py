# This is the code in which not any style include
import streamlit as st
import joblib
import pandas as pd
model = joblib.load("diamond.pkl")
expected_col = joblib.load("D_COl.pkl")

st.title("Diamond Price Prediction 💎💎")
st.markdown("provide the following detail")

caret = st.slider("Caret",0.0,5.0,0.2)
color = st.selectbox("Color",['D','E','F','G','H','I','J'])
tabel = st.number_input("Tabel",0.0,100.0,61.5)
x =  st.slider("X Value ",0.0,10.0,3.2)
y =  st.slider("Y Value ",0.0,10.0,3.2)
z =  st.slider("Z Value ",0.0,10.0,3.2)
clarity =  st.selectbox("Clarity",['SI2','SI1','VS1','VS2','VVS2','VVS1','I1','IF'])
depth = st.number_input("Depth",0.0,100.0,55.0)

color_mapping = {
    'D': 0,
    'E': 1,
    'F': 2,
    'G': 3,
    'H': 4,
    'I': 5,
    'J': 6
}

clarity_mapping = {
    'I1': 0,
    'IF': 1,
    'SI1': 2,
    'SI2': 3,
    'VS1': 4,
    'VS2': 5,
    'VVS1': 6,
    'VVS2': 7
}

color = color_mapping[color]
clarity = clarity_mapping[clarity]

if st.button("Predict"):
    raw_input={
        "clarity" : clarity,
        'carat' :caret ,
        "depth":depth,
        'x':x,
        'y':y,
        'z':z,
        "table":tabel,
        "color":color
    }

    input_df = pd.DataFrame([raw_input ])
    predictions = model.predict(input_df)[0]
    st.success(f"Predicted Diamond Price: ${predictions:,.2f}")




