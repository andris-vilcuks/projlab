import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="Projektēšanas laboratorija", page_icon=":basketball:")

datne = st.file_uploader("Augšupielādēt CSV datni", type=".csv")

if datne:
    df = pd.read_csv(datne)

    st.header("Tabulas priekšskatījums")
    st.dataframe(df)