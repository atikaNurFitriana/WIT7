from PIL import Image
import streamlit as st
import pandas as pd  # pip install pandas
import plotly.express as px  # pip install plotly-express


st.set_page_config(
    page_title="Multipage App",
)

# TOP HEADER IMAGE
image1 = Image.open(
    "C:\Streamlit\IMAGES\H0.png")
st.image(image1)

# SIDEBAR
st.sidebar.success("Select a page above.")

st.sidebar.markdown("# 👨‍💻 Tentang ")
st.sidebar.markdown(
    "Web ini dibuat dalam rangka mengedukasi masyarakat umum tentang **Social Engineering**, agar bisa terhindar dari kejahatan di dunia maya")

st.sidebar.markdown("# Penyusun")
st.sidebar.markdown(
    "Trisna Nurhayati  &  Atika Nur Fitriana")

# PENJELASAN REKAYASA SOSIAL

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
            Dari cuplikan video di atas, kita tahu bahwa tautan terlemah dalam keamaan siber **bukanlah perangkat** atau **operasi sistem** yang digunakan, tetapi **kita (manusia)**.

            Berdasarkan pemaparan Prasad Sawant (26/02/22) dalam kanal YouTube **TEDx Talks** bertajuk **_Social Engineering : The art of hacking human_** disampaikan bahwa sekitar 95% serangan siber terjadi **karena kesalahan manusia**,

            Pada dasarnya meretas _(hacking)_ itu sebuah proses sulit yang membutuhkan keahlian serta pengetahuan. Oleh karena itu, penjahat memilih cara yang **lebih efektif** yaitu dengan melakukan **rekayasa sosial _(social engineering)_**.

            Terdapat banyak jenis rekayasa sosial, yuk cari tahu di halaman berikutnya :smile:.
        """
        )
    with right_column:
        st.write("##")
        image = Image.open('C:\Streamlit\IMAGES\Rekayasa Sosial.png')
        st.image(image)


with st.container():
    "\n"
    "\n"
    "\n"
    st.markdown("##### Grafik Jenis Kejahatan Siber di Indonesia, 2019-2020")
    st.caption("Sumber : lokadata.beritaagar.id")
    excel_file = 'DATA1.xlsx'
    sheet_name = 'DATA'

    df = pd.read_excel(excel_file,
                       sheet_name=sheet_name,
                       usecols='A:B',
                       header=0)

    # st.dataframe(df)
    # kalau ingin menampilkan table excel

    bar_chart = px.bar(df,
                       x='Jumlah Kasus',
                       y='Jenis Kejahatan',
                       text='Jumlah Kasus',
                       color_discrete_sequence=['#D2691E']*len(df),
                       template='plotly_white')
    st.plotly_chart(bar_chart)

    st.markdown("Grafik ini menunjukan bahwa Kejahatan Rekayasa Sosial (Penipuan Online, secara spesifik) adalah salah satu kejahatan yang paling banyak terjadi dibandingkan jenis tindak kejahatan siber lainnya yang dapat memberikan dapat kerugian materi.")
