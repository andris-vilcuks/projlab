# Nepieciešamo moduļu pievienošana
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import base64

# Pārlūkprogrammas cilnes virsraksts un attēls
st.set_page_config(page_title="Projektēšanas laboratorija", page_icon=":basketball:", layout="wide")

# Sānjoslas virsraksts (nepieciešams, lai jau sākumā attēlotu sānjoslu) 
st.sidebar.header("Parametri")

datne = "NBA2022-23.csv"

# Brīdī, kad ir zināms, kura datne tiks lietota, notiek sekojošās darbības:
if datne:

    # Satura sadalījums kolonnās
    col1, col2 = st.columns(2)

    # Datnes nolasīšana
    df = pd.read_csv(datne)
    # Nepieciešamo datu atlase
    df_komandas = df[['Team','PTS','REB','AST','STL','+/-']]

    # Sānjosla - Mājnieku komandas izvēle
    majnieku_izvelne = sorted(df_komandas['Team'].unique())
    majnieki = st.sidebar.selectbox('Mājnieki', majnieku_izvelne)

    # Sānjosla - Viesu komandas izvēle
    viesu_izvelne = sorted(df_komandas.Team.unique())
    viesi = st.sidebar.selectbox('Viesi', viesu_izvelne)

    # Datu tabulu priekšskatījums
    with col1:
        # Kopējo datu tabulas priekšskatījums
        st.header("Tabulas priekšskatījums")
        st.dataframe(df_komandas)

    with col2:
        # Mājnieku atlases tabulas priekšskatījums
        df_majnieki = df_komandas.loc[df_komandas["Team"] == majnieki]
        st.header("Mājnieki: " + majnieki)
        st.dataframe(df_majnieki)
    
        # Viesu atlases tabulas priekšskatījums
        df_viesi = df_komandas.loc[df_komandas["Team"] == viesi]
        st.header("Viesi: " + viesi)
        st.dataframe(df_viesi)

    # Sānjosla - Kolonnas izvēle
    df_komandu_dati = df_komandas.drop(axis=1, columns='Team')
    kolonna = st.sidebar.selectbox('Kolonnas izvēle:', df_komandu_dati.columns)

    st.bar_chart(df_komandas, x="Team", y=kolonna)

    # Mainīgo definēšana, noklusējuma vērtību uzstādīšana
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    # Vērtību atlase aprēķiniem
    # Points(PTS) 5
    m_pts = df_majnieki.iloc[0,1]
    v_pts = df_viesi.iloc[0,1]
    pts = m_pts - v_pts
    if pts >= 0:
        a = 5
    else:
        a = -5

    # Rebounds(REB) 2
    m_reb = df_majnieki.iloc[0,2]
    v_reb = df_viesi.iloc[0,2]
    reb = m_reb - v_reb
    if reb >= 0:
        b = 2
    else:
        b = -2

    # Assists(AST) 3
    m_ast = df_majnieki.iloc[0,3]
    v_ast = df_viesi.iloc[0,3]
    ast = m_ast - v_ast
    if ast >= 0:
        c = 3
    else:
        c = -3

    # Steals(STL) 1
    m_stl = df_majnieki.iloc[0,4]
    v_stl = df_viesi.iloc[0,4]
    stl = m_stl - v_stl
    if stl >= 0:
        d = 1
    else:
        d = -1

    # +/- 4
    m_pm = df_majnieki.iloc[0,5]
    v_pm = df_viesi.iloc[0,5]
    pm = m_pm - v_pm
    if pm >= 0:
        e = 4
    else:
        e = -4  



    # Attēlo galā iegūto rezultātu
    rez1, rez2, rez3, rez4, rez5, rez6, = st.columns(6)

    with rez1:
        # Mājnieku rezultāts
        st.header("Mājnieki: " + majnieki)
        st.header(a+b+c+d+e)
        # Viesu rezultāts
        st.header("Viesi: " + viesi)
        st.header(-a-b-c-d-e)

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