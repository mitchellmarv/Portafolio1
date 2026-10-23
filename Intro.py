import streamlit as st
from PIL import Image

st.set_page_config(page_title="Segundo Portafolio Interfaces Multimodales", page_icon="🌌", layout="wide")

# ─────────────────────────────────────────────
# ESTILOS — tema galaxia (morados y azules)
# ─────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Fondo galaxia: estrellas + degradado profundo */
    .stApp {
        background:
            radial-gradient(1.5px 1.5px at 20px 30px, #ffffff, transparent),
            radial-gradient(1px 1px at 90px 140px, #c4b5fd, transparent),
            radial-gradient(1.5px 1.5px at 160px 70px, #ffffff, transparent),
            radial-gradient(1px 1px at 230px 190px, #93c5fd, transparent),
            radial-gradient(2px 2px at 310px 110px, #ffffff, transparent),
            radial-gradient(1px 1px at 380px 40px, #e9d5ff, transparent),
            radial-gradient(ellipse at 15% 10%, rgba(139,92,246,0.35) 0%, transparent 50%),
            radial-gradient(ellipse at 85% 85%, rgba(59,130,246,0.30) 0%, transparent 50%),
            linear-gradient(160deg, #0b0b2b 0%, #1a1145 45%, #2a1465 100%);
        background-size: 420px 240px, 420px 240px, 420px 240px, 420px 240px,
                         420px 240px, 420px 240px, 100% 100%, 100% 100%, 100% 100%;
        background-attachment: fixed;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1145 0%, #2e1a6b 100%) !important;
        border-right: 1px solid #5b3fc4;
    }
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #e9d5ff !important;
        font-weight: 700 !important;
    }
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] label {
        color: #c4b5fd !important;
    }

    /* Título principal con degradado */
    h1 {
        background: linear-gradient(90deg, #c4b5fd 0%, #818cf8 45%, #38bdf8 100%);
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
        color: #c4b5fd !important;
        font-weight: 800 !important;
        letter-spacing: -0.5px !important;
        padding-bottom: 12px;
        border-bottom: 3px solid transparent;
        border-image: linear-gradient(90deg, #8b5cf6, #3b82f6, transparent) 1;
    }

    h2, h3, h4, h5, h6 {
        color: #c4b5fd !important;
        font-weight: 700 !important;
    }

    p, li {
        color: #d9d6ff !important;
        line-height: 1.6 !important;
    }

    a {
        color: #7dd3fc !important;
        font-weight: 600 !important;
    }
    a:hover {
        color: #e9d5ff !important;
    }

    /* Divisores con degradado luminoso */
    hr {
        border: none !important;
        height: 2px !important;
        background: linear-gradient(90deg, transparent, #8b5cf6, #3b82f6, transparent) !important;
        box-shadow: 0 0 10px rgba(139,92,246,0.6);
        margin: 18px 0 !important;
    }

    /* Imágenes con brillo */
    [data-testid="stImage"] img {
        border-radius: 14px;
        border: 2px solid #6d4fd6;
        box-shadow: 0 0 18px rgba(139,92,246,0.55), 0 0 36px rgba(59,130,246,0.25);
    }
</style>
""", unsafe_allow_html=True)

st.title("Aplicaciones con Inteligencia Artificial (2)")

with st.sidebar:
  st.subheader("Portafolio Interfaces Multimodales (2): Isabella Lizalda Ruiz")
  st.write("Este portafolio reúne un conjunto de aplicaciones web desarrolladas en Streamlit que exploran la integración de Inteligencia Artificial, Visión por Computadora, Procesamiento de Lenguaje Natural (PLN) e Internet de las Cosas (IoT) de forma interactiva. Dentro de estos proyectos abordamos el análisis inteligente de imágenes y bocetos mediante redes neuronales (CNN, MNIST) y modelos multimodales (gpt-4o), la consulta de documentos en formato PDF usando sistemas de Recuperación Aumentada por Generación (RAG) con bases vectoriales (FAISS), y la creación de lienzos creativos con extracción de colorimetría en espacio CIE Lab. Además, conectamos la web con el entorno físico a través de paneles de control IoT y reconocimiento de voz para actuadores mediante el protocolo MQTT (tanto en prototipos base como en versiones personalizadas para simulación en Wokwi), demostrando cómo transformar código en interfaces funcionales, dinámicas y fáciles de usar.")

col1, col2, col3 = st.columns(3)

with col1:

 st.subheader("Clasificación e interpretación de números dibujados a mano con Redes Neuronales")
 image = Image.open('1.jpg')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos cómo dibujar dígitos en un lienzo interactivo para que un modelo de red neuronal convolucional (CNN) entrenado en MNIST prediga el número en tiempo real y muestre un análisis gráfico de las probabilidades de cada opción.")
 url = "https://escritura1-aqjafjmvuz6elzxsvakp7q.streamlit.app"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.divider()

 st.subheader("Análisis de paletas de color y conversión a CIE Lab en lienzos")
 image = Image.open('2.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo dibujar sobre un panel con estilo galáctico para extraer automáticamente la paleta de colores dominantes en el lienzo, identificando sus códigos HEX, RGB y nombres en español mediante conversión a espacio de color CIE Lab.")
 url = "https://dibujorecog-vnxqmegb3pzv5tkguif65r.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

 st.divider()

 st.subheader("Control de actuadores IoT vía protocolo MQTT (Prototipo funcional)")
 image = Image.open('3.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos la versión original del panel para enviar comandos de control a dispositivos IoT (como LEDs y servomotores) publicando mensajes JSON en tópicos de un broker MQTT en tiempo real.")
 url = "https://sensormqtt-eallek5nwy2yt2bpmnfjhy.streamlit.app"
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
