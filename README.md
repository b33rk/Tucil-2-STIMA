# Tugas Kecil 2 Strategi Algoritma

## Daftar Isi 
- [Tugas Kecil 2 Strategi Algoritma](#tugas-kecil-2-strategi-algoritma)
    - [Daftar Isi](#daftar-isi)
    - [Bezier Curve Divide and Conquer](#bezier-curve-divide-and-conquer)
    - [Deskripsi Permasalahan](#deskripsi-permasalahan)
    - [Algoritma yang Digunakan](#algoritma-yang-digunakan)
    - [Struktur Program](#struktur-program)
    - [Requirements Program](#requirements-program)
    - [Menjalankan Program](#menjalankan-program)
    - [How to Use](#how-to-use)
    - [Fitur Unik](#fitur-unik)
    - [Anggota](#anggota)

## Bezier Curve Divide and Conquer 
Dibuat oleh Abdullah Mubarak dan Indraswara Galih Jayanegara

## Deskripsi Permasalahan 
Bezier Curve adalah kurva matematika yang didefinisikan oleh serangkaian titik kontrol yang menentukan jalannya. Metode ini sering digunakan dalam grafika komputer dan desain grafis untuk membuat kurva yang mulus dan tepat. Bezier Curve sering digunakan dalam pembuatan grafis komputer, animasi, dan desain otomotif untuk merepresentasikan bentuk dan jalur dengan presisi tinggi.

Projek ini membuat suatu algoritma dengan pendekatan Divide and Conquer untuk menyelesaikan persoalan Bezier curve dan membuat pendekatan Brute force sebagai perbandingan untuk Divide and Conquer

## Algoritma yang digunakan 
Terdapat dua algoritma yang digunakan: Divide and Conquer sebagai algoritma utama dan Bruteforce sebagai algoritma pembanding.
Algoritma Divide and Conquer menghitung titik tengah antara dua titik sebagai penghitungan utama.
Algoritma Bruteforce menggunakan rumus bezier curve biasa sebagai penghitungan utama.

## Struktur Program 
```
| README.md
|-- doc 
|   |
|-- src
|   |--bruteforce.py
|   |--CLI.py
|   |--dnc.py
|   |--GUI.py
|   |--main.py
|   |--util.py
```

## Requirements Program 
install terlebih dahulu requirements yang diperlukan

pada Windows install
```
pip install PyQt5
```
```
pip install matplotlib
```

Pada WSL Install
```
sudo apt install python3-matplotlib
```
```
sudo apt install python3-pyqt5
```

## Menjalankan Program 
pada windows 
```
.\run-app.bat
```

pada WSL jalankan perintah berikut 
```
.\run-app.sh
```
jika pada WSL tidak bisa jalankan perintah berikut sebelum menjalankan perintah diatas
```
chmod +x run-app.sh
```

### Alternatif 
jika kedua perintah untuk menjalankan program tidak bisa maka jalankan perintah berikut: 

untuk windows: pindah ke folder src
```
python main.py
```

untuk WSL: pindah ke folder src
```
python3 main.py
```

## How to Use
1. Jalankan Program.
2. Pilih algoritma sesuai keinginan.
### Bruteforce
1. Pilih tipe masukan yang diinginkan (iterasi atau jumlah titik akhir).
2. Masukkan titik-titik kontrol yang diinginkan sesuai petunjuk program.
3. Masukkan iterasi atau jumlah titik akhir.
4. Klik <code>enter</code> untuk menampilkan diagram kurva.
### Divide and Conquer
1. Masukkan titik-titik kontrol yang diinginkan sesuai petunjuk program.
2. Masukkan jumlah iterasi.
3. Isi checkbox di samping tombol enter jika ingin menampilkan juga kurva-kurva iterasi sebelumnya.
4. Klik <code>enter</code> untuk menampilkan diagram kurva.
5. Klik <code>animate</code> untuk menampilkan animasi pembentukan kurva dari titik kontrol hingga iterasi masukan.

## Fitur Unik
Pada program ini terdapat beberapa fitur unik:
1. <code>Toolbar</code>. Terdapat toolbar matplotlib di atas gambar plot yang bisa digunakan untuk mengatur ukuran dan hal-hal lain pada plot.
   Untuk petunjuk selengkapnya, silakan kunjungi (https://matplotlib.org/3.2.2/users/navigation_toolbar.html)
2. <code>Checkbox klik plot</code>. Terdapat checkbox pada bagian kiri atas gambar plot, di bawah toolbar.
   Ketika dicentang, program bisa membaca masukan titik dari klik langsung ke gambar plot.
3. <code>Clear all</code>. Berguna untuk menghapus seluruh masukan dan titik-titik di gambar plot.

## Anggota
|Nama           | NIM 
|---------------|----------------| 
| Abdullah Mubarak | 13522101 |
| Indraswara Galih Jayanegara | 13522119|
