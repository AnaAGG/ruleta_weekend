


import streamlit as st

import time

from streamlit_option_menu import option_menu
from streamlit_tags import st_tags


import sys
sys.path.append('src')
import suport_yml as spyml
import suport_stream as spyst


nombre_archivo = 'listado_equipos.yml'

selected2 = option_menu(None, ["Home", "Update",  'Settings'], 
    icons=['house', 'cloud-upload',  'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected2 == "Update":
    st.write("# Code for streamlit tags")
    maxtags = st.slider('Number of tags allowed?', 1, 10, 3, key='perrillo')
    keywords = st_tags(label='# Introduce el nombre de los equipos:',
                        maxtags=maxtags,
                        key="aljnf")
    lista = [key for key in keywords]
    diccionario = {'equipos': lista}
    spyml.creacion_archivo(nombre_archivo, diccionario)
    if st.button('Confirm'):
        st.markdown("""# Equipos actualizados!""")


st.markdown("""# ¡Buenos días equipos!""")
st.markdown("### Bienvenidos a las presentaciones del Hack(io) Weekend")

st.image("imagenes/hackio_weekend.png")
st.image("imagenes/fotos-notion.png")

time.sleep(2)

if st.button('Selecionador de equipos'):
    
    st.write('Turno del equipo...' )
    st.write(spyst.sorteo(nombre_archivo))



  

