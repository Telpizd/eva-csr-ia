
import streamlit as st

# Configuración de la app
st.set_page_config(page_title="Evaluador EVA-CSR", page_icon="📊")

# Mensaje de bienvenida
st.title("Evaluador EVA-CSR")
st.write("Bienvenido/a. Responde con sinceridad para obtener una recomendación personalizada.")

# Campo de nombre
nombre = st.text_input("Ingresa tu nombre (opcional)", value="", help="Este dato es anónimo")

# Formulario de evaluación (Ejemplo)
st.subheader("Cuestionario")
pregunta1 = st.radio("1. En el colegio proporcionan información sobre riesgos sexuales", ["Nada de acuerdo", "Poco de acuerdo", "Medianamente de acuerdo", "Bastante de acuerdo", "Totalmente de acuerdo"])
pregunta2 = st.radio("2. En el colegio puedo decir lo que pienso cuando tengo un problema", ["Nada de acuerdo", "Poco de acuerdo", "Medianamente de acuerdo", "Bastante de acuerdo", "Totalmente de acuerdo"])

# Procesamiento de resultados (simulación)
st.subheader("Resultados")
riesgo = "Alto" if pregunta1 == "Nada de acuerdo" and pregunta2 == "Nada de acuerdo" else "Bajo"
st.write(f"Nivel de riesgo estimado: **{riesgo}**")

# Recomendación personalizada
st.subheader("Recomendación")
if riesgo == "Alto":
    st.write("Te recomendamos acceder a más información educativa sobre prevención del VIH.")
else:
    st.write("Sigues buenas prácticas. Sigue informándote y cuidándote.")

# Mensaje final
st.write("Gracias por participar en esta evaluación.")

