import streamlit as st

st.title("Interactividad en Streamlit")

# Input de texto
nombre = st.text_input("¿Cómo te llamas?")
if st.button("Saludar"): # FALSE
    if nombre:
        st.write(f"Hola, {nombre}!")
    else:
        st.error("Escribe tu nombre primero.")

st.divider()

# # Slider
edad = st.slider(
    "¿Cuántos años tienes?", 
    min_value=1, 
    max_value=100, 
    value=26
)
st.write(f"Tienes {edad} años.")

st.divider()
# # Selectbox
color = st.selectbox(
    "¿Cuál es tu color favorito?", 
    ["Rojo", "Verde", "Azul", "Amarillo"]
)
st.write(f"Tu color favorito es: {color}")
