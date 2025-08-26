import streamlit as st

import time

with st.status("Downloading data...", expanded=True) as status:

    st.write("Searching for data...")

    time.sleep(2)

    st.write("Found URL")

    time.sleep(1)

    st.write("Downloading data ...")

    time.sleep(2)

    status.update(label="Downloaded", state="complete", expanded=False)

st.button("Rerun")