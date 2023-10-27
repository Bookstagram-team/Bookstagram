**<h1>README Tugas 6</h1>**
**<h2>Link: <a href="http://edward-salim-tugas.pbp.cs.ui.ac.id/">http://edward-salim-tugas.pbp.cs.ui.ac.id/</a></h2>**
<br>
**1. Jelaskan perbedaan antara _asynchronous programming_ dengan _synchronous programming_.**

**Jawaban:**

Asynchronous programming dan synchronous programming adalah dua pendekatan yang berbeda dalam menangani eksekusi kode di dalam program. Perbedaan utama antara keduanya terletak pada bagaimana program mengelola tugas-tugas yang mungkin memakan waktu, seperti mengambil data dari jaringan atau melakukan operasi disk yang lambat.

* **Synchronous Programming**
    
    * Ketika sebuah tugas yang memakan waktu (seperti mengambil data dari database atau menunggu respon jaringan) dimulai, program akan berhenti atau "mengunci" eksekusi sampai tugas tersebut selesai. Ini berarti bahwa program tidak akan melanjutkan eksekusi kode lainnya hingga tugas tersebut selesai.
    
    * Kekurangan utama dari pendekatan ini adalah bahwa program bisa terasa tidak responsif jika ada tugas yang memakan waktu lama, karena tidak ada eksekusi kode lain yang dapat berjalan selama tugas tersebut berlangsung.
    
    * Seringkali lebih mudah dipahami dan dikelola karena urutan eksekusi kode lebih langsung dan mudah diprediksi.

* **Asynchronous Programming:**
    * Tugas yang memakan waktu tidak mengunci eksekusi program. Sebaliknya, program dapat melanjutkan eksekusi kode lainnya sambil menunggu tugas tersebut selesai.
    
    * Kekuatan utama dari pendekatan ini adalah kemampuan untuk menjadikan program lebih responsif. Ini memungkinkan aplikasi untuk tetap merespons input pengguna atau menjalankan tugas-tugas lainnya tanpa harus menunggu tugas yang memakan waktu selesai.
    
    * Seringkali lebih kompleks daripada synchronous programming karena memerlukan pengelolaan callback, promise, atau async/await untuk mengontrol urutan eksekusi dan menangani kesalahan.<br><br>

**2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma _event-driven programming_. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**

**Jawaban:**

Paradigma event-driven programming adalah pendekatan pemrograman di mana program merespons kejadian (events) yang terjadi, seperti interaksi pengguna, perubahan status, atau tindakan eksternal, dengan menjalankan tindakan atau kode tertentu. Dalam paradigma ini, program tidak berjalan secara linear dari atas ke bawah, tetapi lebih mirip dengan mesin yang menunggu kejadian dan meresponsnya.

Salah satu fitur utama dari paradigma event-driven programming adalah penggunaan event listeners atau handlers yang mendengarkan kejadian yang terjadi dan menjalankan fungsi tertentu ketika kejadian itu terjadi. Ini memungkinkan program untuk merespons interaksi pengguna atau perubahan data secara dinamis. Contoh penerapannya pada tugas 6 ini adalah penggunaan event-driven programming dalam mengendalikan modal (popup) yang muncul ketika tombol “Add Item by AJAX” ditekan.<br><br>

**3. Jelaskan penerapan _asynchronous programming_ pada AJAX.**

**Jawaban:**

Penerapan asynchronous programming pada AJAX adalah salah satu fitur kunci dari teknologi AJAX (Asynchronous JavaScript and XML). Contoh penerapan asynchronous programming pada AJAX adalah penggunaan XMLHttpRequest atau fetch API untuk melakukan permintaan HTTP dan menangani respons yang diterima. Berikut adalah penjelasan lebih rinci tentang penerapan asynchronous programming pada AJAX:

* **Asynchronous Nature**

    AJAX menekankan sifat asinkron dari permintaan HTTP. Ini berarti bahwa saat melakukan permintaan AJAX, pengguna tidak harus menunggu sampai respons dari server tiba sebelum melanjutkan eksekusi kode. Sebaliknya, pengguna dapat mengirim permintaan AJAX dan melanjutkan eksekusi kode lainnya, dan ketika respons dari server siap, pengguna akan menerima notifikasi atau event yang memungkinkan untuk menangani respons tersebut.

* **Event Handling**

    Ketika permintaan AJAX pengguna selesai, seperti pengambilan data dari server atau pengiriman data ke server, event akan dipicu. Pengguna dapat mengatur event handler untuk menangani respons yang diterima. Misalnya, dapat mengatur event handler untuk mengupdate antarmuka pengguna dengan data yang diterima atau untuk melakukan tindakan tertentu berdasarkan respons tersebut.

* **Callback Functions**

    Dalam AJAX, callback functions akan sering digunakan untuk menentukan tindakan apa yang harus diambil ketika respons dari server telah tiba. Callback functions adalah fungsi JavaScript yang akan dijalankan ketika operasi asinkron selesai. Contohnya, pengguna dapat menggunakan success callback untuk menangani respons yang berhasil dan error callback untuk menangani kesalahan jika permintaan AJAX gagal.

