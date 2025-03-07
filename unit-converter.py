import streamlit as st

# Page Configuration
st.set_page_config(page_title="MeasureWise - Unit Converter", layout="centered")

# Custom CSS for UI Styling
st.markdown("""
    <style>
        body {
            background-color: gray;
        }
        .stApp {
            background-color: #363636;
            padding: 20px;
            border-radius: 10px;
        }
        h1 {
            text-align: center;
            font-size: 38px;
            font-weight: bold;
            color: #ff2c2c;
        }
        h3 {
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            color: #ca3433;
        }
        h4 {
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            color: black;
        }
        label {
            font-size: 18px;
            font-weight: bold;
            color: black;
        }
        .stRadio label {
            font-size: 18px !important;
            font-weight: bold;
            color: whie;
        }
        .stSelectbox label {
            font-size: 18px;
            font-weight: bold;
        }
        .stTextInput, .stNumberInput {
            font-size: 20px;
        }
        .convert-button {
            background-color: #3498DB;
            color: white;
            font-size: 20px;
            font-weight: bold;
            border-radius: 10px;
            padding: 12px;
            width: 100%;
            text-align: center;
            cursor: pointer;
        }
        .convert-button:hover {
            background-color: #2980B9;
        }
    </style>
""", unsafe_allow_html=True)

# Title & Description
st.markdown("<h1>MeasureWise</h1>", unsafe_allow_html=True)
st.markdown("<h3>Smart Unit Converter</h3>", unsafe_allow_html=True)
st.write("Select a category, enter a value, and get the converted result instantly! ⚡")

# Category Selection
category = st.radio("Select a Category:", ["Length", "Weight", "Time"], horizontal=True)

# Available Units per Category
unit_options = {
    "Length": ["Kilometers to Miles", "Miles to Kilometers", "Meters to Feet", "Feet to Meters", 
               "Centimeters to Inches", "Inches to Centimeters", "Meters to Kilometers", "Kilometers to Meters"],
    "Weight": ["Kilograms to Pounds", "Pounds to Kilograms"],
    "Time": ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", 
             "Hours to Days", "Days to Hours"]
}

# Select Unit
unit = st.selectbox("Select Conversion Type:", unit_options[category])

# Function to Handle Unit Conversion
def convert_units(category, value, unit):
    conversions = {
        "Length": {
            "Kilometers to Miles": value * 0.621371,
            "Miles to Kilometers": value / 0.621371,
            "Meters to Feet": value * 3.28084,
            "Feet to Meters": value / 3.28084,
            "Centimeters to Inches": value * 0.393701,
            "Inches to Centimeters": value / 0.393701,
            "Meters to Kilometers": value / 1000,
            "Kilometers to Meters": value * 1000,
        },
        "Weight": {
            "Kilograms to Pounds": value * 2.20462,
            "Pounds to Kilograms": value / 2.20462,
        },
        "Time": {
            "Seconds to Minutes": value / 60,
            "Minutes to Seconds": value * 60,
            "Minutes to Hours": value / 60,
            "Hours to Minutes": value * 60,
            "Hours to Days": value / 24,
            "Days to Hours": value * 24,
        }
    }
    return conversions.get(category, {}).get(unit, "Invalid Conversion")

# User Input Section
st.markdown("---")
st.markdown(f"<h4>{unit}</h4>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    input_value = st.number_input("Enter Value:", min_value=0.0, format="%.2f", key="input")

with col2:
    output_value = st.empty()

# Convert Button
if st.button("🔄 Convert", help="Click to convert"):
    result = convert_units(category, input_value, unit)
    
    # Store conversion history in session state
    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append(f"{input_value} {unit} = {result:.4f}")

    # Display the result
    st.success(f"✅ Converted Value: **{result:.4f}**")

# Conversion History
if "history" in st.session_state and st.session_state.history:
    st.markdown("---")
    st.subheader("📜 Conversion History")
    for entry in reversed(st.session_state.history[-5:]):  # Show last 5 conversions
        st.write(f"🔹 {entry}")
