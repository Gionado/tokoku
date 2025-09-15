Nama : Gionado Gunawan
NPM : 2406496196
Kelas : PBP E


https://gionado-gunawan-tokoku.pbp.cs.ui.ac.id/
https://github.com/Gionado/tokoku.git


TUGAS2
# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Membuat sebuah proyek Django baru.
Untuk membuat  sebuah pryek  Django baru, saya membuat folder baru terlebih dulu, nama folder saya adalah tokoku, kemudian saya membuat virtual environment dengan menjalankan perintah "python -m venv env" dan mengaktifkannya dengan menjalankan perintah "env\Scripts\activate" pada command prompt. Setelah itu, saya membuat file baru bernama requirements.txt untuk menambahkan beberapa dependencies di dalamnya, lalu saya melakukan instalasi terhadap depedencies tersebut dengan menjalankan perintah "pip install -r requirements.txt" setelah mengaktifkan virtual environment, setelah itu baru buat proyek baru Django dengan perintah "django-admin startproject <NamaProyek(proyek saya tokoku)> .". 

Pastikan juga sudah mengonfigurasi environment variables dan proyek dengan membuat file .env (untuk development lokal) dan .env.prod ((untuk production deployment)) dan isi dengan credential yang diberikan Fasilkom. Kemudian modifikasi settings.py untuk menggunakan environment variables. Lalu jalankan server dengan menjalaknkan perintah "python manage.py migrate" (untuk migrasi database) dan "python manage.py runserver" (untuk menjalankan server Django), buka http://localhost:8000 pada web untuk cek keberhasilan. Tutup dengan Ctrl+C


Membuat aplikasi dengan nama main pada proyek tersebut.
Untuk membuat aplikasi main pada proyek tersebut saya menjalankan perintah "python manage.py startapp main".


Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
pastikan virtual environment diaktifkan kemudian tambahkan 'main' pada daftar aplikasi yang ada di settings.py agar aplikasi main dapat dideteksi


Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib sebagai berikut....
Saya membuka models.py pada folder aplikasi main dan menambahkan beberapa perintah/kode untuk menyesuaikan checklist, seperti di bawah ini
class Product(models.Model): -> kelas produk
    pilihan_category = [     -> atribut produk
        ('jersey', 'Jersey'),
        ('sepatu', 'Sepatu'),
        ('celana', 'Celana'),
        ('bola', 'Bola'),
        ('lain lain', 'Lain Lain'),
    ]

    name = models.CharField                                                 -> Menyesuaikan checklist
    price = models.PositiveIntegerField(default=0)                          -> Menyesuaikan checklist
    description = models.TextField()                                        -> Menyesuaikan checklist
    thumbnail = models.URLField(blank=True, null=True)                      -> Menyesuaikan checklist
    category = models.CharField(choices=pilihan_category, default='update') -> Menyesuaikan checklist
    is_featured = models.BooleanField                                       -> Menyesuaikan checklist


Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Pastikan untuk membuat folder templates pada folder aplikasi main kemudian membuat file main.html (digunakan untuk render tampilan)
Saya membuka file views.py pada folder aplikasi main dan menambahkan beberapa perintah/kode seperti di bawah ini
from django.shortcuts import render -> untuk mengimpor fungsi render dari modul django.shortcuts

def show_main(request):             -> mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai
    context = {                     -> dictionary yang berisi data untuk dikirimkan ke tampilan
        'name': 'Gionado Gunawan',  -> nama
        'class': 'PBP E'            -> npm
    }

    return render(request, "main.html", context) -> untuk render tampilan main.html dengan menggunakan fungsi render

Lalu pada file html.py yang telah dibuat tambahkan kode/perintah ini,
<!-- <h1>tokoku</h1>

<h5>NPM: </h5>
<p>{{ npm }}</p>
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}</p>
sintaks {{...}} digunakan untuk menampilkan nilai dari variabel yang telah didefinisikan dalam context. -->


Saya membuat file urls.py pada folder aplikasi main yang telah terbuat sebelumnya, lalu mengisi file tersebut dengan beberapa hal untuk import path (django.urls) dan show_main (main.views), membuat app_name = 'main' untuk namespace unik URL, dan name='show_main' untuk melakukan reverse URL menggunakan nama. Kemudian pada file urls.py yang berada pada folder proyek, Impor fungsi include dari django.urls dan tambahkan rute URL untuk mengarahkan ke tampilan main di dalam list urlpatterns.


Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Saya membuat proyek pada PWS terlebih dulu, kemudian mengubah project environment variable dengan sesuai yang ada pada file .env.prod kemudian saya menambahkan URL deployment PWS pada bagian ALLOWED_HOSTS di settings.py untuk mengakses proyek melalui URL deplyment PWS. kemudian saya melakukan git add,commit, dan push untuk perubahan pada repo git. Kemudian jalankan beberapa perintah yang terdapat pada informasi Project Command dan masukan username dan password. Buka View Project pada web PWS untuk cek proyek sudah bisa diakses apa belum.


# Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Client Browser
      ↓          Request (HTTP)
   urls.py       Mencocokkan URL dengan view yang sesuai
      ↓     
   views.py      Logika aplikasi (olah data, panggil model, dll)
      ↓
   models.py     Akses / query ke database
      ↓
   Template      (HTML file) → Menyusun tampilan untuk user
      ↓
(Client Browser) HTML final dikirim balik oleh Django ke browser dan browser menampilkan halaman web ke user


Kaitan antar file:
urls.py, menentukan routing URL ke fungsi view.
views.py, mengatur logika, ambil data dari model, lalu kirim ke template.
models.py, representasi tabel database, dipakai untuk query/CRUD.
HTML (template), menampilkan data hasil view ke browser.


# Jelaskan peran settings.py dalam proyek Django!
File settings.py adalah pusat konfigurasi untuk seluruh proyek Django. Semua pengaturan penting terkait aplikasi berada di file ini. Beberapa perannya antara lain:
Menentukan database apa yang digunakan beserta nama database, user, password, dan host.
Installed Apps, Berisi daftar aplikasi Django yang aktif dalam proyek.
Middleware, Lapisan yang memproses request dan response.
Template dan Static Files, Menentukan lokasi template HTML dan file statis.
Keamanan, Menyimpan SECRET_KEY, pengaturan DEBUG, dan ALLOWED_HOSTS untuk kontrol akses.


# Bagaimana cara kerja migrasi database di Django?
Langkah 1: Definisikan Model
Di models.py, developer menuliskan kelas model yang merepresentasikan tabel database.

Langkah 2: Buat File Migrasi
Perintah" python manage.py makemigrations" akan membuat file migrasi (berisi instruksi perubahan database).

Langkah 3: Terapkan Migrasi
Perintah "python manage.py migrate" menjalankan instruksi SQL dari file migrasi tersebut ke database. Hasilnya, struktur tabel benar-benar terbentuk atau diperbarui.

Langkah 4: Konsistensi
Django menyimpan catatan migrasi di tabel khusus (django_migrations) agar tahu migrasi mana yang sudah atau belum dijalankan.


# Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sudah menyediakan fitur penting secara bawaan, seperti ORM, autentikasi, admin panel, form handling untuk memudahkan pemula.
Django memakai pola Model–Template–View yang mirip dengan MVC sehingga memiliki alur dan struktur yang jelas.
Django digunakan oleh banyak perusahaan besar.
Django mendorong developer menulis kode yang rapi, aman, dan terstruktu.


# Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Tutorial 1 sudah memiliki penjelasan dan arahan yang baik sehingga membuat saya menjadi lebih mengerti





TUGAS2
