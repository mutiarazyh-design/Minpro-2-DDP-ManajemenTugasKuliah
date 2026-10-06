#Nama: Mutiara Zyahra Al Gazali

#NIM: 2609116026


#Deskripsi Singkat Program:
Program ini merupakan Sistem Manajemen Tugas Kuliah yang berfungsi untuk mengelola dan menyimpan data tugas mahasiswa. Sistem ini menerapkan login dengan dua role, yaitu admin dan user, yang memiliki hak akses berbeda. Admin dapat melakukan proses CRUD, seperti menambahkan, melihat, mengubah, dan menghapus data tugas, sedangkan user hanya memiliki hak untuk melihat data tugas. Program ini juga menerapkan Dictionary, Function, validasi input, dan error handling untuk mendukung proses pengolahan data. Selain itu, program menggunakan library PrettyTable, Getpass, dan Datetime untuk menampilkan data secara lebih terstruktur, menjaga proses login, serta membantu melakukan pengecekan tanggal tugas.


#Penjelasan Alur Flowchart:


<img width="1504" height="1752" alt="Flowchart Mini Project 2_Sistem Manajemen Tugas Kuliah" src="https://github.com/user-attachments/assets/9283b04f-d78f-40c0-8b2d-e54ab2823e7b" />


Alur program diawali dengan start, kemudian pengguna melakukan login dengan memasukkan username dan password. Sistem memeriksa kesesuaian data yang dimasukkan. Jika data login tidak sesuai, sistem menampilkan pesan kesalahan dan pengguna kembali ke halaman login. Jika data benar, sistem memeriksa role pengguna.

Jika pengguna memiliki role admin, sistem menampilkan menu admin yang menyediakan fitur untuk menambah, melihat, mengubah, dan menghapus data tugas. Pada fitur tambah tugas, admin memasukkan data tugas, kemudian sistem melakukan validasi terhadap data tersebut. Jika data tidak sesuai, sistem meminta admin untuk memasukkan data kembali. Jika data sudah sesuai, sistem menyimpan data tugas.

Pada fitur Ubah Tugas, admin memasukkan ID tugas yang ingin diperbarui. Sistem memeriksa keberadaan ID tersebut. Jika tugas tidak ditemukan, sistem menampilkan pesan kesalahan dan mengarahkan admin kembali ke menu. Jika tugas ditemukan, admin memilih data yang ingin diubah, seperti mata kuliah, nama tugas, deadline, atau status. Setelah itu, sistem memperbarui data tugas yang dipilih.

Pada fitur Hapus Tugas, admin memasukkan ID tugas yang akan dihapus. Sistem memeriksa keberadaan tugas berdasarkan ID tersebut. Jika tugas ditemukan, sistem menghapus data dari penyimpanan. Jika tugas tidak ditemukan, sistem menampilkan pesan kesalahan dan mengarahkan pengguna kembali ke menu.

Jika pengguna memiliki role user, sistem hanya memberikan akses untuk melihat data tugas. User tidak memiliki izin untuk menambah, mengubah, atau menghapus data tugas.

Setelah selesai menggunakan fitur yang tersedia, pengguna dapat memilih logout untuk keluar dari akun dan kembali ke halaman login. Pengguna dapat melakukan login kembali menggunakan akun lain. Jika pengguna memilih Keluar, sistem menghentikan program dan alur berakhir pada End.



#Penjelasan Penerapan Nilai Tambah:
Program menerapkan validasi input dan error handling untuk menangani kesalahan pengguna saat memasukkan data. Penggunaan try-except dapat mencegah program berhenti ketika terjadi kesalahan, seperti memasukkan ID tugas dengan huruf. Selain itu, program memvalidasi pilihan menu, status tugas, data kosong, dan format deadline.

Saya juga menggunakan tiga library, yaitu PrettyTable, Getpass, dan Datetime. PrettyTable digunakan untuk menampilkan data dalam bentuk tabel, Getpass digunakan untuk menyembunyikan password saat login, sedangkan Datetime digunakan untuk memeriksa format deadline. Penggunaan library tersebut membantu program menjadi lebih rapi, aman, dan mudah digunakan.


#Dokumentasi Program

1. PrettyTable digunakan untuk menampilkan data tugas dalam bentuk tabel agar lebih rapi dan mudah dibaca.
Getpass digunakan untuk menyembunyikan password saat pengguna melakukan login.
Datetime digunakan untuk memeriksa dan memvalidasi format tanggal pada deadline tugas.

Hak Akses Pengguna
Admin memiliki hak akses untuk menambah, melihat, mengubah, dan menghapus data tugas.
User memiliki hak akses yang terbatas dan hanya dapat melihat data tugas.

Penyimpanan Data
Bagian ini digunakan untuk menyimpan data tugas kuliah. Data dapat ditambah, dilihat, diubah, atau dihapus sesuai dengan hak akses pengguna.


<img width="1920" height="628" alt="Program 1" src="https://github.com/user-attachments/assets/aba8f22e-1565-4f8b-9a9f-f7b18e8bba53" />


