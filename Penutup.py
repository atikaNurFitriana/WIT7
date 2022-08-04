from codecs import namereplace_errors
import streamlit as st
from PIL import Image
import base64
from streamlit_option_menu import option_menu
from st_functions import st_button, load_css

# SIDEBAR
st.sidebar.markdown("  # 📥 Penutup")


# TOP HEADER IMAGE
image2 = Image.open("C:\Streamlit\IMAGES\Penutup header.png")
st.image(image2)
"\n"
"\n"


# TOP INFO
original_title = '<p style="font-family:Isocpeur; color:IndianRed; font-size: 30px;"><b>TEKNIK SOCIAL ENGGINEERING</b></p>'
st.markdown(original_title, unsafe_allow_html=True)
"Perlu untuk diingat, agar terhindar dari bahaya kejahatan *cyber*"

# ANIMASI PENGINGAT UNTUK WASPADA!!!
file_ = open("C:\Streamlit\ANIMASI\PENUTUP.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True)

"Teknik ***Social Engineering*** memanfaatkan sisi kelemahan, manusia."
"Oleh karena itu, **Kesadaran** serta pelatihan individu dan karyawan tentang ***Social engineering*** dan berbagai **teknik** yang dapat digunakan oleh penyerang adalah **pertahanan terbaik** untuk mencegah terjadinya tindak kejahatan"
"\n"
"\n"

"----------------------------------------------------------------------------"
# PAKAI MENU SIDEBAR UNTUK QUIZZ DAN KOLOM PERTANYAAN
with st.sidebar:
    selected = option_menu(menu_title=None,
                           options=["Quizz", "Kolom Komentar"],
                           icons=["patch-question", "chat-dots"],
                           default_index=0, styles={
                               "container": {"padding": "0!important", "background-color": ""},
                               "icon": {"color": "MidnightBlue", "font-size": "15px"},
                               "nav-link": {
                                   "font-size": "15px",
                                   "text-align": "left",
                                   "margin": "0px",
                                   "--hover-color": "",
                               },
                               "nav-link-selected": {"background-color": "MediumAquamarine"},
                           },)


if selected == "Quizz":
    "\n"
    st.subheader("QUIZZZ")

# QUIZZ MUNCUL KETIKA BUTTON DIPRESS
    with st.container():
        "Quiz ini bermaksud untuk memperdalam pembaca, agar lebih memahami contoh kasus *Social Engineering*, dan terhindar dari kejahatan *Social Engineering* "

        "**1. Apa yang dilakukan ketika terdapat email masuk seperti di bawah ini?**"
        "'It has come to our attention that your account may have been accessed by thrid party. please login and change your password, here', https://myaccount.google.com/signoption/password."
        "from <support@google.com>"

        jawaban = st.radio("Pilihan Jawaban :", ('Phishing', 'Bukan Phishing'))
        if jawaban == 'Phishing':
            st.write('BENAR 👍🏼 ')
            "Karena untuk keperluan merubah password, harus dimulai dari kita dulu yang meminta, seperti 'forget password'. Kalau tidak ada permintaan dari kita, berarti itu *phishing*"
        else:
            st.write("SALAH")

        "**2. Apa yang dilakukan ketika terdapat email masuk seperti di bawah ini?**"
        "'Silahkan download laporan keuangan terbaru anda dengan mengklik *disini*'"
        "dari :accounts@bankingroup.thm"

        jawaban2 = st.radio("Pilihan Jawaban :",
                            ('Juga Phishing', 'Bukan Phishing'))
        if jawaban2 == 'Juga Phishing':
            st.write('BENAR 👍🏼 ')
            "Karena laporan keuangan biasanya perlu authentifikasi, dan juga terdapat kesalahan tulisan dinama pengiri yang seharusnya 'bankinggroup'"
        else:
            st.write("SALAH")
        "\n"
        "\n"

        "----------------------------------------------------------------------------"
        "\n"
        "\n"

        # LINK WEBSITE
        original_title = '<p style="font-family:Isocpeur; color:IndianRed; font-size: 20px;">Untuk dapat lebih memahami lebih jauh tentang <i>Cyber Security</i>, silahkan bisa mencoba pelatihan - permainan seru pada website dibawah ini.</p>'
        st.markdown(original_title, unsafe_allow_html=True)

        load_css()
        icon_size = 20
        st_button('newsletter', 'https://tryhackme.com/',
                  'Website pelatihan seru tentang cyber security', icon_size)

        "\n"
        "\n"

# KOLOM KOMENTAR & PERTANYAAN MUNCUL KETIKA BUTTON DIPRESS
if selected == "Kolom Komentar":
    st.subheader("KOLOM KOMENTAR DAN PERTANYAAN")

    with st.form("my_form"):
        st.write(
            "Silahkan mengisikan komentar dan pertanyaan dalam kolom dibawah ini")
        nama = st.text_input("Nama :")
        isi = st.text_input("Isi Komentar atau Pertanyaan :")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        "\n"
        "\n"
        if submitted:
            st.write("Nama : ", nama)
            st.write("Komentar atau Pertanyaan: ")
            st.write(isi)
