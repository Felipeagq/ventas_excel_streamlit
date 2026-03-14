import db 
import streamlit as st 

# Crear usuario
nombre = st.text_input("Ingresa tu nombre",key="n1")
password = st.text_input("Ingresa tu password",key="p1")
if st.button("Crear usuario"):
    if nombre and password:
        db.crear_user(
            user=nombre,
            passw=password
        )
        st.success("Se ha creado el registro correctamente")
    else:
        st.error("Aja papu como crear algo si tengo la info incompleta")

st.divider()
# Leer usuarios
if st.button("Leer todos los usuarios"):
    st.write(db.obtener_usuario())

st.divider()
id_usuario = st.text_input("Ingresa el ID del usuario a buscar")
if st.button("Buscar"):
    st.write(db.obtener_usuario_id(id_usuario))


st.divider()
# Actualizar usuario
id_usuario = st.text_input("Ingresa el ID del usuario a buscar",key="id_usuario_2")
nombre = st.text_input("Ingresa tu nombre",key="n2")
password = st.text_input("Ingresa tu password",key="p2")


st.divider()
# Eliminar usuarios