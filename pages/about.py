import streamlit as st

st.set_page_config(page_title="Projektēšanas laboratorija", page_icon=":basketball:")

st.title('Basketbola spēles rezultāta prognozēšana')

st.header('Rezultāta prognoze')
st.markdown('Izplatīta metode, ko izmanto spēļu rezultātu prognozēšanai komandu sporta veidos, ir pazīstama kā “loģistiskā regresija”. Šis modelis izmanto vairākus mainīgos lielumus abām komandām un izveido formulu, ko var izmantot, lai aprēķinātu katras komandas uzvaras varbūtību. Izmantotie mainīgie parasti ietver spēlētāju vērtējumus, komandu reitingus un iepriekšējo sniegumu.')

st.header('Dati')
st.markdown('Basketbola komandu dati tiek iegūti no vietnes https://www.nba.com/stats/teams/traditional , kurā ir pieejami gan pašreizējās, gan iepriekšējo sezonu komandu dati to apstrādei.')

st.header('Formula')
st.markdown('No iegūtajiem datiem, tiek atlasīti tikai svarīgākie un noteikts to nozīmīgums:')
st.markdown('- Punkti jeb *points* (PTS) - 5')
st.markdown('- Plus/Mīnus (+/-) - 4')
st.markdown('- Piespēles jeb *assists* (AST) - 3')
st.markdown('- Atlēkušās bumbas jeb *rebounds* (REB) - 2')
st.markdown('- Atņemtās bumbas jeb *steals* (PTS) - 1')

st.header('Darbu veidoja:')
st.markdown('Vārds Uzvārds 201RDB001')
st.markdown('Vārds Uzvārds 201RDB002')
st.markdown('Vārds Uzvārds 201RDB003')
st.markdown('Vārds Uzvārds 201RDB004')
st.markdown('Vārds Uzvārds 201RDB005')
st.markdown('Andris Vilčuks 201RDB021')

st.header('Informācijas avoti vietnes izveidei:')
st.markdown('https://docs.streamlit.io/library/get-started')
st.markdown('https://www.nba.com/stats/teams/traditional')