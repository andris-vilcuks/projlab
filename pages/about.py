import streamlit as st

st.set_page_config(page_title="Projektēšanas laboratorija", page_icon=":basketball:", layout="wide")

st.title('Basketbola spēles rezultāta prognozēšana')

st.markdown('Izplatīta metode, ko izmanto spēļu rezultātu prognozēšanai komandu sporta veidos, ir pazīstama kā “loģistisko regresiju”. Šis modelis izmanto vairākus mainīgos lielumus abām komandām un izveido formulu, ko var izmantot, lai aprēķinātu katras komandas uzvaras varbūtību. Izmantotie mainīgie parasti ietver spēlētāju vērtējumus, komandu reitingus un iepriekšējo sniegumu.')

st.markdown(about.md)