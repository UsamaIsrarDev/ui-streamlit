import streamlit as st

# everything is accessible via the st.secrets dict:

st.write("DB username : ", st.secrets["db_username"])

st.write("DB password : ", st.secrets["db_password"])

# add the root level secrets are also accessible as environment variables

import os

st.write(
    "Has environment variables been set : ",
    os.environ["db_username"] == st.secrets["db_username"]
)
