import streamlit as st
from PIL import Image

st.set_page_config(page_title="Aplicaciones de IA", page_icon="☕", layout="wide")

# ─────────────────────────────────────────────
# ESTILOS — paleta café
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(160deg, #fbf6f0 0%, #f3e6d8 100%);
    }

    [data-testid="stSidebar"] {
        background-color: #4b3621 !important;
        border-right: 1px solid #6f4e37;
    }
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #f3e6d8 !important;
        font-weight: 700 !important;
    }
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: #e6d2b8 !important;
    }

    h1 {
        color: #4b3621 !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px !important;
        border-bottom: 3px solid #a9744f;
        padding-bottom: 12px;
    }
    h2, h3 {
        color: #6f4e37 !important;
        font-weight: 700 !important;
    }
    p, li {
        color: #5a4632 !important;
        line-height: 1.6 !important;
    }
    a {
        color: #a9744f !important;
        font-weight: 600 !important;
    }

    hr {
        border: none !important;
        height: 2px !important;
        background: linear-gradient(90deg, transparent, #a9744f, transparent) !important;
        margin: 18px 0 !important;
    }

    [data-testid="stImage"] img {
        border-radius: 12px;
        border: 3px solid #d9bfa3;
        box-shadow: 0 3px 10px rgba(75,54,33,0.15);
    }
</style>
""", unsafe_allow_html=True)

st.title("☕ Aplicaciones de Inteligencia Artificial")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )

col1, col2, col3 = st.columns(3)

with col1:

 st.subheader("Conversión de texto a voz")
 image = Image.open('1.jpg')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos cómo transformar bloques de texto ingresados por el usuario en archivos de audio reproducibles y descargables usando la librería gTTS (Google Text-to-Speech).")
 url = "https://ttsappclase-xuzfpyq3nptmannkrebpq8.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.divider()

 st.subheader("Reconocimiento de texto en imágenes capturadas con cámara")
 image = Image.open('2.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo se extrae texto de una imagen capturada en tiempo real mediante la cámara web, aplicando filtros opcionales de procesamiento de imagen con OpenCV y Tesseract OCR.")
 url = "https://imagenrecog-deypwbnqyfbcniexbfcf2i.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

 st.divider()

 st.subheader("Búsqueda de respuestas por similitud de texto usando TF-IDF")
 image = Image.open('3.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo se procesa un conjunto de documentos de texto mediante técnicas de procesamiento de lenguaje natural (stemming y TF-IDF) para encontrar la mejor respuesta a una pregunta basándose en la similitud cosenoidal.")
 url = "https://questanswer-b5h4uhj4lpwhrbc4qmwfjo.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

with col2:
 st.subheader("Extracción, traducción y síntesis de voz")
 image = Image.open('4.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo se extrae texto del audio del usuario, para luego traducirlo a múltiples idiomas y convertirlo en un archivo de audio reproducible con diferentes acentos.")
 url = "https://tradlizalda-tbbbhpfmhbxv6spytpygsg.streamlit.app"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.divider()

 st.subheader("Generación y análisis de nubes de palabras interactivas")
 image = Image.open('5.jpg')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos cómo procesar textos o archivos cargados para eliminar palabras vacías, personalizar la paleta de colores y generar una nube de palabras interactiva junto con la tabla de frecuencias de los términos más relevantes.")
 url = "https://nubepalabras-2xwaxxthmm8ltubp3jwn5f.streamlit.app"
 st.write(f"Datos: [Enlace]({url})")

 st.divider()

 st.subheader("Clasificación de imágenes en tiempo real con Teachable Machine y Keras")
 image = Image.open('6.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo se utiliza un modelo de visión por computadora previamente entrenado para clasificar en tiempo real las fotos tomadas desde la cámara web (por ejemplo, identificando si lo que aparece en la imagen es humano o no).")
 url = "https://facialrecog-dutnm4dbmue8qpeegpbbvi.streamlit.app"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3:
 st.subheader("Extracción, traducción y generación de audio desde imágenes")
 image = Image.open('7.jpg')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos cómo extraer texto de una imagen tomada con la cámara o cargada como archivo, para luego traducirlo a varios idiomas y convertir la traducción en un archivo de audio con acentos personalizados.")
 url = "https://ocr-more-gvj3bi7jucdwdssczwngjr.streamlit.app"
 st.write(f"RAG: [Enlace]({url})")

 st.divider()

 st.subheader("Evaluación de polaridad y subjetividad en frases")
 image = Image.open('8.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo se analiza el tono emocional de un texto en español traduciéndolo al inglés para determinar si expresa un sentimiento positivo, negativo o neutral, junto con su nivel de subjetividad.")
 url = "https://sentiapp-4ite2mysfh2iont9mwzbts.streamlit.app"
 st.write(f"Vision: [Enlace]({url})")

 st.divider()

 st.subheader("Primera aplicación de Ejemplo")
 image = Image.open('9.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la primera aplicación de ejemplo.")
 url = "https://repos1-4v6tukesdjqytrvjsypysc.streamlit.app"
 st.write(f"Vision: [Enlace]({url})")
