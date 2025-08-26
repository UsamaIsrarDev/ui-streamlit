# https://docs.streamlit.io/library/api-reference/layout/st.expander

import streamlit as st

st.bar_chart({ "data": [1, 3, 6, 3, 6, 7, 5, 1]})

with st.expander("See Explanation"):

    st.write("The chart above shows some numbers I pick for you. I rolled actual dice for these, so they're guarenteed to be random")

    st.image("https://static.streamlit.io/examples/dice.jpg")

