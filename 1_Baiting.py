import streamlit as st
from PIL import Image

st.set_page_config(page_title="Baiting", layout="wide")

# TOP HEADER IMAGE
image1 = Image.open(
    "C:\Streamlit\IMAGES\H1.png")
st.image(image1)

# SIDEBAR
st.sidebar.markdown("# 🎣 Baiting")
st.sidebar.markdown(
    "Tentang teknik kejahatan *Social Engineering*, yaitu *Baiting* yang melingkupi penjelasan, cara kerja, dan bagaimana cara mencegahnya")


# Judul
# with st.container():
#    st.title("BAITING")

# Penjelasan baiting
with st.container():
    st.write("---")
    st.subheader("Apa itu Baiting?")
    st.write("Baiting merupakan salah satu taktik rekayasa sosial di mana peretas memanfaatkan sifat manusia seperti rasa ingin tahu dan rakus untuk memikat korban ke dalam perangkap yang dapat mencuri informasi penting atau menimbulkan kerusakan sistem disebabkan malware.")

# Penjelasan Cara Kerja Baiting
with st.container():
    st.write("##")
    st.subheader("Bagaimana Cara Kerja Baiting?")
with st.container():
    left_column, right_clolumn = st.columns(2)
    with left_column:
        image = Image.open('C:\Streamlit\IMAGES\B1.png')
        st.image(image)
    with right_clolumn:
        st.write("Bentuk umpan yang paling umum menggunakan media fisik untuk menyebarkan malware. Misalnya, peretas meninggalkan umpan flash drive yang terinfeksi malware di area mencolok di mana calon korban pasti akan melihatnya. Ketika korban memasukkan flash drive ke komputer kantor atau rumah, malware secara otomatis diinstal pada sistem.")

with st.container():
    st.write("##")
    left_column, right_clolumn = st.columns(2)
    with left_column:
        st.write("Selain itu, terdapat umpan online seperti situs penyedia file atau aplikasi gratis, hal ini beresiko karena kemungkinan file atau aplikasi tersebut terinfeksi malware.")
    with right_clolumn:
        image = Image.open('C:\Streamlit\IMAGES\B2.png')
        st.image(image)

with st.container():
    st.write("##")
    st.header("Bagaimana Cara Mencegah Baiting?")
    st.write(
        """
        - Memasang perangkat lunas anti virus dan anti malware
        - Menghindari mengunduh file dari situs yang tidak tepercaya
        - Lebih berhati-hati terhadap drive yang ditemukan di tempat umum
        - Membuat prosedur keamanan siber dalam hal ini tata cara menggunakan perangkat eksternal (jika sebuah perusahaan)

"""
    )
