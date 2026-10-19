import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="Asistente STM Montevideo", page_icon="🚌")

st.title("🚌 Asistente STM - Montevideo")
st.write("Escribí tu origen y destino (o de qué esquina a qué zona querés ir) y te ayudo con las opciones del STM.")

# Intentar obtener la clave de API desde los secretos de Streamlit
api_key = st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ Falta configurar la GEMINI_API_KEY en los Secrets de Streamlit.")
else:
    # Configurar la API con la librería clásica
    genai.configure(api_key=api_key)

    # Usar el modelo estándar y estable
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Instrucción del sistema (El rol y personalidad de la IA)
    SYSTEM_INSTRUCTION = """
    Sos un asistente experto en el Sistema de Transporte Metropolitano (STM) de Montevideo y su área metropolitana (Uruguay).
    Tu objetivo es ayudar a los usuarios a planificar sus viajes en ómnibus de forma clara, amable y precisa.

    Reglas de respuesta:
    1. Si el usuario te indica un origen y un destino, indicale qué líneas de ómnibus suelen hacer ese recorrido o qué transbordos/combinaciones le convienen hacer (por ejemplo, en el Intercambiador Belloni, Terminal Colón, Tres Cruces, Paso de la Arena, Río Branco, o esquinas clave como Av. Italia y Propios, 18 de Julio, etc.).
    2. Explicá de forma sencilla cómo usar las tarjetas STM o boletos de transbordo (1 hora / 2 horas) si la ruta requiere combinar.
    3. Usá un lenguaje cordial, coloquial montevideano pero claro y ordenado (podés usar viñetas o listas numeradas).
    4. Si el origen o destino es ambiguo, dale la mejor opción general y decile qué referencia falta para precisar más.
    """

    # Caja de entrada del usuario
    consulta = st.text_input("¿A dónde querés viajar hoy?", placeholder="Ej: Estoy en Colón y quiero ir a Tres Cruces")

    if st.button("Buscar recorrido"):
        if consulta.strip():
            with st.spinner("Consultando opciones de ómnibus y combinaciones... 🚌"):
                try:
                    # Prompt completo combinando las reglas y la consulta
                    prompt_completo = f"{SYSTEM_INSTRUCTION}\n\nConsulta del usuario: {consulta}"
                    
                    # Generar la respuesta
                    response = model.generate_content(prompt_completo)
                    
                    st.markdown("### 🗺️ Sugerencia de recorrido:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Ocurrió un error al consultar la IA: {e}")
        else:
            st.warning("Por favor, ingresá tu origen y destino para poder ayudarte.")
