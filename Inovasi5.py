import streamlit as st
import pandas as pd
import plotly.express as px
import graphviz

st.set_page_config(page_title="INDUSTRI 5.0")

def main():
    st.title("📝 Aplikasi Audit Kesiapan Kampus untuk Industri 5.0 🛡️")
    st.write("Jawablah pertanyaan-pertanyaan di bawah ini dengan benar.")
    st.info("Dikembangkan oleh Kelompok Riset Keamanan Siber, Badan Riset dan Inovasi Nasional")

    st.sidebar.header("Menu")
    selected_page = st.sidebar.radio("Pilih Bagian", [
        "Informasi Umum",
        "PILAR ORGANISASI & MANAJEMEN",
        "Pilar Infrastruktur",
        "Pilar Suprastruktur",
        "Pilar Proses R & D",
        "Pilar Layanan dan Produk",
        "Kesimpulan"
    ])

    if selected_page == "Informasi Umum":
        informasi_umum()
    elif selected_page == "PILAR ORGANISASI & MANAJEMEN":
        Pilar_organisasi()
    elif selected_page == "Pilar Infrastruktur":
        Pilar_infrastruktur()
    elif selected_page == "Pilar Suprastruktur":
        Pilar_suprastruktur()
    elif selected_page == "Pilar Proses R & D":
        Pilar_Proses()
    elif selected_page == "Pilar Layanan dan Produk":
        Layanan()
    elif selected_page == "Kesimpulan":
        kesimpulan()

def informasi_umum():
    st.header("Informasi Umum Organisasi")
    nama_organisasi = st.text_input("Nama Organisasi:")
    alamat_organisasi = st.text_input('Alamat Organisasi')
    jumlah_karyawan = st.number_input("Jumlah Karyawan:", min_value=1, step=1)
    industri = st.selectbox("Industri:", ["Teknologi Informasi", "Keuangan", "Kesehatan", "Manufaktur", "Lainnya"])
    st.session_state['nama_organisasi'] = nama_organisasi
    st.session_state['alamat_organisasi'] = alamat_organisasi
    st.session_state['jumlah_karyawan'] = jumlah_karyawan
    st.session_state['industri'] = industri

def get_score_value(answer):
    """Konversi jawaban ke nilai skor"""
    if answer == 'Belum':
        return 0
    elif answer == 'Sedang':
        return 50
    elif answer == 'Sudah':
        return 100
    return 0

def Pilar_organisasi():
    st.header("PILAR ORGANISASI & MANAJEMEN")
    pertanyaan = [
        "1.1 Kolaborasi antar jurusan?",
        "1.2 Kolaborasi antar lembaga (dalam negeri)",
        "1.3 Strategi & Tata Kelola",
        "1.4 Pembelajaran dan pengembangan SDM (mahasiswa, dosen dan karyawan)",
        "1.5 Kompetensi kepemimpinan / leadership",
        "1.6 Budaya inovasi"
    ]
    total_score = 0
    max_score = len(pertanyaan) * 100
    
    for i, question in enumerate(pertanyaan):
        answer = st.radio(
            question,
            ('Belum', 'Sedang', 'Sudah'),
            horizontal=True,
            index=None,
            key=f"org_{i}"
        )
        score = get_score_value(answer)
        total_score += score
    
    st.session_state['domain1_score'] = total_score
    st.session_state['domain1_max'] = max_score
    st.session_state['pertanyaan1'] = len(pertanyaan)

def Pilar_infrastruktur():
    st.header("Pilar Infrastruktur")
    pertanyaan = [
        "2.1 Web (konektivitas)",
        "2.2 Laboratorium",
        "2.3 Inkubator/working space",
        "2.4 Fasilitas infrastruktur digital"
    ]
    total_score = 0
    max_score = len(pertanyaan) * 100
    
    for i, question in enumerate(pertanyaan):
        answer = st.radio(
            question,
            ('Belum', 'Sedang', 'Sudah'),
            horizontal=True,
            index=None,
            key=f"infra_{i}"
        )
        score = get_score_value(answer)
        total_score += score
    
    st.session_state['domain2_score'] = total_score
    st.session_state['domain2_max'] = max_score
    st.session_state['pertanyaan2'] = len(pertanyaan)

