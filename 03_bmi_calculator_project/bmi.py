# import the streamlit library

import streamlit as st

# give a title to our app
st.title("Welcome to BMI Calaulator")

# take weight input in kgs
weight = st.number_input("Enter your weight (in kgs)")

# take height input
# radio button to choose height format
status = st.radio("select your height format: ", 'cms', 'meter', 'feet')

# compare status value
if status == 'cms':

    # take height input in centimeter
    height = st.number_input("Centimeter")

    try:
        bmi = weight / ((height / 100) ** 2)

    except:
        st.text("Enter some value to height.")

elif status == 'meters':

    # take height input in meters
    height = st.number_input("Meters")

    try:
        bmi = weight / (height ** 2)

    except:
        st.text("Enter some value to height")

else:

    # take height input in Feet
    height = st.number_input("Feet")

    # 1 meter = 3.28

    try:
        bmi = weight / ((height / 3.28) ** 2)

    except:
        st.text("Enter some value to height")

# check if the button is checked or not

if st.button("Calculate BMI"):

    # print the bmi index
    st.text("Your bmi is {}.".format(bmi))

    # give the interpretation of bmi index

    if bmi < 16:
        st.error("You are extremely underweight.")

    elif bmi >= 16 and bmi < 18.5:
        st.warning("You are underweight")

    elif bmi >= 18.5 and bmi < 25:
        st.success('Healthy')

    elif bmi >= 25 and bmi < 30:
        st.warning("Overweight")

    elif bmi >= 30:
        st.error("Extreamely overweight")
