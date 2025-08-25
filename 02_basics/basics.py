# import modules

import streamlit as st

# title
st.title("this is a title")

# header
st.header("this is a header")

# sub header
st.subheader("this is a subheader")

# text
st.text("hello, this is text.")

# markdown
st.markdown("### this is a markdown")

# success
st.success("success")

# info
st.info("info")

# warning
st.warning("warning")

# error
st.error("error")

# exception - this has been added later
exc = ZeroDivisionError("Trying to divide by zero")

st.exception(exc)

# write text
st.write("Text with write")

# break

# writing python inbuild function range
st.write(range(10))

# display images

# import image from pillow to open images
from PIL import Image
img = Image.open('streamlit.png')

# display image using streamlit
# width is used to set the width of an image
st.image(image=img, width=200)

# checkbox
# check if the checkbox is checked
# title of the checkbox is 'show/hide'
if st.checkbox("show/hide"):
    # display the text if the checkbox returns true value
    st.text("showing widget")

# radio button
# first argument is the title of the radio button
# second arguments is the options for the radio button
status = st.radio("select gender", ('male', 'female'))

st.title(status)
# conditional statement to print
# male if male is selected else print female
# show the result using the success function
if (status == 'male'):
    st.success("male")

else:
    st.success("female")

# break

# selection box

# first argument takes the title of the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ", ["dancing", "reading", "sports"])

# print the selected hobby
st.write("Your hobby is: ", hobby)

# multi selectbox

# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ", ["dancing", "reading", "sports"])

# write the selected options
st.write("You selected: ", len(hobbies), hobbies, 'hobbies')

# create a simple button that does nothing

if st.button("About"):
    st.text("welcome to the world of generative ai!")

# break

# text input

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter your name", "type here...")

# display the name when the submit button is clicked
# .title() is used to get the input text string

if st.button("submit"):
    result = name.title()
    st.success(result)

# break

# slider

# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("select the level", 2, 10)

# print the level
# format() is used to print value
# of a variable at a specific position

st.text("selected: {}".format(level))
