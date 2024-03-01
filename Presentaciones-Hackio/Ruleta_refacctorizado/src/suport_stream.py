
import streamlit as st
import random

import sys
sys.path.append('src')
import suport_yml as spyml
import time
def sorteo(file_name): 
    """
    Función que realiza un sorteo de una lista de elementos
    a partir de un archivo YAML y los muestra en pantalla 
    de forma aleatoria.
    args: 
    file_name: str, nombre del archivo YAML
    return:
    data: dict, diccionario con los elementos restantes
    
    """
    # Cargar el archivo YAML``
    data = spyml.abrir_archivo(file_name)
    # hasta que la lista este vacia
    while len(data['equipos']) > 0:
        ## Elegir un elemento aleatorio
        eleccion = random.choice(data['equipos'])
        ## Mostrar el elemento elegido texto o foto
        #st.write(eleccion)

        if eleccion.capitalize() == "Amarillo":
            st.image("imagenes/amarillo.JPG")
        elif eleccion.capitalize() == "Verde":
            st.image("imagenes/verde.JPG")
        elif eleccion.capitalize() == "Blanco":
            st.image("imagenes/blanco.JPG")
        elif eleccion.capitalize() == "Rojo":
            st.image("imagenes/rojo.JPG")
        elif eleccion.capitalize() == "Morado":
            st.image("imagenes/morado.JPG")
        elif eleccion.capitalize() == "Naranja":
            st.image("imagenes/naranja.JPG")
        elif eleccion.capitalize() =="Azul":
            st.image("imagenes/azul.JPG")
    


        ##eliminamos el elemento elegido
        spyml.elimina_archivo(file_name,'equipos',eleccion)
        #contador += 1
        st.balloons()
        time.sleep(8)
        st.experimental_rerun()
    st.write('¡Sorteo completado!')
    
    return data  