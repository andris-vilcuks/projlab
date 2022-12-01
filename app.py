# Nepieciešamo moduļu pievienošana
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Pārlūkprogrammas cilnes virsraksts un attēls
st.set_page_config(page_title="Projektēšanas laboratorija", page_icon=":basketball:", layout="wide")

# Sānjoslas virsraksts (nepieciešams, lai jau sākumā attēlotu sānjoslu) 
st.sidebar.header("Parametri")

# Datnes izvēlne
sagataves = st.sidebar.checkbox("Izmantot iepriekš sagatavotas tabulas", True)

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
    # Nepieciešamo datu atlase (atmet liekos datus)
    if sagataves == True:
        df_komandas = df.drop(["GP","W","L","WIN%","Min","FGM","FGA","FG%","3PM","3PA","3P%","FTM","FTA","FT%","OREB","DREB","TOV","BLK","BLKA","PF","PFD"], axis=1)
    else:
        df_komandas = df

    # Datu tabulas priekšskatījums
    st.header("Tabulas priekšskatījums")
    st.dataframe(df_komandas)



    # Sānjosla - Mājnieku komandas izvēle
    majnieku_izvelne = sorted(df_komandas['Team'].unique())
    majnieki = st.sidebar.selectbox('Mājnieki', majnieku_izvelne)

    # Sānjosla - Viesu komandas izvēle
    viesu_izvelne = sorted(df_komandas.Team.unique())
    viesi = st.sidebar.selectbox('Viesi', viesu_izvelne)

    # Attēlojuma sadalījums kolonnās
    col1, col2 = st.columns(2)

    # Mājnieku atlases tabulas priekšskatījums
    df_majnieki = df_komandas.loc[df_komandas["Team"] == majnieki]
    with col1:
        st.dataframe(df_majnieki)
   
    # Viesu atlases tabulas priekšskatījums
    df_viesi = df_komandas.loc[df_komandas["Team"] == viesi]
    with col2:
        st.dataframe(df_viesi)



