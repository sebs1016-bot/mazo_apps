import streamlit as st
from PIL import Image
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #00FF7F, #1E90FF);
        background-attachment: fixed;
        color: white; /* Color del texto */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones Interfaces Multimodales")
  parrafo = (
    "Portafolio de Aplicaciones desarrolladas por Sebastián Mazo para el curso de Interfaces"
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Aplicación de Introducción")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial") 
 url = "https://intromazo.streamlit.app/"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Interfaz OCR")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://h5xa9bnzarohfcpxhge8gi.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Análisis de texto en español")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://md6icpfgty6kkcg4jbn4f4.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Chatpdf")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://chatpdf-7xnxnkwrvfennmydfgjdwh.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Aplicación del tablero")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://urcp8dlzemfvsxyui7mzvx.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")



with col2: 
 st.subheader("Conversión texto a voz")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://txt2spch-mmanvue2djq9vz8crpspgk.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Análisis de sentimientos")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://2rndnvhzrswx5ytxymjc5z.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Reconocimiento de objetos (YOLO)")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://yolov5-cgftiuqjkuewrazxbr3hse.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")

 st.subheader("Imagen-text")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://ocr-audio-nmhhxzm3fqp94k6lk5hj6b.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Control MQTT")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://sendcmqtt-mxxyp6jy6qkkquywjwtiaa.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")



with col3: 
 st.subheader("Interfaz voz a texto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de texto en inglés")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://2rndnvhzrswx5ytxymjc5z.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Reconocimiento de gestos")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://drawrecog-mk3w2ucznaczizvnz3flib.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

 st.subheader("Reconocimiento de imagen táctil")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://visionapp-zggx2dteh5vaqqgc6qs23.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Control por voz MQTT")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://ctrlvoice-bvwhvuufnhyh4yo42srnb4.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")