def Pilar_suprastruktur():
    st.header("Pilar Suprastruktur")
    pertanyaan = [
        "3.1 Regulasi",
        "3.2 Kurikulum",
        "3.3 Haki/Paten",
        "3.4 Publikasi"
    ]
    total_score = 0
    max_score = len(pertanyaan) * 100
    
    for i, question in enumerate(pertanyaan):
        answer = st.radio(
            question,
            ('Belum', 'Sedang', 'Sudah'),
            horizontal=True,
            index=None,
            key=f"supra_{i}"
        )
        score = get_score_value(answer)
        total_score += score
    
    st.session_state['domain3_score'] = total_score
    st.session_state['domain3_max'] = max_score
    st.session_state['pertanyaan3'] = len(pertanyaan)

def Pilar_Proses():
    st.header("Pilar Proses R & D")
    pertanyaan = [
        "4.1 Tingkat pengembangan R&D (market driven)",
        "4.2 Tingkat pemanfaatan teknologi dari luar (external technology base)",
        "4.3 Tingkat penggunaan teknologi dari dalam (technology insourcing)",
        "4.4 Tingkat penggunaan lisensi",
        "4.5 Tingkat technology spin-offs"
    ]
    total_score = 0
    max_score = len(pertanyaan) * 100
    
    for i, question in enumerate(pertanyaan):
        answer = st.radio(
            question,
            ('Belum', 'Sedang', 'Sudah'),
            horizontal=True,
            index=None,
            key=f"proses_{i}"
        )
        score = get_score_value(answer)
        total_score += score
    
    st.session_state['domain4_score'] = total_score
    st.session_state['domain4_max'] = max_score
    st.session_state['pertanyaan4'] = len(pertanyaan)

def Layanan():
    st.header("Pilar Layanan dan Produk")
    pertanyaan = [
        "5.1 Produk cerdas (Smart Products) yang dihasilkan",
        "5.2 Layanan berbasis data",
        "5.3 Kustomisasi produk"
    ]
    total_score = 0
    max_score = len(pertanyaan) * 100
    
    for i, question in enumerate(pertanyaan):
        answer = st.radio(
            question,
            ('Belum', 'Sedang', 'Sudah'),
            horizontal=True,
            index=None,
            key=f"layanan_{i}"
        )
        score = get_score_value(answer)
        total_score += score
    
    st.session_state['domain5_score'] = total_score
    st.session_state['domain5_max'] = max_score
    st.session_state['pertanyaan5'] = len(pertanyaan)

def buat_flowchart_penilaian():
    dot = graphviz.Digraph()
    dot.attr(rankdir='TB', size='8,5')
    
    # Node styling
    dot.attr('node', shape='box', style='rounded,filled', fillcolor='lightblue')
    
    # Mulai
    dot.node('A', 'Mulai Audit')
    
    # Pilar-pilar
    dot.node('B', 'Pilar 1: Organisasi & Manajemen')
    dot.node('C', 'Pilar 2: Infrastruktur')
    dot.node('D', 'Pilar 3: Suprastruktur')
    dot.node('E', 'Pilar 4: Proses R&D')
    dot.node('F', 'Pilar 5: Layanan & Produk')
    
    # Penilaian
    dot.node('G', 'Hitung Skor per Pilar\n(Belum=0%, Sedang=50%, Sudah=100%)')
    dot.node('H', 'Hitung Total Skor')
    
    # Hasil & Rekomendasi
    dot.node('I', 'Tampilkan Persentase')
    dot.node('J', 'Analisis Rekomendasi')
    dot.node('K', 'Tampilkan Radar Chart')
    dot.node('L', 'Selesai')
    
    # Edges
    dot.edge('A', 'B')
    dot.edge('B', 'C')
    dot.edge('C', 'D')
    dot.edge('D', 'E')
    dot.edge('E', 'F')
    dot.edge('F', 'G')
    dot.edge('G', 'H')
    dot.edge('H', 'I')
    dot.edge('I', 'J')
    dot.edge('J', 'K')
    dot.edge('K', 'L')
    
    return dot

