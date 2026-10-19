import streamlit as st

st.set_page_config(page_title="Asistente STM Montevideo", page_icon="🚌")

st.title("🚌 Asistente STM - Montevideo")
st.write("Hola, estoy armando mi primer asistente de transporte metropolitano con IA.")

# Caja de texto para la consulta
consulta = st.text_input("¿A dónde querés viajar hoy?")

if st.button("Buscar recorrido"):
    if consulta:
        st.success(f"Recibí tu consulta: '{consulta}'")
        st.write("Próximamente aquí te mostraré el ómnibus que te sirve y las combinaciones exactas. 🚀")
    else:
        st.warning("Por favor, escribí un origen y un destino.")
