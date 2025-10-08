Nama : Gionado Gunawan
NPM : 2406496196
Kelas : PBP E


https://gionado-gunawan-tokoku.pbp.cs.ui.ac.id/
https://github.com/Gionado/tokoku.git


# TUGAS2
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






# TUGAS3
# Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery adalah proses bagaimana data dikirimkan, ditransfer, atau didistribusikan dari satu sistem ke sistem lain, atau dari backend ke pengguna akhir dengan cara yang aman, baik, dan cepat. Tanpa mekanisme pengiriman data yang baik, platform hanya menyimpan informasi, tapi tidak bisa dipakai oleh pengguna atau layanan lain. Data delivery diperlukan supaya data yang dimiliki platform bisa sampai ke pihak yang membutuhkan (user, modul lain, atau sistem eksternal), dengan cara yang cepat, aman, konsisten, dan efisien.

Dalam konteks platform web dengabn Django, data delivery berarti proses mengirim data dari server ke client (browser) supaya user bisa melihat dan berinteraksi dengan informasi. Data delivery dibutuhkan agar platform web bukan hanya menyimpan data di database, tapi juga menyajikan data ke user. Kalau data hanya ada di server, user tidak akan tahu update terbaru, data delivery memastikan perubahan di database  sampai ke pengguna. Tanpa data delivery, aplikasi web hanya akan menampilkan halaman statis.


# Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, format data delivery yang lebih baik adalah JSON, karena JSON memiliki struktur dan sintaks yang lebih ringkas sehiongga lebih enak dilihat, sedangkan XML lebih verbose (panjang) karena setiap elemen harus buka-tutup tag. Selain itu, JSON lebih mudah dibaca manusia, lebih dekat dengan struktur data di bahasa pemrograman modern (Python dict, JavaScript object, dsb). JSON parsing juga lebih cepat (library sudah built-in di hampir semua bahasa). Alasan-alasan di ataslah yang membuat saya lebih memilih JSON dan juga yang membuat JSON lebih populer dibandingkan XML.


# Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
is_valid() adalah method utama pada Django Form/ModelForm yang dipakai untuk mengecek apakah data yang dikirim user valid sesuai aturan form yang didefinisikan. Sehingga method is_valid() sangat berguna dan dibutuhkan untuk menjaga keamanan data (data dari user tidak selalu semua bisa dipercaya), Mencegah error runtime(Kalau field butuh angka tapi user masukkan teks, tanpa validasi program bisa crash), dan Memudahkan developer agar tidak perlu tulis validasi manual untuk setiap field.


# Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token dibutuhkan untuk mencegah CSRF (Cross-Site Request Forgery), serangan di mana penyerang memaksa browser korban (yang sudah login) mengirim request berbahaya ke web memakai cookie otentikasi korban. Tanpa CSRF protection, attacker bisa membuat korban melakukan aksi yang tidak diinginkan (transfer uang, ganti email, hapus data, dll).


# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Untuk memenuhi dan mengimplementasikan checklist saya memulai dengan mengimplementasi skeleton sebagai kerangka views, saya membuat folder baru dengan nama templates pada direktori utama proyek dan membuat file baru di dalamnya dengan nama "base.html". "base.html" ini berfungsi untuk menjadi template dasar yang dapat digunakan sebagai kerangka umum untuk halaman web lainnya di dalam proyek. Kemudian saya menambahkan kode pada bagian TEMPLATES di file settings.py, 'DIRS': [BASE_DIR / 'templates'], hal ini berguna untuk mendeteksi file "base.html" sebagai file template yang dapat digunakan.