* **Promises and async/await**

    Selain menggunakan callback, pengguna juga dapat menggunakan konsep promises dan async/await dalam JavaScript modern untuk mengelola operasi AJAX secara lebih bersih dan mudah dibaca. Promises memungkinkan untuk menulis kode yang lebih bersih dengan menghindari callback hell, dan async/await membuat kode tampak seperti operasi sinkron meskipun sebenarnya bersifat asinkron.<br><br>

**4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada _library_ jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.**

**Jawaban:**



* **Fetch API**
    * Bagian dari JavaScript, jadi tidak perlu mengunduh atau memasang library tambahan. Ini adalah bagian dari spesifikasi standar ECMAScript, yang berarti mendukung hampir semua modern browser.
    
    * Fetch API menggunakan promises, yang memungkinkan untuk mengelola operasi asinkron dengan cara yang lebih bersih dan mudah dibaca daripada callback. Async/await dapat digunakan untuk menulis kode yang lebih rapi.
    
    * Lebih ringan daripada jQuery karena hanya berfokus pada AJAX dan tidak memiliki berbagai fitur lain yang kompleks seperti jQuery.

* **jQuery**
    
    * Dirancang untuk menyelesaikan masalah kompatibilitas peramban yang umum. Ini berarti pengguna dapat yakin bahwa kode akan berfungsi dengan baik di banyak jenis peramban.
    
    * Selain AJAX, jQuery juga menyediakan berbagai utilitas untuk manipulasi DOM dan animasi, yang membuatnya lebih kuat untuk pengembangan frontend yang kompleks.
    
    * Memiliki ekosistem plugin yang luas, yang dapat menghemat waktu dalam pengembangan. Pengguna dapat menemukan banyak plugin yang siap digunakan untuk berbagai tugas.

Pemilihan antara Fetch API dan jQuery sangat bergantung pada kebutuhan khusus dari proyek yang sedang dihadapi. Jika proyek mengharuskan penggunaan AJAX yang sederhana dengan fokus pada menjaga proyek tetap ringan dan bersih, maka Fetch API adalah pilihan yang sangat sesuai. Teknologi ini cocok untuk aplikasi modern yang menekankan kecepatan dan efisiensi. Di sisi lain, jika proyek menghadapi masalah kompleks terkait kompatibilitas peramban yang rumit atau memerlukan manipulasi DOM yang mendalam, maka penggunaan jQuery mungkin menjadi lebih tepat. Selain itu, jika tim pengembang telah memiliki pengalaman yang kuat dengan jQuery atau proyek sudah menggunakan jQuery dalam skala besar, maka menggunakan jQuery tetap merupakan pilihan yang valid.<br><br>

**5. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step._**

**Jawaban:**

