import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(page_title="AquaMonitor", layout="wide")

st.markdown("""
<style>
.big-card {
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
}
.good {background-color:#2ecc71;color:white;}
.medium {background-color:#f1c40f;color:black;}
.bad {background-color:#e74c3c;color:white;}
</style>
""", unsafe_allow_html=True)

st.title("🌊 AquaMonitor")
st.subheader("Sistem Monitoring Kualitas Air Laut")
st.write("Analisis kualitas air laut berbasis parameter lingkungan.")

st.divider()

st.markdown("## 📥 Input Parameter")

col1, col2 = st.columns(2)

with col1:
    suhu = st.number_input("🌡️ Suhu (°C)", value=28.0)
    ph = st.number_input("🧪 pH", value=8.0)

with col2:
    salinitas = st.number_input("🧂 Salinitas (ppt)", value=33.0)
    do = st.number_input("💨 DO (mg/L)", value=6.5)

def klasifikasi(ph, do):
    if do < 5 or ph < 7:
        return "Buruk", "bad", "Kondisi air tidak mendukung ekosistem."
    elif 7 <= ph <= 8.5 and 5 <= do <= 7:
        return "Baik", "good", "Semua parameter dalam kondisi optimal."
    else:
        return "Sedang", "medium", "Beberapa parameter perlu perhatian."

if st.button("🔍 Analisis", use_container_width=True):

    status, css_class, ket = klasifikasi(ph, do)

    st.divider()
    st.markdown("## 📊 Hasil Analisis")

    st.markdown(
        f'<div class="big-card {css_class}">Status: {status}</div>',
        unsafe_allow_html=True
    )

    st.info(ket)

    st.markdown("### 🔎 Detail Parameter")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Suhu", f"{suhu} °C")
    c2.metric("pH", ph)
    c3.metric("Salinitas", f"{salinitas} ppt")
    c4.metric("DO", f"{do} mg/L")

    st.markdown("### 📈 Visualisasi")

    data = pd.DataFrame({
        "Parameter": ["Suhu", "pH", "Salinitas", "DO"],
        "Nilai": [suhu, ph, salinitas, do]
    })

    fig = px.bar(
        data,
        x="Parameter",
        y="Nilai",
        color="Parameter",
        title="Perbandingan Parameter Air Laut"
    )

    st.plotly_chart(fig, use_container_width=True)
