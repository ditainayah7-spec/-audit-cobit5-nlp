
import streamlit as st
import pandas as pd

# ==================================================
# 1. KONFIGURASI WEBSITE
# ==================================================
st.set_page_config(
    page_title="Audit Sistem Informasi - COBIT 5",
    layout="wide"
)

# ==================================================
# 2. DESAIN WEBSITE
# ==================================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eaf4ff, #f8fbff, #dcecff);
    color: #17365d;
}
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.hero {
    background: linear-gradient(120deg, #082b59, #1266b3, #42a5f5);
    padding: 38px;
    border-radius: 22px;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 10px 30px rgba(15,65,120,.18);
}
.hero h1, .hero h3 {
    color: white !important;
}
.hero p {
    color: #e5f2ff;
}
.section-title {
    background: linear-gradient(90deg, #d9ebff, #f1f7ff);
    border-left: 6px solid #1976d2;
    padding: 15px 20px;
    border-radius: 11px;
    margin: 25px 0 12px;
    color: #103b70;
    font-size: 20px;
    font-weight: 800;
}
.info-card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #d4e6fa;
    margin: 15px 0;
}
.question-card {
    background: white;
    border: 1px solid #d9e9f8;
    border-radius: 12px;
    padding: 15px;
    margin: 15px 0 8px;
    color: #17365d;
    font-weight: 600;
}
div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(90deg, #064a91, #1685e5) !important;
    color: white !important;
    border: none !important;
    border-radius: 13px !important;
    height: 58px !important;
    font-size: 17px !important;
    font-weight: 800 !important;
}
div[data-testid="stDownloadButton"] button {
    background: linear-gradient(90deg, #064a91, #1685e5);
    color: white;
    border-radius: 12px;
    border: none;
    font-weight: 700;
}
div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #d7e8f9;
    border-radius: 14px;
    padding: 16px;
}
.footer {
    text-align: center;
    color: #54718f;
    font-size: 13px;
    padding: 25px 0;
    border-top: 1px solid #d5e5f5;
    margin-top: 35px;
}
</style>
""", unsafe_allow_html=True)

# ==================================================
# 3. HEADER
# ==================================================
st.markdown("""
<div class="hero">
    <h1> COBIT 5</h1>
    <h3>IT Governance & Management Audit</h3>
    <p>FORM AUDIT SISTEM INFORMASI</p>
    <p>
        Audit tata kelola dan manajemen teknologi informasi
        pada PT Nusantara Logistik Prima.</P>
    <P>
        Dita Noor Inayah | 202453055 | A
    </p>
    <b>EDM • APO • BAI • DSS • MEA</b>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="info-card">
    <h3>Selamat Datang di Form Audit COBIT 5</h3>
    Form ini digunakan untuk mengevaluasi tata kelola dan
    manajemen sistem informasi NLP-Track pada PT Nusantara
    Logistik Prima (NLP).
    <br><br>
    <b>Petunjuk pengisian:</b>
    <ul>
        <li>Pilih Ya, Sebagian, atau Tidak.</li>
        <li>Isi bukti atau catatan audit berdasarkan hasil wawancara,
        observasi, atau dokumentasi.</li>
        <li>Tentukan level saat ini dan level target setiap proses.</li>
        <li>Lengkapi seluruh pertanyaan sebelum memproses hasil audit.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ==================================================
# 4. DATA PROSES DAN PERTANYAAN ASLI TUGAS 1
# ==================================================
domains = {
    "EDM": {
        "name": "Evaluate, Direct and Monitor",
        "focus": "Tata Kelola",
        "processes": {
            "EDM01": {
                "name": "Ensure Governance Framework Setting and Maintenance",
                "questions": [
                    ("1", "Apakah terdapat kerangka tata kelola TI (kebijakan, struktur, peran) yang ditetapkan dan disetujui direksi?", "EDM01.01–.02"),
                    ("2", "Apakah arahan dan komunikasi tata kelola TI disampaikan kepada seluruh pihak terkait, dan dipantau efektivitasnya?", "EDM01.03")
                ]
            },
            "EDM02": {
                "name": "Ensure Benefits Delivery",
                "questions": [
                    ("3", "Apakah investasi TI (termasuk NLP-Track) dievaluasi manfaatnya terhadap target bisnis, misalnya ketepatan waktu pengiriman?", "EDM02.01"),
                    ("4", "Apakah direksi memantau realisasi manfaat investasi TI secara berkala dan menindaklanjuti penyimpangan?", "EDM02.03")
                ]
            },
            "EDM03": {
                "name": "Ensure Risk Optimisation",
                "questions": [
                    ("5", "Apakah direksi telah menetapkan selera dan toleransi risiko terkait TI?", "EDM03.01–.02"),
                    ("6", "Apakah manajemen risiko TI dipantau dan hasilnya dilaporkan ke tingkat direksi?", "EDM03.03")
                ]
            }
        }
    },

    "APO": {
        "name": "Align, Plan and Organise",
        "focus": "Manajemen",
        "processes": {
            "APO01": {
                "name": "Manage the IT Management Framework",
                "questions": [
                    ("7", "Apakah struktur organisasi TI, peran, dan tanggung jawab (RACI) terdokumentasi dan dipahami staf?", "APO01.02–.03"),
                    ("8", "Apakah kebijakan dan prosedur TI (penggunaan sistem, akses, cadangan data) tersedia, terbaru, dan disosialisasikan?", "APO01.07")
                ]
            },
            "APO09": {
                "name": "Manage Service Agreements",
                "questions": [
                    ("9", "Apakah katalog layanan TI dan perjanjian tingkat layanan (SLA) dengan unit bisnis dan pelanggan didefinisikan?", "APO09.01–.03"),
                    ("10", "Apakah pencapaian SLA (misalnya ketersediaan sistem pelacakan) dipantau dan dilaporkan?", "APO09.04")
                ]
            },
            "APO12": {
                "name": "Manage Risk",
                "questions": [
                    ("11", "Apakah risiko TI (kegagalan sistem, kehilangan data, serangan siber) diidentifikasi dan dicatat dalam register risiko?", "APO12.01–.03"),
                    ("12", "Apakah terdapat rencana penanganan risiko dengan penanggung jawab dan batas waktu yang jelas?", "APO12.05–.06")
                ]
            },
            "APO13": {
                "name": "Manage Security",
                "questions": [
                    ("13", "Apakah terdapat sistem manajemen keamanan informasi (kebijakan keamanan, pembagian tanggung jawab)?", "APO13.01"),
                    ("14", "Apakah rencana penanganan risiko keamanan informasi dijalankan dan ditinjau secara berkala?", "APO13.02–.03")
                ]
            }
        }
    },

    "BAI": {
        "name": "Build, Acquire and Implement",
        "focus": "Manajemen",
        "processes": {
            "BAI01": {
                "name": "Manage Programmes and Projects",
                "questions": [
                    ("15", "Apakah proyek pengembangan atau perubahan NLP-Track memiliki rencana program (ruang lingkup, jadwal, biaya, sumber daya)?", "BAI01.04"),
                    ("16", "Apakah kemajuan proyek dipantau dan ada review pascaimplementasi untuk memastikan manfaat tercapai?", "BAI01.06–.09")
                ]
            },
            "BAI02": {
                "name": "Manage Requirements Definition",
                "questions": [
                    ("17", "Apakah kebutuhan pengguna (operasional, gudang, pelanggan) diidentifikasi dan didokumentasikan sebelum pengembangan?", "BAI02.01"),
                    ("18", "Apakah kebutuhan disetujui pemilik proses bisnis dan ditelusuri hingga hasil akhir sistem?", "BAI02.03–.04")
                ]
            },
            "BAI06": {
                "name": "Manage Changes",
                "questions": [
                    ("19", "Apakah setiap perubahan sistem (patch, fitur baru) diajukan, dinilai dampaknya, dan diotorisasi secara formal?", "BAI06.01–.02"),
                    ("20", "Apakah terdapat prosedur perubahan darurat dan pelacakan status perubahan hingga penutupan?", "BAI06.03")
                ]
            },
            "BAI07": {
                "name": "Manage Change Acceptance and Transitioning",
                "questions": [
                    ("21", "Apakah dilakukan pengujian penerimaan (UAT) sebelum sistem dirilis ke produksi?", "BAI07.03–.05"),
                    ("22", "Apakah pengguna dilatih dan tersedia dukungan setelah implementasi (hypercare)?", "BAI07.02, .08")
                ]
            }
        }
    },

    "DSS": {
        "name": "Deliver, Service and Support",
        "focus": "Manajemen",
        "processes": {
            "DSS01": {
                "name": "Manage Operations",
                "questions": [
                    ("23", "Apakah prosedur operasional (penjadwalan batch, pemantauan server, pencadangan) terdokumentasi dan dijalankan?", "DSS01.01–.03"),
                    ("24", "Apakah kondisi lingkungan dan fasilitas (server, jaringan, ruang data) dikelola dan dipantau?", "DSS01.04–.05")
                ]
            },
            "DSS02": {
                "name": "Manage Service Requests and Incidents",
                "questions": [
                    ("25", "Apakah terdapat help desk dengan pencatatan, klasifikasi, prioritas, dan eskalasi insiden serta permintaan layanan?", "DSS02.01–.04"),
                    ("26", "Apakah insiden diselesaikan sesuai target waktu dan penyelesaiannya diverifikasi dengan pengguna?", "DSS02.05–.07")
                ]
            },
            "DSS04": {
                "name": "Manage Continuity",
                "questions": [
                    ("27", "Apakah terdapat rencana kelangsungan bisnis dan pemulihan bencana (BCP/DRP) untuk NLP-Track?", "DSS04.02–.03"),
                    ("28", "Apakah rencana tersebut diuji secara berkala dan data cadangan disimpan di lokasi terpisah?", "DSS04.04, .07")
                ]
            },
            "DSS05": {
                "name": "Manage Security Services",
                "questions": [
                    ("29", "Apakah hak akses pengguna dikelola (pemberian, peninjauan, pencabutan) dan sesuai prinsip hak akses minimum?", "DSS05.04"),
                    ("30", "Apakah terdapat perlindungan terhadap malware, pengamanan jaringan (firewall), dan pemantauan kejadian keamanan?", "DSS05.01–.02, .07")
                ]
            }
        }
    },

    "MEA": {
        "name": "Monitor, Evaluate and Assess",
        "focus": "Manajemen",
        "processes": {
            "MEA01": {
                "name": "Monitor, Evaluate and Assess Performance and Conformance",
                "questions": [
                    ("31", "Apakah indikator kinerja TI (ketersediaan sistem, jumlah insiden, ketepatan waktu proyek) ditetapkan dan diukur?", "MEA01.01–.03"),
                    ("32", "Apakah hasil pengukuran dilaporkan kepada manajemen dan digunakan untuk perbaikan?", "MEA01.04–.05")
                ]
            },
            "MEA02": {
                "name": "Monitor, Evaluate and Assess the System of Internal Control",
                "questions": [
                    ("33", "Apakah pengendalian internal TI dipantau dan dievaluasi secara berkala (self-assessment atau audit internal)?", "MEA02.01–.02"),
                    ("34", "Apakah kelemahan pengendalian yang ditemukan ditindaklanjuti dengan rencana perbaikan?", "MEA02.04–.08")
                ]
            },
            "MEA03": {
                "name": "Monitor, Evaluate and Assess Compliance with External Requirements",
                "questions": [
                    ("35", "Apakah persyaratan hukum dan regulasi yang berlaku (perlindungan data pribadi, pengangkutan, transaksi elektronik) diidentifikasi?", "MEA03.01"),
                    ("36", "Apakah kepatuhan terhadap regulasi tersebut dievaluasi dan dikonfirmasi secara berkala?", "MEA03.03–.04")
                ]
            }
        }
    }
}

# ==================================================
# 5. SKALA JAWABAN DAN PEDOMAN PENILAIAN
# ==================================================
skor_jawaban = {
    "Ya": 1,
    "Sebagian": 0.5,
    "Tidak": 0
}

level_names = {
    0: "Incomplete",
    1: "Performed",
    2: "Managed",
    3: "Established",
    4: "Predictable",
    5: "Optimising"
}

def kategori_pencapaian(persen):
    if persen <= 15:
        return "N - Not achieved"
    elif persen <= 50:
        return "P - Partially achieved"
    elif persen <= 85:
        return "L - Largely achieved"
    return "F - Fully achieved"

# ==================================================
# 6. FORM AUDIT
# ==================================================
st.markdown(
    '<div class="section-title">A. IDENTITAS AUDIT</div>',
    unsafe_allow_html=True
)

with st.form("form_audit_cobit5"):

    col1, col2 = st.columns(2)

    with col1:
        perusahaan = st.text_input(
            "Nama Perusahaan",
            value="PT Nusantara Logistik Prima (NLP)"
        )
        objek = st.text_input(
            "Objek Audit",
            value="NLP-Track"
        )
        auditor = st.text_input("Nama Auditor")
        periode = st.text_input("Periode Audit")

    with col2:
        bidang = st.text_input(
            "Bidang Usaha",
            value="Jasa logistik dan pengiriman barang"
        )
        auditee = st.text_input(
            "Auditee / Penanggung Jawab",
            value="Kepala Divisi TI / CIO"
        )
        metode = st.multiselect(
            "Metode Pengumpulan Data",
            ["Wawancara", "Kuesioner",
             "Monitoring/Observasi", "Dokumentasi"]
        )

    st.markdown(
        '<div class="section-title">B. FORM PERTANYAAN AUDIT</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Jawablah 36 pertanyaan audit berdasarkan kondisi objek audit. "
        "Masukkan bukti atau catatan untuk mendukung setiap jawaban."
    )

    jawaban = {}
    bukti = {}
    level_as_is = {}
    level_to_be = {}

    for kode_domain, domain in domains.items():

        st.markdown(
            f'<div class="section-title">'
            f'{kode_domain} - {domain["name"]}</div>',
            unsafe_allow_html=True
        )

        st.caption(f"Fokus: {domain['focus']}")

        for kode_proses, proses in domain["processes"].items():

            st.markdown(f"### {kode_proses} - {proses['name']}")

            for nomor, pertanyaan, referensi in proses["questions"]:

                st.markdown(
                    f'<div class="question-card">'
                    f'<b>Pertanyaan {nomor}</b><br>{pertanyaan}'
                    f'<br><small>Referensi: {referensi}</small>'
                    f'</div>',
                    unsafe_allow_html=True
                )

                key = f"q_{nomor}"

                jawaban[key] = st.radio(
                    f"Jawaban pertanyaan {nomor}",
                    ["Ya", "Sebagian", "Tidak"],
                    index=None,
                    horizontal=True,
                    key=key
                )

                bukti[key] = st.text_input(
                    f"Bukti / Catatan pertanyaan {nomor}",
                    placeholder="Contoh: Dokumen kebijakan, hasil wawancara, atau hasil observasi",
                    key=f"bukti_{nomor}"
                )

            st.markdown("**Penilaian Capability Level Proses**")

            c1, c2 = st.columns(2)

            with c1:
                level_as_is[kode_proses] = st.selectbox(
                    f"Level saat ini (As-is) - {kode_proses}",
                    options=list(range(6)),
                    format_func=lambda x: f"Level {x} - {level_names[x]}",
                    key=f"as_is_{kode_proses}"
                )

            with c2:
                level_to_be[kode_proses] = st.selectbox(
                    f"Level target (To-be) - {kode_proses}",
                    options=list(range(6)),
                    index=2,
                    format_func=lambda x: f"Level {x} - {level_names[x]}",
                    key=f"to_be_{kode_proses}"
                )

            st.markdown("---")

    st.markdown(
        '<div class="section-title">C. TEMUAN DAN REKOMENDASI AUDIT</div>',
        unsafe_allow_html=True
    )

    temuan = {}
    rekomendasi = {}

    for kode_domain, domain in domains.items():
        for kode_proses, proses in domain["processes"].items():

            st.markdown(f"**{kode_proses} - {proses['name']}**")

            temuan[kode_proses] = st.text_area(
                f"Temuan / Kondisi saat ini {kode_proses}",
                key=f"temuan_{kode_proses}",
                placeholder="Tuliskan temuan berdasarkan hasil audit..."
            )

            rekomendasi[kode_proses] = st.text_area(
                f"Rekomendasi perbaikan {kode_proses}",
                key=f"rekom_{kode_proses}",
                placeholder="Tuliskan rekomendasi perbaikan..."
            )

    submit = st.form_submit_button(
        "📊 PROSES HASIL AUDIT",
        use_container_width=True
    )

# ==================================================
# 7. PROSES DAN ANALISIS HASIL AUDIT
# ==================================================
if submit:

    identitas_valid = bool(
        perusahaan.strip() and objek.strip() and auditor.strip()
    )

    jawaban_lengkap = all(
        nilai is not None for nilai in jawaban.values()
    )

    if not identitas_valid:
        st.error(
            "Nama perusahaan, objek audit, dan nama auditor wajib diisi."
        )

    elif not jawaban_lengkap:
        st.error(
            "Masih terdapat pertanyaan yang belum dijawab. "
            "Lengkapi seluruh 36 pertanyaan."
        )

    else:
        st.success("Hasil audit COBIT 5 berhasil diproses!")

        detail_hasil = []
        rekap_proses = []
        rekap_domain = []

        for kode_domain, domain in domains.items():

            skor_domain = 0
            jumlah_domain = 0

            for kode_proses, proses in domain["processes"].items():

                skor_proses = 0
                jumlah_proses = len(proses["questions"])

                for nomor, pertanyaan, referensi in proses["questions"]:

                    key = f"q_{nomor}"
                    pilihan = jawaban[key]
                    nilai = skor_jawaban[pilihan]

                    skor_proses += nilai
                    skor_domain += nilai
                    jumlah_domain += 1

                    detail_hasil.append({
                        "Perusahaan": perusahaan,
                        "Objek Audit": objek,
                        "Domain": kode_domain,
                        "Proses": kode_proses,
                        "Nomor": nomor,
                        "Pertanyaan": pertanyaan,
                        "Referensi COBIT": referensi,
                        "Jawaban": pilihan,
                        "Skor": nilai,
                        "Bukti / Catatan": bukti[key]
                    })

                persen = (skor_proses / jumlah_proses) * 100
                as_is = level_as_is[kode_proses]
                to_be = level_to_be[kode_proses]
                gap = to_be - as_is

                rekap_proses.append({
                    "Domain": kode_domain,
                    "Proses": kode_proses,
                    "Nama Proses": proses["name"],
                    "Skor": round(skor_proses, 2),
                    "Jumlah Pertanyaan": jumlah_proses,
                    "Pencapaian (%)": round(persen, 2),
                    "Kategori": kategori_pencapaian(persen),
                    "Level As-is": as_is,
                    "Level To-be": to_be,
                    "Gap": gap,
                    "Temuan": temuan[kode_proses],
                    "Rekomendasi": rekomendasi[kode_proses]
                })

            persen_domain = (skor_domain / jumlah_domain) * 100

            rekap_domain.append({
                "Domain": kode_domain,
                "Nama Domain": domain["name"],
                "Jumlah Pertanyaan": jumlah_domain,
                "Pencapaian (%)": round(persen_domain, 2),
                "Kategori": kategori_pencapaian(persen_domain)
            })

        df_detail = pd.DataFrame(detail_hasil)
        df_proses = pd.DataFrame(rekap_proses)
        df_domain = pd.DataFrame(rekap_domain)

        total_persen = df_detail["Skor"].sum() / len(df_detail) * 100

        # ==========================================
        # HASIL AUDIT
        # ==========================================
        st.markdown(
            '<div class="section-title">D. HASIL AUDIT</div>',
            unsafe_allow_html=True
        )

        st.markdown(f"""
        <div class="info-card">
            <h3>Informasi Audit</h3>
            <b>Perusahaan:</b> {perusahaan}<br>
            <b>Objek Audit:</b> {objek}<br>
            <b>Auditor:</b> {auditor}<br>
            <b>Auditee:</b> {auditee}<br>
            <b>Periode:</b> {periode}<br>
            <b>Metode:</b> {", ".join(metode) if metode else "-"}
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        c1.metric("Jumlah Pertanyaan", "36")
        c2.metric("Jumlah Proses", "18")
        c3.metric("Rata-rata Pencapaian", f"{total_persen:.2f}%")

        st.markdown("### Rekapitulasi Pencapaian Domain")
        st.dataframe(
            df_domain,
            use_container_width=True,
            hide_index=True
        )

        st.markdown("### Grafik Pencapaian Domain COBIT 5")

        grafik = df_domain.set_index("Domain")[["Pencapaian (%)"]]
        st.bar_chart(grafik, y="Pencapaian (%)")

        st.markdown("### Rekapitulasi 18 Proses COBIT 5")
        st.dataframe(
            df_proses,
            use_container_width=True,
            hide_index=True
        )

        # ==========================================
        # ANALISIS GAP
        # ==========================================
        st.markdown(
            '<div class="section-title">E. ANALISIS GAP CAPABILITY LEVEL</div>',
            unsafe_allow_html=True
        )

        st.caption(
            "Gap dihitung berdasarkan level target dikurangi level saat ini. "
            "Penetapan level tetap memerlukan pemeriksaan atribut proses COBIT 5."
        )

        df_gap = df_proses[
            ["Domain", "Proses", "Level As-is", "Level To-be", "Gap"]
        ]

        st.dataframe(
            df_gap,
            use_container_width=True,
            hide_index=True
        )

        # ==========================================
        # TEMUAN DAN REKOMENDASI
        # ==========================================
        st.markdown(
            '<div class="section-title">F. TEMUAN DAN REKOMENDASI</div>',
            unsafe_allow_html=True
        )

        for _, row in df_proses.iterrows():
            if row["Temuan"] or row["Rekomendasi"]:
                with st.expander(
                    f"{row['Proses']} - {row['Nama Proses']}"
                ):
                    st.write("**Temuan:**")
                    st.write(row["Temuan"] or "Belum diisi.")

                    st.write("**Rekomendasi:**")
                    st.write(row["Rekomendasi"] or "Belum diisi.")

                    st.write(f"**Prioritas gap:** {row['Gap']}")

        # ==========================================
        # DOWNLOAD HASIL
        # ==========================================
        st.markdown(
            '<div class="section-title">G. DOWNLOAD HASIL AUDIT</div>',
            unsafe_allow_html=True
        )

        st.download_button(
            "⬇️ DOWNLOAD DETAIL JAWABAN AUDIT",
            data=df_detail.to_csv(
                index=False
            ).encode("utf-8-sig"),
            file_name="detail_audit_cobit5.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.download_button(
            "⬇️ DOWNLOAD REKAP PROSES DAN GAP",
            data=df_proses.to_csv(
                index=False
            ).encode("utf-8-sig"),
            file_name="rekap_proses_gap_cobit5.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.download_button(
            "⬇️ DOWNLOAD REKAP DOMAIN",
            data=df_domain.to_csv(
                index=False
            ).encode("utf-8-sig"),
            file_name="rekap_domain_cobit5.csv",
            mime="text/csv",
            use_container_width=True
        )

        st.info(
            "Pedoman skor: Ya = 1, Sebagian = 0,5, Tidak = 0. "
            "Kategori N = 0–15%, P = >15–50%, L = >50–85%, "
            "F = >85–100%. Penilaian ini merupakan persentase "
            "pencapaian pertanyaan proses, bukan otomatis capability level."
        )

# ==================================================
# 8. FOOTER
# ==================================================
st.markdown("""
<div class="footer">
    <b>COBIT 5 | IT Governance & Management Audit</b><br>
    PT Nusantara Logistik Prima • NLP-Track<br>
    Audit Sistem Informasi
</div>
""", unsafe_allow_html=True)
