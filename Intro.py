import streamlit as st
from PIL import Image
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #00FF7F, #1E90FF);
        background-attachment: fixed;
        color: black; /* Color del texto */
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones Interfaces Multimodales")
  parrafo = (
    "Portafolio de Aplicaciones desarrolladas por Sebastián Mazo para el curso de Interfaces. Cada app está identificada por una de mis películas favoritas"
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Aplicación de Introducción")
 image = Image.open('The_Social_Network_film_poster.png')
 st.image(image, width=190)
 url = "https://intromazo.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Interfaz OCR")
 image = Image.open('arrival.jpg')
 st.image(image, width=200)
 url = "https://h5xa9bnzarohfcpxhge8gi.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Análisis de texto en español")
 image = Image.open('get out.jpg')
 st.image(image, width=200)
 url = "https://md6icpfgty6kkcg4jbn4f4.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Chatpdf")
 image = Image.open('her.jpg')
 st.image(image, width=200)
 url = "https://chatpdf-7xnxnkwrvfennmydfgjdwh.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Aplicación del tablero")
 image = Image.open('interstellar-new.jpeg')
 st.image(image, width=200)
 url = "https://urcp8dlzemfvsxyui7mzvx.streamlit.app/"
 st.write(f"[Enlace]({url})")



with col2: 
 st.subheader("Conversión texto a voz")
 image = Image.open('oldboy.jpeg')
 st.image(image, width=200) 
 url = "https://txt2spch-mmanvue2djq9vz8crpspgk.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Análisis de sentimientos")
 image = Image.open('parasite.jpeg')
 st.image(image, width=190)
 url = "https://2rndnvhzrswx5ytxymjc5z.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Reconocimiento de objetos (YOLO)")
 image = Image.open('pulp fiction.jpeg')
 st.image(image, width=200)
 url = "https://yolov5-cgftiuqjkuewrazxbr3hse.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Imagen-text")
 image = Image.open('spiderverse.jpg')
 st.image(image, width=200)
 url = "https://ocr-audio-nmhhxzm3fqp94k6lk5hj6b.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Control MQTT")
 image = Image.open('the lobster.jpeg')
 st.image(image, width=200)
 url = "https://sendcmqtt-mxxyp6jy6qkkquywjwtiaa.streamlit.app/"
 st.write(f"[Enlace]({url})")



with col3: 
 st.subheader("Interfaz voz a texto")
 image = Image.open('the shining.jpg')
 st.image(image, width=190)
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Análisis de texto en inglés")
 image = Image.open('uncut gems.jpg')
 st.image(image, width=200)
 url = "https://2rndnvhzrswx5ytxymjc5z.streamlit.app/"
 st.write(f"[Enlace]({url})")
 
 st.subheader("Reconocimiento de gestos")
 image = Image.open('whiplash.jpg')
 st.image(image, width=200)
 url = "https://drawrecog-mk3w2ucznaczizvnz3flib.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Reconocimiento de imagen táctil")
 image = Image.open('your name.jpg')
 st.image(image, width=200)
 url = "https://visionapp-zggx2dteh5vaqqgc6qs23.streamlit.app/"
 st.write(f"[Enlace]({url})")

 st.subheader("Control por voz MQTT")
 image = Image.open('Everything_Everywhere_All_at_Once.jpg')
 st.image(image, width=200)
 url = "https://ctrlvoice-bvwhvuufnhyh4yo42srnb4.streamlit.app/"
 st.write(f"[Enlace]({url})")



