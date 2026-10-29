from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'inikuncirahasiakita_asek123'

profil = {
    "nama": "Aldoo",
    "umur": 20,
    "kota": "Surabaya",
    "kampus": "Universitas Airlangga",
    "semester": 3
}

media_sosial = [
    {"nama": "Instagram", "link": "https://www.instagram.com/aldoo/", "icon": "instagram"},
    {"nama": "TikTok", "link": "https://www.tiktok.com/@aldoo/", "icon": "tiktok"},
    {"nama": "GitHub", "link": "https://github.com/aldoo/", "icon": "github"},
]

matkul = [
    {"kode": "01", "nama": "Pemrograman Web", "desc": "Belajar membangun aplikasi web dari frontend sampai backend menggunakan teknologi modern."},
    {"kode": "02", "nama": "Basis Data", "desc": "Memahami konsep perancangan, implementasi, dan optimasi database relasional."},
    {"kode": "03", "nama": "Jaringan Komputer", "desc": "Mempelajari arsitektur, protokol, dan keamanan jaringan untuk sistem terdistribusi."}
]

keahlian = [
    {"nama": "HTML & CSS", "level": 90},
    {"nama": "Flask", "level": 85},
    {"nama": "JavaScript", "level": 75},
    {"nama": "Python", "level": 70},
    {"nama": "SQL", "level": 80},
    {"nama": "Git", "level": 65}
]
proyek = [
    {"judul": "Web Portofolio", "desc": "Website portofolio pribadi dengan desain dark glass, animasi CSS, dan Flask.", "tech": ["HTML", "CSS", "Flask"], "icon": "monitor"},
    {"judul": "Sistem Data Mahasiswa", "desc": "Aplikasi CRUD data mahasiswa dengan Flask dan SQLite untuk tugas kuliah.", "tech": ["Flask", "SQLite", "HTML"], "icon": "database"},
    {"judul": "Game Tebak Angka", "desc": "Game sederhana tebak angka berbasis web dengan logika JavaScript interaktif.", "tech": ["HTML", "CSS", "JS"], "icon": "gamepad"},
    {"judul": "Web Scraper", "desc": "Tool scraping sederhana pakai Python untuk mengambil data dari halaman web.", "tech": ["Python", "BeautifulSoup"], "icon": "search"},
    {"judul": "Catatan Kuliah", "desc": "Blog catatan kuliah interaktif untuk dokumentasi materi pembelajaran.", "tech": ["Flask", "Markdown"], "icon": "file"},
    {"judul": "Dashboard Sederhana", "desc": "Dashboard data sederhana dengan grafik CSS murni, tanpa library JS.", "tech": ["HTML", "CSS"], "icon": "chart"}
]
artikel = [
    {"tanggal": "5 Okt 2025", "judul": "CSS Grid vs Flexbox", "ringkas": "Kapan harus pake Grid, kapan harus pake Flexbox? Simpelnya: Grid buat 2 dimensi, Flexbox buat 1 dimensi.", "tag": "CSS"},
    {"tanggal": "2 Okt 2025", "judul": "Flask buat Pemula", "ringkas": "Flask itu micro-framework Python buat web. Ringan, fleksibel, dan cocok buat belajar routing, template, dan static files.", "tag": "Flask"},
    {"tanggal": "28 Sep 2025", "judul": "Kenapa Dark Mode?", "ringkas": "Dark mode bukan cuma soal estetika. Lebih hemat baterai di OLED, lebih nyaman di mata pas malam hari.", "tag": "UI/UX"},
    {"tanggal": "20 Sep 2025", "judul": "CSS Animation Tanpa JS", "ringkas": "Dengan @keyframes, transition, dan animation-delay, kita bisa bikin animasi kompleks tanpa satupun baris JavaScript.", "tag": "CSS"},
    {"tanggal": "15 Sep 2025", "judul": "Variable CSS (Custom Properties)", "ringkas": "CSS variables bikin styling jadi konsisten. Ubah satu nilai di :root, efek ke seluruh halaman.", "tag": "CSS"},
    {"tanggal": "10 Sep 2025", "judul": "Struktur Folder Flask", "ringkas": "Templates/, static/, app.py — itu aja udah cukup buat project kecil. Flask otomatis nyari file di folder itu.", "tag": "Flask"}
]

@app.route('/')
def index():
    return render_template('index.html', aktif="index", profil=profil, matkul=matkul)

@app.route('/about')
def about():
    return render_template('about.html', aktif="about", profil=profil)

@app.route('/contact')
def contact():
    return render_template('contact.html', aktif="contact", media_sosial=media_sosial, profil=profil)

@app.route('/skill')
def skill():
    return render_template('skill.html', aktif="skill", keahlian=keahlian, profil=profil)

@app.route('/project')
def project():
    return render_template('project.html', aktif="project", proyek=proyek, profil=profil)

@app.route('/blog')
def blog():
    return render_template('blog.html', aktif="blog", artikel=artikel, profil=profil)

if __name__ == '__main__':
    app.run(debug=True)