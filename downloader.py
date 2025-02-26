import yt_dlp

def download_playlist(playlist_url, download_type, audio_quality=None, video_resolution=None, ffmpeg_location=None):
    # Opsi umum tambahan untuk menangani error koneksi
    common_opts = {
        'retries': 10,               # Coba ulang hingga 10 kali jika terjadi kegagalan
        'fragment-retries': 10,        # Coba ulang untuk masing-masing fragmen
        'http_chunk_size': 10485760,   # Ukuran chunk HTTP (10MB) untuk menghindari masalah koneksi
    }
    
    if download_type.lower() == "audio":
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': str(audio_quality) if audio_quality else '320',
            }],
            'outtmpl': '%(playlist_title)s/%(title)s.%(ext)s',
            'noplaylist': False,
        }
    elif download_type.lower() == "video":
        if video_resolution:
            try:
                res_value = int(video_resolution.lower().replace("p", ""))
            except ValueError:
                print("Resolusi tidak valid. Menggunakan format terbaik.")
                res_value = None
            if res_value:
                ydl_opts = {
                    'format': f'bestvideo[height={res_value}]+bestaudio/best[height={res_value}]/best',
                    'merge_output_format': 'mp4',
                    'outtmpl': '%(playlist_title)s/%(title)s.%(ext)s',
                    'noplaylist': False,
                }
            else:
                ydl_opts = {
                    'format': 'best',
                    'merge_output_format': 'mp4',
                    'outtmpl': '%(playlist_title)s/%(title)s.%(ext)s',
                    'noplaylist': False,
                }
        else:
            ydl_opts = {
                'format': 'best',
                'merge_output_format': 'mp4',
                'outtmpl': '%(playlist_title)s/%(title)s.%(ext)s',
                'noplaylist': False,
            }
    else:
        print("Tipe download tidak dikenali. Harap pilih 'audio' atau 'video'.")
        return

    # Gabungkan opsi umum dengan opsi khusus
    ydl_opts.update(common_opts)
    
    # Lokasi ffmpeg sudah ditentukan secara langsung
    if ffmpeg_location:
        ydl_opts['ffmpeg_location'] = ffmpeg_location

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([playlist_url])
            print("Download selesai.")
        except Exception as e:
            print(f"Terjadi kesalahan saat download: {e}")

if __name__ == "__main__":
    # Konfigurasi lokasi ffmpeg secara langsung di sini.
    # Ganti path berikut dengan path yang benar sesuai instalasi ffmpeg Anda.
    # Jika ffmpeg sudah ada di PATH, Anda bisa mengosongkan variabel ini (None).
    FFMPEG_LOCATION = r"C:\ffmpeg\bin"

    playlist_url = input("Masukkan URL playlist YouTube: ")
    download_type = input("Pilih tipe download (audio/video): ").strip().lower()
    
    if download_type == "audio":
        audio_quality = input("Masukkan kualitas audio yang diinginkan (misal 320, 192, 128): ").strip()
        download_playlist(
            playlist_url,
            download_type,
            audio_quality=audio_quality,
            ffmpeg_location=FFMPEG_LOCATION if FFMPEG_LOCATION else None
        )
    elif download_type == "video":
        video_resolution = input("Masukkan resolusi video yang diinginkan (misal 1080p atau 720p), atau tekan Enter untuk otomatis: ").strip()
        download_playlist(
            playlist_url,
            download_type,
            video_resolution=video_resolution if video_resolution else None,
            ffmpeg_location=FFMPEG_LOCATION if FFMPEG_LOCATION else None
        )
    else:
        print("Tipe download tidak valid. Harap pilih 'audio' atau 'video'.")