Langkah selanjutnya adalah membuat form input data, pertama, saya membuat file baru bernama "forms.py" pada folder main, file ini berguna untuk membuat struktur form yang dapat menerima data Produk baru. Saya juga menambahkan beberapa import dan fungsi pada file views.py, saya menambahkan Product.objects.all() untuk mengambil seluruh objek Product yang tersimpan pada database. Saya juga menambahkan fungsi create_product untuk membuat form yang dapat menambahkan data produk dan juga fungsi show_product menggunakan get_object_or_404(Product, pk=id) untuk mengambil objek Product berdasarkan primary key (id) dan mengembalikan halaman 404 jika id tidak ditemukan. Lalu saya mengimport fungsi-fungsi tersebut pada file urls.py pada varabel urlpatterns. 

Kemudian saya melakukan perubahan pada file main.html untuk menampilkan data, 
{% extends 'base.html' %}                        -> template ini mewarisi (inherit) template induk bernama base.html
{% block content %} ... {% endblock content %}   -> Ini adalah blok konten yang disediakan oleh base.html.
saya juga menambahkan beberapa hal seperti tombol "Add Product" tombol "Deskripsi" dan tampilan produk.
Kemudian saya membuat 2 file yaitu, create_product.html (untuk tampilan  dalam penambahan produk baru) dan product_detail.html (untuk menampilkan detail  produk) Kemudian saya menambahkan entri url proyek pws pada file settings dengan  CSRF_TRUSTED_ORIGINS = [ "https://gionado-gunawan-tokoku.pbp.cs.ui.ac.id" ]

Langkah selanjutnya adalah untuk mengembalikan data dalam XML dan JSON
Saya memulai dengan mengimport HttpResponse dan serializers pada dile views.py. Kemudian saya membuat 4 fungsi baru pad views.py untuk menyediakan data Produk dalam format XML  dan JSON.
fungsi pertama adalah def show_xml(request):                            -> untuk menampilkan data dalam format XML
    product_list = Product.objects.all()                                -> ambil semua record Product dari database dan menghasilkan QuerySet
    xml_data = serializers.serialize("xml", product_list)               -> konversi QuerySet menjadi string XML 
    return HttpResponse(xml_data, content_type="application/xml")       -> kembalikan response HTTP berisi XML

fungsi kedua adalah def show_json(request):                             -> untuk menampilkan data dalam format JSON
    product_list = Product.objects.all()                                -> ambil semua record Product dari database dan menghasilkan QuerySet
    json_data = serializers.serialize("json", product_list)             -> serialize QuerySet ke format JSON 
    return HttpResponse(json_data, content_type="application/json")     -> kembalikan response dengan Content-Type: application/json

fungsi ketiga adalah def def show_xml_by_id(request, product_id):       -> untuk menampilkan data produk spesifik dalam format XML
    try:    
        product_item = Product.objects.filter(pk=product_id)            -> filter Product berdasarkan primary key product_id
        xml_data = serializers.serialize("xml", product_item)           -> serialize hasil QuerySet (meskipun kosong) menjadi XML
        return HttpResponse(xml_data, content_type="application/xml")   -> kembalikan XML sebagai response
    except Product.DoesNotExist:                                        
        return HttpResponse(status=404)                                 -> catch exception DoesNotExist dan kembalikan 404

fungsi keempat adalah def def show_json_by_id(request, product_id):     -> untuk menampilkan data produk spesifik dalam format JSON
    try:
        product_item = Product.objects.get(pk=product_id)               -> filter Product berdasarkan primary key product_id
        json_data = serializers.serialize("json", [product_item])       -> bungkus objek tunggal di list; lalu diserialisasi ke JSON
        return HttpResponse(json_data, content_type="application/json") -> kembalikan JSON sebagai response.
    except Product.DoesNotExist:                                        
        return HttpResponse(status=404)                                 -> catch exception DoesNotExist dan kembalikan 404

Langkah terakhir adalah saya melakukan push pada git dan pws untuk menyimpan perubahan


# Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tutorial dan penjelasan asdos sudah sangat baik sehingga mempermudah saya untuk lebih mengerti materi dan juga pengerjaan lab





