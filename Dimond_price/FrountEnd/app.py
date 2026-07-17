import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("diamond.pkl")

# Page configuration
st.set_page_config(
    page_title="Diamond Price Predictor",
    page_icon="💎",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

/* Full page background */
.stApp {
    background: linear-gradient(
        120deg,
        #071A52,
        #0B3D91,
        #5B2C83
    );
}


/* Remove top space */
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 1rem;
}

/* Remove header spacing */
header[data-testid="stHeader"] {
    background: transparent;
    height: 0rem;
}


/* Sidebar top alignment */
section[data-testid="stSidebar"] > div {
    padding-top: 0rem !important;
}

/* Title */
h1 {
    color: #E6FFFF !important;
    text-align: center;
    font-size: 45px !important;
    font-weight: 800 !important;
    text-shadow: 0 0 15px #00FFFF;
}


/* All text */
p, label, span {
    color: white !important;
}


/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #081B33,
        #4A1A5C
    );
}


/* Input labels */
div[data-testid="stWidgetLabel"] {
    color: white !important;
}


/* Text and number input boxes */
div[data-testid="stNumberInput"] input {

    background-color: #102A43 !important;

    color: white !important;

    -webkit-text-fill-color: white !important;

    border: 2px solid #00D9FF !important;

    border-radius: 10px;
}


/* Selectbox */
div[data-testid="stSelectbox"] div[data-baseweb="select"] {

    background-color: #102A43 !important;

    border: 2px solid #00D9FF !important;

    border-radius: 10px;

}


div[data-testid="stSelectbox"] span {

    color: white !important;

}


/* Dropdown menu */
ul[role="listbox"] {

    background-color: #102A43 !important;

}


li[role="option"] {

    color: white !important;

}


/* Slider */
div[data-testid="stSlider"] {

    color: white !important;

}


/* Predict button */
.stButton button {

    background: linear-gradient(
        90deg,
        #00D9FF,
        #0066FF,
        #9B59B6
    );

    color:white !important;

    font-size:20px;

    font-weight:bold;

    border-radius:15px;

    height:55px;

    width:100%;

    border:none;

    box-shadow:0 0 20px #00D9FF;

}


.stButton button:hover {

    transform:scale(1.03);

    box-shadow:0 0 35px #00FFFF;

}


/* Prediction result box */
div[data-testid="stAlert"] {

    background-color:#102A43 !important;

    border:2px solid #00D9FF;

    border-radius:15px;

}


div[data-testid="stMetric"] {

    background-color:#102A43;

    border:2px solid #00D9FF;

    border-radius:20px;

    padding:25px;

    color:white !important;

    box-shadow:0 0 25px #00D9FF;

}
section[data-testid="stSidebar"] h2 {
    color: #E6FFFF !important;
    font-size: 28px !important;
    font-weight: 800 !important;
    text-shadow:
        0 0 10px #00FFFF,
        0 0 20px #0077FF;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("💎 Diamond Price Prediction")
st.write("### Predict the estimated market price of a diamond using Machine Learning")


# Sidebar
st.sidebar.header("🔍 Diamond Features")


carat = st.sidebar.slider(
    "💎 Carat",
    0.0,
    5.0,
    0.2
)

color = st.sidebar.selectbox(
    "🌈 Color",
    ['D','E','F','G','H','I','J']
)

clarity = st.sidebar.selectbox(
    "✨ Clarity",
    ['SI2','SI1','VS1','VS2','VVS2','VVS1','I1','IF']
)

depth = st.sidebar.number_input(
    "📏 Depth",
    0.0,
    100.0,
    61.5
)

table = st.sidebar.number_input(
    "📐 Table",
    0.0,
    100.0,
    55.0
)

x = st.sidebar.slider(
    "X Dimension",
    0.0,
    10.0,
    3.2
)

y = st.sidebar.slider(
    "Y Dimension",
    0.0,
    10.0,
    3.2
)

z = st.sidebar.slider(
    "Z Dimension",
    0.0,
    10.0,
    3.2
)


# Encoding
color_mapping = {
    'D':0,
    'E':1,
    'F':2,
    'G':3,
    'H':4,
    'I':5,
    'J':6
}

clarity_mapping = {
    'I1':0,
    'IF':1,
    'SI1':2,
    'SI2':3,
    'VS1':4,
    'VS2':5,
    'VVS1':6,
    'VVS2':7
}


color_num = color_mapping[color]
clarity_num = clarity_mapping[clarity]


# Prediction
if st.button("🔮 Predict Diamond Price"):

    input_data = {
        "clarity":[clarity_num],
        "carat":[carat],
        "depth":[depth],
        "x":[x],
        "y":[y],
        "z":[z],
        "table":[table],
        "color":[color_num]
    }


    input_df = pd.DataFrame(input_data)

    input_df = input_df[expected_col]

    prediction = model.predict(input_df)[0]


    st.success("Prediction Completed Successfully 🎉")

    st.metric(
        "💰 Estimated Diamond Price",
        f"${prediction:,.2f}"
    )

    st.balloons()
















