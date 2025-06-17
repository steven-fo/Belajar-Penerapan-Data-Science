# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Tantangan jumlah dropout ini terletak pada deteksi sejak dini agar jumlah mahasiswa yang terancam dropout bisa dicegah. Beberapa pertanyaan bisnis yang bisa dijadikan acauan sebagai berikut: bagaimana mendeteksi mahasiswa yang terancam dropout, apa komponen utama yang menjadi penentu dalam seberapa terancam mahasiswa untuk dropout, dan apa rekomendasi aksi yang harus dilakukan untuk mencegah mahasiswa dropout.

### Cakupan Proyek
Proyek ini mencakup analisis data, pemahaman data, mencari faktor utama penentu dropout lalu membuat dashboard untuk mendapatkan insight tentang mahasiswa yang dropout. Dari insight tersebut, didapat rekomendasi aksi yang harus dilakukan untuk mencegah jumlah dropout semakin banyak.

### Persiapan

Sumber data: dataset yang digunakan merupakan dataset yang diambil dari Jaya Jaya Institut [link](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Setup environment:
```
conda create --name dicoding
```

Install requirements:
```
pip install -r requirements.txt
```

## Business Dashboard
Dashboard ini menampilkan ringkasan statistik dan visualisasi performa akademik mahasiswa berdasarkan status akhir mereka: lulus, masih aktif, dan dropout. Terlihat bahwa mahasiswa yang dropout memiliki jumlah mata kuliah yang disetujui serta nilai (grade) yang jauh lebih rendah dibanding mahasiswa yang lulus, baik pada semester pertama maupun kedua.

Polanya menunjukkan bahwa mahasiswa yang dropout sudah mengalami kesulitan akademik sejak semester pertama. Jumlah mata kuliah yang diluluskan dan nilai yang rendah bisa menjadi indikator awal risiko dropout. Informasi ini berguna untuk mendeteksi mahasiswa berisiko dan merancang intervensi lebih dini.

## Menjalankan Sistem Machine Learning
Dalam proyek ini, sebuah prototipe telah disiapkan untuk melakukan prediksi menggunakan model yang telah dilatih. Isi data sesuai fieldnya, lalu di paling bawah klik tombol predict, hasil prediksi pun akan muncul.

- **Menjalankan secara lokal**
  Buka terminal pada direktori proyek, kemudian ketik:

  ```bash
  streamlit run app.py
  ```

- **Akses melalui web**
  Silakan buka prototipe langsung di [tautan ini](https://education-institution-project-stevenfo.streamlit.app/).

## Conclusion
Proyek deteksi dropout mahasiswa di Jaya Jaya Institut berhasil mengidentifikasi bahwa performa akademik semester pertama merupakan prediktor terkuat untuk dropout. Mahasiswa yang dropout memiliki rata-rata nilai jauh lebih rendah (8-10) dibanding yang lulus (28-30) dan hanya menyelesaikan 3-4 mata kuliah per semester. Model Random Forest yang dikembangkan mampu memprediksi risiko dropout dengan akurasi tinggi.

Sistem ini membuktikan bahwa 6 bulan pertama perkuliahan adalah periode kritis yang menentukan keberhasilan akademik. Dengan implementasi early warning system berbasis machine learning, Jaya Jaya Institut dapat melakukan intervensi dini, meningkatkan retention rate, dan mengoptimalkan alokasi sumber daya pendidikan untuk memberikan setiap mahasiswa kesempatan terbaik mencapai kelulusan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- Deteksi Dini: Identifikasi mahasiswa dengan jumlah mata kuliah lulus dan nilai yang rendah sejak semester pertama sebagai kelompok berisiko tinggi untuk dropout.

- Pendampingan Akademik: Berikan bimbingan belajar atau tutoring tambahan untuk mahasiswa yang menunjukkan performa akademik rendah di awal studi.

- Monitoring Berkala: Lakukan evaluasi rutin setiap akhir semester untuk memantau perkembangan mahasiswa, khususnya pada semester pertama dan kedua.

- Intervensi Psikologis dan Konseling: Tawarkan layanan konseling untuk membantu mahasiswa mengatasi tekanan akademik atau pribadi yang mungkin memengaruhi performa belajar.

- Peringatan Dini Otomatis: Kembangkan sistem peringatan berbasis data yang dapat memberi notifikasi kepada dosen wali atau staf akademik saat mahasiswa menunjukkan gejala awal risiko dropout.