# TUGAS4
# Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
AuthenticationForm di Django adalah salah satu built-in form yang disediakan oleh modul django.contrib.auth.forms.
Form ini dipakai untuk menangani proses login user. Secara default, AuthenticationForm berisi dua field utama, yaitu username dan password. Ketika form ini divalidasi, Django akan secara otomatis memverifikasi apakah kombinasi username dan password benar serta apakah user masih aktif. Jadi, kita tidak perlu menulis ulang logika otentikasi dasar.

Kelebihan, 
- Mudah digunakan karena tinggal dipanggil tanpa harus membuat form login dari nol
- Terintegrasi dengan sistem autentikasi Django karena langsung bekerja dengan authenticate() dan login()
- Sudah ada validasi bawaan untuk mengecek username, password, serta status akun (aktif/nonaktif)
- Menangani hal-hal penting seperti hashing password dan mencegah kebocoran informasi

Kekurangan,
- Kurang fleksibel karena hanya mendukung autentikasi berbasis username dan password secara default. Kalau ingin login pakai email atau kombinasi lain perlu kustomisasi
-  Terikat ke model User bawaan Django, kalau pakai custom user model dengan field login berbeda (misalnya pakai email), perlu modifikasi tambahan


# Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi adalah proses untuk memastikan identitas pengguna. Misalnya, ketika seseorang masuk ke sistem dengan username dan password, menggunakan akun Google, atau bahkan sidik jari, sistem akan melakukan verifikasi agar dapat mengenali siapa pengguna tersebut. Hasil dari autentikasi adalah sistem mengetahui identitas pengguna yang sedang masuk.
Django sudah menyediakan authentication system di django.contrib.auth.
Beberapa hal yang ditangani adalah login dan logout, verifikasi user, informasi login di session, dan juga mengubah cara autentikasi (misalnya login pakai email).

Sementara itu, otorisasi adalah proses untuk menentukan hak akses pengguna terhadap suatu resource setelah identitasnya dikenali. Contohnya, seorang admin diberi izin untuk menghapus pengguna lain, sedangkan pengguna biasa hanya diperbolehkan mengedit profil miliknya sendiri. Jadi, autentikasi memastikan siapa penggunanya, sedangkan otorisasi mengatur apa saja yang boleh dilakukan pengguna tersebut.
Django punya sistem permissions & groups untuk mengatur otorisasi.
Permissions bisa dicek dengan user.has_perm('app_name.permission_code')
Groups merupakan kumpulan permission yang bisa diberikan ke banyak user sekaligus
Juga ada decorators dan mixins untuk membatasi akses ke view


# Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Dalam konteks aplikasi web, session dan cookies sama-sama dipakai untuk menyimpan state agar interaksi pengguna tidak selalu bersifat stateless. Namun keduanya memiliki karakteristik yang berbeda.

Cookies, data kecil yang disimpan langsung di browser pengguna.
Kelebihan:
- Sederhana dan cepat, data langsung dikirim bersama setiap request ke server.
- Tidak membebani server karena data disimpan di sisi klien.
- Bisa bertahan lama karena jika diatur dengan expiry, cookie bisa tetap ada walau browser ditutup.
Kekurangan:
- Memiliki ukuran terbatas, biasanya maksimal sekitar 4KB per cookie.
- Rentan dimanipulasi, karena disimpan di klien, pengguna bisa mengubahnya.
- Masalah keamanan, jika tidak dienkripsi atau diberi proteksi, rentan dicuri melalui XSS atau sniffing.

Session, session menyimpan data di sisi server, sedangkan browser hanya menyimpan ID session (biasanya lewat cookie).
Kelebihan:
- Lebih aman karena data utama tidak ada di browser, hanya ID yang dikirim.
- Mampu menyimpan lebih banyak data, tidak terbatas ukuran kecil seperti cookie.
- Lebih fleksibel: cocok untuk menyimpan informasi kompleks seperti status login dan keranjang belanja.
Kekurangan:
- Membebani server  karena data disimpan di server, jika pengguna banyak, bisa menambah beban memori atau database.
- Bergantung pada mekanisme penyimpanan, perlu konfigurasi tambahan (misalnya session di file, database, atau cache).
- Bisa hilang saat browser ditutup.


# Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Secara default, cookies tidak sepenuhnya aman dalam pengembangan web. Ada beberapa risiko potensial yang harus diwaspadai ketika menyimpan data di cookies, yaitu
- Manipulasi data, kaarena cookies disimpan di sisi klien (browser), pengguna bisa membaca dan bahkan mengubah isinya.
- Pencurian cookie (Session Hijacking), jika cookie tidak dilindungi, penyerang bisa mencurinya dan menggunakannya untuk berpura-pura sebagai user sah.
- Kebocoran data sensitif,  menyimpan informasi penting (misalnya password atau nomor kartu kredit) di cookie bisa membocorkan data ke pihak lain.

Cara Django menangani hal tersebut adalah dengan menggunakan beberapa mekanisme bawaan untuk membuat penggunaan cookies lebih aman, contohnya adalah
- HttpOnly flag. secara default, cookies Django seperti sessionid diset HttpOnly=True, sehingga tidak bisa diakses lewat JavaScript. Ini mencegah pencurian lewat XSS.
- Secure flag, jika SESSION_COOKIE_SECURE = True atau CSRF_COOKIE_SECURE = True, cookie hanya akan dikirim lewat HTTPS, mencegah pencurian lewat jaringan tidak terenkripsi.
- CSRF Token, Django otomatis melindungi form dengan CSRF token untuk mencegah Cross-Site Request Forgery, serangan yang bisa mengeksploitasi cookie aktif user.
- Signed Cookies, Django menyediakan django.http.HttpResponse.set_signed_cookie() untuk menyimpan data dalam cookie yang sudah diberi tanda tangan digital. Dengan begitu, jika cookie diubah secara manual, tanda tangannya tidak valid dan Django akan menolaknya.


# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Membuat Fungsi Registrasi Akun
Saya mengawali dengan mengimport beberapa hal pada file "views.py", yaitu UserCreationForm dan messages untuk mempermudah pembuatan formulir pendaftaran user. Saya kemudian membuat fungsi registrasi pada file tersebut. Setelah membuat fungsi baru pada file "views.py", saya membuat file baru dengan nama register.html pada folder templates di main sebagai tampilan untuk registrasi  akun user. kemudian saya menghubungkannya dengan mengimport register pada file urls.py dan menambahkan pathnya pada urlpatterns.

Membuat Fungsi Login Akun
Untuk membuat fungsi login akun,langkahnya hampir mirip dengan langkah dalam membuat fungsi registrasi akun, saya mengimport authenticate, login, dan AuthenticationForm terlebih dahulu, setelah itu, baru saya membuat fungsi baru untuk login user. Kemudian saya membuat file baru dengan nama login.html pada folder templates di main sebagai tampilan untuk login akun user. kemudian saya menghubungkannya dengan mengimport login pada file "urls.py" dan menambahkan pathnya pada urlpatterns.

Membuat Fungsi Logout
Untuk membuat fungsi logout, saya mengimport logout bersama dengan authenticate dan login pada file "views.py", kemudian saya membuat fungsi logout pada file tersebut. Kemudian saya menambahkan tombol logout pada file "main.html", kemudian saya menghubungkannya dengan mengimport logout pada file "urls.py" dan menambahkan pathnya pada urlpatterns.

Memisahkan Akses Halaman Produk
Untuk membuat tampilan produk hanya dapat diakses oleh pengguna yang memiliki akun, saya harus melakukan restriksi. Saya awali dengan mengimport from django.contrib.auth.decorators import login_required pada "views.py". Kemudian pada tepat di bagian atas fungsi show_main dan show_product saya menambahkan @login_required(login_url='/login') agar fungsi ini hanya  dapat dijalankan jika user  sudha melakukan login.