def generate_recommendations(persentase_total, pilar_data):
    """Generate rekomendasi berdasarkan hasil penilaian"""
    recommendations = []
    
    # Rekomendasi keseluruhan
    if persentase_total < 70:
        recommendations.append({
            'type': 'peringatan',
            'title': 'TINGKAT KESELURUHAN RENDAH',
            'message': f'Tingkat kesiapan organisasi ({persentase_total:.2f}%) masih di bawah ambang batas 70%. Perlu peningkatan menyeluruh untuk mencapai standar Industri 5.0.',
            'priority': 'tinggi'
        })
    elif persentase_total < 85:
        recommendations.append({
            'type': 'peringatan',
            'title': 'TINGKAT KESELURUHAN SEDANG',
            'message': f'Tingkat kesiapan organisasi ({persentase_total:.2f}%) cukup baik namun masih ada ruang untuk peningkatan menuju excellence.',
            'priority': 'sedang'
        })
    else:
        recommendations.append({
            'type': 'sukses',
            'title': 'TINGKAT KESELURUHAN BAIK',
            'message': f'Selamat! Tingkat kesiapan organisasi ({persentase_total:.2f}%) sudah sangat baik. Pertahankan dan terus tingkatkan kualitasnya.',
            'priority': 'rendah'
        })
    
    # Rekomendasi per pilar
    for nama_pilar, score, max_score, jumlah_pertanyaan in pilar_data:
        if max_score > 0:
            persentase_pilar = (score / max_score) * 100
            
            if persentase_pilar < 70:
                recommendations.append({
                    'type': 'pilar-rendah',
                    'title': f'PERLU PENINGKATAN: {nama_pilar}',
                    'message': f'Pilar {nama_pilar} memiliki tingkat kesiapan {persentase_pilar:.2f}% (skor {score}/{max_score}). Fokus pada peningkatan area ini untuk hasil yang lebih baik.',
                    'priority': 'tinggi'
                })
            elif persentase_pilar < 85:
                recommendations.append({
                    'type': 'pilar-sedang',
                    'title': f'DAPAT DITINGKATKAN: {nama_pilar}',
                    'message': f'Pilar {nama_pilar} memiliki tingkat kesiapan {persentase_pilar:.2f}% (skor {score}/{max_score}). Masih ada potensi untuk peningkatan.',
                    'priority': 'sedang'
                })
    
    return recommendations

def display_recommendations(recommendations):
    """Tampilkan rekomendasi dengan styling yang sesuai"""
    st.subheader("📊 Rekomendasi Peningkatan")
    
    # Kelompokkan rekomendasi berdasarkan prioritas
    high_priority = [r for r in recommendations if r['priority'] == 'tinggi']
    medium_priority = [r for r in recommendations if r['priority'] == 'sedang']
    low_priority = [r for r in recommendations if r['priority'] == 'rendah']
    
    # Tampilkan rekomendasi prioritas tinggi
    if high_priority:
        st.markdown("### ⚠️ Prioritas Tinggi - Segera Ditindaklanjuti")
        for rec in high_priority:
            if rec['type'] == 'peringatan':
                st.error(f"**{rec['title']}**\n\n{rec['message']}")
            else:
                st.warning(f"**{rec['title']}**\n\n{rec['message']}")
    
    # Tampilkan rekomendasi prioritas sedang
    if medium_priority:
        st.markdown("### 🔧 Prioritas Sedang - Disarankan untuk Ditingkatkan")
        for rec in medium_priority:
            st.info(f"**{rec['title']}**\n\n{rec['message']}")
    
    # Tampilkan rekomendasi prioritas rendah
    if low_priority:
        st.markdown("### ✅ Prioritas Rendah - Pertahankan Kinerja")
        for rec in low_priority:
            st.success(f"**{rec['title']}**\n\n{rec['message']}")

