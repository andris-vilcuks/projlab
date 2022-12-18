import streamlit as st

st.set_page_config(page_title="Projektēšanas laboratorija", page_icon=":basketball:")

st.title('Basketbola spēles rezultāta prognozēšana')

st.header('Rezultāta prognoze')
st.markdown('Izplatīta metode, ko izmanto spēļu rezultātu prognozēšanai komandu sporta veidos, ir pazīstama kā “loģistiskā regresija”. Šis modelis izmanto vairākus mainīgos lielumus abām komandām un izveido formulu, ko var izmantot, lai aprēķinātu katras komandas uzvaras varbūtību. Izmantotie mainīgie parasti ietver spēlētāju vērtējumus, komandu reitingus un iepriekšējo sniegumu.')

st.header('Dati')
st.markdown('Basketbola komandu dati tiek iegūti no vietnes https://www.nba.com/stats/teams/traditional , kurā ir pieejami gan pašreizējās, gan iepriekšējo sezonu komandu dati to apstrādei.')
st.markdown('Pēc nepieciešamības, lietotājam ir iespēja arī ievietot savu .csv datni datu apstrādei. Lai būtu iespējama pilnvērtīga datu apstrāde, lietotājam ir nepieciešamas kolonnas ar nosaukumiem:')
st.markdown('- TEAM')
st.markdown('- PTS')
st.markdown('- +/-')
st.markdown('- AST')
st.markdown('- REB')
st.markdown('- STL')

st.header('Formula')
st.markdown('No iegūtajiem datiem, tiek atlasīti tikai svarīgākie un noteikts to nozīmīgums ar skaitlisku vērtību:')
st.markdown('- Punkti jeb *points* (PTS) - 5')
st.markdown('- Plus/Mīnus (+/-) - 4')
st.markdown('- Piespēles jeb *assists* (AST) - 3')
st.markdown('- Atlēkušās bumbas jeb *rebounds* (REB) - 2')
st.markdown('- Atņemtās bumbas jeb *steals* (STL) - 1')

st.header('Darbu veidoja:')
st.markdown('Pauls Brikmanis 201RDB002')
st.markdown('Vladlens Fedosiks 201DDB023')
st.markdown('Marsels Kirilko 201RDB122')
st.markdown('Marika Krūmiņa 201RDB079')
st.markdown('Kristiāns Staņa 201RDB026')
st.markdown('Andris Vilčuks 201RDB021')

st.header('Informācijas avoti vietnes izveidei:')
st.markdown('https://docs.streamlit.io/library/get-started')
st.markdown('https://www.nba.com/stats/teams/traditional')