Menggunakan Data Dari Cookies
import HttpResponseRedirect, reverse, dan datetime pada bagian paling atas pada file "views.py". Kemudian tambahkan response.set_cookie('last_login', str(datetime.datetime.now()))  pada bagian login untuk menyimpan cookie baru bernama last_login yang berisi timestamp terakhir kali pengguna melakukan login dan pada fungsi show_main tambahkan 'last_login': request.COOKIES.get('last_login', 'Never') ke dalam variabel context. Kemudian hapus cookie last_login setelah user  logout dengan menambahkan response.delete_cookie('last_login') pada fungsi logout. Saya juga menambahkan teks sesi terakhir login pada file "main.html" untuk menampilkan riwayat terakhir login. 

Menghubungkan Model Product dengan User
Saya awali dengan mengimport User pada file "models.py" Kemudian saya menambahkan user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) pada class Product hal ini bertujuan untuk menghubungkan satu produk dengan satu user melalui sebuah relationship. Kemudian saya melakukan migrasi terlebih dahulu (pastikanenv dinyalakan) karena saya melakukan perubahan pada model. Selanjutnya, saya melakukan sedikit perubahan pada fungsi create_product untuk mengisi field user dengan nilai request.user, yaitu pengguna yang sedang login agar etiap objek yang dibuat akan secara otomatis terhubung dengan pengguna yang membuatnya.
kode yang saya tambahkan adalah product_entry = form.save(commit = False) dan product_entry.user = request.user.
Kemudian saya melakukan sedikit perubahan pada fungsishow_main yaitu menambahkan filter_type = request.GET.get("filter", "all") untuk mengfilter produk. Kemudian saya menambahkan tombol filter produk user danallproduk pada file "main.html" dansaya juga  menambahkan nama pemilik produk dan nama user/pengguna yang sedang login di file "main.html"





