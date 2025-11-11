# youtube_downloader_360p.py
import yt_dlp

# لینک ویدیو رو اینجا بذار
URL = "https://youtu.be/"  # عوض کن با لینک خودت

# تنظیمات دانلود - فقط 360p
ydl_opts = {
    'format': 'bestvideo[height<=360]+bestaudio/best',  # حداکثر 360p + بهترین صدا
    'outtmpl': '%(title)s.%(ext)s',                      # اسم فایل: عنوان ویدیو
    'merge_output_format': 'mp4',                        # خروجی نهایی MP4
    'writesubtitles': True,                              # زیرنویس دستی
    'writeautomaticsub': True,                           # زیرنویس خودکار
    'subtitleslangs': ['en', 'fa'],                      # انگلیسی و فارسی
    #'cookiesfrombrowser': ('chrome',),
}

# دانلود
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL])

print("دانلود با کیفیت 360p تموم شد!")