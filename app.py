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
    # Nepieciešamo datu atlase (atmet liekos datus)

    #df_komandas = df.drop(["GP","W","L","WIN%","Min","FGM","FGA","FG%","3PM","3PA","3P%","FTM","FTA","FT%","OREB","DREB","TOV","BLK","BLKA","PF","PFD"], axis=1)
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

        # Mājnieku atlases tabulas priekšskatījums
        df_majnieki = df_komandas.loc[df_komandas["Team"] == majnieki]
        st.header("Mājnieki:")
        st.dataframe(df_majnieki)
    
        # Viesu atlases tabulas priekšskatījums
        df_viesi = df_komandas.loc[df_komandas["Team"] == viesi]
        st.header("Viesi:")
        st.dataframe(df_viesi)

    with col2:
        st.area_chart(df_komandas)

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
        a = -2

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


    # Aprēķinu attēlošana
    rez1,rez2,rez3,rez4,rez5 = st.columns(5)
    with rez1:
        st.metric("PTS", m_pts, pts)
    with rez2:
        st.metric("REB", m_reb, reb)
    with rez3:
        st.metric("AST", m_ast, ast)
    with rez4:
        st.metric("STL", m_stl, stl)
    with rez5:
        st.metric("+/-", m_pm, pm)

    # Attēlo galā iegūto rezultātu
    co1,co2 = st.columns(2)
    with co1:
        # Mājnieku rezultāts
        st.header(majnieki)
        st.header(a+b+c+d+e)
    with co2:
        # Viesu rezultāts
        st.header(viesi)
        st.header(-a-b-c-d-e)