# TUGAS2
# Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
1. Inline Style CSS yang ditulis langsung pada atribut elemen HTML sehingga punya prioritas paling tinggi.
2. ID Selector (#id) lebih kuat dibanding class, attribute, atau element, karena hanya ada satu elemen dengan ID tertentu, maka dianggap sangat spesifik.
3. Class, Pseudo-class, dan Attribute Selector ketiga hal ini berada pada level yang sama, bisa dipakai beberapa elemen tapi tidak sekuat ID.
4. Element Selector dan Pseudo-element Selector, bisa mencakup banyak elemen sekaligus.
5. !important (override semua), namun bukan bagian dari sistem specificity, tapi sebuah flag (penanda khusus) yang kita tambahkan untuk memaksa aturan tertentu mengalahkan aturan lain, meskipun specificity-nya lebih rendah.


# Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design adalah teknik membuat website yang dimana tampilannya dapat menyesuaikan sesuai dengan ukuran layar device yang digunakan.
Responsive design menjadi konsep yang penting karena dapat meningkatkan user experience dimana misalnya user menggunakan device seperti handphone dengan layar yang kecil, dengan adanya responsive design web dapat lebih nyaman digunakan (teks yang jelas, tombol yang mudah diklik, dll). Selain itu, responsive design juga meningkatkan fleksibilitas dan efisiensi dimana satu kode basis bisa dipakai di semua perangkat, tanpa bikin versi berbeda.

Contoh Website yang sudah menerapkan responsif design
Instagram, karena foto dan feed otomatis sudah menyesuaikan layar, sedangkan di desktop ada sidebar, di HP layout berubah lebih ramping, untuk memberikan user experience yang lebih baik. Tokopedia juga sudah menerapkan responsive design, karena grid produk bisa menyesuaikan device yang digunakan, di desktop tampil beberapa kolom, sedangkan di HP biasanya 2 kolom agar nyaman dilihat.

Contoh Website yang belum menerapkan responsif design
Website lama sekolah/kampus
Biasanya dibuat dengan layout fixed size. Di HP, teks jadi sangat kecil, tabel tidak muat, pengguna harus scroll horizontal maupun vertikal untuk membaca. Biasanya website sekolah/kampus yang lama ini belum diperbarui yang dimana sering dibuat hanya untuk layar komputer, belum mempertimbangkan akses mobile. Juga terdapat situs lama pemerintah, banyak situs resmi instansi pemerintah memakai template jadul yang hanya cocok di desktop, formulir dan menu sering tidak menyesuaikan layar kecil, hal ini karena pengembangan tidak fokus ke UX, hanya sekadar “ada website”, dan jarang diperbarui sesuai standar modern.


# Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin
Margin digunakan untuk mengatur jarak antara elemen dengan elemen lain di sekitarnya, berfungsi untuk memberi ruang antar elemen supaya tidak saling menempel. Contoh implementasi: div { margin: 20px; }

Border
Merupakan garis yang mengelilingi content dan elemen, border memiliki warna, ketebalan, tipe (solid, dashed, dotted), berguna untuk memberi batas visual, bisa juga untuk desain. Contoh implementasi: div class="bg-white rounded-lg border border-gray-200 p-6 sm:p-8 form-style"

Padding
Merupakan karak antara isi elemen (content) dengan border, berguna untuk memberi ruang agar konten tidak menempel langsung ke border. Contoh implementasi: div { padding: 15px; }


# Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox digunakan untuk mengatur layout 1 dimensi (searah, entah horizontal atau vertical). Elemen-elemen anak (flex items) diatur secara fleksibel di dalam kontainer (flex container). Berguna untuk navbar, button group, card list yang ditata sejajar.
Properti utama:
display: flex;   mengaktifkan flexbox pada parent.
flex-direction   menentukan arah (row, column, row-reverse, column-reverse).
justify-content  mengatur perataan horizontal (start, center, space-between, dll.).
align-items      mengatur perataan vertikal.
flex-wrap        apakah item boleh turun ke baris berikutnya.

Grid digunakan untuk mengatur layout 2 dimensi (baris dan kolom). Elemen anak bisa ditempatkan secara eksplisit pada grid tertentu. Berguna untuk layout halaman penuh, dashboard, atau galeri foto.
Properti utama:
display: grid;                              mengaktifkan grid pada parent.
grid-template-columns & grid-template-rows  menentukan jumlah & ukuran kolom/baris.
gap                                         jarak antar grid.
grid-column & grid-row                      menentukan posisi item.


# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Untuk mengimplementasi checklist di atas saya mengawali dengan menambahkan framework CSS Tailwind ke aplikasi. Saya memulai dengan menambahkan tag meta name="viewport" pada file "base.html" hal ini saya lakukan agar web aplikasi dapat menyesuaikan ukuran perangkat yang digunakan user saat membuka web tersebut (responsive web design), kemudian saya menyambungkan template django dengan tailwind dengan cara menambahkan script cdn tailwind di bagian head pada file "base.html" (script src="https://cdn.tailwindcss.com").

Memberi style pada aplikasi dengan tailwind dan juga external CSS
Langkah selanjutnya adalah untuk memberi style pada aplikasi dengan tailwind dan juga external CSS. Sebelum saya styling saya menambahkan middleware WhiteNoise pada file "settings.py" hal ini berguna agar django dapat mengelola file statis secara otomatis dalam mode produksi tanpa perlu konfigurasi yang kompleks, serta membuat file statis tersebut bisa diakses di deployment. Saya juga mengubah konfigurasi pada STATIC_URL, STATIC_ROOT, STATICFILES_DIRS agar merujuk ke /static root project pada mode production.

Kemudian saya melakukan styling dengan membuat folder baru yaitu folder css dan menambah file baru yaitu "global.css" untuk custom atau style css. Setelah itu, saya menghubungkan tailwind dan file tersebut dengan menambahkan file tersebut pada file "base.html". Saya juga menambahkan kode untuk styling pada file "global.css" agar sesuai dengan kustomisasi yang saya inginkan, misalnya seperti border warna coklat dan sudut yang melengkung.

Menambahkan navbar pada aplikasi
Saya melanjutkan dengan menambahkan navbar pada aplikasi untuk menavigasi berbagai halaman atau fitur yang saya ingin tampilkan. Saya memulai dengan membuat file baru bernama "navbar.html" pada folder templates, kemudian saya melakukan kustomisasi file navbar tersebut dengan menggunakan Tailwind CSS, beberapa contoh hal yang saya lakukan adalah Struktur navbar terdiri dari title di kiri, menu navigasi di tengah, dan user section di kanan. Kemudian saya menautkan file navbar pada file "main.html" {% include 'navbar.html' %}.

Menambahkan fungsi untuk mengedit product
Langkah selanjutnya adalah saya menambahkan fungsi untuk mengedit produk (nama produk, gambar, deskripsi, dan harga), saya lakukan dengan menambahkan fungsi baru pada file "views.py" yaitu fungsi edit_product. Kemudian saya juga membuat file html baru untuk menunjukan halaman html edit_product pada folder main/templates dengan nama "edit_product.html", saya juga menambahkan kustomisasi menggunakan Tailwind CSS dengan merubah beberapa hal seperti posisi dan ukuran text, warna text, dan warna button. Jangan lupa juga untuk menghubungkan fungsi ini ke url path di file "urls.py" dan menambahkan fiturnya pada "main.html".

Menambahkan fungsi untuk menghapus product
Langkah selanjutnya adalah saya menambahkan fungsi untuk menghapus produk, saya lakukan dengan menambahkan fungsi baru pada file "views.py" yaitu fungsi delete_product, saya juga menambahkan kustomisasi menggunakan Tailwind CSS dengan merubah beberapa hal seperti posisi dan ukuran text, warna text, dan warna button. Jangan lupa juga untuk menghubungkan fungsi ini ke url path di file "urls.py" dan menambahkan fiturnya pada "main.html".

Styling halaman login, register, detail product, dan create product
Untuk mengstyling halaman-halamn tersebut, saya menimpa file html dari halaman-halaman tersebut dengan kustomisasi dengan menggunakan Tailwind CSS. Beberapa contoh perubahan/kustomisasi yang saya lakukan adalah warna text, warna button, warna border, dan pada detail product saya menyesuaikan ukuran gambar agar ukurannya sesuai dengan gambar aslinya, saya juga menambahkan border pada gambarnya.

Styling home
Saya melakukan beberapa perubahan yang cukup banyak pada halaman homee yaitu dengan menambahkan file "card_product.html" file ini berguna untuk menampilkan suatu gambaran produk dalam rupa kartu pada home page. Saya juga menambahkan fitur sorting untuk product yang berstatus featured pada halaman home. Selain itu, saya juga menambahkan gambar berupa file "no-product.png" untuk ditunjukkan ketiga filter (all products, my products, featured product) belum memiliki product, kemudian saya menghubungkannya pada file "main.html". Saya juga melakukan beberapa perubahan terhadap template pada card product yaitu saya menambahkan efek zoom dan shadow saat hover kursor ke card product dan juga saya melakukan perubahan pada tombol read more pada card agar lebih tampak seperti button.


# TUGAS6
# Apa perbedaan antara synchronous request dan asynchronous request?
Synchronous request adalah permintaan ke server yang dilakukan secara berurutan. Artinya, ketika sebuah request dikirim, browser harus menunggu respons dari server terlebih dahulu sebelum bisa menjalankan kode berikutnya. Akibatnya, jika proses di server memakan waktu lama, halaman akan tampak “diam” atau tidak merespons. Contohnya seperti ketika pengguna mengirim form dan seluruh halaman direload untuk menampilkan hasil.

Sebaliknya, asynchronous request tidak menunggu respons dari server untuk melanjutkan eksekusi kode. Browser tetap bisa menjalankan proses lain sambil menunggu jawaban dari server di latar belakang. AJAX (Asynchronous JavaScript and XML) bekerja dengan cara ini, sehingga memungkinkan halaman web memperbarui sebagian konten tanpa perlu memuat ulang seluruh halaman. Dengan cara ini, pengguna merasakan pengalaman yang lebih cepat dan interaktif.


# Bagaimana AJAX bekerja di Django (alur request–response)?
Ketika pengguna melakukan suatu aksi di halaman web—misalnya menekan tombol “Tambah ke Keranjang”—JavaScript akan menangkap aksi itu dan mengirimkan permintaan AJAX ke server Django. Permintaan ini bisa berupa POST atau GET request yang ditujukan ke salah satu fungsi view di Django.

Django kemudian menerima request tersebut, memproses data yang dikirim, dan mengembalikan respons dalam format JSON, bukan halaman HTML utuh seperti pada request biasa. Setelah itu, JavaScript di sisi pengguna menerima JSON response ini dan memperbarui tampilan halaman secara langsung, misalnya menambah jumlah barang di ikon keranjang tanpa harus me-reload halaman.

Jadi, alurnya bisa diringkas seperti ini: pengguna melakukan aksi -> JavaScript mengirim AJAX request -> Django memproses data dan mengirim JSON response -> JavaScript memperbarui tampilan halaman secara dinamis.


# Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
AJAX memberikan banyak keuntungan dibandingkan render biasa. Karena tidak perlu me-reload seluruh halaman, prosesnya menjadi jauh lebih cepat dan efisien. Pengguna bisa melihat perubahan di layar secara langsung tanpa menunggu halaman baru dimuat.

Selain itu, AJAX membuat pengalaman pengguna terasa lebih modern dan interaktif—misalnya untuk fitur pencarian langsung, notifikasi, komentar, atau penambahan produk ke keranjang belanja. Dengan hanya mengirim data yang dibutuhkan (bukan seluruh HTML), AJAX juga menghemat bandwidth dan mempercepat waktu respons server.


# Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Keamanan tetap sangat penting saat menggunakan AJAX untuk proses sensitif seperti login dan register. Pertama, pastikan Django tetap menggunakan CSRF token di setiap request AJAX agar terhindar dari serangan Cross-Site Request Forgery. Token ini bisa dikirim melalui header X-CSRFToken di JavaScript.

Kedua, gunakan HTTPS agar data seperti username dan password terenkripsi selama proses pengiriman. Ketiga, semua validasi input tetap harus dilakukan di sisi server, bukan hanya di JavaScript, karena pengguna bisa saja memanipulasi request mereka.

Selain itu, pastikan endpoint login dan register hanya menerima metode POST, bukan GET, untuk mencegah kebocoran data sensitif. Terakhir, kirim respons yang minimal, misalnya hanya status sukses atau gagal, tanpa menyertakan data pribadi pengguna di dalam JSON.


# Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
AJAX sangat meningkatkan pengalaman pengguna pada sebuah website. Karena AJAX memungkinkan pembaruan konten tanpa memuat ulang halaman, pengguna merasakan kecepatan dan kelancaran interaksi yang jauh lebih baik. Misalnya, ketika menekan tombol “Like” atau menambahkan item ke keranjang, hasilnya langsung muncul tanpa mengganggu aktivitas lain di halaman.

Selain itu, AJAX memungkinkan website memberikan feedback langsung kepada pengguna, seperti menampilkan indikator loading, pesan sukses, atau notifikasi error dengan cepat. Hal ini membuat website terasa lebih responsif, dinamis, dan menyerupai aplikasi modern (seperti SPA — Single Page Application). Secara keseluruhan, penggunaan AJAX membuat interaksi pengguna terasa lebih natural, cepat, dan nyaman.