2. Bagian ini berfungsi sebagai sistem login dengan batas maksimal 3 kali percobaan. Setelah login berhasil, program menentukan role admin atau user yang digunakan untuk mengatur hak akses dan menu yang dapat digunakan oleh pengguna.


<img width="1920" height="979" alt="Program 2" src="https://github.com/user-attachments/assets/328d116f-3b56-4e46-8985-3f22ff75955c" />


3. Bagian ini berfungsi untuk menambahkan data tugas baru. Program memvalidasi mata kuliah, nama tugas, deadline, dan status sebelum data disimpan. Penggunaan while, if-elif-else, dan try-except membantu menangani kesalahan input sehingga program tetap berjalan.


<img width="1920" height="979" alt="Program 3" src="https://github.com/user-attachments/assets/fff41bc4-b745-4b7d-a86c-b20f09f43ebb" />


4. Bagian ini merupakan tahap akhir dalam proses penambahan tugas. Program memvalidasi status tugas, memberikan ID secara otomatis, lalu menyimpan data ke dalam Dictionary. Setelah data berhasil disimpan, program menampilkan pesan bahwa tugas berhasil ditambahkan. Bagian ini juga menerapkan function dan dictionary sesuai dengan kebutuhan program.


<img width="1920" height="955" alt="Program 4" src="https://github.com/user-attachments/assets/d43627dd-0afc-4444-999d-9726baa446ef" />


5. Bagian ini berfungsi untuk menampilkan data tugas yang telah tersimpan. Program mengecek ketersediaan data terlebih dahulu. Jika data tersedia, program menampilkannya menggunakan PrettyTable agar lebih rapi dan mudah dibaca.


<img width="1920" height="968" alt="Program 5" src="https://github.com/user-attachments/assets/a3dac62c-2f1c-46e0-bda6-8640241d5fad" />


6. Bagian ini digunakan untuk memilih data tugas yang akan diubah. Program mengecek ketersediaan data terlebih dahulu, kemudian meminta pengguna memasukkan ID tugas. Penggunaan try-except membantu menangani kesalahan ketika pengguna memasukkan ID yang bukan angka. Jika ID tidak ditemukan, program menampilkan pesan kesalahan.


<img width="1920" height="1014" alt="Program 6" src="https://github.com/user-attachments/assets/0b692cdf-ec1a-4420-a590-ac2b5b30c3a4" />


7. Bagian ini berfungsi untuk mengubah nama mata kuliah pada tugas yang telah dipilih. Program meminta pengguna memasukkan nama mata kuliah baru dan melakukan validasi agar input tidak kosong. Jika data valid, program memperbarui nama mata kuliah pada Dictionary data_tugas.


<img width="1920" height="1007" alt="Program 7" src="https://github.com/user-attachments/assets/aa9abb6a-b847-4be8-baf2-78b93bdc9a57" />


8. Bagian ini berfungsi untuk mengubah data tugas yang telah tersimpan. Program mencari tugas berdasarkan ID dan melakukan validasi terhadap input. Setelah tugas ditemukan, admin dapat memilih bagian data yang ingin diubah. Penggunaan try-except membantu menangani kesalahan ID sehingga program tetap berjalan.


<img width="1920" height="981" alt="Program 8" src="https://github.com/user-attachments/assets/d0c4c10a-b4e5-4b85-b4f3-1d775cb665c2" />


9. Bagian ini berfungsi sebagai pengatur utama jalannya program. Program melakukan proses login terlebih dahulu, kemudian memeriksa role pengguna. Admin diarahkan ke menu admin dengan akses CRUD, sedangkan user diarahkan ke menu user yang hanya dapat melihat tugas. Setelah melakukan logout, pengguna kembali ke halaman login.


<img width="1920" height="668" alt="Program 9" src="https://github.com/user-attachments/assets/6f817838-494c-49eb-aecc-8f9237482e1e" />


#Dokumentasi Output


1. Program menampilkan halaman LOGIN SISTEM TUGAS, kemudian pengguna memasukkan username dan password akun admin. Sistem memeriksa data yang dimasukkan dan jika sesuai, sistem menampilkan pesan “Login berhasil!” serta menetapkan role pengguna sebagai admin. Setelah itu, pengguna diarahkan ke Menu Admin sesuai dengan hak akses yang dimilikinya.


<img width="1920" height="872" alt="OUTPUT 1  MINPRO 2" src="https://github.com/user-attachments/assets/f99409d5-994a-42b2-ac76-591f1713f8d9" />


2. Admin memilih menu 1. Tambah Tugas, kemudian program meminta data berupa mata kuliah DDP, nama tugas Mini Project 1, deadline 12-09-2026, dan status Selesai. Setelah seluruh data dimasukkan dengan benar, program menampilkan pesan “Tugas berhasil ditambahkan!”.


<img width="1920" height="921" alt="OUTPUT 2  MINPRO 2" src="https://github.com/user-attachments/assets/628110ef-8448-4c07-9e65-d7c26f8ce35f" />


