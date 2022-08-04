import streamlit as st
from PIL import Image
import base64
from streamlit_option_menu import option_menu
from st_functions import st_button, load_css

# SIDEBAR
st.sidebar.markdown("# 🗑 Dumpster Diving")
st.sidebar.markdown(
    "Tentang teknik kejahatan di dunia maya yang bernama *Dumpster Diving* yang melingkupi deskripsi dan bagaimana cara mencegahnya")

# TOP HEADER IMAGE
image5 = Image.open(
    "C:\Streamlit\IMAGES\Dumpster header.png")
st.image(image5)
"\n"
"\n"


# TOP INFO
col1, col2 = st.columns(2)


# PENJELASAN AWAL DUMPSTER DIVING
with col1:
    file_ = open("C:\Streamlit\ANIMASI\dumpsterr.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True)

with col2:
    original_title = '<p style="font-family:Isocpeur; color:IndianRed; font-size: 26px;">APA ITU <i>DUMPSTER DIVING</i></p>'
    st.markdown(original_title, unsafe_allow_html=True)

    "Metode mencari informasi penting di lokasi **tempat pembuangan** perusahaan atau individu,  untuk kemudian digunakan sebagai **bahan menyerang** individu, perusahaan, atau jaringan perusahaan."
    "Tempat pembuangan tidak hanya secara **fisik**, tetapi juga **elektronik**. *Hackers* menggunakan ***malware*** untuk mencari informasi dari data sampah elektronik."
    "Statistik menunjukan bahwa orang Amerika mendapatkan hampir **4 juta spam email** setiap tahun, dan lebih dari **88% informasi** didapatkan dari metode dumpster diving."
    "\n"

# LINK VIDEO YOUTUBE
load_css()
icon_size = 20
st_button('youtube', 'https://www.youtube.com/watch?v=UkVPbQpeyxY',
          'Video Animasi tentang Dumpster Diving', icon_size)

"\n"
"\n"

# DATA YANG INGIN DICARI PENJAHAT
"\n"
st.markdown("#### DATA YANG DICARI")
"\n"
image = Image.open("C:\Streamlit\IMAGES\DataPenting.png")
st.image(image, caption="Data Penting yang Menjadi Sasaran *Hackers*")


# BAHAYA SELANJUTNYA APA YAAAA
"\n"
st.markdown("#### TINDAK KEJAHATAN SELANJUTNYA")
"Contohnya : Dari nota pembelian, penjahat dapat menggunakan data untuk membuat akun kartu kredit baru, seolah-olah sebagai pemilik rekening untuk kemudian mengakses dana dari rekening tersebut."
"\n"
file_ = open("C:\Streamlit\ANIMASI\Afterdumpster diving.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True)


# CARA MENCEGAHNYA
"\n"
st.markdown("#### BAGAIMANA MENCEGAHNYA?")
"\n"

# PILIHAN CARA-CARA
selected = option_menu(menu_title=None,
                       options=["1. Managemen Data Elektronik",
                                "2. Managemen Data Non Elektronik", "3. Training"],
                       icons=["folder-fill", "file-text-fill", "easel2-fill"],
                       default_index=0, styles={
                           "container": {"padding": "0!important", "background-color": ""},
                           "icon": {"color": "MidnightBlue", "font-size": "18px"},
                           "nav-link": {
                               "font-size": "18px",
                               "text-align": "left",
                               "margin": "0px",
                               "--hover-color": "",
                           },
                           "nav-link-selected": {"background-color": "MediumAquamarine"},
                       },)

if selected == "1. Managemen Data Elektronik":
    st.markdown("##### **Managemen Data Elektronik**")
    "- **Management data** : Data penting perlu penanganan khusus."
    "- Membuat **kebijakan** tentang berapa lama data elektronik disimpan."
    "- Memastikan semua data pada laptop atau komputer yang sudah tidak digunakan telah **dihapus sempurna**"

    col1, col2 = st.columns((2, 8))

    with col2:
        image = Image.open("C:\Streamlit\IMAGES\delete files.jpg")
        st.image(
            image, caption="Penghapusan data elektronik penting yang sudah tidak terpakai", width=400)


if selected == "2. Managemen Data Non Elektronik":
    st.markdown("##### **Managemen Data Elektronik**")
    "- Memastikan semua informasi penting dalam bentuk tercetak **dihancurkan dalam mesin penghancur kertas** sebelum dibuang."
    "- Menggunakan **tinta tidak permanen**"
    "- Membuat **tempat sampah khusus** untuk sampah penting (terkunci)."
    "- Memilih **rekan pengelolaan daur ulang** sampah yang terpercaya"

    col1, col2 = st.columns((2, 8))

    with col2:
        image = Image.open(
            "C:\Streamlit\IMAGES\Hancurkan Kertas.jpg")
        st.image(
            image, caption="Penghancuran data non elektronik penting yang sudah tidak terpakai", width=400)


if selected == "3. Training":
    st.markdown("##### **Pelatihan Karyawan**")
    "Mengedukasi kepada seluruh karyawan bahaya dari *Dumpster Diving*"

    col1, col2 = st.columns((2, 8))

    with col2:
        image = Image.open(
            "C:\Streamlit\IMAGES\Training.jpg")
        st.image(
            image, caption="Pelatihan Karyawan", width=400)
