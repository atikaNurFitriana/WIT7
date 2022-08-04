from contextlib import redirect_stderr
import streamlit as st
from PIL import Image
import base64

# SIDEBAR
st.sidebar.markdown("# 🔐 Scareware - Ransomware")
st.sidebar.markdown(
    "Tentang teknik kejahatan di dunia maya yang bernama *Scareware* dan *Ransomware*, perbedaannya dan bagaimana mencegahnya")

# TOP HEADER IMAGE
image2 = Image.open("C:\Streamlit\IMAGES\Ransomware header.png")
st.image(image2)

"\n"
"\n"

# ISI MATERI 1, DENGAN 2 KOLOM
col1, col2 = st.columns((2, 4))

# SCAREWARE
with col1:
    file_ = open("C:\Streamlit\VIDEO\MALWARE_animasi.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True)

with col2:
    original_title = '<p style="font-family:Isocpeur; color:SaddleBrown; font-size: 30px;">APA ITU <i>SCAREWARE</i> ?</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    "Tindakan kejahatan di dunia maya, dimana korban seolah-olah merasa bahwa komputer sedang terserang **virus**, kemudian *Hacker* akan mengirimkan instruksi agar korban **menginstall *software*** yang tidak diperlukan atau ***malware*** itu sendiri. Fungsinya adalah untuk kemudian digunakan sebagai alat mencuri data pribadi korban."


"\n"
"\n"

# RANSOMWARE
original_title = '<p style="font-family:Isocpeur; color:SaddleBrown; font-size: 30px;">APA BEDANYA DENGAN <i>RANSOMWARE</i> ?</p>'
st.markdown(original_title, unsafe_allow_html=True)

"Mirip seperti *Scareware*, akan tetapi *Hacker* akan meminta korban untuk mengirimkan sejumlah **uang**. Setelah korban mengirimkan uang, *Hacker* baru akan mengirimkan kode atau program untuk menghilangkan virus atau membuka akses computer korban yang terkunci akibat virus tersebut."

"\n"
"\n"
"\n"
"Untuk lebih detail, mengenai apa itu *Scareware* dan *Ransomware*, serta bagaiamana cara mencegahnya, dapat dilihat pada video animasi di bawah ini."
"\n"

# VIDEO SCAREWARE RANSOMWARE
video_file = open("C:\Streamlit\VIDEO\MALWARE2.mp4", "rb")
video_bytes = video_file.read()

st.video(video_bytes)
"Judul Video : Apa itu *Scareware*, *Ransomware*, dan Bagaimana Cara Mencegahnya"
