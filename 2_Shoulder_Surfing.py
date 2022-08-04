import streamlit as st
from PIL import Image

st.set_page_config(page_title="Shoulder Surfing", layout="wide")

# Judul
with st.container():
    st.title("SHOULDER SURFING")

# Penjelasan shoulder surfing

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.subheader("Apa itu Shoulder Surfing?")
        st.write("_Shoulder surfing_ adalah cara yang digunakan penjahat untuk menemukan kata sandi, nomor identifikasi pribadi, nomor akun, dan informasi lainnya dari calon korban dengan cara mengamati mereka.")
    with right_column:
        st.write("##")
        # image tentang bagaimana cara kerja shoulder surfing
        image = Image.open('C:\Streamlit\IMAGES\SS.png')
        st.image(image)

with st.container():
    st.write("##")
    left_column, right_column = st.columns(2)
    with left_column:
        # image tentang dimana terjadi shoulder surfing
        image = Image.open('C:\Streamlit\IMAGES\SS1.png')
        st.image(image)
    with right_column:
        # image tentang mencegah shoulder surfing
        image = Image.open('C:\Streamlit\IMAGES\SS2.png')
        st.image(image)
