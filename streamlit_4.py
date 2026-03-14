import streamlit as st
import pandas as pd

st.title("Análisis de Ventas desde Excel")

# ── Cargar Excel ────────────────────────────────────────────
archivo = st.file_uploader("Sube tu archivo Excel", type=["xlsx", "xls"])

if archivo is None:
    st.info("Sube un archivo Excel para comenzar el análisis.")
    st.stop()

df = pd.read_excel(archivo)
st.dataframe(df)

# ── Filtros ────────────────────────────────────────────────
st.subheader("Filtros")

col1, col2, col3 = st.columns(3)

with col1:
    regiones = st.multiselect(
        "Región", 
        df["Region"].unique(), 
        default=df["Region"].unique()
    )
with col2:
    vendedores = st.multiselect(
        "Vendedor", 
        df["Vendedor"].unique(), 
        default=df["Vendedor"].unique()
    )
with col3:
    meses = st.multiselect(
        "Mes", 
        df["Mes"].unique(),
        default=df["Mes"].unique()
    )

filtrado = df[
    df["Region"].isin(regiones) &
    df["Vendedor"].isin(vendedores) &
    df["Mes"].isin(meses)
]

# ── Tabla ──────────────────────────────────────────────────
st.subheader("Datos")
st.dataframe(filtrado, use_container_width=True)

# # ── Gráficas ───────────────────────────────────────────────
st.subheader("Ventas por Vendedor")
st.bar_chart(filtrado.groupby("Vendedor")["Ventas"].sum())

st.subheader("Ventas por Región")
st.bar_chart(filtrado.groupby("Region")["Ventas"].sum())

st.subheader("Ventas por Mes")
st.line_chart(filtrado.groupby("Mes")["Ventas"].sum())
