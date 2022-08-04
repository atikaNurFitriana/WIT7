import streamlit as st
from PIL import Image

st.set_page_config(page_title="Pretexting", layout="wide")

# Judul
with st.container():
    st.title("PRETEXTING")


# Penjelasan pretexting

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.subheader("Apa itu Pretexting?")
        st.write(
            """
            _Pretexting_ adalah jenis serangan rekayasa sosial yang mana penjahat telah menyusun skenario, atau dalih yang memancing korban untuk memberikan informasi pribadi.

            Informasi tersebut dapat berupa kata sandi, informasi kartu kredit, informasi identitas pribadi, data rahasia, atau apa pun yang dapat digunakan untuk tindakan penipuan seperti pencurian identitas.

            Penjahat dapat menyamar sebagai otoritas personel hukum, kolega, lembaga perbankan, petugas pajak, penyelidik asuransi, dll. Mereka akan berusaha mendapatkan kepercayaan korban hingga memperoleh informasi mereka.

            Misalnya, seorang penjahat dapat menyamar sebagai orang yang bekerja di perusahaan kartu kredit dan menelepon korban untuk meminta konfirmasi detail akun mereka. Jika korban memercayai mereka, mereka mungkin akan menyerahkan informasi pembayaran mereka, tanpa diketahui bahwa itu memang mengarah ke tangan penjahat dunia maya.
            """
        )
    with right_column:
        st.write("##")
        image = Image.open('C:\Streamlit\IMAGES\PT.png')
        st.image(image)

with st.container():
    st.write("##")
    st.header("Bagaimana Cara Mencegah Pretexting?")
    st.write(
        """
        - Hindari membagikan informasi pribadi ke sosial media
        - Jika terlanjur membagikan informasi pribasi, minta agar informasi tersebut ditarik
        - Gunakan saluran resmi dan terpercaya untuk memverifikasi alamat email dan nomor telepon Anda, jika menerima pesan mencurigakan
        - Jangan berikan informasi pribadi dan kata sandi Anda pada pihak manapun
        - Batalkan bantuan dari perusahaan jika sebelumnya Anda tidak meminta bantuan
"""
    )