3. Admin memilih menu 2. Lihat Tugas, kemudian program menampilkan seluruh data tugas dalam bentuk tabel menggunakan PrettyTable. Tabel tersebut menampilkan ID, Mata Kuliah, Nama Tugas, Deadline, dan Status. Berdasarkan hasil output, terdapat 6 data tugas yang telah tersimpan dalam sistem.


<img width="1920" height="795" alt="OUTPUT 3  MINPRO 2" src="https://github.com/user-attachments/assets/85657a7d-8ac7-4a17-be0f-38fc57cb1edd" />


4. Admin memilih menu 3. Ubah Tugas, kemudian program menampilkan daftar tugas dan meminta ID tugas yang ingin diubah. Admin memilih ID 2, lalu program menampilkan beberapa pilihan data yang dapat diubah, yaitu mata kuliah, nama tugas, deadline, status, dan kembali. Admin memilih bagian Status dan mengubahnya menjadi Selesai. Setelah perubahan berhasil dilakukan, program menampilkan pesan “Status berhasil diubah!”.


<img width="1920" height="665" alt="OUTPUT 4  MINPRO 2" src="https://github.com/user-attachments/assets/ff6c73d5-1b8a-4f73-9159-63699003e62e" />


5. Admin memilih menu 4. Hapus Tugas, kemudian program menampilkan halaman “HAPUS DATA TUGAS”. Pada halaman tersebut, admin dapat memilih data tugas yang ingin dihapus dari sistem.


<img width="1920" height="852" alt="OUTPUT 5  MINPRO 2" src="https://github.com/user-attachments/assets/9d29e7fc-7236-450e-b044-8cacc88f91af" />


6. Setelah selesai menggunakan Menu Admin - Manajemen Tugas, pengguna memilih opsi 5 untuk keluar dari sesi admin. Program kemudian mengarahkan pengguna kembali ke halaman login. Pengguna memasukkan username: user dan berhasil masuk dengan role user. Setelah login berhasil, program menampilkan Menu User - Tugas Kuliah yang memiliki pilihan 1. Lihat Tugas dan 2. Keluar. Pengguna kemudian memilih opsi 1 untuk melihat data tugas.


<img width="1920" height="809" alt="OUTPUT 6  MINPRO 2" src="https://github.com/user-attachments/assets/70bf7f39-9b99-4edb-a898-8b974004cb55" />


7. Program menampilkan Menu User yang berisi DAFTAR TUGAS KULIAH dalam bentuk tabel yang berisi kolom ID, Mata Kuliah, Nama Tugas, Deadline, dan Status. Terdapat 5 data tugas, yaitu tugas dari mata kuliah DDP berupa Mini Project 1 dan Mini Project 2, serta mata kuliah PTI berupa Post Test 1, 2, dan 3. Seluruh tugas tersebut memiliki status Selesai. Setelah pengguna menekan tombol Enter, sistem kembali menampilkan Menu User - Tugas Kuliah.


<img width="1920" height="1080" alt="OUTPUT 7  MINPRO 2" src="https://github.com/user-attachments/assets/390333c6-b481-41b9-8aa6-6ef5f40d4994" />


8. Pengguna memilih opsi 2 (Keluar) pada Menu User - Tugas Kuliah. Sistem kemudian menampilkan notifikasi “Keluar dari menu user” dan mengarahkan pengguna kembali ke halaman utama Login Sistem Tugas.


<img width="1920" height="962" alt="OUTPUT 8  MINPRO 2" src="https://github.com/user-attachments/assets/4636f011-7853-4255-989e-05b644534dad" />


9. Jika proses admin saat menambahkan tugas baru. Setelah berhasil login, admin memilih menu Tambah Tugas dan memasukkan data mata kuliah DDP, nama tugas MinPro 2, serta status Selesai. Saat memasukkan deadline, admin menggunakan format 06 10 2026 yang tidak sesuai sehingga program menampilkan pesan “Format deadline salah! Gunakan format DD-MM-YYYY.” Admin kemudian memasukkan kembali deadline dengan format yang benar, yaitu 06-10-2026. Setelah semua data valid, program menampilkan pesan “Tugas berhasil ditambahkan!”. Hal ini menunjukkan bahwa program dapat memvalidasi input dan menangani kesalahan tanpa menghentikan proses.


<img width="1920" height="872" alt="Output 9" src="https://github.com/user-attachments/assets/51fee17c-f173-419e-b22b-f1f10fc06f8b" />


10. Jika kondisi ketika pengguna gagal melakukan login. Pengguna memasukkan username user dengan password yang salah sehingga program menampilkan pesan “Username atau password salah!”. Sistem memberikan maksimal tiga kesempatan untuk melakukan login. Setelah tiga kali percobaan gagal, sistem menampilkan pesan “Anda gagal login. Program selesai.”. Proses tersebut menunjukkan bahwa program menerapkan batas percobaan login sebagai bentuk validasi dan keamanan.


<img width="1920" height="643" alt="Output 10" src="https://github.com/user-attachments/assets/e7277787-8b06-4743-8f9f-cb504f3170aa" />


