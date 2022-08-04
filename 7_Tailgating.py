import streamlit as st
from PIL import Image
import base64

# SIDEBAR
st.sidebar.markdown("# 🏃‍♀️ 🏃 Tailgating")
st.sidebar.markdown(
    "Tentang teknik kejahatan di dunia maya yang bernama *Tailgating* atau bisa disebut juga *Piggybacking* yang melingkupi perbedaannya dan bagaimana cara mencegahnya")

# TOP HEADER IMAGE
image4 = Image.open(
    "C:\Streamlit\IMAGES\Tailgating header.png")
st.image(image4)
"\n"
"\n"

# MATERI
# ISI MATERI 1, DENGAN 2 KOLOM
col1, col2 = st.columns(2)

with col2:
    original_title = '<p style="font-family:Isocpeur; color:SaddleBrown; font-size: 30px;"><b>TAILGATING</b> ?</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    st.write("Orang yang **tidak memiliki otoritas** menggunakan akses dari pihak yang memiliki otoritas khusus tersebut untuk memasuki daerah terbatas.")
    st.write("atau, **mengikuti secara diam-diam** pihak yang memiliki otoritas khusus tersebut, untuk turut memasuki daerah terbatas. ***(PIGGYBACKING)*** ")
    "\n"
    st.write("Secara sederhana, tidak terlihat berbahaya, akan tetapi dapat menimbulkan dampak yang berbahaya ketika orang yang tidak berkepentingan tersebut kemudian mencuri **data penting perusahaan**.")
    "\n"

    st.write(
        "Gambaran tentang 'Tailgating' dapat dilihat pada [video ini](https://www.youtube.com/watch?v=xGuOanYTQ9o)")

with col1:
    st.markdown("#### CARA KERJA")
    file_ = open("C:\Streamlit\ANIMASI\TAILGATING WAYS.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True)
    "\n"
    "\n"

# PERBEDAAN TAILGATING DAN PIGGY BACKING
st.markdown("##### PERBEDAAN 'TAILGATING' DAN 'PIGGYBACKING")
"\n"
"\n"
image5 = Image.open(
    "C:\Streamlit\IMAGES\PIGGY BACKING vs TAILGATING.png")
st.image(image5, caption="Gambaran Perbedaan 'Tailgating' dan 'Piggybacking'")
"\n"
"\n"

# CARA MENCEGAH
st.markdown("#### BAGAIMANA MENCEGAHNYA?")
"\n"
with st.expander("1. Desain Pintu Masuk"):
    st.write("Menggunakan sistem 2 pintu pada akses masuk. Pintu pertama harus tertutup dulu, setelah beberapa saat baru pintu kedua terbuka.")
    col1, col2 = st.columns((2, 8))

    with col2:
        image6 = Image.open("C:\Streamlit\IMAGES\desai pintu masuk.jpg")
        st.image(
            image6, caption="Desain pintu masuk dari yang paling aman", width=400)

with st.expander("2. Penggunaan Sensor pada Pintu Masuk"):
    st.write("Sensor mampu mendeteksi jumlah kartu akses yang diinput dan jumlah orang yang melewati akses masuk. Jika terdapat perbedaan, maka alarm keamanan akan menyala. ")
    col1, col2 = st.columns((2, 8))

    with col2:
        image7 = Image.open("C:\Streamlit\IMAGES\sensor pintu masuk.jpg")
        st.image(image7, caption="Sensor pada Pintu Masuk", width=400)

    col1, col2 = st.columns((2, 8))

    with col2:
        image8 = Image.open("C:\Streamlit\IMAGES\Sensor pintu masuk2.png")
        st.image(image8, caption="Kinerja Sensor pada Pintu Masuk", width=400)

with st.expander("3. Penggunaan Akses Sidik Jari"):
    st.write("Menggunakan sidik jari sebagai kode akses masuk")
    col1, col2, col3 = st.columns(3)

    with col2:
        image9 = Image.open("C:\Streamlit\IMAGES\Akkses sidik jari.jpg")
        st.image(image9, caption="Akses Sidik Jari")

with st.expander("4. Penggunaan Kartu Identitas"):
    st.write("Menggunakan kartu identitas bagi seluruh karyawan dan juga tamu, agar semua yang masuk terdaftar dengan jelas sebagai karyawan atau tamu. Dan tamu perlu mengikuti prosedur yang ketat, dengan meninggalkan identitas di resepsionis.")
    col1, col2 = st.columns((2, 8))

    with col2:
        image10 = Image.open("C:\Streamlit\IMAGES\KartuIdentitas.png")
        st.image(image10, caption="Penggunaan Kartu Identitas", width=400)


with st.expander("5. Pelatihan Keamanan Kepada Seluruh Karyawan"):
    st.write(
        "Pelatihan akan keamanan 'Cyber' , yang termasuk bahanya *Tailgating* bagi perusahaan")
