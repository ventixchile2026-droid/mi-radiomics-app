import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="Mi Radiomics App - Prueba", layout="centered")
st.title("Mi Radiomics App — Prueba rápida")

st.markdown("""
Sube una imagen tomada con el teléfono para verificar que la app funciona.
Este es un ejemplo mínimo; cuando esté publicado, podremos subir la versión completa con calibración y extracción de features.
""")

uploaded = st.file_uploader("Sube una imagen (jpg, png, tiff)", type=["jpg","jpeg","png","tif","tiff"])
if uploaded:
    try:
        img = Image.open(io.BytesIO(uploaded.getvalue()))
        st.image(img, caption="Imagen subida", width="stretch")
        st.success("Imagen recibida. Aquí iría el procesamiento radiómico.")
    except Exception as e:
        st.error(f"No se pudo abrir la imagen: {e}")

st.markdown("---")
st.write("Siguientes pasos recomendados:")
st.write("1) Si la app funciona, subo la versión completa con calibración por patrón y extracción de features (PyRadiomics).")
st.write("2) Si usas PyRadiomics/SimpleITK necesitaremos desplegar con Docker/Render o conda (te ayudo).")
