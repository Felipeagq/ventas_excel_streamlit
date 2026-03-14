import streamlit as st
import pandas as pd
import numpy as np

st.title("Mi primera app con Streamlit")

# Texto
st.write("Hola! Esto es un texto normal.")

# Dataset aleatorio
df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=["Columna A", "Columna B", "Columna C"]
)

st.subheader("Tabla de datos")
st.dataframe(df)

st.subheader("Gráfica de líneas")
st.line_chart(df)
