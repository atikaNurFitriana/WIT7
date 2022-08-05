import streamlit as st
from PIL import Image

st.set_page_config(page_title="Phising", layout="wide")
# TOP HEADER IMAGE
image1 = Image.open(
    "C:\Streamlit\IMAGES\H4.png")
st.image(image1)


# SIDEBAR
st.sidebar.markdown(" # 🎣 Phishing")
st.sidebar.markdown(
    "Tentang teknik kejahatan *Social Engineering*, yaitu *Phishing* yang melingkupi penjelasan, cara kerja, dan bagaimana cara mencegahnya")

# Judul
# with st.container():
#    st.title("PHISING")


# Penjelasan pretexting

with st.container():
    st.write("---")
    st.subheader("Apa itu Phising?")
    left_column, right_clolumn = st.columns(2)
    with left_column:
        st.write(
            """
         Phishing merupakan salah satu rekayasa sosial di mana korban dihubungi melalui email, telepon, atau pesan teks oleh seseorang yang menyamar sebagai lembaga yang sah untuk memikat individu agar memberikan data sensitif seperti informasi identitas pribadi, detail kartu kredit dan perbankan, serta kata sandi.

         Informasi tersebut kemudian digunakan untuk mengakses akun penting dan dapat mengakibatkan pencurian identitas dan kerugian finansial.

         """
        )
    with right_clolumn:
        st.write(
            """
            Phising diketaui sebagai taktik rekayasa sosial yang terbaik karena memungkinkan peretas menargetkan ratusan atau bahkan ribuan korban sekaligus. 

         Kita semua berisiko menjadi korban serangan phishing karena ketergantungan kita yang meningkat pada komunikasi email dan perangkat seluler.
         """
        )

with st.container():
    st.subheader("Bagaimana Cara Kerja Phising?")
    image = Image.open('C:\Streamlit\IMAGES\P.png')
    st.image(image)

with st.container():
    st.write("##")
    st.subheader("Bagaimana Cara Mencegah Phising?")
    st.write(
        """
        - Filter spam dapat digunakan. Umumnya, filter menilai asal pesan, perangkat lunak yang digunakan untuk mengirim pesan, dan tampilan pesan untuk menentukan apakah itu spam. Terkadang, filter spam bahkan memblokir email dari sumber yang sah, sehingga tidak selalu 100% akurat.
        - Pengaturan browser harus diubah untuk mencegah pembukaan situs web palsu. Peramban menyimpan daftar situs web palsu dan ketika Anda mencoba mengakses situs web tersebut, alamatnya diblokir atau pesan peringatan ditampilkan. Pengaturan browser sebaiknya hanya memungkinkan situs web yang dapat dipercaya untuk dibuka.
        - Mengubah kata sandi secara teratur, dan tidak pernah menggunakan kata sandi yang sama untuk banyak akun. Sebaiknya situs web juga menggunakan sistem CAPTCHA untuk keamanan tambahan.
        - Bank dan organisasi keuangan menggunakan sistem pemantauan untuk mencegah phishing. Individu dapat melaporkan phishing ke pihak berwenang di mana tindakan hukum dapat diambil terhadap situs web penipuan ini
        - Jika verifikasi diperlukan, selalu hubungi perusahaan secara pribadi sebelum memasukkan detail apa pun secara online.
        - Jika ada tautan dalam email, arahkan kursor ke URL terlebih dahulu. Situs web aman dengan sertifikat Secure Socket Layer (SSL) yang valid dimulai dengan “https”. 

"""
    )
