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
    - [Anggota](#anggota)

## Bezier Curve Divide and Conquer 
Dibuat oleh Abdullah Mubarak dan Indraswara Galih Jayanegara

## Deskripsi Permasalahan 
Bezier Curve adalah kurva matematika yang didefinisikan oleh serangkaian titik kontrol yang menentukan jalannya. Metode ini sering digunakan dalam grafika komputer dan desain grafis untuk membuat kurva yang mulus dan tepat. Bezier Curve sering digunakan dalam pembuatan grafis komputer, animasi, dan desain otomotif untuk merepresentasikan bentuk dan jalur dengan presisi tinggi.

Projek ini membuat suatu algoritma dengan pendekatan Divide and Conquer untuk menyelesaikan persoalan Bezier curve dan membuat pendekatan Brute force sebagai perbandingan untuk Divide and Conquer

## Algoritma yang digunakan 
Terdapat dua algoritma yang digunakan: Divide and Conquer sebagai algoritma utama dan bruteforce sebagai algoritma pembanding.

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
jika kedua perintah untuk menjalankan program tidak bisa maka jalankan perintah berikut 


untuk windows: pindah ke folder src
```
python main.py
```

untuk WSL: pindah ke folder src
```
python3 main.py
```



## Anggota
|Nama           | NIM 
|---------------|----------------| 
| Abdullah Mubarok | 13522101 |
| Indraswara Galih Jayanegara | 13522119|
