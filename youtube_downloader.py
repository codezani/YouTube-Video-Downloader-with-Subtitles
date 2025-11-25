# youtube_downloader_360p.py
import yt_dlp
import os

URL = "https://youtu.be/"
FILENAME = "MyVideo_360p.mp4"

ydl_opts = {
    'format': 'bestvideo[height<=360]+bestaudio/best[acodec^=opus]/best',
    'outtmpl': FILENAME,
    'merge_output_format': 'mp4',
    'writesubtitles': True,
    'writeautomaticsub': True,
    'subtitleslangs': ['en', 'fa'],
    'subtitlesformat': 'srt',
    'cookiefile': 'cookies.txt' if os.path.exists('cookies.txt') else None,
    'cookies_from_browser': ('chrome',) if not os.path.exists('cookies.txt') else None,
    'nooverwrites': False,
    # اضافه برای کمتر کردن هشدارها (اختیاری)
    'quiet': False,  # True کن اگر نمی‌خوای خروجی ببینی
    'extractor_args': {'youtube': {'player_skip': ['js']}},  # nsig رو skip می‌کنه اگر لازم نبود
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])
    print(f"دانلود موفق → {FILENAME} (با زیرنویس en/fa)")
except Exception as e:
    print("خطا:", e)
