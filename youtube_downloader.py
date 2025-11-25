# youtube_downloader_360p.py
import yt_dlp
import os

# لینک ویدیو (هر بار عوض کن)
URL = "https://youtu.be/"

# اسم دلخواهت برای فایل (هر چی دوست داری بنویس)
FILENAME = "MyVideo_360p.mp4"    # ← اینجا عوض کن

ydl_opts = {
    'format': 'bestvideo[height<=360]+bestaudio/best[acodec^=opus]/best',  # بهترین صدا رو هم می‌گیره
    'outtmpl': FILENAME,                                                   # اسم ثابت
    'merge_output_format': 'mp4',

    # زیرنویس
    'writesubtitles': True,
    'writeautomaticsub': True,
    'subtitleslangs': ['en', 'fa'],
    'subtitlesformat': 'srt',                  # بهتره SRT بشه (همه جا باز می‌شه)

    # اگر فایل cookies.txt تو همون پوشه باشه، خودکار استفاده می‌کنه
    'cookiefile': 'cookies.txt' if os.path.exists('cookies.txt') else None,

    # اگر کوکی نذاشتی و yt-dlp خطای لاگین داد، از مرورگر بگیره (خیلی راحت!)
    'cookies_from_browser': ('chrome',) if not os.path.exists('cookies.txt') else None,

    # جلوگیری از اووررایت فایل قبلی (اگر قبلاً دانلود کردی)
    'skip_download': False,
    'nooverwrites': False,                     # اجازه می‌ده فایل قبلی رو جایگزین کنه
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])
    print(f"دانلود با موفقیت تموم شد → {FILENAME}")
except Exception as e:
    print("مشکلی پیش اومد:")
    print(e)
