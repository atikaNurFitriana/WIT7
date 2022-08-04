from PIL import Image
import streamlit as st


st.set_page_config(
    page_title="Multipage App",
)

st.title("SOCIAL ENGINEERING")

st.sidebar.success("Select a page above.")

st.sidebar.markdown("# Tentang")
st.sidebar.markdown(
    "Web ini dibuat dalam rangka mengedukasi masyarakat umum tentang **Social Engineering**, agar bisa terhindar dari kejahatan di dunia maya")

st.sidebar.markdown("# Penyusun")
st.sidebar.markdown(
    "Trisna Nurhayati  &  Atika Nur Fitriana")

# Penjelasan rekayasa sosial

with st.container():
    st.write("---")
    st.subheader("Apakah Kalian Tahu Tautan Terlemah dalam Keamaan Siber?")
    # Insert video
    video_file = open('C:\Streamlit\VIDEO\sc.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write(
            """
            Dari cuplikan video di atas, kita tahu bahwa tautan terlemah dalam keamaan siber bukanlah perangkat atau operasi sistem yang digunakan, tetapi kita (manusia).

            Berdasarkan pemaparan Prasad Sawant (26/02/22) dalam kanal YouTube TEDx Talks bertajuk **_Social Engineering : The art of hacking human_** disampaikan bahwa sekitar 95% serangan siber terjadi karena kesalahan manusia,

            Pada dasarnya meretas _(hacking)_ itu sebuah proses sulit yang membutuhkan keahlian serta pengetahuan. Oleh karena itu, penjahat memilih cara yang lebih efektif yaitu dengan melakukan rekayasa sosial _(social engineering)_.

            Terdapat banyak jenis rekayasa sosial, yuk cari tahu di halaman berikutnya :smile:.
        """
        )
    with right_column:
        st.write("##")
        image = Image.open('C:\Streamlit\IMAGES\Rekayasa Sosial.png')
        st.image(image)
