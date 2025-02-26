Berikut adalah contoh README.md yang ditulis dengan gaya santai dan mudah dipahami:

---

# Downloader YouTube Playlist dengan Python

Project ini adalah alat sederhana yang menggunakan library **yt-dlp** untuk mengunduh playlist YouTube, baik dalam bentuk video (MP4) maupun audio (MP3). Anda bisa memilih resolusi video (misalnya 1080p atau 720p) atau kualitas audio (misalnya 320, 192, atau 128 kbps) sesuai kebutuhan. Untuk menggabungkan stream video dan audio, project ini menggunakan **ffmpeg**.

## Fitur
- **Download Playlist YouTube:** Mudah mengunduh semua video dalam playlist.
- **Pilihan Tipe Download:** Download sebagai video (MP4) atau audio (MP3).
- **Kustomisasi Resolusi/Kualitas:** Tentukan resolusi video yang diinginkan atau kualitas audio yang diinginkan.
- **Penanganan Koneksi:** Sudah dilengkapi opsi retry untuk mengatasi masalah koneksi internet.

## Persyaratan
- **Python 3.6 ke atas**
- **yt-dlp:** Untuk mengunduh video dari YouTube.
- **ffmpeg:** Untuk proses merging video & audio (jika download video) dan ekstraksi audio.

## Instalasi

### 1. Install Python
Pastikan Python sudah terinstal di komputer Anda. Jika belum, Anda bisa download dari [python.org](https://www.python.org/downloads/).

### 2. Clone/Download Repository
Download atau clone project ini ke komputer Anda.

### 3. Install Library yang Dibutuhkan
Buka terminal/Command Prompt dan jalankan:
```bash
pip install yt-dlp
```

### 4. Install FFmpeg
**Untuk Windows:**
- Download FFmpeg dari [gyan.dev](https://www.gyan.dev/ffmpeg/builds/). Pilih versi "release full" (format ZIP).
- Ekstrak file ZIP tersebut ke folder, misalnya `C:\ffmpeg`.
- Tambahkan folder `C:\ffmpeg\bin` ke Environment Variables (PATH) agar bisa diakses dari Command Prompt.  
  Cara menambahkan ke PATH:
  - Buka **Control Panel** → **System and Security** → **System** → **Advanced system settings** → **Environment Variables**.
  - Di bagian **System variables**, cari variabel `Path`, lalu klik **Edit**.
  - Klik **New** dan masukkan `C:\ffmpeg\bin`, kemudian simpan.

**Untuk Linux/macOS:**
- Linux: Biasanya cukup dengan menjalankan perintah `sudo apt install ffmpeg` (Ubuntu/Debian).
- macOS: Jika menggunakan Homebrew, jalankan `brew install ffmpeg`.

## Cara Penggunaan

1. **Buka Terminal atau Command Prompt**  
   Navigasikan ke folder di mana file `downloader.py` berada.

2. **Jalankan Script**
   ```bash
   python downloader.py
   ```

3. **Ikuti Petunjuk di Layar**
   - Masukkan URL playlist YouTube yang ingin didownload.
   - Pilih tipe download (ketik `audio` untuk MP3 atau `video` untuk MP4).
   - Untuk video: masukkan resolusi yang diinginkan (misalnya `1080p` atau `720p`).
   - Untuk audio: masukkan kualitas audio yang diinginkan (misalnya `320`, `192`, atau `128`).
   - **Catatan:** Jika ffmpeg sudah ada di PATH, cukup tekan Enter ketika diminta lokasi ffmpeg. Jika tidak, Anda bisa mengatur lokasi ffmpeg langsung di kode (sudah diatur dalam variabel `FFMPEG_LOCATION`).

## Contoh Penggunaan
Misalnya, jika Anda ingin mendownload playlist sebagai video dengan resolusi 1080p, Anda cukup:
- Masukkan URL playlist.
- Ketik `video` saat diminta tipe download.
- Ketik `1080p` saat diminta resolusi video.

## Troubleshooting
- **Error ffmpeg:** Jika muncul error terkait ffmpeg (misalnya "ffmpeg is not installed"), pastikan ffmpeg sudah terinstall dengan benar dan PATH sudah dikonfigurasi atau lokasi ffmpeg sudah diatur di kode.
- **Error Koneksi:** Jika terjadi error koneksi, coba periksa kestabilan internet Anda. Script sudah disetting untuk melakukan retry secara otomatis.

## Lisensi
Project ini bebas untuk digunakan dan dimodifikasi sesuai kebutuhan Anda.

---

Semoga README ini membantu dan selamat mencoba! Jika ada pertanyaan atau saran, jangan ragu untuk menghubungi saya.
