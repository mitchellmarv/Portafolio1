import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Conversión de texto a voz")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos cómo se extrae texto de una imagen capturada en tiempo real mediante la cámara web, aplicando filtros opcionales de procesamiento de imagen con OpenCV y Tesseract OCR.") 
 url = "https://ttsappclase-xuzfpyq3nptmannkrebpq8.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Reconocimiento de texto en imágenes capturadas con cámara")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://imagenrecog-deypwbnqyfbcniexbfcf2i.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Búsqueda de respuestas por similitud de texto usando TF-IDF")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo se procesa un conjunto de documentos de texto mediante técnicas de procesamiento de lenguaje natural (stemming y TF-IDF) para encontrar la mejor respuesta a una pregunta basándose en la similitud cosenoidal.") 
 url = "https://questanswer-b5h4uhj4lpwhrbc4qmwfjo.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://tradlizalda-tbbbhpfmhbxv6spytpygsg.streamlit.app"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Extracción, traducción y síntesis de voz desde imágenes")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos cómo se extrae texto del audio del usuario, para luego traducirlo a múltiples idiomas y convertirlo en un archivo de audio reproducible con diferentes acentos.") 
 url = "https://tradlizalda-tbbbhpfmhbxv6spytpygsg.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Clasificación de imágenes en tiempo real con Teachable Machine y Keras")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo se utiliza un modelo de visión por computadora previamente entrenado para clasificar en tiempo real las fotos tomadas desde la cámara web (por ejemplo, identificando si lo que aparece en la imagen es humano o no).).") 
 url = "https://facialrecog-dutnm4dbmue8qpeegpbbvi.streamlit.app"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Generación en Contexto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://ocr-more-gvj3bi7jucdwdssczwngjr.streamlit.app"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Evaluación de polaridad y subjetividad en frases")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo se analiza el tono emocional de un texto en español traduciéndolo al inglés para determinar si expresa un sentimiento positivo, negativo o neutral, junto con su nivel de subjetividad.") 
 url = "https://sentiapp-4ite2mysfh2iont9mwzbts.streamlit.app"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Primera aplicación de Ejemplo")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la primera aplicación de ejemplo.") 
 url = "https://repos1-4v6tukesdjqytrvjsypysc.streamlit.app"
 st.write(f"Vision: [Enlace]({url})")


