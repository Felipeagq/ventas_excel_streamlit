import streamlit as st
from db import crear_user, obtener_usuario, actualizar_usuario, eliminar_usuario

st.title("Gestión de Usuarios")

# ── Crear usuario ──────────────────────────────────────────
st.subheader("Crear usuario")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Crear"):
    if username and password:
        crear_user(username, password)
        st.success(f"Usuario '{username}' creado!")
    else:
        st.warning("Completa los dos campos.")

# ── Listar usuarios ────────────────────────────────────────
st.subheader("Usuarios en la base de datos")

if st.button("Actualizar lista"):
    pass  # solo fuerza el re-render

usuarios = obtener_usuario()
if usuarios:
    data = [{"ID": u.id, "Username": u.username} for u in usuarios]
    st.table(data)
else:
    st.info("No hay usuarios registrados.")

# ── Actualizar usuario ─────────────────────────────────────
st.subheader("Actualizar usuario")
id_actualizar = st.number_input("ID a actualizar", min_value=1, step=1)
nuevo_nombre = st.text_input("Nuevo username")
nueva_password = st.text_input("Nueva password", type="password")

if st.button("Actualizar"):
    resultado = actualizar_usuario(id_actualizar, nuevo_nombre, nueva_password)
    if resultado:
        st.success("Usuario actualizado!")
    else:
        st.error("No se encontró el ID.")

# ── Eliminar usuario ───────────────────────────────────────
st.subheader("Eliminar usuario")
id_eliminar = st.number_input("ID a eliminar", min_value=1, step=1, key="del")

if st.button("Eliminar"):
    resultado = eliminar_usuario(id_eliminar)
    if resultado:
        st.success("Usuario eliminado!")
    else:
        st.error("No se encontró el ID.")