def kesimpulan():
    st.header("Kesimpulan")

    # Inisialisasi default jika belum ada
    score_domains = ['domain1_score', 'domain2_score', 'domain3_score', 'domain4_score', 'domain5_score']
    max_domains = ['domain1_max', 'domain2_max', 'domain3_max', 'domain4_max', 'domain5_max']
    pertanyaans = ['pertanyaan1', 'pertanyaan2', 'pertanyaan3', 'pertanyaan4', 'pertanyaan5']

    for d in score_domains + max_domains:
        if d not in st.session_state:
            st.session_state[d] = 0
    for p in pertanyaans:
        if p not in st.session_state:
            st.session_state[p] = 0

    total_score = sum(st.session_state[d] for d in score_domains)
    total_max_score = sum(st.session_state[d] for d in max_domains)

    if total_max_score == 0:
        st.warning("Belum ada data yang diisi.")
        return

    persentase_total = (total_score / total_max_score) * 100

    # Data pilar untuk rekomendasi
    pilar_data = [
        ("PILAR ORGANISASI & MANAJEMEN", st.session_state.domain1_score, st.session_state.domain1_max, st.session_state.pertanyaan1),
        ("Pilar Infrastruktur", st.session_state.domain2_score, st.session_state.domain2_max, st.session_state.pertanyaan2),
        ("Pilar Suprastruktur", st.session_state.domain3_score, st.session_state.domain3_max, st.session_state.pertanyaan3),
        ("Pilar Proses R & D", st.session_state.domain4_score, st.session_state.domain4_max, st.session_state.pertanyaan4),
        ("Pilar Layanan dan Produk", st.session_state.domain5_score, st.session_state.domain5_max, st.session_state.pertanyaan5),
    ]

    # Generate rekomendasi
    recommendations = generate_recommendations(persentase_total, pilar_data)

    st.success(f"Organisasi telah mencapai tingkat kesiapan **{persentase_total:.2f}%** dari total maksimal {total_max_score} poin.")

    # Tab untuk berbagai tampilan
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Hasil Penilaian", "🔄 Flowchart Proses", "📋 Detail Perhitungan", "💡 Rekomendasi"])

    with tab1:
        # Data untuk radar chart
        data_list = [
            ['PILAR ORGANISASI & MANAJEMEN', (st.session_state.domain1_score / st.session_state.domain1_max * 100) if st.session_state.domain1_max > 0 else 0],
            ['Pilar Infrastruktur', (st.session_state.domain2_score / st.session_state.domain2_max * 100) if st.session_state.domain2_max > 0 else 0],
            ['Pilar Suprastruktur', (st.session_state.domain3_score / st.session_state.domain3_max * 100) if st.session_state.domain3_max > 0 else 0],
            ['Pilar Proses R & D', (st.session_state.domain4_score / st.session_state.domain4_max * 100) if st.session_state.domain4_max > 0 else 0],
            ['Pilar Layanan dan Produk', (st.session_state.domain5_score / st.session_state.domain5_max * 100) if st.session_state.domain5_max > 0 else 0],
        ]
        kolom = ['Persyaratan', 'Persentase (%)']
        df = pd.DataFrame(data_list, columns=kolom)

        fig = px.line_polar(
            df,
            r="Persentase (%)",
            theta="Persyaratan",
            line_close=True,
            range_r=[0, 100]
        )
        fig.update_traces(fill='toself')

        tampilkan_tabel = st.checkbox("Tampilkan Detail Penilaian", value=False)
        if tampilkan_tabel:
            st.info("Klik kotak di atas untuk menyembunyikan detail penilaian")
            st.plotly_chart(fig, use_container_width=True)
            st.table(df)
        else:
            st.info("Klik kotak di atas untuk menampilkan detail penilaian")

    with tab2:
        st.subheader("Flowchart Proses Penilaian")
        st.markdown("""
        Diagram alir berikut menunjukkan tahapan proses penilaian kesiapan organisasi untuk Industri 5.0:
        """)
        
        # Buat dan tampilkan flowchart
        flowchart = buat_flowchart_penilaian()
        st.graphviz_chart(flowchart)
        
        st.markdown("""
        ### Penjelasan Tahapan:
        1. **Mulai Audit** - Memulai proses audit kesiapan
        2. **Evaluasi Pilar** - Menilai setiap pilar secara berurutan
        3. **Hitung Skor** - Menghitung skor dengan sistem:
           - **Belum** = 0%
           - **Sedang** = 50%
           - **Sudah** = 100%
        4. **Total Skor** - Menjumlahkan semua skor tercapai
        5. **Persentase** - Menghitung persentase kesiapan
        6. **Analisis Rekomendasi** - Memberikan saran peningkatan
        7. **Visualisasi** - Menampilkan hasil dalam bentuk chart
        """)

    with tab3:
        st.subheader("Detail Perhitungan Nilai")
        
        # Tampilkan detail per pilar
        for nama_pilar, score, max_score, jumlah_pertanyaan in pilar_data:
            if max_score > 0:
                persentase_pilar = (score / max_score) * 100
                st.markdown(f"""
                **{nama_pilar}:**
                - Jumlah Pertanyaan: {jumlah_pertanyaan}
                - Skor Tercapai: {score} dari {max_score}
                - Persentase: **{persentase_pilar:.2f}%**
                """)
            else:
                st.markdown(f"""
                **{nama_pilar}:**
                - Jumlah Pertanyaan: {jumlah_pertanyaan}
                - Skor Tercapai: 0 dari 0
                - Persentase: **0.00%**
                """)
        
        st.divider()
        st.markdown(f"""
        **TOTAL KESELURUHAN:**
        - Skor Tercapai: {total_score} dari {total_max_score}
        - Persentase Kesiapan: **{persentase_total:.2f}%**
        """)

    with tab4:
        display_recommendations(recommendations)
        
        # Tampilkan rekomendasi spesifik berdasarkan ambang batas
        if persentase_total < 70:
            st.divider()
            st.subheader("🎯 Rencana Aksi Prioritas")
            
            # Rekomendasi berdasarkan pilar dengan nilai terendah
            pilar_scores = []
            for nama_pilar, score, max_score, jumlah_pertanyaan in pilar_data:
                if max_score > 0:
                    persentase_pilar = (score / max_score) * 100
                    pilar_scores.append((nama_pilar, persentase_pilar, score, max_score))
            
            # Urutkan berdasarkan nilai terendah
            pilar_scores.sort(key=lambda x: x[1])
            
            st.markdown("### 🔝 Pilar yang Perlu Diprioritaskan:")
            for i, (nama_pilar, persentase_pilar, score, max_score) in enumerate(pilar_scores[:3]):
                if persentase_pilar < 70:
                    st.markdown(f"""
                    {i+1}. **{nama_pilar}** - {persentase_pilar:.2f}% 
                       - Target peningkatan: Minimal 70%
                       - Gap yang perlu ditutup: {((70 - persentase_pilar) / 100 * max_score):.0f} poin
                    """)
            
            st.markdown("### 📋 Langkah-langkah Umum yang Disarankan:")
            st.markdown("""
            1. **Formulasi Strategi** - Buat roadmap peningkatan berdasarkan prioritas
            2. **Alokasi Sumber Daya** - Fokus pada area dengan gap terbesar
            3. **Pelatihan dan Pengembangan** - Tingkatkan kompetensi SDM
            4. **Infrastruktur Digital** - Investasi pada teknologi dan fasilitas
            5. **Kolaborasi** - Tingkatkan kerjasama internal dan eksternal
            6. **Monitoring dan Evaluasi** - Lakukan review berkala setiap 3-6 bulan
            """)

if __name__ == "__main__":
    main()