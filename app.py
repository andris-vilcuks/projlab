# Nepieciešamo moduļu pievienošana
import streamlit as st
import pandas as pd
import numpy as np

# Pārlūkprogrammas cilnes virsraksts un attēls
st.set_page_config(page_title="Projektēšanas laboratorija", page_icon=":basketball:", layout="wide")

# Sānjoslas virsraksts (nepieciešams, lai jau sākumā attēlotu sānjoslu) 
st.sidebar.header("Parametri")

# Datnes izvēlne
izvelne = st.sidebar.checkbox("Izmantot savu .csv datni")

if izvelne == True:
    # Ja ķeksis ir ielikts, lietotājs augšupielādē savus datus
    datne = st.file_uploader("Augšupielādēt CSV datni", type=".csv")
else:
    # Ja ķeksis nav ielikts, izvēlas sagatavotos datus
    gads = st.sidebar.selectbox('Gads:', list(reversed(range(1996,2023))))
    datne = "NBA"+str(gads)+"-"+str(gads+1)+".csv"

# Brīdī, kad ir zināms, kura datne tiks lietota, notiek sekojošās darbības:
if datne:

    # Datnes nolasīšana
    df = pd.read_csv(datne)
    # Nepieciešamo datu atlase
    df_komandas = df[['TEAM','PTS','REB','AST','STL','+/-']]

    # Sānjosla - Kolonnas izvēle
    df_komandu_dati = df_komandas.drop(axis=1, columns='TEAM')
    kolonna = st.sidebar.selectbox('Kolonnas izvēle:', df_komandu_dati.columns)

    # Sānjosla - Mājnieku komandas izvēle
    majnieku_izvelne = sorted(df_komandas['TEAM'].unique())
    majnieki = st.sidebar.selectbox('Mājnieki', majnieku_izvelne)

    # Sānjosla - Viesu komandas izvēle
    viesu_izvelne = sorted(df_komandas.TEAM.unique())
    viesi = st.sidebar.selectbox('Viesi', viesu_izvelne)

    # Datu tabulu priekšskatījums
    st.header("Tabulas priekšskatījums:")
    st.dataframe(df)

    # Satura sadalījums kolonnās
    col1, col2 = st.columns(2)

    with col1:
        # Kopējo datu (pēc atlases) tabulas priekšskatījums
        st.dataframe(df_komandas)

    with col2:
        # Mājnieku atlases tabulas priekšskatījums
        df_majnieki = df_komandas.loc[df_komandas["TEAM"] == majnieki]
        st.header("Mājnieki: " + majnieki)
        st.dataframe(df_majnieki)
    
        # Viesu atlases tabulas priekšskatījums
        df_viesi = df_komandas.loc[df_komandas["TEAM"] == viesi]
        st.header("Viesi: " + viesi)
        st.dataframe(df_viesi)

    st.bar_chart(df_komandas, x="TEAM", y=kolonna)

    # Mainīgo definēšana, noklusējuma vērtību uzstādīšana
    a = 0
    b = 0

    # Vērtību atlase aprēķiniem
    # Points(PTS) 5
    m_pts = df_majnieki.iloc[0,1]
    v_pts = df_viesi.iloc[0,1]
    pts = m_pts - v_pts
    if pts >= 0:
        a = a + 5
    else:
        b = b + 5

    # Rebounds(REB) 2
    m_reb = df_majnieki.iloc[0,2]
    v_reb = df_viesi.iloc[0,2]
    reb = m_reb - v_reb
    if reb >= 0:
        a = a + 2
    else:
        b = b + 2

    # Assists(AST) 3
    m_ast = df_majnieki.iloc[0,3]
    v_ast = df_viesi.iloc[0,3]
    ast = m_ast - v_ast
    if ast >= 0:
        a = a + 3
    else:
        b = b + 3

    # Steals(STL) 1
    m_stl = df_majnieki.iloc[0,4]
    v_stl = df_viesi.iloc[0,4]
    stl = m_stl - v_stl
    if stl >= 0:
        a = a + 1
    else:
        b = b + 1

    # +/- 4
    m_pm = df_majnieki.iloc[0,5]
    v_pm = df_viesi.iloc[0,5]
    pm = m_pm - v_pm
    if pm >= 0:
        a = a + 4
    else:
        b = b + 4



    # Attēlo galā iegūto rezultātu
    rez0, rez1, rez2, rez3, rez4, rez5, rez6, = st.columns(7)

    with rez0:
        # Mājnieku rezultāts
        st.metric("Mājnieki: " + majnieki, a)
    with rez1:
        # Viesu rezultāts
        st.metric("Viesi: " + viesi, b)
    # Starpības
    with rez2:
        st.metric("PTS", m_pts, pts)
    with rez3:
        st.metric("REB", m_reb, reb)
    with rez4:
        st.metric("AST", m_ast, ast)
    with rez5:
        st.metric("STL", m_stl, stl)
    with rez6:
        st.metric("+/-", m_pm, pm)