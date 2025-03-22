
import streamlit as st

st.set_page_config(page_title="Evaluador EVA-CSR", page_icon="📊", layout="centered")

st.title("Evaluador EVA-CSR")
st.markdown("Bienvenido/a. Responde con sinceridad para obtener una recomendación personalizada.")
nombre = st.text_input("Ingresa tu nombre (opcional)", help="Este dato es anónimo")

st.subheader("Cuestionario")

respuestas = []
opciones = ["Nada de acuerdo", "Poco de acuerdo", "Medianamente de acuerdo", "Bastante de acuerdo", "Totalmente de acuerdo"]

preguntas = [
    "1. En el colegio proporcionan información precisa sobre los riesgos de la actividad sexual.",
    "2. En el colegio puedo decir lo que pienso cuando tengo un problema.",
    "3. Aceptaría tener relaciones sexuales si son planeadas con tiempo con mi pareja.",
    "4. En el colegio explican la forma correcta del uso del condón.",
    "5. En el colegio puedo expresar mis sentimientos cuando tengo un problema.",
    "6. Tendría relaciones sexuales si siento compromiso de la otra persona en una relación sentimental.",
    "7. En el colegio fomentan el uso del condón como una responsabilidad del hombre y la mujer.",
    "8. Considero que es maltrato hacia la pareja o expareja los insultos.",
    "9. Aceptaría tener relaciones sexuales si me siento seguro (a) con mi pareja.",
    "10. En el colegio proporcionan información precisa para retrasar el inicio de la actividad sexual.",
    "11. Creo que es maltrato hacia la pareja o expareja las humillaciones.",
    "12. Tendría relaciones sexuales si siento deseo sexual por mi pareja.",
    "13. En el colegio proporcionan información sobre infecciones de transmisión sexual como el VIH/SIDA.",
    "14. Pienso que es maltrato hacia la pareja o expareja los desprecios.",
    "15. Aceptaría tener relaciones sexuales si siento amor por mi pareja.",
    "16. En el colegio promueven cuestionar tabúes en torno a la vida sexual.",
    "17. Creo que es maltrato hacia la pareja o expareja las amenazas.",
    "18. Aceptaría tener relaciones sexuales si siento plena confianza de mi pareja.",
    "19. En el colegio promueven reflexionar críticamente sobre la vida sexual de las personas.",
    "20. El centro de salud de mi localidad no me ha brindado información sobre temas relacionados con el VIH/SIDA.",
    "21. Aceptaría tener relaciones sexuales con una persona que acabo de conocer porque me resulta agradable y atractiva.",
    "22. En el colegio me han brindado suficiente información sobre cómo prevenir la infección por el VIH/SIDA.",
    "23. Podría contar con mi familia cuando tengo un problema.",
    "24. He tenido relaciones sexuales en un sitio donde los encuentros sexuales sean anónimos.",
    "25. El centro de salud de mi localidad me ha capacitado sobre temas relacionados con el VIH/SIDA.",
    "26. En mi casa disfrutan ayudarme en las cosas que me importan.",
    "27. Aceptaría tener relaciones sexuales por dinero.",
    "28. El centro de salud de mi localidad me ha informado sobre mis derechos en salud sexual y reproductiva y VIH/SIDA.",
    "29. Mi familia me anima para conseguir logros académicos en el colegio."
]

for pregunta in preguntas:
    respuestas.append(st.radio(pregunta, opciones, key=pregunta[:20]))

if st.button("Enviar respuestas"):
    st.subheader("Resultado simulado:")
    st.write("Gracias por participar, {}. Según tus respuestas, tu nivel de riesgo será evaluado en la versión completa.".format(nombre if nombre else "Usuario/a"))
