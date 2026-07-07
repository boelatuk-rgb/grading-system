import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sistem Grading SD", layout="centered")

Inisialisasi session state
if 'data_siswa' not in st.session_state: 
    st.session_state.data_siswa = []

st.title("Sistem Grading Otomatis Sekolah Dasar")

--- BAGIAN INPUT (Dipindah ke atas agar state terupdate sebelum render tabel) ---
st.subheader("Input Data Siswa")
with st.expander("Klik untuk Input Data Baru", expanded=True):
    nama = st.text_input("Nama Siswa")
    col1, col2, col3 = st.columns(3)
    with col1: sumatif_raw = st.text_input("Nilai Sumatif (Bobot 5)", help="0-100")
    with col2: formatif_raw = st.text_input("Nilai Formatif (Bobot 3)", help="0-100")
    with col3: tambahan_raw = st.text_input("Nilai Tambahan (Bobot 2)", help="0-100", value="0")

if st.button("Hitung dan Simpan"):
    if nama:
        existing_names = [s['Nama'] for s in st.session_state.data_siswa]
        if nama in existing_names:
            st.warning(f"Peringatan: Nama {nama} sudah ada di dalam daftar!")
        else:
            try:
                s = float(sumatif_raw if sumatif_raw else 0)
                f = float(formatif_raw if formatif_raw else 0)
                t = float(tambahan_raw if tambahan_raw else 0)
                if not (0<=s<=100 and 0<=f<=100 and 0<=t<=100):
                    st.error("Rentang 0-100!"); st.stop()
                bw = 5 + 3 + (2 if t > 0 else 0)
                na = (s*5 + f*3 + t*2) / bw
                g = "A" if na>=85 else "B" if na>=75 else "C" if na>=60 else "D"
                st.session_state.data_siswa.append({"Nama": nama, "Nilai Akhir": na, "Grade": g})
                st.success(f"Data {nama} disimpan!")
                st.rerun()
            except:
