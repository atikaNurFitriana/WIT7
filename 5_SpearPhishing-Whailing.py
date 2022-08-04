import streamlit as st
from PIL import Image
import base64
from st_functions import st_button, load_css

# SIDEBAR
st.sidebar.markdown("# 🎣 SparePhishing - Whailing")
st.sidebar.markdown(
    "Tentang teknik kejahatan di dunia maya, bentuk lain dari *Phishing*, yaitu *SparePhishing* dan *Whailing* yang melingkupi perbedaannya dan bagaimana cara mencegahnya")


# TOP HEADER IMAGE
image1 = Image.open(
    'C:\Streamlit\IMAGES\Phishing header.png')
st.image(image1)
"\n"
"\n"


# DIAGRAM PERBEDAAN
image = Image.open(
    'C:\Streamlit\IMAGES\Perbedaan Phishing, Spear Phishing, dan Whailing.png')
st.image(image, caption="Perbedaan Phishing, Spear Phishing, dan Whailing")

"Untuk mendapatkan gambaran lebih detil tentang perbedaan tersebut, dapat klik link dibawah"
load_css()
icon_size = 20
st_button('youtube', 'https://www.youtube.com/watch?v=JzoJeJBdhuI',
          'Video Perbandingan Phishing,Spear Phishing, dan Whailing', icon_size)

"\n"
"\n"
"\n"
# ISI MATERI 1, DENGAN 2 TAB
tab1, tab2, = st.tabs(["Spear Phishing", "Whailing"])


# MATERI SPEAR PHISHING
with tab1:
    col1, col2 = st.columns((2, 3))

    with col1:
        file_ = open("C:\Streamlit\ANIMASI\spearphishing.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True)

    with col2:
        original_title = '<p style="font-family:Isocpeur; color:SaddleBrown; font-size: 30px;"><b>SPEAR PHISHING</b></p>'
        st.markdown(original_title, unsafe_allow_html=True)
        "Seperti *Phishing* pada umumnya. Akan tetapi, penjahat siber secara spesifik memilih kelompok atau orang tertentu sebagai target. Sehingga, pesan *Phishing* dipersonalisasi sesuai dengan target. Contohnya dengan menyebut nama, alamat, dan informasi pribadi lainnya. Penjahat juga berpura-pura menjadi orang yang dikenal target."

    "\n"
    "\n"
    st.markdown("#### CARA KERJA *SPEARPHISHING*")
    image = Image.open("C:\Streamlit\IMAGES\Cara Kerja Phishing.png")
    st.image(image, caption="Cara Kerja Spear Phishing")


# MATERI WHAILING
with tab2:
    col1, col2 = st.columns((2, 3))

    with col2:
        original_title = '<p style="font-family:Isocpeur; color:SaddleBrown; font-size: 30px;"><b>WHAILING</b></p>'
        st.markdown(original_title, unsafe_allow_html=True)
        "Seperti *Spear Phishing*, tetapi targetnya adalah orang memiliki posisi penting dalam suatu perusahaan. Contohnya, CEO, direktur keuangan, dan lain lain. Tujuannya adalah untuk membuat korban mengirim uang dalam jumlah besar."
        st.write(
            "Gambaran proses tindak kejahatan *Whailing* dapat dilihat pada [klik video ini](https://www.cisco.com/c/en/us/products/security/what-is-cybersecurity.html?socialshare=video-blade-cyberattack)")

    with col1:
        file_ = open("C:\Streamlit\ANIMASI\Whailing.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True)

    st.markdown("#### CONTOH KASUS")
    "Di tahun 2016, Karyawan perusahaan Seagate yang secara tidak sengaja mengirimkan email terkait data pendapatan pajak beberapa petinggi perusahaan saat itu kepada pihak ketiga yang tidak dapat diverifikasi. Setelah melaporkan “phishing scam” tersebut kepada Internal Revenue Service (IRS) dan FBI, ternyata ditemukan bahwa ribuan data pribadi telah diambil pada serangan tersebut."


"----------------------------------------------------------------------------"
"\n"
# KESIMPULAN MENCEGAH
st.markdown("#### BAGAIMANA MENCEGAHNYA?")
image = Image.open("C:\Streamlit\IMAGES\Cara mencegah Phishing.png")
st.image(image, caption="Cara Mencegah Spear Phishing dan Whailing secara Keseluruhan")
"\n"
"\n"
"- Pelatihan **kesadaran keamanan 'cyber'**"
"- Mengurangi informasi pribadi yang dibagikan di **media sosial**"
"- **Update software**, sehingga system memiliki keamanan terkini."
"- Membuat **kebijakan** di perusahaan terkait keamanan 'cyber', contoh: sistem email monitoring"
"- **Pelatihan kesadaran** keamanan 'cyber' bagi seluruh karyawan"
"- Membuat **multi level verifikasi** pada sistem perusahaan"
"- Membatasi informasi pribadi karyawan yang tersedia disitus web resmi atau media sosial"
"- Melengkapi perangkat lunak pada perangkat perusahaan dengan **'anti-malware dan firewall'**"
