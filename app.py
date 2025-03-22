# Versión extendida de la app EVA-CSR con cálculo de puntaje, recomendación, escudo UNAL y visualización gráfica
import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import io

# Configuración inicial de la página
st.set_page_config(page_title="Evaluador EVA-CSR", page_icon="🔒", layout="centered")

# Encabezado institucional con imagen y nombre de la facultad
col1, col2 = st.columns([1, 6])
with col1:
    try:
        logo = Image.open("unal_logo.png")  # Asegúrate que el archivo esté en el repositorio
        st.image(logo, width=70)
    except:
        st.text("[Logo UNAL]")
with col2:
    st.markdown("""
    ### **Facultad de Enfermería - Universidad Nacional de Colombia**  
    #### Evaluador EVA-CSR - Escala de Vulnerabilidad al VIH en Adolescentes Escolarizados
    """)

# Bienvenida
st.markdown("Bienvenido/a. Responde con sinceridad para obtener una recomendación educativa personalizada.")
nombre = st.text_input("Ingresa tu nombre (opcional)", help="No se guardará tu identidad, este resultado es anónimo.")

# Opciones de respuesta
opciones = ["Nada de acuerdo", "Poco de acuerdo", "Medianamente de acuerdo", "Bastante de acuerdo", "Totalmente de acuerdo"]

# Preguntas validadas
preguntas = [
    "1. En el colegio proporcionan información precisa sobre riesgos sexuales.",
    "2. En el colegio puedo decir lo que pienso cuando tengo un problema.",
    "3. Aceptaría tener relaciones sexuales si son planeadas con mi pareja.",
    "4. En el colegio explican la forma correcta del uso del condón.",
    "5. En el colegio puedo expresar mis sentimientos cuando tengo un problema.",
    "6. Tendría relaciones sexuales si siento compromiso de la otra persona.",
    "7. En el colegio fomentan el uso del condón como responsabilidad compartida.",
    "8. Considero que es maltrato hacia la pareja o ex pareja los insultos.",
    "9. Aceptaría relaciones sexuales si me siento seguro(a) con mi pareja.",
    "10. En el colegio proporcionan información para retrasar el inicio sexual.",
    "11. Creo que es maltrato hacia la pareja o ex pareja las humillaciones.",
    "12. Tendría relaciones sexuales si siento deseo sexual por mi pareja.",
    "13. En el colegio informan sobre infecciones de transmisión sexual como VIH/SIDA.",
    "14. Pienso que es maltrato hacia la pareja o ex pareja los desprecios.",
    "15. Aceptaría relaciones sexuales si siento amor por mi pareja.",
    "16. En el colegio promueven debates sobre sexualidad.",
    "17. Creo que es maltrato hacia la pareja o ex pareja las amenazas.",
    "18. Aceptaría relaciones sexuales si siento plena confianza en mi pareja.",
    "19. En el colegio promueven respeto sobre la vida sexual de las personas.",
    "20. El centro de salud de mi localidad brinda información sobre sexualidad.",
    "21. Me siento presionado(a) por una persona que acabo de conocer.",
    "22. En el colegio brindan información sobre prevención del VIH/SIDA.",
    "23. Podría acudir con mi familia cuando tengo un problema.",
    "24. Tendría relaciones sexuales en un sitio donde los encuentros son anónimos.",
    "25. El centro de salud me ha capacitado sobre temas de VIH/SIDA.",
    "26. Siento que mis padres me apoyan en cosas que me importan.",
    "27. Aceptaría tener relaciones sexuales por dinero.",
    "28. El centro de salud me ha informado sobre derechos sexuales y reproductivos.",
    "29. Mi familia me anima a conseguir logros académicos."
]

# Registro de respuestas
puntaje_total = 0
respuestas = []

with st.form("formulario"):
    for i, pregunta in enumerate(preguntas):
        seleccion = st.radio(pregunta, opciones, key=f"pregunta_{i}")
        respuestas.append(seleccion)
        puntaje_total += opciones.index(seleccion) + 1
    enviar = st.form_submit_button("Enviar respuestas")

# Resultados y visualización
if enviar:
    st.markdown("## Resultado personalizado:")
    if nombre:
        st.write(f"Gracias por participar, **{nombre}**.")
    else:
        st.write("Gracias por participar.")

    st.write(f"Tu puntaje total fue: **{puntaje_total}** sobre 145")

    # Visualización: barra de riesgo
    st.markdown("### Nivel de riesgo de vulnerabilidad al VIH")
    fig, ax = plt.subplots(figsize=(6, 1.2))
    ax.barh([0], [puntaje_total], color="orange")
    ax.set_xlim(0, 145)
    ax.set_yticks([])
    ax.set_xticks([0, 70, 110, 145])
    ax.set_xticklabels(["0", "70", "110", "145"])
    ax.set_title("Puntaje de riesgo")
    st.pyplot(fig)

    # Interpretación
    if puntaje_total <= 70:
        st.warning("**Riesgo alto de vulnerabilidad al VIH.** Es fundamental recibir intervención educativa y apoyo profesional urgente.")
    elif 71 <= puntaje_total <= 110:
        st.info("**Riesgo moderado.** Requiere refuerzo educativo sobre salud sexual y toma de decisiones responsables.")
    else:
        st.success("**Riesgo bajo.** Se recomienda mantener los factores protectores y continuar con educación sexual saludable.")
