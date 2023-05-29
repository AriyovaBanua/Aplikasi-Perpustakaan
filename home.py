import streamlit as st
import pandas as pd
import json

# Data contoh
data = pd.DataFrame({
    'Judul',
    'Pengarang',
    'Tahun Terbit'
})

# Tampilan halaman utama
def main():
    st.title('Aplikasi Perpustakaan')
    menu = ['Daftar Buku', 'Tambah Buku']
    choice = st.sidebar.selectbox('Menu', menu)
    load_data()
    if choice == 'Daftar Buku':
        show_books()
    elif choice == 'Tambah Buku':
        add_book()

# Tampilan daftar buku
def show_books():
    st.header('Daftar Buku')
    st.table(data)

# Tampilan tambah buku
def add_book():
    st.header('Tambah Buku')
    judul = st.text_input('Judul')
    pengarang = st.text_input('Pengarang')
    tahun_terbit = st.number_input('Tahun Terbit', min_value=0, max_value=9999, step=1)

    if st.button('Tambah'):
        data.loc[len(data)] = [judul, pengarang, tahun_terbit]
        save_data()
        st.success('Buku berhasil ditambahkan!')

# Membaca data dari file JSON
def load_data():
    try:
        with open('data.json', 'r') as file:
            data_json = file.read()
            global data
            data = pd.read_json(data_json)
    except FileNotFoundError:
        data = pd.DataFrame(columns=['Judul', 'Pengarang', 'Tahun Terbit'])

# Simpan data ke file JSON
def save_data():
    data_json = data.to_json(orient='records')
    with open('data.json', 'w') as file:
        file.write(data_json)

# Menjalankan aplikasi
if __name__ == '__main__':
    main()