1. **Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.**

    * **AJAX GET**

        1. **Ubahlah kode tabel data item agar dapat mendukung AJAX GET.**

            1. Pertama-tama, saya mengakses berkas "main.html" dalam direktori "main/templates" dan menghapus kode tabel yang telah saya buat dalam tutorial sebelumnya. Kemudian, saya menambahkan elemen &lt;table id="item_table">&lt;/table> untuk menyiapkan tempat bagi tabel data item yang akan ditampilkan.

        2. **Lakukan pengambilan task menggunakan AJAX GET.**

            1. Selanjutnya, saya membuat sebuah fungsi bernama get_item_json dalam berkas "views.py" yang bertugas mengembalikan data dalam format JSON. Fungsi ini memungkinkan penampilan data item pada halaman HTML dengan menggunakan fetch API, tergantung pada pengguna yang sedang login.

            2. Selanjutnya, saya membuka berkas "urls.py" dalam folder "main" dan mengimpor fungsi get_item_json, kemudian menambahkan path URL yang mengarah ke fungsi tersebut ke dalam daftar urlpatterns (path('get-item/', get_item_json, name='get_item_json'))

            3. Kemudian, saya membuat sebuah blok &lt;script> di bagian bawah berkas HTML dan mendefinisikan fungsi getItems() di dalamnya. Fungsi ini menggunakan fetch API untuk mengambil data JSON secara asinkron. Setelah data berhasil diambil, saya menggunakan metode .then() untuk melakukan parsing data JSON menjadi objek JavaScript yang dapat diolah lebih lanjut.<br><br>

    * **AJAX POST**
        
        3. **Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.**

            1. Langkah pertama yang saya ambil adalah menambahkan kode untuk mengimplementasikan modal dengan menggunakan komponen Bootstrap dalam aplikasi saya.

            2. Kemudian, saya menyisipkan sebuah tombol dengan peran penting dalam mengaktifkan modal tersebut. Kode tombol yang saya tambahkan yaitu &lt;button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Item by AJAX&lt;/button>. Penggunaan atribut data-bs-toggle dan data-bs-target adalah bagian integral dari Bootstrap yang memungkinkan penggunaan modal dengan mudah. 

        4. **Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.**

            1. Saya melanjutkan dengan pembuatan fungsi baru dalam berkas "views.py" yang saya beri nama add_item_ajax. Fungsi ini menerima parameter request yang akan digunakan untuk menangani permintaan dari pengguna. Untuk memastikan keamanan, saya menambahkan dekorator @csrf_exempt di atas fungsi add_item_ajax.

            2. Dalam implementasi fungsi add_item_ajax, saya menjalankan beberapa tindakan penting yang diperlukan. Salah satu tindakan tersebut adalah menggunakan kode name = request.POST.get("name") untuk mengambil nilai yang dikirimkan dalam request dengan nama "name". Hal yang sama dilakukan untuk "amount", "description", dan "user" dengan menggunakan request.user. Nilai-nilai yang berhasil diambil ini kemudian digunakan untuk membentuk sebuah objek Item baru. Dengan memasukkan nilai-nilai ini sebagai parameter, saya berhasil menambahkan item baru ke dalam basis data dengan menggunakan data yang diterima dari permintaan AJAX.

        5. **Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.**

            1. Setelahnya, saya membuka berkas "urls.py" dalam folder "main" dan mengimpor fungsi add_item_ajax. Selanjutnya, saya menambahkan path URL yang mengarah ke fungsi tersebut ke dalam daftar urlpatterns dengan perintah path('create-ajax/', add_item_ajax, name='add_item_ajax').

        6. **Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.**

            1. Selanjutnya, saya membuat fungsi JavaScript baru dengan nama addItem() untuk menghubungkan form yang telah saya buat dalam modal dengan path "/create-ajax/" atau URL dari fungsi add_item_ajax yang telah saya definisikan dalam berkas "views.py". Fungsi ini bertujuan untuk menambahkan data ke basis data secara asinkron melalui AJAX, berdasarkan input yang diberikan oleh pengguna. Dalam implementasi fungsi addItem(), saya menggunakan kode new FormData(document.querySelector('#form')) untuk membuat objek FormData baru. Objek FormData ini akan mengumpulkan data dari form yang ada dalam modal, sehingga nantinya data tersebut dapat dikirimkan ke server. Setelah proses pengiriman data berhasil, saya menggunakan document.getElementById("form").reset() untuk mengosongkan isi dari field-field form pada modal setelah data berhasil ditambahkan.

            2. Untuk memastikan fungsi addItem() dijalankan saat pengguna mengklik tombol "Add Item" pada modal, saya menambahkan atribut onclick pada tombol tersebut dengan kode document.getElementById("button_add").onclick = addItem. 

        7. **Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan.**

            1. Selanjutnya, saya membuat sebuah fungsi baru dalam blok &lt;script> yang saya beri nama refreshItems(). Fungsi ini bertujuan untuk melakukan refresh data item secara asinkron. Dalam implementasinya, saya menggunakan document.getElementById("item_table") untuk mengambil elemen berdasarkan ID-nya. Pada baris kode ini, elemen yang saya tuju adalah elemen &lt;table> yang memiliki ID "item_table". Saya menggunakan properti innerHTML untuk mengelola isi dari elemen tersebut. Jika innerHTML bernilai "", maka hal ini akan mengosongkan semua elemen anak (child elements) dari elemen yang dituju. Kemudian, saya menggunakan metode forEach() untuk melakukan perulangan (loop) pada data items yang telah diambil sebelumnya menggunakan fungsi getItems(). Dalam setiap iterasi loop, saya menggabungkan (concatenate) data dari objek item dengan variabel htmlString yang digunakan untuk membangun struktur tabel. Terakhir, saya memanggil fungsi refreshItems() setiap kali untuk memastikan daftar item diperbarui secara otomatis tanpa perlu melakukan reload halaman utama.<br><br>

    * **Melakukan perintah collectstatic.**

        8. **Perintah ini bertujuan untuk mengumpulkan file static dari setiap aplikasi kamu ke dalam suatu folder yang dapat dengan mudah disajikan pada produksi.**

            1. Langkah pertama yang saya ambil adalah berpindah ke direktori proyek "ewod_hearthstone" menggunakan perintah cd. Setelah berada dalam direktori proyek, saya mengaktifkan lingkungan virtual (environment) jika digunakan untuk memisahkan dan mengisolasi dependensi proyek.

            2. Selanjutnya, saya menjalankan perintah python manage.py collectstatic pada terminal. Tujuan dari perintah ini adalah untuk mengumpulkan semua file static dari setiap aplikasi dalam proyek saya dan menempatkannya dalam satu folder khusus. Hasil pengumpulan ini disimpan dalam direktori yang telah dikonfigurasi dalam pengaturan Django, dan dalam kasus ini, hasil pengumpulan disimpan di 'C:\Users\felicia salim\ewod_hearthstone\static'.