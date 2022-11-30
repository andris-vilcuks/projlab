import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Pārlūkprogrammas cilnes virsraksts un attēls
st.set_page_config(page_title="Projektēšanas laboratorija", page_icon=":basketball:")

# Sānjoslas virsraksts (nepieciešams, lai jau sākumā attēlotu sānjoslu) 
st.sidebar.header("Parametri")

# Datnes izvēlne
sagataves = st.checkbox("Izmantot iepriekš sagatavotas tabulas", True)

# Ja ir ieķeksēts, tad izvēlas jau sagatavotu tabulu
if sagataves == True:
    datne = "NBA2022-23.csv"

# Ja izņem ķeksi, tad lietotājam nepieciešams augšupielādēt .csv datni patstāvīgi
if sagataves == False:
    datne = st.file_uploader("Augšupielādēt CSV datni", type=".csv")

# Brīdī, kad ir zināms, kura datne tiks lietota, notiek sekojošās darbības:
if datne:
    # Datnes nolasīšana
    df = pd.read_csv(datne)
    komandas = df.drop(["GP","W","L","WIN%","Min","FGM","FGA","FG%","3PM","3PA","3P%","FTM","FTA","FT%","OREB","DREB","TOV","BLK","BLKA","PF","PFD",], axis=1)

    # Datu tabulas priekšskatījums
    st.header("Tabulas priekšskatījums")
    st.dataframe(komandas)

    # Mājnieku komandas izvēle
    majnieku_izvelne = sorted(komandas.Team.unique())
    majnieki = st.sidebar.selectbox('Komandas', majnieku_izvelne)

    # Viesu komandas izvēle