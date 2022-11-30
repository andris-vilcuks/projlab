import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats
from scipy.stats import norm
import altair as alt

st.set_page_config(
    page_title="Projektēšanas laboratorija", page_icon=":basketball:", initial_sidebar_state="expanded"
)