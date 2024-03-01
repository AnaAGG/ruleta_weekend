import streamlit as st
import random
import time


st.markdown("""# ¡Buenos días equipos!""")
st.markdown("### Bienvenidos a las presentaciones del Hack(io) Weekend")

st.image("hackio_weekend.png")
st.image("fotos-notion.png")


contador = 0
# Paso 2: Crear una lista de elementos

colores = ["Amarillo", "Azul", "Verde", "Blanco", "Morado", "Rojo", "Naranja"]

if st.button(f"El orden de presentación de los equipos es ..."):
    while len(colores) > 0:
        time.sleep(2)
        # Paso 3: Elegir un elemento aleatorio
        eleccion = random.choice(colores)
        colores.remove(eleccion)
        st.write(eleccion)


