import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

st.title("Análisis de Ventas desde Excel v3")

# ── Cargar Excel ────────────────────────────────────────────
archivos = st.file_uploader("Sube uno o varios archivos Excel", type=["xlsx", "xls"], accept_multiple_files=True)

if not archivos:
    st.info("Sube al menos un archivo Excel para comenzar el análisis.")
    st.stop()

df = pd.concat([pd.read_excel(f) for f in archivos], ignore_index=True)
st.caption(f"{len(archivos)} archivo(s) cargado(s) — {len(df):,} filas en total")
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

# ── Helpers ────────────────────────────────────────────────
def fig_to_bytes(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return buf

# ── Gráficas ───────────────────────────────────────────────
st.subheader("Ventas por Vendedor")
fig1, ax1 = plt.subplots()
filtrado.groupby("Vendedor")["Ventas"].sum().plot(kind="bar", ax=ax1)
ax1.set_ylabel("Ventas")
st.pyplot(fig1)
st.download_button("Descargar PNG", fig_to_bytes(fig1), "ventas_vendedor.png", "image/png")
plt.close(fig1)

st.subheader("Ventas por Región")
fig2, ax2 = plt.subplots()
filtrado.groupby("Region")["Ventas"].sum().plot(kind="bar", ax=ax2)
ax2.set_ylabel("Ventas")
st.pyplot(fig2)
st.download_button("Descargar PNG", fig_to_bytes(fig2), "ventas_region.png", "image/png")
plt.close(fig2)

st.subheader("Ventas por Mes")
fig3, ax3 = plt.subplots()
filtrado.groupby("Mes")["Ventas"].sum().plot(kind="line", marker="o", ax=ax3)
ax3.set_ylabel("Ventas")
st.pyplot(fig3)
st.download_button("Descargar PNG", fig_to_bytes(fig3), "ventas_mes.png", "image/png")
plt.close(fig3)
